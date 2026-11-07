"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, Play, Globe, Award, ArrowRightLeft } from "lucide-react";
import Link from "next/link";

interface LanguageDetail {
  name: string;
  ext: string;
  phase: number;
  paradigm: string;
  type: string;
  description: string;
  strengths: string[];
  sources: string[];
  targets: string[];
}

const CATALOG_DETAILS: LanguageDetail[] = [
  {
    name: "Python", ext: ".py", phase: 1, paradigm: "Multi-paradigm", type: "General",
    description: "Highly readable general-purpose language preferred for AI, scripting, and web frameworks.",
    strengths: ["Readability", "Rich ecosystems", "Rapid prototyping"],
    sources: ["COBOL", "BASIC", "FORTRAN", "LISP", "Java", "C++", "C"],
    targets: ["JavaScript", "C++", "Rust", "Go", "Mojo"]
  },
  {
    name: "JavaScript", ext: ".js", phase: 1, paradigm: "Event-driven", type: "Web",
    description: "The ubiquitous engine of web clients and servers running asynchronously on the V8 engine.",
    strengths: ["Ubiquity", "Dynamic features", "Event-driven loops"],
    sources: ["Python", "Java", "C++", "TypeScript", "ML"],
    targets: ["Python", "Rust", "Go"]
  },
  {
    name: "TypeScript", ext: ".ts", phase: 1, paradigm: "Static OOP", type: "Web",
    description: "Strict syntactical superset of JavaScript adding optional static typing for structural safety.",
    strengths: ["Type safety", "IntelliSense", "Refactoring safety"],
    sources: ["JavaScript", "Java", "C++"],
    targets: ["JavaScript", "Python", "Rust"]
  },
  {
    name: "Java", ext: ".java", phase: 1, paradigm: "Object-Oriented", type: "General",
    description: "Enterprise runtime standard using class-based structures and JVM bytecode safety.",
    strengths: ["Cross-platform JVM", "Type system", "Enterprise support"],
    sources: ["COBOL", "PL/I", "Ada", "BASIC"],
    targets: ["Python", "C++", "Kotlin"]
  },
  {
    name: "C++", ext: ".cpp", phase: 1, paradigm: "Systems OOP", type: "Systems",
    description: "Extremely optimized, static-typed compilation standard supporting granular memory handles.",
    strengths: ["High performance", "Memory manipulation", "Hardware control"],
    sources: ["C", "Ada", "Fortran", "Modula-2"],
    targets: ["Rust", "Carbon", "Python"]
  },
  {
    name: "C", ext: ".c", phase: 1, paradigm: "Procedural", type: "Systems",
    description: "System standard procedural structure that directly manipulates machine code and pointers.",
    strengths: ["Minimal overhead", "Portability", "Direct hardware maps"],
    sources: ["Algol", "Pascal", "BASIC"],
    targets: ["C++", "Rust", "Zig"]
  },
  {
    name: "Rust", ext: ".rs", phase: 1, paradigm: "Safe Systems", type: "Systems",
    description: "Ultra-high performance systems dialect securing memory invariants via borrow checking.",
    strengths: ["Memory safety", "Concurrency stability", "Rich cargo ecosystem"],
    sources: ["C++", "C", "Go", "Ada"],
    targets: ["C++", "JavaScript", "Python"]
  },
  {
    name: "Go", ext: ".go", phase: 1, paradigm: "Concurrent", type: "Systems",
    description: "Static dialect supporting ultra-fast network servers using goroutine channels.",
    strengths: ["Concurrency simplicity", "Fast builds", "Single binary builds"],
    sources: ["C++", "Java", "Python"],
    targets: ["Rust", "TypeScript"]
  },
  {
    name: "Swift", ext: ".swift", phase: 1, paradigm: "Multi-paradigm", type: "Mobile",
    description: "Fast, safe, and interactive Apple compiler ecosystem replacing Objective-C.",
    strengths: ["Memory safety", "Fast compile runs", "SwiftUI rendering"],
    sources: ["Java", "C++", "Python"],
    targets: ["Rust", "Python"]
  },
  {
    name: "Kotlin", ext: ".kt", phase: 1, paradigm: "Functional OOP", type: "Mobile",
    description: "Modern JVM dialect designed as a concise, null-safe Java replacement.",
    strengths: ["Null safety", "Interoperability", "Expressive syntax"],
    sources: ["Java", "Python"],
    targets: ["Java", "JavaScript"]
  },
  {
    name: "Ruby", ext: ".rb", phase: 1, paradigm: "Dynamic OOP", type: "General",
    description: "Dynamic language focusing on simplicity and productivity.",
    strengths: ["Developer happiness", "Elegant syntax", "Metaprogramming"],
    sources: ["Python", "Smalltalk", "LISP"],
    targets: ["Python", "JavaScript"]
  },
  {
    name: "PHP", ext: ".php", phase: 1, paradigm: "Web Scripting", type: "Web",
    description: "Server-side scripting engine specifically built for dynamic web presentation.",
    strengths: ["Fast deployment", "Database mapping", "Massive web footprint"],
    sources: ["C", "Java", "Python"],
    targets: ["JavaScript", "Python"]
  },
  {
    name: "COBOL", ext: ".cbl", phase: 2, paradigm: "Business", type: "Enterprise",
    description: "Legacy business and financial transaction processing monolith powering global banking.",
    strengths: ["High-precision math", "Record parsing", "Mainframe stability"],
    sources: ["PL/I", "RPG"],
    targets: ["Python", "Java", "Rust", "C++"]
  },
  {
    name: "Fortran", ext: ".f90", phase: 3, paradigm: "Numeric", type: "Scientific",
    description: "Scientific and engineering numeric processing engine optimized for supercomputers.",
    strengths: ["Matrix processing", "Scientific computations", "Vectorization"],
    sources: ["Algol", "BASIC"],
    targets: ["Python", "C++", "Mojo"]
  },
  {
    name: "BASIC", ext: ".bas", phase: 3, paradigm: "Procedural", type: "General",
    description: "Classic symbolic instruction code designed for straightforward procedural programming.",
    strengths: ["Simplicity", "Interactive parsing", "Minimal footprint"],
    sources: ["Fortran"],
    targets: ["Python", "Pascal", "Java"]
  },
  {
    name: "Pascal", ext: ".pas", phase: 3, paradigm: "Structured", type: "General",
    description: "Classic structured syntax standard enforcing clean software design.",
    strengths: ["Structured loops", "Strong typing", "Clean readability"],
    sources: ["Algol"],
    targets: ["C", "Ada", "Python"]
  },
  {
    name: "Ada", ext: ".adb", phase: 3, paradigm: "Concurrent", type: "Systems",
    description: "Mission-critical systems dialect enforcing design-by-contract safety architectures.",
    strengths: ["Safety runtime", "Strong concurrency", "High integrity"],
    sources: ["Pascal", "Algol"],
    targets: ["C++", "Rust", "Java"]
  },
  {
    name: "LISP", ext: ".lisp", phase: 3, paradigm: "Functional", type: "Symbolic",
    description: "Pioneering functional symbolic language utilizing parenthesized S-expressions.",
    strengths: ["Homoiconicity", "Extensible macros", "Symbolic parsing"],
    sources: ["Prolog", "ML"],
    targets: ["Python", "JavaScript", "Rust"]
  },
  {
    name: "Algol", ext: ".alg", phase: 3, paradigm: "Procedural", type: "Historical",
    description: "The historical ancestor of structured block-level procedural programming.",
    strengths: ["Algorithm validation", "Block nested structures", "Lexical scope"],
    sources: ["Fortran"],
    targets: ["Pascal", "C", "Ada"]
  },
  {
    name: "Smalltalk", ext: ".st", phase: 3, paradigm: "Pure OOP", type: "General",
    description: "Pure object-oriented architecture based on message passing.",
    strengths: ["Dynamic reflection", "Message loops", "Live object systems"],
    sources: ["LISP"],
    targets: ["Ruby", "Java", "Python"]
  },
  {
    name: "Prolog", ext: ".pl", phase: 3, paradigm: "Logic", type: "AI",
    description: "Declarative logic programming framework resolved via facts and rules.",
    strengths: ["Pattern matching", "Database reasoning", "AI heuristics"],
    sources: ["LISP"],
    targets: ["Python", "JavaScript", "Rust"]
  },
  {
    name: "SNOBOL4", ext: ".sno", phase: 4, paradigm: "Pattern Match", type: "Strings",
    description: "Specialized string-processing and pattern-matching language.",
    strengths: ["Text manipulation", "Pattern matching", "Dynamic strings"],
    sources: ["COBOL", "BASIC"],
    targets: ["Python", "JavaScript"]
  },
  {
    name: "PL/I", ext: ".pli", phase: 4, paradigm: "Structured", type: "Enterprise",
    description: "IBM mainframe architecture combining scientific and business transaction processing.",
    strengths: ["Broad data specs", "Structured buffers", "Mainframe stability"],
    sources: ["COBOL", "Algol", "Fortran"],
    targets: ["Java", "Python", "C++"]
  },
  {
    name: "Modula-2", ext: ".mod", phase: 4, paradigm: "Modular", type: "Systems",
    description: "Pascal successor introducing modular compiler partitions and encapsulated units.",
    strengths: ["Modular abstraction", "Type safety", "Low-level system link"],
    sources: ["Pascal"],
    targets: ["Ada", "C++", "Rust"]
  },
  {
    name: "RPG", ext: ".rpg", phase: 4, paradigm: "Report Gen", type: "Enterprise",
    description: "IBM i / AS/400 high-level business application and report generation language.",
    strengths: ["Tabular data layouts", "Mainframe speed", "Record formatting"],
    sources: ["COBOL", "PL/I"],
    targets: ["Java", "Python"]
  },
  {
    name: "Eiffel", ext: ".e", phase: 4, paradigm: "Contract OOP", type: "General",
    description: "Object-oriented language pioneering Design by Contract (pre/postconditions).",
    strengths: ["Design by Contract", "Multiple inheritance", "Void safety"],
    sources: ["Ada", "Smalltalk"],
    targets: ["C++", "Java", "Python"]
  },
  {
    name: "Forth", ext: ".fs", phase: 4, paradigm: "Stack-based", type: "Systems",
    description: "Minimalist stack-based environment utilizing Reverse Polish Notation words.",
    strengths: ["Extreme lightweight", "Direct hardware control", "Rapid stack execution"],
    sources: ["C", "BASIC"],
    targets: ["C", "Python", "Rust"]
  },
  {
    name: "ML", ext: ".ml", phase: 4, paradigm: "Functional", type: "General",
    description: "Functional programming language featuring Hindley-Milner static type inference.",
    strengths: ["Type inference", "Pattern matching", "Algebraic data types"],
    sources: ["LISP"],
    targets: ["Rust", "TypeScript", "Python"]
  },
  {
    name: "Solidity", ext: ".sol", phase: 5, paradigm: "Smart Contract", type: "Blockchain",
    description: "Contract-oriented language for implementing smart contracts on EVM blockchains.",
    strengths: ["Ethereum EVM support", "State variable safety", "Events & modifiers"],
    sources: ["JavaScript", "C++", "Python"],
    targets: ["TypeScript", "Python", "Rust"]
  },
  {
    name: "Mojo", ext: ".mojo", phase: 5, paradigm: "AI Hardware", type: "AI",
    description: "High-performance Python superset designed for AI hardware and SIMD accelerators.",
    strengths: ["Python syntax compatibility", "MLIR performance", "Zero-cost abstractions"],
    sources: ["Python", "C++", "Rust"],
    targets: ["Python", "C++", "Rust"]
  },
  {
    name: "Zig", ext: ".zig", phase: 5, paradigm: "Robust Systems", type: "Systems",
    description: "Modern C replacement eliminating hidden control flow and preprocessor macros.",
    strengths: ["Comptime execution", "No hidden allocations", "Seamless C ABI"],
    sources: ["C", "C++"],
    targets: ["C", "Rust", "Python"]
  },
  {
    name: "Carbon", ext: ".carbon", phase: 5, paradigm: "C++ Successor", type: "Systems",
    description: "Experimental C++ successor with clean modern generics and bidirectional C++ interop.",
    strengths: ["C++ interoperability", "Modern syntax", "Memory safety migration"],
    sources: ["C++", "Rust"],
    targets: ["C++", "Rust", "Python"]
  },
  {
    name: "C#", ext: ".cs", phase: 6, paradigm: "Enterprise OOP", type: "General",
    description: "Modern, component-oriented language powering .NET cloud services, game development, and desktop apps.",
    strengths: ["Rich standard library", "Strong type system", "Async/await natively"],
    sources: ["Java", "C++", "Python"],
    targets: ["Java", "Python", "Rust", "TypeScript"]
  },
  {
    name: "Dart", ext: ".dart", phase: 6, paradigm: "Client-Optimized OOP", type: "Mobile",
    description: "Client-optimized language for fast apps on any platform, foundation of Flutter multiplatform UI.",
    strengths: ["Hot reload", "AOT & JIT compilation", "Sound null safety"],
    sources: ["JavaScript", "TypeScript", "Java"],
    targets: ["TypeScript", "JavaScript", "Python"]
  },
  {
    name: "Lua", ext: ".lua", phase: 6, paradigm: "Embedded Scripting", type: "Scripting",
    description: "Powerful, efficient, lightweight scripting language designed for extending applications and game engines.",
    strengths: ["Embeddable", "Ultra-fast execution", "Tiny footprint"],
    sources: ["Python", "JavaScript", "Ruby"],
    targets: ["Python", "JavaScript", "C"]
  },
  {
    name: "R", ext: ".r", phase: 6, paradigm: "Statistical Computing", type: "Scientific",
    description: "Leading language and environment for statistical computing, graphics, bioinformatics, and data analysis.",
    strengths: ["Matrix/vector operations", "Rich CRAN ecosystem", "Publication graphics"],
    sources: ["Python", "Julia"],
    targets: ["Python", "Julia"]
  },
  {
    name: "Julia", ext: ".jl", phase: 6, paradigm: "High-Performance Numerical", type: "Scientific",
    description: "High-level, high-performance dynamic programming language for technical, numerical, and scientific computing.",
    strengths: ["Solves two-language problem", "Multiple dispatch", "C-like speed"],
    sources: ["Python", "R", "C++"],
    targets: ["Python", "C++", "Rust"]
  },
  {
    name: "Scala", ext: ".scala", phase: 6, paradigm: "Functional & Object", type: "General",
    description: "Combines object-oriented and functional programming in one concise, high-level JVM language.",
    strengths: ["Advanced type system", "Concurrency with Akka", "JVM ecosystem"],
    sources: ["Java", "Haskell", "Python"],
    targets: ["Java", "Kotlin", "Python"]
  },
  {
    name: "Haskell", ext: ".hs", phase: 6, paradigm: "Pure Functional", type: "Functional",
    description: "Pioneering purely functional language with strong static typing, lazy evaluation, and type classes.",
    strengths: ["Mathematical purity", "Compile-time correctness", "High concurrency"],
    sources: ["ML", "LISP", "Scala"],
    targets: ["Scala", "Rust", "Python"]
  },
  {
    name: "Elixir", ext: ".ex", phase: 6, paradigm: "Concurrent Actor", type: "Systems",
    description: "Dynamic, functional language designed for building scalable and maintainable applications on the Erlang BEAM.",
    strengths: ["Extreme fault tolerance", "Massive concurrency", "Distributed by default"],
    sources: ["Ruby", "Python", "Erlang"],
    targets: ["Rust", "Go", "Python"]
  },
  {
    name: "Bash", ext: ".sh", phase: 6, paradigm: "Shell Automation", type: "DevOps",
    description: "Standard UNIX shell command language for DevOps, pipeline automation, and system administration.",
    strengths: ["Universal system availability", "Pipeline chaining", "Process orchestration"],
    sources: ["Python", "Perl"],
    targets: ["Python", "Go"]
  },
  {
    name: "SQL", ext: ".sql", phase: 6, paradigm: "Relational / Procedural", type: "Database",
    description: "Domain-specific language for managing data held in relational database management systems.",
    strengths: ["Declarative set operations", "Optimized query planners", "ACID guarantees"],
    sources: ["Python"],
    targets: ["Python"]
  },
  {
    name: "Objective-C", ext: ".m", phase: 6, paradigm: "Smalltalk OOP", type: "Mobile",
    description: "Apple's foundational language blending C with Smalltalk messaging for macOS and iOS app ecosystems.",
    strengths: ["Dynamic runtime dispatch", "Seamless C/C++ interop", "Deep Cocoa legacy"],
    sources: ["Swift", "C++", "Java"],
    targets: ["Swift", "C++", "Rust"]
  },
  {
    name: "Move", ext: ".move", phase: 6, paradigm: "Smart Contracts", type: "Blockchain",
    description: "Next-generation smart contract language designed with first-class resources and verifiable safety for Aptos/Sui.",
    strengths: ["Linear logic resources", "Formal verification", "Reentrancy immunity"],
    sources: ["Rust", "Solidity"],
    targets: ["Rust", "Solidity"]
  },
  {
    name: "Perl", ext: ".pm", phase: 6, paradigm: "Text & Scripting", type: "Scripting",
    description: "Highly capable, feature-rich programming language with 36 years of development and CPAN ecosystem.",
    strengths: ["Regular expressions", "System scripting", "Text parsing"],
    sources: ["Python", "Ruby", "Bash"],
    targets: ["Python", "Bash"]
  }
];

