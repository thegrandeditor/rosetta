"use client";

import React, { useState } from "react";
import { Search, Play } from "lucide-react";

interface LanguageCardData {
  name: string;
  ext: string;
  phase: number;
  paradigm: string;
  type: string;
}

const CATALOG_LANGUAGES: LanguageCardData[] = [
  { name: "Python", ext: ".py", phase: 1, paradigm: "Multi-paradigm", type: "General" },
  { name: "JavaScript", ext: ".js", phase: 1, paradigm: "Event-driven", type: "Web" },
  { name: "TypeScript", ext: ".ts", phase: 1, paradigm: "Static OOP", type: "Web" },
  { name: "Java", ext: ".java", phase: 1, paradigm: "Object-Oriented", type: "General" },
  { name: "C++", ext: ".cpp", phase: 1, paradigm: "Systems OOP", type: "Systems" },
  { name: "C", ext: ".c", phase: 1, paradigm: "Procedural", type: "Systems" },
  { name: "Rust", ext: ".rs", phase: 1, paradigm: "Safe Systems", type: "Systems" },
  { name: "Go", ext: ".go", phase: 1, paradigm: "Concurrent", type: "Systems" },
  { name: "Swift", ext: ".swift", phase: 1, paradigm: "Multi-paradigm", type: "Mobile" },
  { name: "Kotlin", ext: ".kt", phase: 1, paradigm: "Functional OOP", type: "Mobile" },
  { name: "Ruby", ext: ".rb", phase: 1, paradigm: "Dynamic OOP", type: "General" },
  { name: "PHP", ext: ".php", phase: 1, paradigm: "Web Scripting", type: "Web" },
  { name: "COBOL", ext: ".cbl", phase: 2, paradigm: "Business", type: "Enterprise" },
  { name: "Fortran", ext: ".f90", phase: 3, paradigm: "Numeric", type: "Scientific" },
  { name: "BASIC", ext: ".bas", phase: 3, paradigm: "Procedural", type: "General" },
  { name: "Pascal", ext: ".pas", phase: 3, paradigm: "Structured", type: "General" },
  { name: "Ada", ext: ".adb", phase: 3, paradigm: "Concurrent", type: "Systems" },
  { name: "LISP", ext: ".lisp", phase: 3, paradigm: "Functional", type: "Symbolic" },
  { name: "Algol", ext: ".alg", phase: 3, paradigm: "Procedural", type: "Historical" },
  { name: "Smalltalk", ext: ".st", phase: 3, paradigm: "Pure OOP", type: "General" },
  { name: "Prolog", ext: ".pl", phase: 3, paradigm: "Logic", type: "AI" },
  { name: "SNOBOL4", ext: ".sno", phase: 4, paradigm: "Pattern Match", type: "Strings" },
  { name: "PL/I", ext: ".pli", phase: 4, paradigm: "Structured", type: "Enterprise" },
  { name: "Modula-2", ext: ".mod", phase: 4, paradigm: "Modular", type: "Systems" },
  { name: "RPG", ext: ".rpg", phase: 4, paradigm: "Report Gen", type: "Enterprise" },
  { name: "Eiffel", ext: ".e", phase: 4, paradigm: "Contract OOP", type: "General" },
  { name: "Forth", ext: ".fs", phase: 4, paradigm: "Stack-based", type: "Systems" },
  { name: "ML", ext: ".ml", phase: 4, paradigm: "Functional", type: "General" },
  { name: "Solidity", ext: ".sol", phase: 5, paradigm: "Smart Contract", type: "Blockchain" },
  { name: "Mojo", ext: ".mojo", phase: 5, paradigm: "AI Hardware", type: "AI" },
  { name: "Zig", ext: ".zig", phase: 5, paradigm: "Robust Systems", type: "Systems" },
  { name: "Carbon", ext: ".carbon", phase: 5, paradigm: "C++ Successor", type: "Systems" },
  { name: "C#", ext: ".cs", phase: 6, paradigm: "Enterprise OOP", type: "General" },
  { name: "Dart", ext: ".dart", phase: 6, paradigm: "Client-Optimized OOP", type: "Mobile" },
  { name: "Lua", ext: ".lua", phase: 6, paradigm: "Embedded Scripting", type: "Scripting" },
  { name: "R", ext: ".r", phase: 6, paradigm: "Statistical Computing", type: "Scientific" },
  { name: "Julia", ext: ".jl", phase: 6, paradigm: "High-Performance Numerical", type: "Scientific" },
  { name: "Scala", ext: ".scala", phase: 6, paradigm: "Functional & Object", type: "General" },
  { name: "Haskell", ext: ".hs", phase: 6, paradigm: "Pure Functional", type: "Functional" },
  { name: "Elixir", ext: ".ex", phase: 6, paradigm: "Concurrent Actor", type: "Systems" },
  { name: "Bash", ext: ".sh", phase: 6, paradigm: "Shell Automation", type: "DevOps" },
  { name: "SQL", ext: ".sql", phase: 6, paradigm: "Relational / Procedural", type: "Database" },
  { name: "Objective-C", ext: ".m", phase: 6, paradigm: "Smalltalk OOP", type: "Mobile" },
  { name: "Move", ext: ".move", phase: 6, paradigm: "Smart Contracts", type: "Blockchain" },
  { name: "Perl", ext: ".pm", phase: 6, paradigm: "Text & Scripting", type: "Scripting" }
];

