import argparse
import sys
import os

if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from rosetta.cli.resolver import get_frontend, get_backend, LEGACY_EXTENSIONS, BACKENDS
from rosetta.hermes.pipeline import HermesPipeline
from rosetta.hermes.passes.standard_passes import (
    TypeInferencePass,
    ScopeResolutionPass,
    IdiomNormalizationPass,
    DesugarListCompPass,
    LegacyIndexingPass,
    RedundantDeclarationPass,
    StdlibNormalizationPass,
    LibraryMappingPass,
    MemorySafetyNormalizationPass,
)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "learn":
        parser = argparse.ArgumentParser(description="ROSETTA Auto-Learn Engine")
        parser.add_argument("command", choices=["learn"])
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--grammar", help="Path to ANTLR4 .g4 grammar file")
        group.add_argument("--bnf", help="Path to BNF/EBNF file")
        group.add_argument("--corpus", help="Path to sample code corpus directory or file")
        parser.add_argument("--name", help="Output language name (optional)")
        args = parser.parse_args()

        from rosetta.autolearn.engine import AutoLearnEngine
        engine = AutoLearnEngine()
        try:
            if args.grammar:
                res = engine.learn_from_grammar(args.grammar, args.name)
            elif args.bnf:
                res = engine.learn_from_bnf(args.bnf, args.name)
            elif args.corpus:
                res = engine.learn_from_corpus(args.corpus, args.name)
            print(res)
            sys.exit(0)
        except Exception as e:
            print(f"Error during learning: {str(e)}")
            sys.exit(1)

    parser = argparse.ArgumentParser(description="ROSETTA Universal Transpiler")
    parser.add_argument("input_file", help="Source code file to transpile")
    parser.add_argument("--to", required=True, choices=list(BACKENDS.keys()), help="Target language")
    parser.add_argument("--frontend", choices=["ast", "antlr"], default="ast", help="Frontend implementation to use (for Python)")
    parser.add_argument("--show-ir", action="store_true", help="Print the Rosetta IR to terminal")
    parser.add_argument("--passes", help="Comma-separated list of Hermes passes to run")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: File {args.input_file} not found.")
        sys.exit(1)

    with open(args.input_file, "r", encoding="utf-8") as f:
        source = f.read()

    # Phase 1: BABEL (Frontend)
    if args.input_file.endswith(".py") and args.frontend == "antlr":
        from rosetta.babel.python.antlr_frontend import PythonAntlrFrontend
        frontend = PythonAntlrFrontend()
    else:
        ext = os.path.splitext(args.input_file)[1].lower()
        try:
            frontend = get_frontend(ext)
        except ValueError as err:
            print(f"Error: {err}")
            sys.exit(1)

    ir = frontend.parse(source)

    # Phase 2: HERMES (Pipeline)
    pipeline = HermesPipeline()

    ext = os.path.splitext(args.input_file)[1].lower()
    if ext in LEGACY_EXTENSIONS:
        pipeline.add_pass(LegacyIndexingPass())
        pipeline.add_pass(RedundantDeclarationPass())

    if args.passes:
        pass_names = args.passes.split(",")
        for name in pass_names:
            name = name.strip()
            if name == "type_inference":
                pipeline.add_pass(TypeInferencePass())
            elif name == "scope_resolution":
                pipeline.add_pass(ScopeResolutionPass())
            elif name == "idiom_normalization":
                pipeline.add_pass(IdiomNormalizationPass())
            elif name == "desugar_list_comp":
                pipeline.add_pass(DesugarListCompPass())
            elif name == "stdlib_normalization":
                pipeline.add_pass(StdlibNormalizationPass())
    else:
        pipeline.add_pass(StdlibNormalizationPass())
        pipeline.add_pass(LibraryMappingPass(args.to))
        pipeline.add_pass(MemorySafetyNormalizationPass(args.to))
        pipeline.add_pass(TypeInferencePass())
        pipeline.add_pass(IdiomNormalizationPass())

    ir = pipeline.run(ir)

    if args.show_ir:
        print("--- ROSETTA IR ---")
        print(ir)
        print("------------------")

    # Phase 3: CIPHER (Backend)
    try:
        backend = get_backend(args.to)
    except ValueError as err:
        print(f"Error: {err}")
        sys.exit(1)

    output = backend.emit(ir)
    print(output)


if __name__ == "__main__":
    main()