export default function LanguagesClient() {
  const [search, setSearch] = useState("");
  const [selectedPhase, setSelectedPhase] = useState<number | "all">("all");
  const [focusedLanguage, setFocusedLanguage] = useState<LanguageDetail | null>(null);

  const phases = [
    { num: 1, label: "Phase 1: Modern" },
    { num: 2, label: "Phase 2: Enterprise" },
    { num: 3, label: "Phase 3: Legacy" },
    { num: 4, label: "Phase 4: Specialized" },
    { num: 5, label: "Phase 5: Emerging" },
    { num: 6, label: "Phase 6: Universal" },
  ];

  const filteredList = CATALOG_DETAILS.filter((lang) => {
    const matchesSearch =
      lang.name.toLowerCase().includes(search.toLowerCase()) ||
      lang.ext.toLowerCase().includes(search.toLowerCase()) ||
      lang.paradigm.toLowerCase().includes(search.toLowerCase());
    const matchesPhase = selectedPhase === "all" || lang.phase === selectedPhase;
    return matchesSearch && matchesPhase;
  });

  return (
    <div className="min-h-screen bg-[#FAF6F0] text-[#141413] py-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        
        {/* Title */}
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#D6CFC2] bg-white text-xs font-mono font-bold text-[#F40009] uppercase tracking-widest mb-3">
            <Globe className="w-3.5 h-3.5" />
            UNIVERSAL LANGUAGE MATRIX
          </div>
          <h1 className="font-space font-extrabold text-4xl md:text-5xl tracking-tight text-[#141413]">
            45+ Universal <span className="text-[#F40009]">Languages</span>
          </h1>
          <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base">
            Rosetta's universal language matrix spans modern, enterprise, legacy, scientific, systems, and smart contracts — with continuous runtime auto-learning.
          </p>
        </div>

        {/* Search & Filter */}
        <div className="editorial-card rounded-2xl p-5 mb-10 bg-white flex flex-col md:flex-row gap-4 items-center justify-between">
          <div className="relative w-full md:w-96">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-[#78716C]" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search by language name, extension, or paradigm..."
              className="w-full h-10 pl-10 pr-4 rounded-xl bg-[#FAF6F0] border border-[#D6CFC2] text-[#141413] font-mono text-xs placeholder-[#78716C] focus:outline-none focus:border-[#F40009]"
            />
          </div>

          <div className="flex flex-wrap items-center gap-1.5">
            <button
              onClick={() => setSelectedPhase("all")}
              className={`px-3.5 py-1.5 rounded-full text-xs font-mono font-bold transition-all cursor-pointer ${
                selectedPhase === "all"
                  ? "bg-[#F40009] text-white"
                  : "bg-[#FAF6F0] text-[#57534E] hover:text-[#141413]"
              }`}
            >
              All ({filteredList.length})
            </button>
            {phases.map((ph) => (
              <button
                key={ph.num}
                onClick={() => setSelectedPhase(ph.num)}
                className={`px-3.5 py-1.5 rounded-full text-xs font-mono font-bold transition-all cursor-pointer ${
                  selectedPhase === ph.num
                    ? "bg-[#F40009] text-white"
                    : "bg-[#FAF6F0] text-[#57534E] hover:text-[#141413]"
                }`}
              >
                {ph.label}
              </button>
            ))}
          </div>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
          {filteredList.map((lang) => (
            <div
              key={lang.name}
              onClick={() => setFocusedLanguage(lang)}
              className="bg-white rounded-2xl p-6 border border-[#E5DEC9] hover:border-[#F40009] hover:shadow-[4px_4px_0px_#F40009] transition-all cursor-pointer flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="font-space font-extrabold text-lg text-[#141413]">
                    {lang.name}
                  </span>
                  <span className="font-mono text-xs font-bold text-[#F40009]">{lang.ext}</span>
                </div>
                <p className="text-[#57534E] text-xs leading-relaxed mb-4">
                  {lang.description}
                </p>
              </div>

              <div className="flex items-center gap-1.5 pt-3 border-t border-[#F3EDE2]">
                <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
                  Phase {lang.phase}
                </span>
                <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-[#FAF6F0] border border-[#E5DEC9] text-[#57534E]">
                  {lang.paradigm}
                </span>
              </div>
            </div>
          ))}
        </div>

        {/* Modal */}
        <AnimatePresence>
          {focusedLanguage && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                onClick={() => setFocusedLanguage(null)}
                className="absolute inset-0 bg-[#141413]/50 backdrop-blur-xs"
              />

              <motion.div
                initial={{ opacity: 0, scale: 0.96, y: 12 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                exit={{ opacity: 0, scale: 0.96, y: 12 }}
                className="editorial-card rounded-3xl p-8 max-w-xl w-full relative z-10 bg-white"
              >
                <button
                  onClick={() => setFocusedLanguage(null)}
                  className="absolute top-6 right-6 font-mono text-xs font-bold text-[#57534E] hover:text-[#F40009] cursor-pointer"
                >
                  [CLOSE]
                </button>

                <div className="flex items-center gap-3 mb-4">
                  <div className="w-11 h-11 rounded-xl bg-[#F40009] text-white flex items-center justify-center font-space font-extrabold text-lg">
                    {focusedLanguage.name.charAt(0)}
                  </div>
                  <div>
                    <h2 className="font-space font-extrabold text-2xl text-[#141413]">
                      {focusedLanguage.name}{" "}
                      <span className="font-mono text-sm text-[#F40009]">{focusedLanguage.ext}</span>
                    </h2>
                    <p className="text-xs font-mono text-[#57534E]">
                      Phase {focusedLanguage.phase} &bull; {focusedLanguage.paradigm}
                    </p>
                  </div>
                </div>

                <p className="text-[#44403C] text-sm leading-relaxed mb-6">
                  {focusedLanguage.description}
                </p>

                <div className="mb-6">
                  <h3 className="font-mono text-xs font-bold text-[#141413] uppercase mb-2 flex items-center gap-1.5">
                    <Award className="w-4 h-4 text-[#F40009]" />
                    Strengths
                  </h3>
                  <div className="flex flex-wrap gap-2">
                    {focusedLanguage.strengths.map((str) => (
                      <span key={str} className="px-3 py-1 rounded-full bg-[#FAF6F0] border border-[#E5DEC9] text-xs font-semibold text-[#141413]">
                        {str}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-4 mb-6 border-t border-[#E5DEC9] pt-4">
                  <div>
                    <h4 className="font-mono text-xs font-bold text-[#57534E] uppercase mb-2 flex items-center gap-1">
                      <ArrowRightLeft className="w-3.5 h-3.5 text-[#F40009]" />
                      Common Sources
                    </h4>
                    <div className="flex flex-wrap gap-1.5">
                      {focusedLanguage.sources.map((src) => (
                        <span key={src} className="px-2 py-0.5 rounded bg-[#FAF6F0] border border-[#D6CFC2] text-xs font-mono text-[#141413]">
                          {src}
                        </span>
                      ))}
                    </div>
                  </div>
                  <div>
                    <h4 className="font-mono text-xs font-bold text-[#F40009] uppercase mb-2 flex items-center gap-1">
                      <ArrowRightLeft className="w-3.5 h-3.5" />
                      Common Targets
                    </h4>
                    <div className="flex flex-wrap gap-1.5">
                      {focusedLanguage.targets.map((tgt) => (
                        <span key={tgt} className="px-2 py-0.5 rounded bg-[#F40009]/10 text-xs font-mono font-bold text-[#F40009]">
                          {tgt}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                <Link
                  href="/transpile"
                  onClick={() => setFocusedLanguage(null)}
                  className="w-full h-11 rounded-full bg-[#F40009] hover:bg-[#d00008] text-white font-space font-bold text-xs tracking-wider flex items-center justify-center gap-2 transition-all"
                >
                  <Play className="w-3.5 h-3.5 fill-current" />
                  OPEN {focusedLanguage.name.toUpperCase()} IN WORKBENCH
                </Link>
              </motion.div>
            </div>
          )}
        </AnimatePresence>

      </div>
    </div>
  );
}
