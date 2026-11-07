"use client";

import React from "react";
import { ShieldCheck, Server, Coins, ArrowRight } from "lucide-react";

const STATS = [
  {
    icon: <Server className="w-5 h-5 text-[#F40009]" />,
    val: "800 Billion+",
    lbl: "Lines of COBOL still running in global financial cores",
  },
  {
    icon: <ShieldCheck className="w-5 h-5 text-[#F40009]" />,
    val: "100% Deterministic",
    lbl: "Static AST transpilation with zero LLM hallucinations or data leakage",
  },
  {
    icon: <Coins className="w-5 h-5 text-[#F40009]" />,
    val: "Air-Gapped Ready",
    lbl: "Self-host inside private enterprise VPCs via Docker Compose",
  },
];

const COBOL_CODE = `       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 GREETING PIC X(13)
          VALUE 'HELLO ROSETTA'.
       PROCEDURE DIVISION.
           DISPLAY GREETING.
           STOP RUN.`;

const PYTHON_CODE = `def hello():
    greeting = "HELLO ROSETTA"
    print(greeting)

if __name__ == "__main__":
    hello()`;

export default function EnterpriseSection() {
  return (
    <section id="enterprise" className="py-20 bg-[#F3EDE2] border-t border-[#E5DEC9]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          
          {/* Left Column */}
          <div className="lg:col-span-6 flex flex-col text-left">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#F40009]/30 bg-white w-fit mb-5">
              <span className="font-mono text-xs text-[#F40009] tracking-wider uppercase font-bold">
                ENTERPRISE MODERNIZATION
              </span>
            </div>

            <h2 className="font-space text-3xl md:text-4xl font-extrabold tracking-tight text-[#141413] leading-tight">
              The COBOL Problem <br />
              <span className="text-[#F40009]">is officially solved.</span>
            </h2>

            <p className="mt-4 text-[#57534E] font-sans leading-relaxed text-sm md:text-base">
              Banks, insurance grids, and national infrastructure run on legacy mainframes. Rosetta eliminates multi-million-dollar manual rewrites using deterministic AST compilation.
            </p>

            <div className="mt-7 space-y-3">
              {STATS.map((stat, idx) => (
                <div
                  key={idx}
                  className="flex items-start gap-4 p-4 rounded-xl border border-[#E5DEC9] bg-white"
                >
                  <div className="w-10 h-10 rounded-lg bg-[#FAF6F0] border border-[#E5DEC9] flex items-center justify-center shrink-0">
                    {stat.icon}
                  </div>
                  <div>
                    <h4 className="font-space text-base font-bold text-[#141413]">
                      {stat.val}
                    </h4>
                    <p className="text-xs font-sans text-[#57534E] mt-0.5">
                      {stat.lbl}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            <div className="mt-8">
              <a
                href="/docs"
                className="inline-flex items-center justify-center px-6 py-3.5 rounded-full bg-[#F40009] hover:bg-[#d00008] text-sm font-bold text-white transition-all shadow-sm"
              >
                <span>View Enterprise Docker Guide</span>
                <ArrowRight className="w-4 h-4 ml-2" />
              </a>
            </div>
          </div>

          {/* Right Column: Clean Editorial Comparison Card */}
          <div className="lg:col-span-6 w-full">
            <div className="editorial-card rounded-2xl p-6 bg-white space-y-4">
              <div className="flex items-center justify-between border-b border-[#E5DEC9] pb-3 text-xs font-mono">
                <span className="font-bold text-[#141413]">MAINFRAME MIGRATION PREVIEW</span>
                <span className="px-2.5 py-0.5 rounded-full bg-[#F40009]/10 text-[#F40009] font-bold">
                  VERIFIED AST
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="rounded-xl border border-[#E5DEC9] bg-[#FAF6F0] p-4">
                  <span className="font-mono text-xs text-[#57534E] uppercase block mb-2 font-bold">
                    COBOL_INPUT.cbl
                  </span>
                  <pre className="font-mono text-xs text-[#141413] leading-relaxed overflow-x-auto">
                    {COBOL_CODE}
                  </pre>
                </div>

                <div className="rounded-xl border border-[#F40009]/30 bg-[#FFF5F5] p-4">
                  <span className="font-mono text-xs text-[#F40009] uppercase block mb-2 font-bold">
                    PYTHON_OUTPUT.py
                  </span>
                  <pre className="font-mono text-xs text-[#141413] font-medium leading-relaxed overflow-x-auto">
                    {PYTHON_CODE}
                  </pre>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
