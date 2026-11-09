import sys
import os
import time
import re
from typing import Dict, Any
from pathlib import Path

# Dynamic injection of Rosetta root path
_DEFAULT_ROOT = str(Path(__file__).resolve().parent.parent.parent)
ROSETTA_ROOT = os.environ.get("ROSETTA_ROOT", "/app" if os.path.exists("/app/rosetta") else _DEFAULT_ROOT)
if ROSETTA_ROOT not in sys.path:
    sys.path.insert(0, ROSETTA_ROOT)

try:
    from rosetta.cli.mcp_server import (
        transpile as engine_transpile,
        inspect_ir as engine_inspect_ir,
        get_supported_languages as engine_get_languages,
    )
    print(f"[rosetta_bridge] Successfully loaded Rosetta engine from {ROSETTA_ROOT}!")
except Exception as e:
    import traceback
    print(f"[rosetta_bridge] WARNING: Failed to import rosetta engine: {e}", file=sys.stderr)
    traceback.print_exc()
    engine_transpile = None
    engine_inspect_ir = None
    engine_get_languages = None

# Smart language signatures for heuristics-based detection
SIGNATURES = {
    "cobol": [
        r"IDENTIFICATION\s+DIVISION",
        r"PROGRAM-ID\.",
        r"DATA\s+DIVISION",
        r"WORKING-STORAGE\s+SECTION",
        r"PROCEDURE\s+DIVISION",
        r"DISPLAY\s+['\"].*['\"]",
        r"STOP\s+RUN",
    ],
    "solidity": [
        r"pragma\s+solidity",
        r"contract\s+\w+",
        r"mapping\s*\(\s*\w+\s*=>\s*\w+\)",
        r"event\s+\w+\s*\(",
        r"emit\s+\w+\s*\(",
    ],
    "mojo": [
        r"@parameter",
        r"fn\s+\w+\s*\(.*inout.*\)",
        r"struct\s+\w+\s*:\n\s*var",
        r"let\s+\w+\s*=\s*\d+;",
        r"var\s+\w+\s*:\s*\w+",
    ],
    "zig": [
        r"@import\s*\(\s*['\"]std['\"]\s*\)",
        r"pub\s+fn\s+\w+",
        r"defer\s*\{",
        r"errdefer\s*",
        r"const\s+\w+\s*=\s*@import",
        r"std\.debug\.print",
    ],
    "carbon": [
        r"package\s+\w+\s+api;",
        r"interface\s+\w+\s*\{",
        r"impl\s+\w+\s+as\s+\w+",
        r"class\s+\w+\s*\{.*radius.*\}",
        r"fn\s+\w+\s*\(\s*\w+\s*:\s*\w+\s*\)\s*->\s*\w+",
    ],
    "fortran": [
        r"PROGRAM\s+\w+",
        r"PRINT\s*\*,",
        r"SUBROUTINE\s+\w+",
        r"CHARACTER\s*\(.*LEN\s*=\s*\*\)",
        r"END\s+PROGRAM",
    ],
    "python": [
        r"def\s+\w+\s*\(.*\):",
        r"import\s+\w+",
        r"from\s+\w+\s+import",
        r"print\s*\(",
        r"elif\s+",
        r"if\s+__name__\s*==\s*['\"]__main__['\"]:",
        r"\b\w+\s*=\s*[0-9a-zA-Z_+\-*/\(\)]+",
    ],
    "rust": [
        r"fn\s+main\s*\(\s*\)",
        r"let\s+mut\s+",
        r"println!\s*\(",
        r"use\s+std\s*::",
        r"impl\s+\w+\s*\{",
    ],
    "go": [
        r"package\s+main",
        r"func\s+main\s*\(\s*\)",
        r"import\s+\(\s*[\w\"\s\n]+",
        r"fmt\.Print",
        r"go\s+func\s*\(",
    ],
    "java": [
        r"public\s+class\s+\w+",
        r"public\s+static\s+void\s+main",
        r"System\.out\.print",
        r"import\s+java\.",
    ],
    "cpp": [
        r"#include\s+<iostream>",
        r"int\s+main\s*\(\s*\)\s*\{",
        r"std\s*::\s*cout",
        r"using\s+namespace\s+std",
    ],
    "c": [
        r"#include\s+<stdio\.h>",
        r"printf\s*\(",
        r"int\s+main\s*\(",
    ],
    "js": [
        r"const\s+\w+\s*=\s*require\(",
        r"console\.log\(",
        r"function\s+\w+\s*\(",
    ],
    "ts": [
        r"interface\s+\w+\s*\{",
        r"let\s+\w+\s*:\s*\w+\s*=",
        r"function\s+\w+\s*\(.*:\s*\w+\)",
    ],
    "kotlin": [
        r"fun\s+main\s*\(",
        r"val\s+\w+\s*=",
        r"println\s*\(",
    ],
    "swift": [
        r"func\s+\w+\s*\(.*\)\s*->",
        r"import\s+Foundation",
    ],
    "ruby": [
        r"def\s+\w+\n",
        r"puts\s+['\"]",
        r"\bend\b",
    ],
    "php": [
        r"<\?php",
        r"\$\w+\s*=",
        r"echo\s+['\"]",
    ],
    "csharp": [
        r"Console\.(WriteLine|Write)\(",
        r"using\s+System;",
        r"namespace\s+[A-Za-z0-9_.]+",
    ],
    "dart": [
        r"void\s+main\s*\(\s*\)",
        r"import\s+['\"]package:",
        r"\bprint\s*\(",
    ],
    "lua": [
        r"\blocal\s+\w+\s*=",
        r"\bfunction\s+[A-Za-z0-9_:]+\s*\(",
        r"\bend\b",
    ],
    "r": [
        r"\b\w+\s*<-\s*",
        r"library\s*\(\s*\w+\s*\)",
        r"setRefClass\(",
    ],
    "julia": [
        r"function\s+\w+\(.*\)\s*$",
        r"println\s*\(",
        r"::Vector\{",
    ],
    "scala": [
        r"object\s+\w+\s*\{",
        r"def\s+main\(.*Array\[String\]",
        r"val\s+\w+\s*:\s*[A-Z]",
    ],
    "haskell": [
        r"module\s+\w+\s+where",
        r"main\s*::\s*IO",
        r"putStrLn\s+",
    ],
    "elixir": [
        r"defmodule\s+[A-Za-z0-9_.]+\s+do",
        r"IO\.puts\(",
        r"defstruct\s+",
    ],
    "bash": [
        r"#!/bin/bash",
        r"#!/usr/bin/env bash",
        r"\becho\s+",
        r"if\s+\[\[.*\]\];\s*then",
    ],
    "sql": [
        r"DECLARE\s+@\w+",
        r"SELECT\s+.*FROM",
        r"CREATE\s+PROCEDURE",
    ],
    "objc": [
        r"#import\s+<Foundation/Foundation.h>",
        r"NSLog\s*\(@?",
        r"@interface\s+\w+",
    ],
    "move": [
        r"module\s+0x[0-9a-fA-F]+::\w+",
        r"public\s+fun\s+\w+",
        r"debug::print",
    ],
    "perl": [
        r"use\s+strict;",
        r"use\s+warnings;",
        r"my\s+\$\w+\s*=",
    ],
}


