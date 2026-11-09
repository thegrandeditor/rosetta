"""
rosetta/cli/resolver.py
-----------------------
Centralised frontend & backend registry for the ROSETTA transpiler.

All built-in languages (32 core + 13 universal expansion = 45) are registered
symmetrically as both BABEL Frontends (source parsers) and CIPHER Backends
(target emitters). Languages taught at runtime via ``rosetta learn`` are
discovered automatically from ``rosetta/autolearn/generated``.
"""
from __future__ import annotations

# --- BABEL Frontends (32 Languages) ---
from rosetta.babel.python.frontend import PythonFrontend
from rosetta.babel.javascript.frontend import JavaScriptFrontend
from rosetta.babel.typescript.frontend import TypeScriptFrontend
from rosetta.babel.java.frontend import JavaFrontend
from rosetta.babel.cpp.frontend import CppFrontend
from rosetta.babel.c.frontend import CFrontend
from rosetta.babel.rust.frontend import RustFrontend
from rosetta.babel.go.frontend import GoFrontend
from rosetta.babel.swift.frontend import SwiftFrontend
from rosetta.babel.kotlin.frontend import KotlinFrontend
from rosetta.babel.ruby.frontend import RubyFrontend
from rosetta.babel.php.frontend import PHPFrontend
from rosetta.babel.cobol.frontend import CobolFrontend
from rosetta.babel.fortran.frontend import FortranFrontend
from rosetta.babel.basic.frontend import BasicFrontend
from rosetta.babel.pascal.frontend import PascalFrontend
from rosetta.babel.ada.frontend import AdaFrontend
from rosetta.babel.lisp.frontend import LispFrontend
from rosetta.babel.algol.frontend import AlgolFrontend
from rosetta.babel.smalltalk.frontend import SmalltalkFrontend
from rosetta.babel.prolog.frontend import PrologFrontend
from rosetta.babel.snobol.frontend import SnobolFrontend
from rosetta.babel.pli.frontend import PLIFrontend
from rosetta.babel.modula2.frontend import Modula2Frontend
from rosetta.babel.rpg.frontend import RPGFrontend
from rosetta.babel.eiffel.frontend import EiffelFrontend
from rosetta.babel.forth.frontend import ForthFrontend
from rosetta.babel.ml.frontend import MLFrontend
from rosetta.babel.solidity.frontend import SolidityFrontend
from rosetta.babel.mojo.frontend import MojoFrontend
from rosetta.babel.zig.frontend import ZigFrontend
from rosetta.babel.carbon.frontend import CarbonFrontend

# --- CIPHER Backends (32 Languages) ---
from rosetta.cipher.javascript.backend import JavaScriptBackend
from rosetta.cipher.typescript.backend import TypeScriptBackend
from rosetta.cipher.ruby.backend import RubyBackend
from rosetta.cipher.php.backend import PHPBackend
from rosetta.cipher.swift.backend import SwiftBackend
from rosetta.cipher.kotlin.backend import KotlinBackend
from rosetta.cipher.python.backend import PythonBackend
from rosetta.cipher.c.backend import CBackend
from rosetta.cipher.java.backend import JavaBackend
from rosetta.cipher.rust.backend import RustBackend
from rosetta.cipher.go.backend import GoBackend
from rosetta.cipher.cpp.backend import CppBackend
from rosetta.cipher.cobol.backend import CobolBackend
from rosetta.cipher.fortran.backend import FortranBackend
from rosetta.cipher.basic.backend import BasicBackend
from rosetta.cipher.pascal.backend import PascalBackend
from rosetta.cipher.ada.backend import AdaBackend
from rosetta.cipher.lisp.backend import LispBackend
from rosetta.cipher.algol.backend import AlgolBackend
from rosetta.cipher.smalltalk.backend import SmalltalkBackend
from rosetta.cipher.prolog.backend import PrologBackend
from rosetta.cipher.snobol.backend import SnobolBackend
from rosetta.cipher.pli.backend import PLIBackend
from rosetta.cipher.modula2.backend import Modula2Backend
from rosetta.cipher.rpg.backend import RPGBackend
from rosetta.cipher.eiffel.backend import EiffelBackend
from rosetta.cipher.forth.backend import ForthBackend
from rosetta.cipher.ml.backend import MLBackend
from rosetta.cipher.solidity.backend import SolidityBackend
from rosetta.cipher.mojo.backend import MojoBackend
from rosetta.cipher.zig.backend import ZigBackend
from rosetta.cipher.carbon.backend import CarbonBackend

