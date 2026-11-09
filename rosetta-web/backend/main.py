from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Any
import time

from backend.models import (
    TranspileRequest, TranspileResponse, 
    DetectRequest, DetectResponse, 
    LanguageInfo, LanguagesResponse,
    LearnRequest, LearnResponse,
)
from backend.rosetta_bridge import transpile_code, detect_language, inspect_code

app = FastAPI(
    title="ROSETTA API",
    description="Futuristic Transpiler Engine API wrapper for Rosetta",
    version="1.0.0"
)

# CORS setup for local Next.js client
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Supports flexible local/cloud development setups
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Deep Metadata for all 32 languages
LANGUAGE_CATALOG: List[LanguageInfo] = [
    # Phase 1 & 2: Foundation & Modern (Cyan Glow)
    LanguageInfo(
        name="Python", ext=".py", phase=1, paradigm="Multi-paradigm", 
        glowColor="cyan", sampleCode="def greet(name: str):\n    print(f\"Hello, {name}!\")\n\ngreet(\"Rosetta\")"
    ),
    LanguageInfo(
        name="JavaScript", ext=".js", phase=1, paradigm="Event-driven / Prototype", 
        glowColor="cyan", sampleCode="function greet(name) {\n    console.log(`Hello, ${name}!`);\n}\n\ngreet(\"Rosetta\");"
    ),
    LanguageInfo(
        name="TypeScript", ext=".ts", phase=1, paradigm="Static OOP / Functional", 
        glowColor="cyan", sampleCode="function greet(name: string): void {\n    console.log(`Hello, ${name}!`);\n}\n\ngreet(\"Rosetta\");"
    ),
    LanguageInfo(
        name="Java", ext=".java", phase=1, paradigm="Strict Object-Oriented", 
        glowColor="cyan", sampleCode="public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Rosetta!\");\n    }\n}"
    ),
    LanguageInfo(
        name="C++", ext=".cpp", phase=1, paradigm="Systems OOP / Generic", 
        glowColor="cyan", sampleCode="#include <iostream>\n\nint main() {\n    std::cout << \"Hello, Rosetta!\" << std::endl;\n    return 0;\n}"
    ),
    LanguageInfo(
        name="C", ext=".c", phase=1, paradigm="Procedural / Imperative", 
        glowColor="cyan", sampleCode="#include <stdio.h>\n\nint main() {\n    printf(\"Hello, Rosetta!\\n\");\n    return 0;\n}"
    ),
    LanguageInfo(
        name="Rust", ext=".rs", phase=1, paradigm="Concurrent / Safe Systems", 
        glowColor="cyan", sampleCode="fn main() {\n    println!(\"Hello, Rosetta!\");\n}"
    ),
    LanguageInfo(
        name="Go", ext=".go", phase=1, paradigm="Concurrent / Procedural", 
        glowColor="cyan", sampleCode="package main\n\nimport \"fmt\"\n\nfn main() {\n    fmt.Println(\"Hello, Rosetta!\")\n}"
    ),
    LanguageInfo(
        name="Swift", ext=".swift", phase=1, paradigm="Protocols / Multi-paradigm", 
        glowColor="cyan", sampleCode="print(\"Hello, Rosetta!\")"
    ),
    LanguageInfo(
        name="Kotlin", ext=".kt", phase=1, paradigm="Modern Functional OOP", 
        glowColor="cyan", sampleCode="fun main() {\n    println(\"Hello, Rosetta!\")\n}"
    ),
    LanguageInfo(
        name="Ruby", ext=".rb", phase=1, paradigm="Dynamic OOP / Scripting", 
        glowColor="cyan", sampleCode="puts 'Hello, Rosetta!'"
    ),
    LanguageInfo(
        name="PHP", ext=".php", phase=1, paradigm="Dynamic Web Scripting", 
        glowColor="cyan", sampleCode="<?php\necho \"Hello, Rosetta!\";\n?>"
    ),
    LanguageInfo(
        name="COBOL", ext=".cbl", phase=2, paradigm="Business / Legacy Record", 
        glowColor="cyan", sampleCode="       DATA DIVISION.\n       WORKING-STORAGE SECTION.\n       01 GREETING PIC X(12) VALUE 'HELLO ROSETTA'.\n       PROCEDURE DIVISION.\n           DISPLAY GREETING.\n           STOP RUN."
    ),

    # Phase 3: Legacy & Lost (Purple Glow)
    LanguageInfo(
        name="Fortran", ext=".f90", phase=3, paradigm="Numeric Computing", 
        glowColor="purple", sampleCode="PROGRAM HELLO\n    PRINT *, 'Hello, World!'\n    CALL GREET('Rosetta')\nEND PROGRAM HELLO\n\nSUBROUTINE GREET(NAME)\n    CHARACTER(LEN=*) :: NAME\n    PRINT *, 'Greetings, ', NAME\nEND SUBROUTINE GREET"
    ),
    LanguageInfo(
        name="Visual Basic", ext=".vb", phase=3, paradigm="Event-Driven Rapid App", 
        glowColor="purple", sampleCode="Module Program\n    Sub Main()\n        Console.WriteLine(\"Hello from Visual Basic!\")\n    End Sub\nEnd Module"
    ),
    LanguageInfo(
        name="Delphi", ext=".delphi", phase=3, paradigm="Object Pascal Native", 
        glowColor="purple", sampleCode="program HelloDelphi;\nbegin\n    Writeln('Hello from Delphi!');\nend."
    ),
    LanguageInfo(
        name="BASIC", ext=".bas", phase=3, paradigm="Procedural Imperative", 
        glowColor="purple", sampleCode="10 PRINT \"HELLO WORLD\"\n20 PRINT \"ROSETTA ENGINE\"\n30 END"
    ),
    LanguageInfo(
        name="Pascal", ext=".pas", phase=3, paradigm="Structured / Strongly Typed", 
        glowColor="purple", sampleCode="program Hello;\nbegin\n  writeln('Hello, World!');\nend."
    ),
    LanguageInfo(
        name="Ada", ext=".adb", phase=3, paradigm="Concurrent / Real-time Systems", 
        glowColor="purple", sampleCode="with Ada.Text_IO; use Ada.Text_IO;\nprocedure Hello is\nbegin\n  Put_Line(\"Hello, World!\");\nend Hello;"
    ),
    LanguageInfo(
        name="LISP", ext=".lisp", phase=3, paradigm="Functional / Symbolic Metaprogramming", 
        glowColor="purple", sampleCode="(defun hello ()\n  (format t \"Hello, World!~%\"))\n(hello)"
    ),
    LanguageInfo(
        name="Algol", ext=".alg", phase=3, paradigm="Structured Procedural", 
        glowColor="purple", sampleCode="begin\n  print((\"Hello, World!\", newline))\nend"
    ),
    LanguageInfo(
        name="Smalltalk", ext=".st", phase=3, paradigm="Pure Message-Passing OOP", 
        glowColor="purple", sampleCode="Transcript show: 'Hello, World!'; cr."
    ),
    LanguageInfo(
        name="Prolog", ext=".pl", phase=3, paradigm="Logic / Declarative Rules", 
        glowColor="purple", sampleCode="hello :-\n    write('Hello, World!'), nl."
    ),

    # Phase 4: Declarative & Specialized (Gold Glow)
    LanguageInfo(
        name="SNOBOL4", ext=".sno", phase=4, paradigm="Pattern Matching String Processing", 
        glowColor="gold", sampleCode="      OUTPUT = \"HELLO WORLD\"\nEND"
    ),
    LanguageInfo(
        name="PL/I", ext=".pli", phase=4, paradigm="Structured Records", 
        glowColor="gold", sampleCode="hello: procedure options (main);\n   put list ('Hello, World!');\nend hello;"
    ),
    LanguageInfo(
        name="Modula-2", ext=".mod", phase=4, paradigm="Modular Strongly Typed", 
        glowColor="gold", sampleCode="MODULE Hello;\nFROM InOut IMPORT WriteString, WriteLn;\nBEGIN\n  WriteString(\"Hello, World!\");\n  WriteLn;\nEND Hello."
    ),
    LanguageInfo(
        name="RPG", ext=".rpg", phase=4, paradigm="Business Report Generation", 
        glowColor="gold", sampleCode="     D Name            S             10A   Inz('Rosetta')\n     C     'Hello '      dsply     Name"
    ),
    LanguageInfo(
        name="Eiffel", ext=".e", phase=4, paradigm="Design by Contract OOP", 
        glowColor="gold", sampleCode="class HELLO\ncreate make\nfeature\n    make is\n    do\n        io.put_string (\"Hello, World!%N\")\n    end\nend"
    ),
    LanguageInfo(
        name="Forth", ext=".fs", phase=4, paradigm="Stack-based Concatenative", 
        glowColor="gold", sampleCode=": HELLO ( -- ) CR .\" Hello, World!\" ;\nHELLO"
    ),
    LanguageInfo(
        name="ML", ext=".ml", phase=4, paradigm="Statically Typed Functional", 
        glowColor="gold", sampleCode="print \"Hello, World!\\n\";"
    ),

    # Phase 5: Emerging & Future (Green Glow)
    LanguageInfo(
        name="Solidity", ext=".sol", phase=5, paradigm="Smart Contracts / Blockchain", 
        glowColor="green", sampleCode="contract SimpleBank {\n    mapping(address => uint) balances;\n    event Transfer(address indexed from, address indexed to, uint amount);\n    \n    function deposit(uint amount) public payable {\n        balances[msg.sender] = balances[msg.sender] + amount;\n        emit Transfer(address(0), msg.sender, amount);\n    }\n}"
    ),
    LanguageInfo(
        name="Mojo", ext=".mojo", phase=5, paradigm="Accelerated AI Systems", 
        glowColor="green", sampleCode="@parameter\nfn process(inout x: Int) -> Int {\n    let y = 10;\n    x = x + y;\n    return x;\n}\n\nstruct Point {\n    var x: Float;\n    var y: Float;\n}"
    ),
    LanguageInfo(
        name="Zig", ext=".zig", phase=5, paradigm="Robust General Systems", 
        glowColor="green", sampleCode="const std = @import(\"std\");\n\npub fn add(x: i32, y: i32) i32 {\n    defer {\n        const temp = 1;\n    }\n    return x + y;\n}"
    ),
    LanguageInfo(
        name="Carbon", ext=".carbon", phase=5, paradigm="C++ Evolution Systems", 
        glowColor="green", sampleCode="package Geometry api;\n\ninterface Shape {\n    fn area() -> Float {\n    }\n}\n\nclass Circle {\n    var radius: Float;\n}\n\nimpl Circle as Shape {\n    fn area() -> Float {\n        let pi: Float = 3;\n        return pi;\n    }\n}"
    ),
    LanguageInfo(
        name="Arduino", ext=".ino", phase=5, paradigm="Embedded Systems C++",
        glowColor="cyan", sampleCode="void setup() {\n    Serial.begin(9600);\n    Serial.println(\"Hello from Arduino!\");\n}\n\nvoid loop() {\n}"
    ),

    # Phase 6: Universal & Specialized (45 Languages Matrix)
    LanguageInfo(
        name="C#", ext=".cs", phase=6, paradigm="Enterprise / Component OOP",
        glowColor="cyan", sampleCode="class Program {\n    static void Main() {\n        int x = 42;\n        System.Console.WriteLine(x);\n    }\n}"
    ),
    LanguageInfo(
        name="Dart", ext=".dart", phase=6, paradigm="Client-Optimized OOP",
        glowColor="cyan", sampleCode="void main() {\n  var name = 'Rosetta';\n  print('Hello, $name!');\n}"
    ),
    LanguageInfo(
        name="Lua", ext=".lua", phase=6, paradigm="Lightweight Embedded Scripting",
        glowColor="gold", sampleCode="local x = 10\nlocal y = 20\nprint(x + y)"
    ),
    LanguageInfo(
        name="R", ext=".r", phase=6, paradigm="Statistical & Data Computing",
        glowColor="purple", sampleCode="x <- c(10, 20, 30)\nprint(x)"
    ),
    LanguageInfo(
        name="Julia", ext=".jl", phase=6, paradigm="High-Performance Numerical",
        glowColor="green", sampleCode="function greet(name::String)\n    println(\"Hello, \", name)\nend\n\ngreet(\"Rosetta\")"
    ),
    LanguageInfo(
        name="Scala", ext=".scala", phase=6, paradigm="Functional & Object Systems",
        glowColor="cyan", sampleCode="object Main {\n  def main(args: Array[String]): Unit = {\n    val msg = \"Rosetta Universal\"\n    println(msg)\n  }\n}"
    ),
    LanguageInfo(
        name="Haskell", ext=".hs", phase=6, paradigm="Pure Functional / Strong Static",
        glowColor="purple", sampleCode="main :: IO ()\nmain = do\n  let x = 42\n  print x"
    ),
    LanguageInfo(
        name="Elixir", ext=".ex", phase=6, paradigm="Concurrent Actor / Fault-Tolerant",
        glowColor="green", sampleCode="defmodule Greeter do\n  def hello(name) do\n    IO.puts(\"Hello, #{name}!\")\n  end\nend\n\nGreeter.hello(\"Rosetta\")"
    ),
    LanguageInfo(
        name="Bash", ext=".sh", phase=6, paradigm="POSIX Shell / System Automation",
        glowColor="gold", sampleCode="#!/usr/bin/env bash\nset -euo pipefail\n\nNAME=\"Rosetta\"\necho \"Hello, ${NAME}!\""
    ),
    LanguageInfo(
        name="PowerShell", ext=".ps1", phase=6, paradigm="Object-Oriented Scripting",
        glowColor="cyan", sampleCode="Write-Host \"Hello, Rosetta from PowerShell!\""
    ),
    LanguageInfo(
        name="SQL", ext=".sql", phase=6, paradigm="Relational & Procedural Data",
        glowColor="purple", sampleCode="DECLARE @greeting NVARCHAR(50) = N'Hello, Rosetta!';\nPRINT @greeting;"
    ),
    LanguageInfo(
        name="Objective-C", ext=".m", phase=6, paradigm="Dynamic Smalltalk-style OOP",
        glowColor="cyan", sampleCode="#import <Foundation/Foundation.h>\n\nint main() {\n    @autoreleasepool {\n        NSLog(@\"Hello, Rosetta!\");\n    }\n    return 0;\n}"
    ),
    LanguageInfo(
        name="Move", ext=".move", phase=6, paradigm="Asset-Oriented Smart Contracts",
        glowColor="green", sampleCode="module 0x1::hello {\n    use std::debug;\n    public entry fun main() {\n        let x = 42;\n        debug::print(&x);\n    }\n}"
    ),
    LanguageInfo(
        name="Perl", ext=".pm", phase=6, paradigm="Practical Extraction & Scripting",
        glowColor="gold", sampleCode="use strict;\nuse warnings;\n\nmy $message = 'Hello, Rosetta!';\nprint $message, \"\\n\";"
    ),
]

