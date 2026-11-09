import sys
import os
from dataclasses import is_dataclass

if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    FastMCP = None

from rosetta.ir.nodes import Program
from rosetta.cli.resolver import get_frontend, get_backend, LEGACY_EXTENSIONS, FRONTENDS, BACKENDS
from rosetta.hermes.pipeline import HermesPipeline
from rosetta.hermes.passes.standard_passes import (
    TypeInferencePass,
    IdiomNormalizationPass,
    LegacyIndexingPass,
    RedundantDeclarationPass,
    StdlibNormalizationPass,
    LibraryMappingPass,
    MemorySafetyNormalizationPass,
)

if FastMCP is not None:
    mcp = FastMCP("ROSETTA Universal Transpiler")
else:
    class _MockMCP:
        def tool(self):
            def decorator(f):
                return f
            return decorator
        def run(self):
            pass
    mcp = _MockMCP()


def serialize_ir_node(node) -> dict | list | str | int | float | bool | None:
    """Recursively converts a RosettaNode dataclass tree into a JSON-serializable dict."""
    if node is None or isinstance(node, (str, int, float, bool)):
        return node
    if isinstance(node, list):
        return [serialize_ir_node(item) for item in node]
    if isinstance(node, dict):
        return {k: serialize_ir_node(v) for k, v in node.items()}
    if is_dataclass(node):
        res = {"node_type": type(node).__name__}
        for attr, val in vars(node).items():
            if attr == "metadata" and not val:
                continue
            res[attr] = serialize_ir_node(val)
        return res
    return str(node)


FALLBACK_CANDIDATES = [
    ".py", ".js", ".ts", ".c", ".cpp", ".rs", ".go", ".java", ".kt", ".swift",
    ".rb", ".php", ".cbl", ".f90", ".bas", ".pas", ".adb", ".zig", ".sol",
    ".mojo", ".lisp", ".st", ".pl", ".sno", ".pli", ".mod", ".rpg", ".e",
    ".fs", ".ml", ".carbon"
]


@mcp.tool()
def transpile(source: str, input_ext: str, target_lang: str) -> str:
    """
    Transpiles source code from an input language (determined by its file extension)
    to a target programming language.
    """
    frontend = get_frontend(input_ext)
    ir = frontend.parse(source)

    ext = input_ext.lower().strip()
    if not ext.startswith("."):
        ext = "." + ext

    # If non-empty source parsed into 0 statements, try smart fallback frontends
    if source.strip() and isinstance(ir, Program) and len(ir.body) == 0:
        for fallback_ext in FALLBACK_CANDIDATES:
            if fallback_ext == ext:
                continue
            try:
                alt_fe = get_frontend(fallback_ext)
                alt_ir = alt_fe.parse(source)
                if isinstance(alt_ir, Program) and len(alt_ir.body) > 0:
                    ir = alt_ir
                    ext = fallback_ext
                    frontend = alt_fe
                    break
            except Exception:
                pass

        if isinstance(ir, Program) and len(ir.body) == 0:
            raise ValueError(
                f"Source code could not be parsed as {frontend.language_id.upper()}. "
                f"Please verify that the selected Source Node matches your code syntax."
            )

    pipeline = HermesPipeline()
    if ext in LEGACY_EXTENSIONS:
        pipeline.add_pass(LegacyIndexingPass())
        pipeline.add_pass(RedundantDeclarationPass())

    pipeline.add_pass(StdlibNormalizationPass())
    pipeline.add_pass(LibraryMappingPass(target_lang))
    pipeline.add_pass(MemorySafetyNormalizationPass(target_lang))
    pipeline.add_pass(TypeInferencePass())
    pipeline.add_pass(IdiomNormalizationPass())
    ir = pipeline.run(ir)

    backend = get_backend(target_lang)
    return backend.emit(ir)


@mcp.tool()
def inspect_ir(source: str, input_ext: str, target_lang: str = "py") -> dict:
    """
    Parses source code, runs HERMES passes, and returns both the pre-pass and post-pass
    serialized Rosetta IR AST along with pass telemetry.
    """
    frontend = get_frontend(input_ext)
    raw_ir = frontend.parse(source)

    ext = input_ext.lower().strip()
    if not ext.startswith("."):
        ext = "." + ext

    # Smart fallback if 0 statements parsed from non-empty code
    if source.strip() and isinstance(raw_ir, Program) and len(raw_ir.body) == 0:
        for fallback_ext in FALLBACK_CANDIDATES:
            if fallback_ext == ext:
                continue
            try:
                alt_fe = get_frontend(fallback_ext)
                alt_ir = alt_fe.parse(source)
                if isinstance(alt_ir, Program) and len(alt_ir.body) > 0:
                    raw_ir = alt_ir
                    ext = fallback_ext
                    frontend = alt_fe
                    break
            except Exception:
                pass

        if isinstance(raw_ir, Program) and len(raw_ir.body) == 0:
            raise ValueError(
                f"Source code could not be parsed as {frontend.language_id.upper()}. "
                f"Please verify that the selected Source Node matches your code syntax."
            )

    raw_tree = serialize_ir_node(raw_ir)

    pipeline = HermesPipeline()
    ext = input_ext.lower().strip()
    if not ext.startswith("."):
        ext = "." + ext
    active_passes = []
    if ext in LEGACY_EXTENSIONS:
        pipeline.add_pass(LegacyIndexingPass())
        pipeline.add_pass(RedundantDeclarationPass())
        active_passes.extend(["LegacyIndexingPass", "RedundantDeclarationPass"])

    pipeline.add_pass(StdlibNormalizationPass())
    pipeline.add_pass(LibraryMappingPass(target_lang))
    pipeline.add_pass(MemorySafetyNormalizationPass(target_lang))
    pipeline.add_pass(TypeInferencePass())
    pipeline.add_pass(IdiomNormalizationPass())
    active_passes.extend([
        "StdlibNormalizationPass",
        "LibraryMappingPass",
        "MemorySafetyNormalizationPass",
        "TypeInferencePass",
        "IdiomNormalizationPass",
    ])

    optimized_ir = pipeline.run(raw_ir)
    optimized_tree = serialize_ir_node(optimized_ir)

    backend = get_backend(target_lang)
    emitted = backend.emit(optimized_ir)

    return {
        "frontend": frontend.language_id,
        "frontend_version": frontend.supported_version,
        "backend": backend.language_id,
        "backend_style": backend.style_guide,
        "passes": active_passes,
        "raw_ir": raw_tree,
        "optimized_ir": optimized_tree,
        "result": emitted,
    }


@mcp.tool()
def get_supported_languages() -> dict:
    """
    Returns the supported input extensions and output target languages.
    """
    return {
        "input_extensions": sorted(list(set(FRONTENDS.keys()))),
        "target_languages": sorted(list(set(BACKENDS.keys()))),
    }


if __name__ == "__main__":
    mcp.run()