def transpile_code(source: str, from_lang: str, to_lang: str) -> Dict[str, Any]:
    """
    Translates source code using the loaded Rosetta engine and returns
    transpiled code, AST inspection data, and active HERMES passes.
    """
    start_time = time.time()

    from_ext = from_lang.lower().strip()
    if not from_ext.startswith("."):
        from_ext = "." + from_ext

    to_lang = to_lang.lower().strip().lstrip(".")

    try:
        ast_data = None
        passes_list = None
        if engine_inspect_ir is not None:
            inspection = engine_inspect_ir(source, from_ext, to_lang)
            output = inspection["result"]
            ast_data = inspection["optimized_ir"]
            passes_list = inspection["passes"]
        elif engine_transpile is not None:
            output = engine_transpile(source, from_ext, to_lang)
        else:
            output = f"// [MOCK OUTPUT] Transpiled from {from_ext} to {to_lang}\n{source}"

        elapsed_ms = (time.time() - start_time) * 1000
        tokens = len(source.split()) + len(output.split())

        return {
            "result": output,
            "tokens_used": tokens,
            "time_ms": round(elapsed_ms, 2),
            "ast": ast_data,
            "passes": passes_list,
        }
    except Exception as e:
        raise RuntimeError(f"Rosetta engine compilation failed: {str(e)}")


def inspect_code(source: str, from_lang: str, to_lang: str = "py") -> Dict[str, Any]:
    """
    Returns full BABEL + HERMES + CIPHER inspection metadata for the Web Studio AST Inspector.
    """
    from_ext = from_lang.lower().strip()
    if not from_ext.startswith("."):
        from_ext = "." + from_ext
    to_lang = to_lang.lower().strip().lstrip(".")

    if engine_inspect_ir is None:
        raise RuntimeError("Rosetta inspection engine is not available")
    return engine_inspect_ir(source, from_ext, to_lang)


def detect_language(source: str) -> Dict[str, Any]:
    """
    Heuristically detects programming language and provides confidence score.
    """
    scores = {lang: 0 for lang in SIGNATURES}

    for lang, regexes in SIGNATURES.items():
        for regex in regexes:
            matches = re.findall(regex, source, re.IGNORECASE)
            if matches:
                scores[lang] += len(matches) * 20

    detected_lang = "python"
    highest_score = 0

    for lang, score in scores.items():
        if score > highest_score:
            highest_score = score
            detected_lang = lang

    confidence = min(highest_score / 100.0, 1.0)
    if highest_score == 0:
        confidence = 0.35

    ext_mapping = {
        "cobol": ".cbl",
        "solidity": ".sol",
        "mojo": ".mojo",
        "zig": ".zig",
        "carbon": ".carbon",
        "fortran": ".f90",
        "python": ".py",
        "rust": ".rs",
        "go": ".go",
        "java": ".java",
        "cpp": ".cpp",
        "c": ".c",
        "js": ".js",
        "ts": ".ts",
        "kotlin": ".kt",
        "swift": ".swift",
        "ruby": ".rb",
        "php": ".php",
        "csharp": ".cs",
        "dart": ".dart",
        "lua": ".lua",
        "r": ".r",
        "julia": ".jl",
        "scala": ".scala",
        "haskell": ".hs",
        "elixir": ".ex",
        "bash": ".sh",
        "sql": ".sql",
        "objc": ".m",
        "move": ".move",
        "perl": ".pm",
    }

    return {
        "language": ext_mapping.get(detected_lang, ".py"),
        "confidence": round(confidence, 2),
    }
