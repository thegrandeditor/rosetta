import { NextResponse } from "next/server";

const FALLBACK_LANGUAGES = [
  { name: "Python", ext: ".py", phase: 1, paradigm: "Multi-paradigm", glowColor: "cyan", sampleCode: "def greet(name: str):\n    print(f\"Hello, {name}!\")\n\ngreet(\"Rosetta\")" },
  { name: "JavaScript", ext: ".js", phase: 1, paradigm: "Event-driven / Prototype", glowColor: "cyan", sampleCode: "function greet(name) {\n    console.log(`Hello, ${name}!`);\n}\n\ngreet(\"Rosetta\");" },
  { name: "TypeScript", ext: ".ts", phase: 1, paradigm: "Static OOP / Functional", glowColor: "cyan", sampleCode: "function greet(name: string): void {\n    console.log(`Hello, ${name}!`);\n}\n\ngreet(\"Rosetta\");" },
  { name: "Java", ext: ".java", phase: 1, paradigm: "Strict Object-Oriented", glowColor: "cyan", sampleCode: "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Rosetta!\");\n    }\n}" },
  { name: "C++", ext: ".cpp", phase: 1, paradigm: "Systems OOP / Generic", glowColor: "cyan", sampleCode: "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, Rosetta!\" << std::endl;\n    return 0;\n}" },
  { name: "C", ext: ".c", phase: 1, paradigm: "Procedural / Imperative", glowColor: "cyan", sampleCode: "#include <stdio.h>\n\nint main() {\n    printf(\"Hello, Rosetta!\\n\");\n    return 0;\n}" },
  { name: "Rust", ext: ".rs", phase: 1, paradigm: "Concurrent / Safe Systems", glowColor: "cyan", sampleCode: "fn main() {\n    println!(\"Hello, Rosetta!\");\n}" },
  { name: "Go", ext: ".go", phase: 1, paradigm: "Concurrent / Procedural", glowColor: "cyan", sampleCode: "package main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"Hello, Rosetta!\")\n}" },
  { name: "Swift", ext: ".swift", phase: 1, paradigm: "Protocols / Multi-paradigm", glowColor: "cyan", sampleCode: "print(\"Hello, Rosetta!\")" },
  { name: "Kotlin", ext: ".kt", phase: 1, paradigm: "Modern Functional OOP", glowColor: "cyan", sampleCode: "fun main() {\n    println(\"Hello, Rosetta!\")\n}" },
  { name: "Ruby", ext: ".rb", phase: 1, paradigm: "Dynamic OOP / Scripting", glowColor: "cyan", sampleCode: "puts 'Hello, Rosetta!'" },
  { name: "PHP", ext: ".php", phase: 1, paradigm: "Dynamic Web Scripting", glowColor: "cyan", sampleCode: "<?php\necho \"Hello, Rosetta!\";\n?>" },
  { name: "COBOL", ext: ".cbl", phase: 2, paradigm: "Business / Legacy Record", glowColor: "cyan", sampleCode: "       DATA DIVISION.\n       WORKING-STORAGE SECTION.\n       01 GREETING PIC X(12) VALUE 'HELLO ROSETTA'.\n       PROCEDURE DIVISION.\n           DISPLAY GREETING.\n           STOP RUN." },
  { name: "Fortran", ext: ".f90", phase: 3, paradigm: "Numeric Computing", glowColor: "purple", sampleCode: "PROGRAM HELLO\n    PRINT *, 'Hello, World!'\nEND PROGRAM HELLO" },
  { name: "BASIC", ext: ".bas", phase: 3, paradigm: "Procedural Imperative", glowColor: "purple", sampleCode: "10 PRINT \"HELLO WORLD\"\n20 END" },
  { name: "Pascal", ext: ".pas", phase: 3, paradigm: "Structured / Strongly Typed", glowColor: "purple", sampleCode: "program Hello;\nbegin\n  writeln('Hello, World!');\nend." },
  { name: "Ada", ext: ".adb", phase: 3, paradigm: "Concurrent / Real-time Systems", glowColor: "purple", sampleCode: "with Ada.Text_IO; use Ada.Text_IO;\nprocedure Hello is\nbegin\n  Put_Line(\"Hello, World!\");\nend Hello;" },
  { name: "LISP", ext: ".lisp", phase: 3, paradigm: "Homoiconic / Functional", glowColor: "purple", sampleCode: "(print \"Hello, World!\")" },
  { name: "Algol", ext: ".alg", phase: 3, paradigm: "Block-structured Procedural", glowColor: "purple", sampleCode: "BEGIN\n   outstring(1, \"Hello, World!\");\nEND" },
  { name: "Smalltalk", ext: ".st", phase: 3, paradigm: "Pure Message-Passing OOP", glowColor: "purple", sampleCode: "Transcript show: 'Hello, World!'." },
  { name: "Prolog", ext: ".pl", phase: 3, paradigm: "Declarative Logic", glowColor: "purple", sampleCode: "greet(rosetta).\n?- greet(X)." },
  { name: "SNOBOL4", ext: ".sno", phase: 4, paradigm: "Pattern Matching / Strings", glowColor: "gold", sampleCode: "      OUTPUT = 'Hello, World!'\nEND" },
  { name: "PL/I", ext: ".pli", phase: 4, paradigm: "Enterprise Scientific / Business", glowColor: "gold", sampleCode: "HELLO: PROCEDURE OPTIONS(MAIN);\n   PUT LIST('Hello, World!');\nEND HELLO;" },
  { name: "Modula-2", ext: ".mod", phase: 4, paradigm: "Modular Systems", glowColor: "gold", sampleCode: "MODULE Hello;\nBEGIN\nEND Hello." },
  { name: "RPG", ext: ".rpg", phase: 4, paradigm: "IBM i Transactional Business", glowColor: "gold", sampleCode: "     C     'Hello'       DSPLY\n     C                   SETON                                        LR" },
  { name: "Eiffel", ext: ".e", phase: 4, paradigm: "Design by Contract OOP", glowColor: "gold", sampleCode: "class HELLO\nfeature\n   make do print (\"Hello\") end\nend" },
  { name: "Forth", ext: ".fs", phase: 4, paradigm: "Stack-based Concatenative", glowColor: "gold", sampleCode: ": HELLO CR .\" Hello, World!\" ;\nHELLO" },
  { name: "ML", ext: ".ml", phase: 4, paradigm: "Statically Typed Functional", glowColor: "gold", sampleCode: "print \"Hello, World!\\n\";" },
  { name: "Solidity", ext: ".sol", phase: 5, paradigm: "Smart Contracts / Blockchain", glowColor: "green", sampleCode: "contract SimpleBank {\n    mapping(address => uint) balances;\n}" },
  { name: "Mojo", ext: ".mojo", phase: 5, paradigm: "Accelerated AI Systems", glowColor: "green", sampleCode: "fn main():\n    let x = 42\n    print(x)" },
  { name: "Zig", ext: ".zig", phase: 5, paradigm: "Robust General Systems", glowColor: "green", sampleCode: "const std = @import(\"std\");\npub fn add(x: i32, y: i32) i32 {\n    return x + y;\n}" },
  { name: "Carbon", ext: ".carbon", phase: 5, paradigm: "C++ Evolution Systems", glowColor: "green", sampleCode: "package Geometry api;\nclass Circle {\n    var radius: Float;\n}" },
  { name: "C#", ext: ".cs", phase: 6, paradigm: "Enterprise / Component OOP", glowColor: "cyan", sampleCode: "class Program {\n    static void Main() {\n        int x = 42;\n        Console.WriteLine(x);\n    }\n}" },
  { name: "Dart", ext: ".dart", phase: 6, paradigm: "Client-Optimized OOP", glowColor: "cyan", sampleCode: "void main() {\n  var name = 'Rosetta';\n  print(name);\n}" },
  { name: "Lua", ext: ".lua", phase: 6, paradigm: "Lightweight Embedded Scripting", glowColor: "gold", sampleCode: "local x = 10\nprint(x)" },
  { name: "R", ext: ".r", phase: 6, paradigm: "Statistical & Data Computing", glowColor: "purple", sampleCode: "x <- 42\nprint(x)" },
  { name: "Julia", ext: ".jl", phase: 6, paradigm: "High-Performance Numerical", glowColor: "green", sampleCode: "x = 42\nprintln(x)" },
  { name: "Scala", ext: ".scala", phase: 6, paradigm: "Functional & Object Systems", glowColor: "cyan", sampleCode: "object Main {\n  val msg = \"Rosetta\"\n  println(msg)\n}" },
  { name: "Haskell", ext: ".hs", phase: 6, paradigm: "Pure Functional / Strong Static", glowColor: "purple", sampleCode: "main = do\n  let x = 42\n  print x" },
  { name: "Elixir", ext: ".ex", phase: 6, paradigm: "Concurrent Actor / Fault-Tolerant", glowColor: "green", sampleCode: "defmodule Main do\n  IO.puts(\"Hello, Rosetta!\")\nend" },
  { name: "Bash", ext: ".sh", phase: 6, paradigm: "POSIX Shell / System Automation", glowColor: "gold", sampleCode: "#!/usr/bin/env bash\nNAME=\"Rosetta\"\necho $NAME" },
  { name: "SQL", ext: ".sql", phase: 6, paradigm: "Relational & Procedural Data", glowColor: "purple", sampleCode: "DECLARE @x INT = 42;\nPRINT @x;" },
  { name: "Objective-C", ext: ".m", phase: 6, paradigm: "Dynamic Smalltalk-style OOP", glowColor: "cyan", sampleCode: "int x = 42;\nNSLog(@\"%d\", x);" },
  { name: "Move", ext: ".move", phase: 6, paradigm: "Asset-Oriented Smart Contracts", glowColor: "green", sampleCode: "module 0x1::hello {\n    public entry fun main() {\n        let x = 42;\n        debug::print(&x);\n    }\n}" },
  { name: "Perl", ext: ".pm", phase: 6, paradigm: "Practical Extraction & Scripting", glowColor: "gold", sampleCode: "use strict;\nmy $x = 42;\nprint $x;" },
  { name: "Visual Basic", ext: ".vb", phase: 3, paradigm: "Event-Driven Rapid App", glowColor: "purple", sampleCode: "Module Program\n    Sub Main()\n        Console.WriteLine(\"Hello from VB!\")\n    End Sub\nEnd Module" },
  { name: "Delphi", ext: ".delphi", phase: 3, paradigm: "Object Pascal Native", glowColor: "purple", sampleCode: "program HelloDelphi;\nbegin\n    Writeln('Hello from Delphi!');\nend." },
  { name: "PowerShell", ext: ".ps1", phase: 6, paradigm: "Object-Oriented Scripting", glowColor: "cyan", sampleCode: "Write-Host \"Hello, Rosetta from PowerShell!\"" },
  { name: "Arduino", ext: ".ino", phase: 5, paradigm: "Embedded Systems C++", glowColor: "cyan", sampleCode: "void setup() {\n    Serial.begin(9600);\n}\nvoid loop() {}" },
  { name: "Matlab", ext: ".matlab", phase: 6, paradigm: "Matrix & Technical Numerical", glowColor: "cyan", sampleCode: "A = [1 2; 3 4];\nv = [1; 0];\ndisp(A * v);" },
  { name: "VBA", ext: ".vba", phase: 3, paradigm: "Office Automation & Event-Driven", glowColor: "purple", sampleCode: "Sub RosettaGreet()\n    MsgBox \"Hello from VBA!\"\nEnd Sub" },
  { name: "Assembly", ext: ".asm", phase: 3, paradigm: "Low-Level Machine Code", glowColor: "gold", sampleCode: "global _start\nsection .text\n_start:\n    mov rax, 60\n    syscall" },
  { name: "HCL", ext: ".tf", phase: 6, paradigm: "Declarative Infrastructure-as-Code", glowColor: "purple", sampleCode: "variable \"region\" {\n  default = \"us-east-1\"\n}" },
  { name: "GraphQL", ext: ".gql", phase: 6, paradigm: "Declarative Schema & Query Language", glowColor: "green", sampleCode: "type Query {\n  languages: [String!]!\n}" }
];

export async function GET() {
  const apiBase = (process.env.ROSETTA_API_URL || process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8008").replace(/\/$/, "");
  try {
    const response = await fetch(`${apiBase}/api/languages`, {
      signal: AbortSignal.timeout(3500),
      cache: "no-store",
    });
    if (response.ok) {
      const data = await response.json();
      return NextResponse.json(data);
    }
  } catch (e) {
    // Fallback to static 45-language catalog when FastAPI is unreachable
  }
  return NextResponse.json({ languages: FALLBACK_LANGUAGES });
}
