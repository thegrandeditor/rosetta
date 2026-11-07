import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const source = body.source || "";
    const apiBase = (process.env.ROSETTA_API_URL || process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8008").replace(/\/$/, "");

    // 1. Try FastAPI server first (local or remote cloud deployment)
    try {
      const response = await fetch(`${apiBase}/api/detect`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(3000),
      });

      if (response.ok) {
        const data = await response.json();
        return NextResponse.json(data);
      }
    } catch (e) {
      // Fallback to static heuristics in API route
    }

    // 2. High-fidelity static heuristics (works everywhere, including Vercel)
    const result = detectLanguageHeuristically(source);
    return NextResponse.json(result);

  } catch (err: any) {
    return NextResponse.json(
      { error: err.message || "Failed to auto-detect language" },
      { status: 500 }
    );
  }
}

function detectLanguageHeuristically(source: string) {
  const SIGNATURES: Record<string, string[]> = {
    "cobol": [
      "IDENTIFICATION DIVISION",
      "PROGRAM-ID",
      "DATA DIVISION",
      "WORKING-STORAGE SECTION",
      "PROCEDURE DIVISION",
      "DISPLAY",
      "STOP RUN"
    ],
    "solidity": [
      "pragma solidity",
      "contract ",
      "mapping",
      "event ",
      "emit "
    ],
    "mojo": [
      "@parameter",
      "fn ",
      "inout",
      "struct ",
      "let ",
      "var "
    ],
    "zig": [
      "@import",
      "pub fn ",
      "defer ",
      "errdefer ",
      "std.debug.print"
    ],
    "carbon": [
      "package ",
      "interface ",
      "impl ",
      "class "
    ],
    "fortran": [
      "PROGRAM ",
      "PRINT *,",
      "SUBROUTINE ",
      "END PROGRAM"
    ],
    "python": [
      "def ",
      "import ",
      "from ",
      "print(",
      "elif ",
      "__main__"
    ],
    "rust": [
      "fn main()",
      "let mut ",
      "println!",
      "use std::"
    ],
    "go": [
      "package main",
      "func main()",
      "import (",
      "fmt.Print"
    ],
    "csharp": [
      "Console.WriteLine",
      "using System;",
      "namespace "
    ],
    "dart": [
      "void main()",
      "package:flutter",
      "print("
    ],
    "lua": [
      "local ",
      "function ",
      "end"
    ],
    "r": [
      " <- ",
      "library(",
      "setRefClass("
    ],
    "julia": [
      "println(",
      "::String",
      "::Vector{"
    ],
    "scala": [
      "object Main",
      "Array[String]",
      "val "
    ],
    "haskell": [
      "module Main where",
      "main :: IO",
      "putStrLn"
    ],
    "elixir": [
      "defmodule ",
      "IO.puts(",
      "defstruct "
    ],
    "bash": [
      "#!/usr/bin/env bash",
      "#!/bin/bash",
      "echo "
    ],
    "sql": [
      "DECLARE @",
      "SELECT ",
      "PRINT @"
    ],
    "objc": [
      "#import <Foundation/Foundation.h>",
      "NSLog(@",
      "@interface "
    ],
    "move": [
      "module 0x",
      "public entry fun",
      "debug::print"
    ],
    "perl": [
      "use strict;",
      "use warnings;",
      "my $"
    ]
  };

  const scores: Record<string, number> = {};
  for (const lang of Object.keys(SIGNATURES)) {
    scores[lang] = 0;
    for (const signature of SIGNATURES[lang]) {
      const regex = new RegExp(signature.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
      const matches = source.match(regex);
      if (matches) {
        scores[lang] += matches.length * 20;
      }
    }
  }

  let detectedLang = "python";
  let highestScore = 0;
  for (const [lang, score] of Object.entries(scores)) {
    if (score > highestScore) {
      highestScore = score;
      detectedLang = lang;
    }
  }

  const confidence = Math.min(highestScore / 100.0, 1.0) || 0.35;
  const extMapping: Record<string, string> = {
    "cobol": ".cbl",
    "solidity": ".sol",
    "mojo": ".mojo",
    "zig": ".zig",
    "carbon": ".carbon",
    "fortran": ".f90",
    "python": ".py",
    "rust": ".rs",
    "go": ".go",
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
    "perl": ".pm"
  };

  return {
    language: extMapping[detectedLang] || ".py",
    confidence: Number(confidence.toFixed(2))
  };
}