export default function LanguagesSection() {
  const [search, setSearch] = useState("");
  const [selectedPhase, setSelectedPhase] = useState<number | "all">("all");

  const filtered = CATALOG_LANGUAGES.filter((lang) => {
    const matchesSearch =
      lang.name.toLowerCase().includes(search.toLowerCase()) ||
      lang.ext.toLowerCase().includes(search.toLowerCase()) ||
      lang.paradigm.toLowerCase().includes(search.toLowerCase());
    const matchesPhase = selectedPhase === "all" || lang.phase === selectedPhase;
    return matchesSearch && matchesPhase;
  });

  const handleInject = (ext: string) => {
    const workbench = document.getElementById("workbench");
    if (workbench) {
      workbench.scrollIntoView({ behavior: "smooth" });
      let sampleBtnName = "";
      if (ext === ".cbl") sampleBtnName = "COBOL";
      else if (ext === ".f90") sampleBtnName = "FORTRAN";
      else if (ext === ".py") sampleBtnName = "Python";
      else if (ext === ".rs") sampleBtnName = "Rust";
      else if (ext === ".sol") sampleBtnName = "Solidity";

      if (sampleBtnName) {
        const matchingBtn = Array.from(document.querySelectorAll("button")).find(
          el => el.textContent === sampleBtnName
        );
        if (matchingBtn) {
          setTimeout(() => matchingBtn.click(), 400);
        }
      }
    }
  };

  return (
    <section id="languages" className="py-20 bg-[#FAF6F0]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#D6CFC2] bg-white text-xs font-mono font-semibold text-[#F40009] uppercase tracking-widest mb-3">
            UNIVERSAL COMPILATION INDEX
          </div>
          <h2 className="font-space text-3xl md:text-4xl font-extrabold tracking-tight text-[#141413]">
            45+ Supported Languages
          </h2>
          <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base">
            Bidirectional parsing and code generation across 50+ years of computing history.
          </p>
        </div>

        {/* Search & Phase Filter Bar */}
        <div className="p-4 rounded-2xl bg-white border border-[#E5DEC9] mb-10 flex flex-col md:flex-row gap-4 items-center justify-between shadow-xs">
          <div className="relative w-full md:w-80">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-[#78716C]" />
            <input
              type="text"
              placeholder="Search language or extension..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full pl-10 pr-4 py-2 rounded-xl bg-[#FAF6F0] border border-[#D6CFC2] text-xs text-[#141413] placeholder-[#78716C] focus:outline-none focus:border-[#F40009]"
            />
          </div>

          <div className="flex flex-wrap gap-1.5">
            <button
              onClick={() => setSelectedPhase("all")}
              className={`px-3.5 py-1.5 rounded-full text-xs font-mono font-bold transition-all cursor-pointer ${
                selectedPhase === "all"
                  ? "bg-[#F40009] text-white"
                  : "bg-[#FAF6F0] text-[#57534E] hover:text-[#141413]"
              }`}
            >
              All ({filtered.length})
            </button>
            {[1, 2, 3, 4, 5, 6].map((ph) => (
              <button
                key={ph}
                onClick={() => setSelectedPhase(ph)}
                className={`px-3.5 py-1.5 rounded-full text-xs font-mono font-bold transition-all cursor-pointer ${
                  selectedPhase === ph
                    ? "bg-[#F40009] text-white"
                    : "bg-[#FAF6F0] text-[#57534E] hover:text-[#141413]"
                }`}
              >
                Phase {ph}
              </button>
            ))}
          </div>
        </div>

        {/* Clean Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 gap-4">
          {filtered.map((lang) => (
            <div
              key={lang.name}
              className="p-5 rounded-2xl bg-white border border-[#E5DEC9] hover:border-[#F40009] transition-all flex flex-col justify-between group shadow-xs"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-xs font-bold text-[#F40009]">
                    {lang.ext}
                  </span>
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold bg-[#FAF6F0] border border-[#E5DEC9] text-[#57534E]">
                    P{lang.phase}
                  </span>
                </div>
                <h4 className="font-space text-lg font-bold text-[#141413] mb-1">
                  {lang.name}
                </h4>
                <p className="text-xs font-mono text-[#78716C]">
                  {lang.paradigm}
                </p>
              </div>

              <div className="flex items-center justify-between border-t border-[#F3EDE2] pt-3 mt-4">
                <span className="text-[10px] font-mono text-[#78716C] uppercase">
                  {lang.type}
                </span>
                {[".cbl", ".f90", ".py", ".rs", ".sol"].includes(lang.ext) && (
                  <button
                    onClick={() => handleInject(lang.ext)}
                    className="inline-flex items-center gap-1 text-xs font-mono font-bold text-[#F40009] hover:underline cursor-pointer"
                  >
                    <span>Try</span>
                    <Play className="w-2.5 h-2.5 fill-current" />
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