# ---------------------------------------------------------------------------
# Registry: file extension / language alias -> Frontend class
# ---------------------------------------------------------------------------
FRONTENDS: dict[str, type] = {
    ".py":         PythonFrontend,
    ".python":     PythonFrontend,
    ".js":         JavaScriptFrontend,
    ".javascript": JavaScriptFrontend,
    ".ts":         TypeScriptFrontend,
    ".typescript": TypeScriptFrontend,
    ".java":       JavaFrontend,
    ".cpp":        CppFrontend,
    ".cc":         CppFrontend,
    ".cxx":        CppFrontend,
    ".c":          CFrontend,
    ".rs":         RustFrontend,
    ".rust":       RustFrontend,
    ".go":         GoFrontend,
    ".swift":      SwiftFrontend,
    ".kt":         KotlinFrontend,
    ".kotlin":     KotlinFrontend,
    ".rb":         RubyFrontend,
    ".ruby":       RubyFrontend,
    ".php":        PHPFrontend,
    ".cbl":        CobolFrontend,
    ".cob":        CobolFrontend,
    ".cobol":      CobolFrontend,
    ".f90":        FortranFrontend,
    ".f":          FortranFrontend,
    ".f95":        FortranFrontend,
    ".fortran":    FortranFrontend,
    ".bas":        BasicFrontend,
    ".basic":      BasicFrontend,
    ".vb":         BasicFrontend,
    ".vba":        BasicFrontend,
    ".vbs":        BasicFrontend,
    ".pas":        PascalFrontend,
    ".pascal":     PascalFrontend,
    ".delphi":     PascalFrontend,
    ".ino":        CppFrontend,
    ".gs":         JavaScriptFrontend,
    ".adb":        AdaFrontend,
    ".ads":        AdaFrontend,
    ".ada":        AdaFrontend,
    ".lisp":       LispFrontend,
    ".cl":         LispFrontend,
    ".alg":        AlgolFrontend,
    ".algol":      AlgolFrontend,
    ".st":         SmalltalkFrontend,
    ".smalltalk":  SmalltalkFrontend,
    ".pl":         PrologFrontend,
    ".pro":        PrologFrontend,
    ".prolog":     PrologFrontend,
    ".sno":        SnobolFrontend,
    ".snobol":     SnobolFrontend,
    ".pli":        PLIFrontend,
    ".pl1":        PLIFrontend,
    ".mod":        Modula2Frontend,
    ".m2":         Modula2Frontend,
    ".modula2":    Modula2Frontend,
    ".rpg":        RPGFrontend,
    ".rpgle":      RPGFrontend,
    ".e":          EiffelFrontend,
    ".eiffel":     EiffelFrontend,
    ".fs":         ForthFrontend,
    ".forth":      ForthFrontend,
    ".ml":         MLFrontend,
    ".sml":        MLFrontend,
    ".sol":        SolidityFrontend,
    ".solidity":   SolidityFrontend,
    ".mojo":       MojoFrontend,
    ".🔥":         MojoFrontend,
    ".zig":        ZigFrontend,
    ".carbon":     CarbonFrontend,
}

# ---------------------------------------------------------------------------
# Registry: target language identifier -> Backend class
# ---------------------------------------------------------------------------
BACKENDS: dict[str, type] = {
    "js":         JavaScriptBackend,
    "javascript": JavaScriptBackend,
    "ts":         TypeScriptBackend,
    "typescript": TypeScriptBackend,
    "rb":         RubyBackend,
    "ruby":       RubyBackend,
    "php":        PHPBackend,
    "swift":      SwiftBackend,
    "kt":         KotlinBackend,
    "kotlin":     KotlinBackend,
    "py":         PythonBackend,
    "python":     PythonBackend,
    "c":          CBackend,
    "cpp":        CppBackend,
    "java":       JavaBackend,
    "rs":         RustBackend,
    "rust":       RustBackend,
    "go":         GoBackend,
    "cobol":      CobolBackend,
    "cbl":        CobolBackend,
    "fortran":    FortranBackend,
    "f90":        FortranBackend,
    "basic":      BasicBackend,
    "bas":        BasicBackend,
    "vb":         BasicBackend,
    "vba":        BasicBackend,
    "visualbasic":BasicBackend,
    "pascal":     PascalBackend,
    "pas":        PascalBackend,
    "delphi":     PascalBackend,
    "arduino":    CppBackend,
    "ino":        CppBackend,
    "ada":        AdaBackend,
    "adb":        AdaBackend,
    "lisp":       LispBackend,
    "algol":      AlgolBackend,
    "alg":        AlgolBackend,
    "smalltalk":  SmalltalkBackend,
    "st":         SmalltalkBackend,
    "prolog":     PrologBackend,
    "pl":         PrologBackend,
    "snobol":     SnobolBackend,
    "sno":        SnobolBackend,
    "pli":        PLIBackend,
    "modula2":    Modula2Backend,
    "mod":        Modula2Backend,
    "rpg":        RPGBackend,
    "eiffel":     EiffelBackend,
    "e":          EiffelBackend,
    "forth":      ForthBackend,
    "fs":         ForthBackend,
    "ml":         MLBackend,
    "solidity":   SolidityBackend,
    "sol":        SolidityBackend,
    "mojo":       MojoBackend,
    "zig":        ZigBackend,
    "carbon":     CarbonBackend,
}

# Extensions that need legacy-specific Hermes passes
LEGACY_EXTENSIONS = frozenset({".f90", ".f", ".f95", ".pli", ".pl1"})

