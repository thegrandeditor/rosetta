"use client";

import React, { useState } from "react";
import Link from "next/link";
import { ArrowRight, Terminal, Check, Copy } from "lucide-react";

const HERO_DEMOS = [
  {
    id: "cobol",
    label: "COBOL → Python",
    from: "COBOL (.cbl)",
    to: "Python (.py)",
    source: `       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SALARY PIC 9(6) VALUE 125000.
       01 BONUS  PIC 9(5) VALUE 15000.
       PROCEDURE DIVISION.
           ADD BONUS TO SALARY.
           DISPLAY "TOTAL: " SALARY.
           STOP RUN.`,
    target: `def payroll():
    salary: int = 125000
    bonus: int = 15000
    salary = salary + bonus
    print("TOTAL: ", salary)

if __name__ == "__main__":
    payroll()`,
  },
  {
    id: "cpp",
    label: "C++ Pointers → Rust",
    from: "C++ (.cpp)",
    to: "Rust (.rs)",
    source: `int main() {
    int* ptr = malloc(64);
    *ptr = 42;
    printf("%d\\n", *ptr);
    free(ptr);
    return 0;
}`,
    target: `fn main() {
    let mut ptr = Box::new(0);
    *ptr = 42;
    println!("{}", *ptr);
    drop(ptr);
}`,
  },
  {
    id: "sol",
    label: "Solidity → TypeScript",
    from: "Solidity (.sol)",
    to: "TypeScript (.ts)",
    source: `contract Vault {
    mapping(address => uint) balances;
    function deposit(uint amount) public {
        balances[msg.sender] += amount;
    }
}`,
    target: `export class Vault {
    balances: Record<string, number> = {};
    deposit(amount: number, sender: string): void {
        this.balances[sender] = (this.balances[sender] ?? 0) + amount;
    }
}`,
  },
];