@app.get("/")
def root():
    return {"message": "ROSETTA Engine API is active", "docs": "/docs", "health": "/api/health"}

@app.get("/api/health")
def health_check():
    """
    Rosetta Engine health check.
    """
    return {"status": "healthy", "engine": "ROSETTA v2.5.0-core", "timestamp": time.time()}

@app.get("/api/languages", response_model=LanguagesResponse)
def get_languages():
    """
    Returns lists of all supported built-in languages plus any dynamically learned languages.
    """
    from rosetta.cli.resolver import discover_learned_languages
    learned = discover_learned_languages()
    
    catalog = list(LANGUAGE_CATALOG)
    existing_exts = {l.ext for l in catalog}
    for lang_id, info in learned.items():
        ext = f".{lang_id}"
        if ext not in existing_exts:
            catalog.append(
                LanguageInfo(
                    name=lang_id.capitalize(),
                    ext=ext,
                    phase=7,
                    paradigm="Auto-Learned Dynamic Language",
                    glowColor="gold",
                    sampleCode=f"// Auto-learned {lang_id}\nfn main() {{\n    print(\"Hello from {lang_id}!\");\n}}"
                )
            )
            existing_exts.add(ext)
            
    return LanguagesResponse(languages=catalog)


@app.post("/api/learn", response_model=LearnResponse)
def post_learn(payload: LearnRequest):
    """
    Teaches Rosetta a new programming language at runtime via grammar, BNF, or corpus.
    The language is immediately compiled, registered, and ready for bidirectional transpilation!
    """
    from rosetta.autolearn.engine import AutoLearnEngine
    engine = AutoLearnEngine()
    
    try:
        if payload.grammar:
            # Check if payload.grammar is a path or raw text
            import tempfile, os
            if os.path.exists(payload.grammar):
                msg = engine.learn_from_grammar(payload.grammar, payload.name)
            else:
                with tempfile.NamedTemporaryFile("w", suffix=".g4", delete=False, encoding="utf-8") as f:
                    f.write(payload.grammar)
                    temp_path = f.name
                msg = engine.learn_from_grammar(temp_path, payload.name)
                os.remove(temp_path)
        elif payload.bnf:
            import tempfile, os
            if os.path.exists(payload.bnf):
                msg = engine.learn_from_bnf(payload.bnf, payload.name)
            else:
                with tempfile.NamedTemporaryFile("w", suffix=".bnf", delete=False, encoding="utf-8") as f:
                    f.write(payload.bnf)
                    temp_path = f.name
                msg = engine.learn_from_bnf(temp_path, payload.name)
                os.remove(temp_path)
        elif payload.corpus:
            import tempfile, os
            if os.path.exists(payload.corpus):
                msg = engine.learn_from_corpus(payload.corpus, payload.name)
            else:
                with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
                    f.write(payload.corpus)
                    temp_path = f.name
                msg = engine.learn_from_corpus(temp_path, payload.name)
                os.remove(temp_path)
        else:
            raise HTTPException(status_code=400, detail="Provide grammar, bnf, or corpus in payload")
            
        lang_id = (payload.name or "custom").lower()
        return LearnResponse(
            success=True,
            message=msg,
            language_id=lang_id,
            ext=f".{lang_id}"
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/detect", response_model=DetectResponse)
def post_detect(payload: DetectRequest):
    """
    Heuristically checks code structural markers to identify source language.
    """
    try:
        res = detect_language(payload.source)
        return DetectResponse(language=res["language"], confidence=res["confidence"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/transpile", response_model=TranspileResponse)
def post_transpile(payload: TranspileRequest):
    """
    Invokes the active transpilation pipeline using Rosetta IR Babel frontend and Cipher target.
    """
    try:
        res = transpile_code(payload.source, payload.from_lang, payload.to_lang)
        return TranspileResponse(
            result=res["result"],
            tokens_used=res["tokens_used"],
            time_ms=res["time_ms"],
            ast=res.get("ast"),
            passes=res.get("passes"),
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/inspect")
def post_inspect(payload: TranspileRequest):
    """
    Returns the serialized Rosetta IR AST before and after HERMES passes.
    """
    try:
        return inspect_code(payload.source, payload.from_lang, payload.to_lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
