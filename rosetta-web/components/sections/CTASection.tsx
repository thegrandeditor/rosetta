"use client";

import React from "react";
import Link from "next/link";
import { Terminal, ArrowRight } from "lucide-react";

export default function CTASection() {
  return (
    <section id="cta" className="py-20 bg-[#FAF6F0] border-t border-[#E5DEC9]">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="editorial-card rounded-3xl p-8 md:p-12 bg-white flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="text-left max-w-xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#E5DEC9] bg-[#FAF6F0] text-xs font-mono font-bold text-[#F40009] uppercase mb-3">
              <Terminal className="w-3.5 h-3.5" />
              READY FOR PRODUCTION
            </div>
            <h2 className="font-space text-3xl md:text-4xl font-extrabold tracking-tight text-[#141413]">
              Start Translating with{" "}
              <span
                className="text-[#F40009] italic"
                style={{ fontFamily: "'Lobster Two', Georgia, serif" }}
              >
                Rosetta
              </span>
            </h2>
            <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base leading-relaxed">
              Launch the interactive browser studio or install the command-line compiler and MCP server in seconds.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-3 shrink-0">
            <Link
              href="/transpile"
              className="px-7 py-3.5 rounded-full bg-[#F40009] hover:bg-[#d00008] text-white font-bold text-sm flex items-center justify-center gap-2 shadow-sm transition-all"
            >
              <span>Launch Workbench</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
            <Link
              href="/docs"
              className="px-7 py-3.5 rounded-full border-2 border-[#141413] bg-white hover:bg-[#FAF6F0] text-[#141413] font-bold text-sm flex items-center justify-center transition-all"
            >
              CLI &amp; MCP Docs
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