export default function HeroSection() {
  const [activeIdx, setActiveIdx] = useState(0);
  const [copiedCli, setCopiedCli] = useState(false);

  const activeDemo = HERO_DEMOS[activeIdx];

  const copyCli = () => {
    navigator.clipboard.writeText("pip install -e . && rosetta --help");
    setCopiedCli(true);
    setTimeout(() => setCopiedCli(false), 2000);
  };

  return (
    <section className="relative w-full py-20 md:py-28 px-4 sm:px-6 lg:px-8 border-b border-[#E5DEC9] bg-[#FAF6F0]">
      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        {/* Left Column: Editorial Headline & CTAs */}
        <div className="lg:col-span-6 flex flex-col items-start text-left">
          <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full border border-[#F40009]/30 bg-[#F40009]/10 text-[#F40009] text-xs font-semibold tracking-wide mb-6">
            <span className="h-2 w-2 rounded-full bg-[#F40009]"></span>
            UNIVERSAL 45+ &times; 45+ SOURCE-TO-SOURCE COMPILER
          </div>

          <h1 className="font-space font-extrabold text-5xl sm:text-6xl lg:text-7xl leading-[1.06] tracking-tight text-[#141413]">
            Every Language. <br />
            <span
              className="text-[#F40009] italic font-bold"
              style={{ fontFamily: "'Lobster Two', Georgia, serif" }}
            >
              Refreshed &amp; Simple.
            </span>
          </h1>

          <p className="mt-6 text-base md:text-lg text-[#57534E] font-sans max-w-xl leading-relaxed">
            Deterministic AST transpilation across <strong>45+ programming languages</strong>. Migrate legacy <span className="text-[#141413] font-semibold">COBOL</span>, <span className="text-[#141413] font-semibold">Fortran</span>, and <span className="text-[#141413] font-semibold">PL/I</span> into modern <span className="text-[#F40009] font-semibold">Python</span>, <span className="text-[#F40009] font-semibold">Rust</span>, <span className="text-[#F40009] font-semibold">Go</span>, and <span className="text-[#F40009] font-semibold">Carbon</span> with zero manual rewrites.
          </p>

          {/* Action Buttons */}
          <div className="mt-8 flex flex-wrap gap-3 items-center">
            <Link
              href="/transpile"
              className="px-7 py-3.5 rounded-full bg-[#F40009] hover:bg-[#d00008] text-sm font-bold text-white transition-all shadow-sm flex items-center gap-2"
            >
              <span>Open Code Workbench</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              href="/languages"
              className="px-7 py-3.5 rounded-full border-2 border-[#141413] bg-white hover:bg-[#F3EDE2] text-sm font-bold text-[#141413] transition-all"
            >
              Browse 45+ Languages
            </Link>
          </div>

          {/* Copyable CLI Pill */}
          <div className="mt-8 inline-flex items-center gap-3 px-4 py-2.5 rounded-xl border border-[#E5DEC9] bg-white text-xs font-mono text-[#44403C] shadow-xs">
            <Terminal className="w-4 h-4 text-[#F40009]" />
            <span>$ rosetta legacy_module.cbl --to py</span>
            <button
              onClick={copyCli}
              className="ml-2 p-1 rounded hover:bg-[#FAF6F0] text-[#78716C] hover:text-[#141413] transition-colors cursor-pointer"
              title="Copy CLI command"
            >
              {copiedCli ? <Check className="w-3.5 h-3.5 text-[#F40009]" /> : <Copy className="w-3.5 h-3.5" />}
            </button>
          </div>
        </div>

        {/* Right Column: Tactile Editorial Code Card (Replaces 3D Monolith) */}
        <div className="lg:col-span-6 w-full">
          <div className="editorial-card rounded-2xl overflow-hidden bg-white">
            {/* Card Top Bar */}
            <div className="px-5 py-3.5 border-b-2 border-[#141413] bg-[#FAF6F0] flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <span className="h-3 w-3 rounded-full bg-[#F40009] border border-[#141413]"></span>
                <span className="h-3 w-3 rounded-full bg-[#E5DEC9] border border-[#141413]"></span>
                <span className="font-mono text-xs font-bold text-[#141413] ml-1">
                  LIVE COMPILER PREVIEW
                </span>
              </div>

              {/* Preset Switcher Pills */}
              <div className="flex items-center gap-1.5">
                {HERO_DEMOS.map((demo, idx) => (
                  <button
                    key={demo.id}
                    onClick={() => setActiveIdx(idx)}
                    className={`px-3 py-1 rounded-full text-xs font-bold transition-all cursor-pointer ${
                      activeIdx === idx
                        ? "bg-[#F40009] text-white"
                        : "bg-white border border-[#D6CFC2] text-[#57534E] hover:text-[#141413]"
                    }`}
                  >
                    {demo.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Split Code Comparison */}
            <div className="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-[#E5DEC9]">
              {/* Source */}
              <div className="p-5 bg-[#FAF6F0]/50">
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-xs font-bold text-[#57534E] uppercase">
                    SOURCE: {activeDemo.from}
                  </span>
                  <span className="px-2 py-0.5 rounded bg-[#E5DEC9]/60 font-mono text-[10px] font-semibold text-[#44403C]">
                    BABEL PARSER
                  </span>
                </div>
                <pre className="font-mono text-xs text-[#141413] leading-relaxed overflow-x-auto">
                  {activeDemo.source}
                </pre>
              </div>

              {/* Target */}
              <div className="p-5 bg-[#FFF5F5]/60">
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-xs font-bold text-[#F40009] uppercase">
                    OUTPUT: {activeDemo.to}
                  </span>
                  <span className="px-2 py-0.5 rounded bg-[#F40009]/10 font-mono text-[10px] font-bold text-[#F40009]">
                    CIPHER EMITTER
                  </span>
                </div>
                <pre className="font-mono text-xs text-[#141413] font-medium leading-relaxed overflow-x-auto">
                  {activeDemo.target}
                </pre>
              </div>
            </div>

            {/* Card Footer */}
            <div className="px-5 py-3 border-t border-[#E5DEC9] bg-white flex items-center justify-between text-xs font-mono text-[#57534E]">
              <span>HERMES Passes: TypeInference &bull; MemorySafety &bull; StdlibMap</span>
              <Link href="/transpile" className="font-bold text-[#F40009] hover:underline">
                Try Custom Code &rarr;
              </Link>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
