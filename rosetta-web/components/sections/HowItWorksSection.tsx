"use client";

import React from "react";
import { Code, Settings, Download, ArrowRight } from "lucide-react";

const STEPS = [
  {
    num: "01",
    title: "Paste or Pipe Your Code",
    desc: "Drop source code in any of the 45+ supported languages into the workbench or CLI. Rosetta auto-detects the dialect signature immediately.",
    icon: <Code className="w-6 h-6 text-[#F40009]" />,
  },
  {
    num: "02",
    title: "HERMES AST Normalization",
    desc: "The compiler parses your code into the canonical Rosetta IR, resolving types, pointer safety, 1-based array indexing, and standard libraries.",
    icon: <Settings className="w-6 h-6 text-[#141413]" />,
  },
  {
    num: "03",
    title: "Clean Target Output",
    desc: "CIPHER emits idiomatic target code ready for production deployment—with full AST inspection and zero LLM hallucinations.",
    icon: <Download className="w-6 h-6 text-[#F40009]" />,
  },
];

export default function HowItWorksSection() {
  return (
    <section id="how-it-works" className="py-20 bg-[#F3EDE2] border-y border-[#E5DEC9]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div className="text-center max-w-3xl mx-auto mb-14">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#D6CFC2] bg-white text-xs font-mono font-semibold text-[#F40009] uppercase tracking-widest mb-3">
            TRANSPILATION PIPELINE
          </div>
          <h2 className="font-space text-3xl md:text-4xl font-extrabold tracking-tight text-[#141413]">
            Three Steps. Zero Latency.
          </h2>
          <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base">
            A deterministic three-stage compiler architecture converting abstract syntax trees across 45+ languages.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {STEPS.map((step, idx) => (
            <div
              key={step.num}
              className="bg-white border-2 border-[#141413] rounded-2xl p-7 flex flex-col relative shadow-[4px_4px_0px_#F40009]"
            >
              <div className="flex items-center justify-between mb-5">
                <div className="w-12 h-12 rounded-xl border border-[#E5DEC9] bg-[#FAF6F0] flex items-center justify-center">
                  {step.icon}
                </div>
                <span className="font-space font-black text-3xl text-[#E5DEC9]">
                  {step.num}
                </span>
              </div>

              <h3 className="font-space text-xl font-bold text-[#141413] mb-2">
                {step.title}
              </h3>

              <p className="text-[#57534E] text-sm font-sans leading-relaxed flex-grow">
                {step.desc}
              </p>

              {idx < 2 && (
                <div className="hidden lg:flex absolute top-1/2 -right-5 w-8 h-8 rounded-full border-2 border-[#141413] bg-white items-center justify-center -translate-y-1/2 text-[#141413] z-10">
                  <ArrowRight className="w-4 h-4" />
                </div>
              )}
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