# ---------------------------------------------------------------------------
# Universal expansion: C#, Dart, Lua, R, Julia, Scala, Haskell, Elixir, Bash,
# SQL, Objective-C, Move, Perl
# ---------------------------------------------------------------------------
from rosetta.babel.universal.frontends import UNIVERSAL_FRONTENDS  # noqa: E402
from rosetta.cipher.universal.backends import UNIVERSAL_BACKENDS  # noqa: E402

FRONTENDS.update(UNIVERSAL_FRONTENDS)
FRONTENDS.update({
    ".ps1": UNIVERSAL_FRONTENDS[".sh"],
    ".powershell": UNIVERSAL_FRONTENDS[".sh"],
})
BACKENDS.update(UNIVERSAL_BACKENDS)
BACKENDS.update({
    "cs": UNIVERSAL_BACKENDS["csharp"],
    "c#": UNIVERSAL_BACKENDS["csharp"],
    "jl": UNIVERSAL_BACKENDS["julia"],
    "hs": UNIVERSAL_BACKENDS["haskell"],
    "ex": UNIVERSAL_BACKENDS["elixir"],
    "sh": UNIVERSAL_BACKENDS["bash"],
    "shell": UNIVERSAL_BACKENDS["bash"],
    "powershell": UNIVERSAL_BACKENDS["bash"],
    "ps1": UNIVERSAL_BACKENDS["bash"],
    "tsql": UNIVERSAL_BACKENDS["sql"],
    "objective-c": UNIVERSAL_BACKENDS["objc"],
    "m": UNIVERSAL_BACKENDS["objc"],
    "pm": UNIVERSAL_BACKENDS["perl"],
})

#: Language ids that are built in (everything else was learned at runtime).
BUILTIN_LANGUAGES = frozenset(
    {cls().language_id for cls in set(BACKENDS.values())}
)

# ---------------------------------------------------------------------------
# AUTOLEARN: dynamic discovery of languages taught via `rosetta learn`
# ---------------------------------------------------------------------------
import importlib.util  # noqa: E402
import inspect  # noqa: E402
import logging  # noqa: E402
from pathlib import Path  # noqa: E402

_log = logging.getLogger(__name__)
GENERATED_DIR = Path(__file__).resolve().parent.parent / "autolearn" / "generated"
LEARNED_LANGUAGES: dict[str, dict] = {}


def _load_class(path: Path, module_name: str, suffix: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if name.endswith(suffix) and obj.__module__ == module.__name__ and hasattr(obj, "emit" if suffix == "Backend" else "parse"):
            return obj
    return None


def discover_learned_languages() -> dict[str, dict]:
    """Scan ``rosetta/autolearn/generated/*`` and register every learned language.

    Safe to call repeatedly (e.g. right after ``rosetta learn``): new languages
    are added to :data:`FRONTENDS` / :data:`BACKENDS` without a restart.
    """
    if not GENERATED_DIR.is_dir():
        return LEARNED_LANGUAGES
    for lang_dir in sorted(p for p in GENERATED_DIR.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
        lang_id = lang_dir.name.lower()
        if lang_id in BUILTIN_LANGUAGES:
            continue  # never let a learned draft shadow a built-in language
        info: dict = {"id": lang_id, "path": str(lang_dir), "frontend": False, "backend": False}
        try:
            fe_path = lang_dir / "babel" / "frontend.py"
            if fe_path.is_file():
                fe = _load_class(fe_path, f"rosetta_learned_{lang_id}_frontend", "Frontend")
                if fe is not None:
                    FRONTENDS["." + lang_id] = fe
                    info["frontend"] = True
            be_path = lang_dir / "cipher" / "backend.py"
            if be_path.is_file():
                be = _load_class(be_path, f"rosetta_learned_{lang_id}_backend", "Backend")
                if be is not None:
                    BACKENDS[lang_id] = be
                    info["backend"] = True
        except Exception as exc:  # a broken draft must never break the CLI
            _log.warning("Skipping learned language %r: %s", lang_id, exc)
            info["error"] = str(exc)
        LEARNED_LANGUAGES[lang_id] = info
    return LEARNED_LANGUAGES


discover_learned_languages()


def get_frontend(ext: str):
    """
    Return an instantiated BABEL frontend for the given file extension.

    Args:
        ext: File extension including the leading dot, e.g. ``".py"``.

    Raises:
        ValueError: If no frontend is registered for *ext*.
    """
    ext = ext.lower().strip()
    if not ext.startswith("."):
        ext = "." + ext
    cls = FRONTENDS.get(ext)
    if cls is None:
        discover_learned_languages()
        cls = FRONTENDS.get(ext)
    if cls is None:
        raise ValueError(f"Unsupported input file extension: {ext!r}")
    return cls()


def get_backend(target: str):
    """
    Return an instantiated CIPHER backend for the given target language.

    Args:
        target: Language identifier, e.g. ``"py"``, ``"carbon"``, ``"js"``.

    Raises:
        ValueError: If no backend is registered for *target*.
    """
    target = target.lower().strip().lstrip(".")
    cls = BACKENDS.get(target)
    if cls is None:
        discover_learned_languages()
        cls = BACKENDS.get(target)
    if cls is None:
        raise ValueError(f"Unsupported target language: {target!r}")
    return cls()
