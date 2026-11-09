"use client";

import React, { useState } from "react";
import Link from "next/link";
import {
  BookOpen,
  Sparkles,
  Play,
  Code2,
  ArrowRight,
  Check,
  HelpCircle,
  Layers,
  Sliders,
  ShieldCheck,
  Zap,
  Copy,
  Cpu,
  Eye,
  FileCode,
  CheckCircle2,
  Terminal,
} from "lucide-react";

export default function WorkbenchGuidePage() {
  const [copiedCode, setCopiedCode] = useState<string | null>(null);

  const handleCopy = (code: string, id: string) => {
    navigator.clipboard.writeText(code);
    setCopiedCode(id);
    setTimeout(() => setCopiedCode(null), 2000);
  };

  return (
    <div className="min-h-screen bg-[#FAF6F0] text-[#141413] py-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-5xl mx-auto space-y-16">
        
        {/* Hero Section */}
        <div className="text-center max-w-3xl mx-auto space-y-4">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-[#D6CFC2] bg-white text-xs font-mono font-bold text-[#F40009] uppercase tracking-widest shadow-2xs">
            <BookOpen className="w-3.5 h-3.5" />
            LEARNER&apos;S WORKBENCH HANDBOOK
          </div>
          <h1 className="font-space font-extrabold text-4xl sm:text-5xl tracking-tight text-[#141413]">
            How to Use the <span className="text-[#F40009]">Rosetta Workbench</span>
          </h1>
          <p className="text-[#57534E] text-base sm:text-lg font-sans leading-relaxed">
            A beginner-friendly visual guide to understanding deterministic AST transpilation, compiler passes, and translating code across 50+ languages in seconds.
          </p>
          <div className="flex items-center justify-center gap-3 pt-2">
            <Link
              href="/transpile"
              className="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-[#F40009] hover:bg-[#d00008] text-white font-space font-bold text-xs uppercase tracking-wider transition-all shadow-sm"
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              Open Live Workbench
            </Link>
            <Link
              href="/benchmarks"
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white border border-[#D6CFC2] text-[#141413] hover:border-[#F40009] font-space font-bold text-xs uppercase tracking-wider transition-all"
            >
              <Zap className="w-3.5 h-3.5 text-[#F40009]" />
              View Speed Benchmarks
            </Link>
          </div>
        </div>

        {/* 30-Second Quickstart Card */}
        <div className="editorial-card rounded-3xl p-8 bg-white border border-[#E5DEC9] shadow-sm">
          <div className="flex items-center gap-3 mb-6 pb-4 border-b border-[#F3EDE2]">
            <div className="w-10 h-10 rounded-xl bg-[#F40009]/10 text-[#F40009] flex items-center justify-center">
              <Zap className="w-5 h-5" />
            </div>
            <div>
              <h2 className="font-space font-extrabold text-xl text-[#141413]">
                The 30-Second Quickstart
              </h2>
              <p className="font-mono text-xs text-[#78716C]">
                Translate your first code snippet in 3 simple steps
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9] flex flex-col justify-between">
              <div>
                <div className="w-7 h-7 rounded-full bg-[#F40009] text-white font-mono font-bold text-xs flex items-center justify-center mb-3">
                  1
                </div>
                <h3 className="font-space font-bold text-sm text-[#141413] mb-1">
                  Pick a Preset or Paste Code
                </h3>
                <p className="text-xs text-[#57534E] leading-relaxed">
                  Click one of the top preset pills (like <code className="font-mono text-[#F40009] bg-white px-1 rounded">COBOL</code> or <code className="font-mono text-[#F40009] bg-white px-1 rounded">FORTRAN</code>), or paste your own code into the left editor pane.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-[#E5DEC9] text-[11px] font-mono text-[#78716C]">
                Tip: Auto-detect identifies the language instantly!
              </div>
            </div>

            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9] flex flex-col justify-between">
              <div>
                <div className="w-7 h-7 rounded-full bg-[#F40009] text-white font-mono font-bold text-xs flex items-center justify-center mb-3">
                  2
                </div>
                <h3 className="font-space font-bold text-sm text-[#141413] mb-1">
                  Choose Your Target
                </h3>
                <p className="text-xs text-[#57534E] leading-relaxed">
                  Select your desired output language from the right dropdown (e.g., <code className="font-mono text-[#F40009] bg-white px-1 rounded">Python (.py)</code>, <code className="font-mono text-[#F40009] bg-white px-1 rounded">Rust (.rs)</code>, or <code className="font-mono text-[#F40009] bg-white px-1 rounded">TypeScript (.ts)</code>).
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-[#E5DEC9] text-[11px] font-mono text-[#78716C]">
                Supports 50+ modern, legacy &amp; systems targets.
              </div>
            </div>

            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9] flex flex-col justify-between">
              <div>
                <div className="w-7 h-7 rounded-full bg-[#F40009] text-white font-mono font-bold text-xs flex items-center justify-center mb-3">
                  3
                </div>
                <h3 className="font-space font-bold text-sm text-[#141413] mb-1">
                  Hit Translate &amp; Export
                </h3>
                <p className="text-xs text-[#57534E] leading-relaxed">
                  Click the red <strong className="text-[#F40009]">Translate Now</strong> button. Your code compiles deterministically in sub-milliseconds. Toggle between readable code and the raw AST.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-[#E5DEC9] text-[11px] font-mono text-[#78716C]">
                Click Copy or Download to save your output file.
              </div>
            </div>
          </div>
        </div>

        {/* Visual Anatomy of the Workbench */}
        <div className="space-y-6">
          <div className="text-center max-w-2xl mx-auto">
            <h2 className="font-space font-extrabold text-2xl sm:text-3xl text-[#141413]">
              Visual Anatomy of the Workbench
            </h2>
            <p className="text-[#57534E] text-sm font-sans mt-2">
              Every element on your screen explained in plain, jargon-free language.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* Card 1: Source Editor */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-3">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-full bg-[#F40009]/10 text-[#F40009]">
                  LEFT PANEL
                </span>
                <span className="font-mono text-xs text-[#78716C]">Input Buffer</span>
              </div>
              <h3 className="font-space font-bold text-lg text-[#141413] mb-2 flex items-center gap-2">
                <Code2 className="w-4 h-4 text-[#F40009]" />
                Source Editor &amp; Auto-Detect
              </h3>
              <p className="text-[#57534E] text-xs leading-relaxed mb-4">
                This is where you type, paste, or load your source code. You can manually pick your input language from the dropdown, or let ROSETTA&apos;s heuristic classifier detect it automatically.
              </p>
              <div className="p-3 rounded-xl bg-[#FAF6F0] border border-[#E5DEC9] text-xs font-mono text-[#141413]">
                <span className="text-[#78716C]">Live Indicator: </span>
                <span className="text-[#F40009] font-bold">Auto: COBOL (80%)</span>
                <p className="text-[11px] text-[#57534E] mt-1 font-sans">
                  The green/red pill shows the detected language and matching confidence score in real time.
                </p>
              </div>
            </div>

            {/* Card 2: Target Editor */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-3">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-full bg-[#141413]/10 text-[#141413]">
                  RIGHT PANEL
                </span>
                <span className="font-mono text-xs text-[#78716C]">Output Buffer</span>
              </div>
              <h3 className="font-space font-bold text-lg text-[#141413] mb-2 flex items-center gap-2">
                <Eye className="w-4 h-4 text-[#F40009]" />
                Target Editor &amp; [CODE | IR AST] Toggle
              </h3>
              <p className="text-[#57534E] text-xs leading-relaxed mb-4">
                Displays the transpiled target program. Use the top toggle buttons to switch between:
              </p>
              <div className="space-y-2">
                <div className="p-2.5 rounded-lg bg-[#FAF6F0] border border-[#E5DEC9] text-xs font-mono">
                  <strong className="text-[#F40009]">[CODE] Mode:</strong> Human-readable, idiomatic target code ready to run.
                </div>
                <div className="p-2.5 rounded-lg bg-[#FAF6F0] border border-[#E5DEC9] text-xs font-mono">
                  <strong className="text-[#141413]">[IR AST] Mode:</strong> The structural JSON syntax tree showing exact compiler tokens and semantic nodes.
                </div>
              </div>
            </div>

            {/* Card 3: HERMES Passes Sidebar */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-3">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-full bg-[#F40009]/10 text-[#F40009]">
                  LEFT SIDEBAR
                </span>
                <span className="font-mono text-xs text-[#78716C]">Compiler Optimizations</span>
              </div>
              <h3 className="font-space font-bold text-lg text-[#141413] mb-2 flex items-center gap-2">
                <Sliders className="w-4 h-4 text-[#F40009]" />
                HERMES Optimization Passes
              </h3>
              <p className="text-[#57534E] text-xs leading-relaxed mb-4">
                Compiler &quot;passes&quot; are automated optimization steps that transform your code to be faster, safer, and cleaner before writing target syntax. You can toggle each pass on or off with the checkboxes.
              </p>
              <div className="grid grid-cols-2 gap-2 text-xs font-mono">
                <div className="p-2 rounded bg-[#FAF6F0] border border-[#E5DEC9]">
                  &bull; Loop Unrolling
                </div>
                <div className="p-2 rounded bg-[#FAF6F0] border border-[#E5DEC9]">
                  &bull; Function Inlining
                </div>
                <div className="p-2 rounded bg-[#FAF6F0] border border-[#E5DEC9]">
                  &bull; Safe Allocator
                </div>
                <div className="p-2 rounded bg-[#FAF6F0] border border-[#E5DEC9]">
                  &bull; Dead Code Elim
                </div>
              </div>
            </div>

            {/* Card 4: Compiler Log Stream */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-3">
                <span className="font-mono text-xs font-bold px-2.5 py-1 rounded-full bg-[#141413]/10 text-[#141413]">
                  BOTTOM DOCK
                </span>
                <span className="font-mono text-xs text-[#78716C]">Real-Time Terminal</span>
              </div>
              <h3 className="font-space font-bold text-lg text-[#141413] mb-2 flex items-center gap-2">
                <Terminal className="w-4 h-4 text-[#F40009]" />
                Compiler Log Stream
              </h3>
              <p className="text-[#57534E] text-xs leading-relaxed mb-4">
                The terminal bar at the bottom provides a live diagnostic audit of every compilation step. It shows when AST parsing began, which optimization passes ran, memory buffers, and compilation speed down to 0.1 milliseconds.
              </p>
              <div className="p-3 rounded-xl bg-[#141413] text-[#FAF6F0] font-mono text-[11px] leading-relaxed">
                <div>[00] SYS_INIT :: Rosetta Compiler Workbench ready.</div>
                <div className="text-emerald-400">[01] AST_PARSE :: 18 nodes synthesized in 0.36ms</div>
                <div className="text-[#F40009]">[02] EMIT_TARGET :: Python (.py) output verified 100%</div>
              </div>
            </div>

          </div>
        </div>

        {/* HERMES Passes Deep Dive (Plain English) */}
        <div className="editorial-card rounded-3xl p-8 bg-white border border-[#E5DEC9] shadow-sm space-y-6">
          <div className="max-w-2xl">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#F40009]/10 text-[#F40009] font-mono text-xs font-bold mb-2">
              <Sliders className="w-3.5 h-3.5" />
              DEEP DIVE
            </div>
            <h2 className="font-space font-extrabold text-2xl text-[#141413]">
              What Do the HERMES Passes Actually Do?
            </h2>
            <p className="text-xs text-[#57534E] mt-1 font-sans leading-relaxed">
              In industrial compilers (like LLVM and GCC), code undergoes optimization transformations called &quot;passes&quot;. Here is why each one matters:
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-2">
                <h4 className="font-space font-bold text-sm text-[#141413]">
                  1. Loop Unrolling
                </h4>
                <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
                  Performance
                </span>
              </div>
              <p className="text-xs text-[#57534E] leading-relaxed mb-3">
                <strong>Plain English:</strong> Instead of checking a condition 4 times in a loop, the compiler replicates the loop body 4 times sequentially.
              </p>
              <div className="p-3 rounded-lg bg-white border border-[#D6CFC2] text-[11px] font-mono text-[#141413]">
                <div className="text-[#78716C]">// Eliminates branch prediction misses in the CPU</div>
                for (i=0; i&lt;4; i++) &#123; process(i); &#125;<br />
                <span className="text-[#F40009]">&rarr; process(0); process(1); process(2); process(3);</span>
              </div>
            </div>

            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-2">
                <h4 className="font-space font-bold text-sm text-[#141413]">
                  2. Function Inlining
                </h4>
                <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
                  Speed &amp; Call Stack
                </span>
              </div>
              <p className="text-xs text-[#57534E] leading-relaxed mb-3">
                <strong>Plain English:</strong> If a function is tiny (like <code className="font-mono">add(a, b)</code>), the compiler pastes the arithmetic directly where it is called instead of jumping to a separate function in memory.
              </p>
              <div className="p-3 rounded-lg bg-white border border-[#D6CFC2] text-[11px] font-mono text-[#141413]">
                <div className="text-[#78716C]">// Avoids creating unnecessary call stack frames</div>
                let sum = add(x, y);<br />
                <span className="text-[#F40009]">&rarr; let sum = x + y;</span>
              </div>
            </div>

            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-2">
                <h4 className="font-space font-bold text-sm text-[#141413]">
                  3. Safe Allocator
                </h4>
                <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
                  Security &amp; Memory
                </span>
              </div>
              <p className="text-xs text-[#57534E] leading-relaxed mb-3">
                <strong>Plain English:</strong> When translating high-level code (like Python or Java) into low-level code (C, C++, Rust), this pass adds automatic memory freeing and boundary checks to prevent crashes and buffer overflows.
              </p>
              <div className="p-3 rounded-lg bg-white border border-[#D6CFC2] text-[11px] font-mono text-[#141413]">
                <div className="text-[#78716C]">// Prevents memory leaks and dangling pointer exploits</div>
                char* buffer = malloc(size);<br />
                <span className="text-[#F40009]">&rarr; std::unique_ptr&lt;char[]&gt; buffer = make_unique(size);</span>
              </div>
            </div>

            <div className="p-5 rounded-2xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <div className="flex items-center justify-between mb-2">
                <h4 className="font-space font-bold text-sm text-[#141413]">
                  4. Dead Code Elimination
                </h4>
                <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
                  Clean Code
                </span>
              </div>
              <p className="text-xs text-[#57534E] leading-relaxed mb-3">
                <strong>Plain English:</strong> Finds unused variables, unreachable <code className="font-mono">if (false)</code> blocks, and uncalled helper functions, and strips them from the output so your codebase stays lean.
              </p>
              <div className="p-3 rounded-lg bg-white border border-[#D6CFC2] text-[11px] font-mono text-[#141413]">
                <div className="text-[#78716C]">// Deletes unread declarations</div>
                int unused_counter = 42;<br />
                <span className="text-[#F40009]">&rarr; [Stripped during IR optimization pass]</span>
              </div>
            </div>
          </div>
        </div>

        {/* What is an AST & Why Determinism Matters */}
        <div className="editorial-card rounded-3xl p-8 bg-[#141413] text-[#FAF6F0] space-y-6">
          <div className="max-w-2xl">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#F40009] text-white font-mono text-xs font-bold mb-2">
              <Cpu className="w-3.5 h-3.5" />
              CORE COMPUTER SCIENCE
            </div>
            <h2 className="font-space font-extrabold text-2xl sm:text-3xl text-white">
              What is an AST? (And Why LLMs Make Mistakes)
            </h2>
            <p className="text-xs sm:text-sm text-[#A8A29E] mt-2 font-sans leading-relaxed">
              If code were a spoken human language, an <strong>Abstract Syntax Tree (AST)</strong> would be the grammar tree diagram showing the exact subject, verb, and object of every sentence.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
            <div className="p-6 rounded-2xl bg-[#1C1A17] border border-[#3E3830] space-y-3">
              <div className="text-[#F40009] font-mono text-xs font-bold uppercase tracking-wider">
                Traditional LLMs (ChatGPT / Claude)
              </div>
              <h3 className="font-space font-bold text-base text-white">
                Probabilistic Next-Token Guessing
              </h3>
              <p className="text-xs text-[#A8A29E] leading-relaxed">
                When you ask an AI model to translate COBOL or C++ into Python, it guesses words based on statistical probability. It doesn&apos;t know if a variable really exists or if a math operation will overflow.
              </p>
              <div className="p-3 rounded-xl bg-[#2A2620] border border-[#443E34] text-xs font-mono text-rose-300">
                &times; 2–4 seconds per translation<br />
                &times; Risk of silent bugs &amp; hallucinations<br />
                &times; Costs token fees on every run
              </div>
            </div>

            <div className="p-6 rounded-2xl bg-[#1C1A17] border border-[#3E3830] space-y-3">
              <div className="text-emerald-400 font-mono text-xs font-bold uppercase tracking-wider">
                ROSETTA Compiler Engine
              </div>
              <h3 className="font-space font-bold text-base text-white">
                Mathematical Semantic Invariance
              </h3>
              <p className="text-xs text-[#A8A29E] leading-relaxed">
                ROSETTA parses your source code into an unambiguous AST graph. It verifies types, variable scopes, and logic mathematically, then emits the target code with 100% semantic identity.
              </p>
              <div className="p-3 rounded-xl bg-[#2A2620] border border-[#443E34] text-xs font-mono text-emerald-300">
                &check; 0.36 milliseconds (10,000x faster)<br />
                &check; 0.0% hallucinations (mathematical guarantee)<br />
                &check; $0 token costs &bull; 100% on-premise capable
              </div>
            </div>
          </div>
        </div>

        {/* Guided Exercises for Beginners */}
        <div className="space-y-6">
          <div className="text-center max-w-2xl mx-auto">
            <h2 className="font-space font-extrabold text-2xl sm:text-3xl text-[#141413]">
              3 Guided Hands-On Exercises
            </h2>
            <p className="text-[#57534E] text-sm font-sans mt-2">
              Try these sample scenarios in the Workbench right now to see the compiler in action.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            {/* Exercise 1 */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9] flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-[#F40009]/10 text-[#F40009]">
                    EXERCISE 01
                  </span>
                  <span className="font-mono text-xs text-[#78716C]">Legacy Modernization</span>
                </div>
                <h3 className="font-space font-bold text-base text-[#141413] mb-2">
                  Modernize 1960s COBOL to Python
                </h3>
                <p className="text-xs text-[#57534E] leading-relaxed mb-4">
                  Banks and governments have billions of lines of COBOL. Click the <strong>COBOL</strong> preset on the Workbench and translate it to clean Python 3 with zero syntax errors.
                </p>
              </div>
              <Link
                href="/transpile"
                className="w-full py-2.5 rounded-xl bg-[#FAF6F0] hover:bg-[#F40009] text-[#141413] hover:text-white border border-[#D6CFC2] hover:border-[#F40009] font-space font-bold text-xs uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5"
              >
                Try COBOL &rarr; Python
                <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            {/* Exercise 2 */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9] flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-[#F40009]/10 text-[#F40009]">
                    EXERCISE 02
                  </span>
                  <span className="font-mono text-xs text-[#78716C]">Systems Safety</span>
                </div>
                <h3 className="font-space font-bold text-base text-[#141413] mb-2">
                  Migrate C++ to Memory-Safe Rust
                </h3>
                <p className="text-xs text-[#57534E] leading-relaxed mb-4">
                  White House cybersecurity guidelines mandate eliminating C++ memory leaks. Use the Workbench with <strong>Safe Allocator</strong> enabled to transpile into borrow-checked Rust code.
                </p>
              </div>
              <Link
                href="/transpile"
                className="w-full py-2.5 rounded-xl bg-[#FAF6F0] hover:bg-[#F40009] text-[#141413] hover:text-white border border-[#D6CFC2] hover:border-[#F40009] font-space font-bold text-xs uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5"
              >
                Try C++ &rarr; Rust
                <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            {/* Exercise 3 */}
            <div className="editorial-card rounded-2xl p-6 bg-white border border-[#E5DEC9] flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-[#F40009]/10 text-[#F40009]">
                    EXERCISE 03
                  </span>
                  <span className="font-mono text-xs text-[#78716C]">Web3 &amp; FinTech</span>
                </div>
                <h3 className="font-space font-bold text-base text-[#141413] mb-2">
                  Solidity Smart Contract to TypeScript
                </h3>
                <p className="text-xs text-[#57534E] leading-relaxed mb-4">
                  Need to test an Ethereum smart contract in an off-chain Node.js or web app? Select the <strong>Solidity</strong> preset and compile directly into strongly-typed TypeScript classes.
                </p>
              </div>
              <Link
                href="/transpile"
                className="w-full py-2.5 rounded-xl bg-[#FAF6F0] hover:bg-[#F40009] text-[#141413] hover:text-white border border-[#D6CFC2] hover:border-[#F40009] font-space font-bold text-xs uppercase tracking-wider text-center transition-all flex items-center justify-center gap-1.5"
              >
                Try Solidity &rarr; TS
                <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            </div>

          </div>
        </div>

        {/* Learner's FAQ */}
        <div className="editorial-card rounded-3xl p-8 bg-white border border-[#E5DEC9] shadow-sm space-y-6">
          <div className="flex items-center gap-2 font-space font-extrabold text-xl text-[#141413]">
            <HelpCircle className="w-5 h-5 text-[#F40009]" />
            Frequently Asked Questions for Learners
          </div>

          <div className="space-y-4">
            <div className="p-4 rounded-xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <h4 className="font-space font-bold text-sm text-[#141413] mb-1">
                Do I need to install anything on my computer to use the Workbench?
              </h4>
              <p className="text-xs text-[#57534E] leading-relaxed">
                No. The Workbench runs 100% in your web browser. You don&apos;t need Node.js, Python, or compilers installed locally.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <h4 className="font-space font-bold text-sm text-[#141413] mb-1">
                Can I transpile my own code files instead of the presets?
              </h4>
              <p className="text-xs text-[#57534E] leading-relaxed">
                Yes! Simply paste any code into the left pane. You can also automate whole codebases with the <Link href="/docs" className="text-[#F40009] underline font-semibold">ROSETTA CLI</Link>.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <h4 className="font-space font-bold text-sm text-[#141413] mb-1">
                What does &quot;IR AST&quot; stand for?
              </h4>
              <p className="text-xs text-[#57534E] leading-relaxed">
                <strong>IR</strong> means <em>Intermediate Representation</em>, and <strong>AST</strong> means <em>Abstract Syntax Tree</em>. It is the internal data structure Rosetta uses to represent the logical meaning of your program before translating it to target syntax.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-[#FAF6F0] border border-[#E5DEC9]">
              <h4 className="font-space font-bold text-sm text-[#141413] mb-1">
                Can I download or copy my transpiled code?
              </h4>
              <p className="text-xs text-[#57534E] leading-relaxed">
                Yes. Click the <strong>Copy</strong> icon on the top right of the target editor to copy to your clipboard, or click the <strong>Download</strong> icon to save the file with the appropriate file extension.
              </p>
            </div>
          </div>
        </div>

        {/* Bottom CTA Banner */}
        <div className="p-8 rounded-3xl bg-[#F40009] text-white text-center space-y-4 shadow-md">
          <h2 className="font-space font-extrabold text-2xl sm:text-3xl">
            Ready to Try It Yourself?
          </h2>
          <p className="text-white/90 text-sm max-w-xl mx-auto font-sans leading-relaxed">
            Jump into the live Workbench, load a preset, and watch ROSETTA compile code between 50+ programming languages in real time.
          </p>
          <div className="pt-2">
            <Link
              href="/transpile"
              className="inline-flex items-center gap-2 px-8 py-3 rounded-full bg-white text-[#F40009] font-space font-bold text-xs uppercase tracking-wider hover:bg-[#FAF6F0] transition-all shadow-sm"
            >
              <Play className="w-4 h-4 fill-current" />
              Launch Workbench Now
            </Link>
          </div>
        </div>

      </div>
    </div>
  );
}
