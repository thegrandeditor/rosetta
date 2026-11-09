"use client";

import React, { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { 
  Search, 
  HelpCircle, 
  ChevronDown, 
  Cpu, 
  ShieldCheck, 
  Layers, 
  Sparkles, 
  Code2, 
  Terminal, 
  ArrowRight,
  BookOpen,
  CheckCircle2,
  Lock
} from "lucide-react";
import Link from "next/link";

interface FAQItem {
  id: string;
  category: "Architecture" | "Languages" | "HERMES" | "Enterprise" | "AutoLearn";
  question: string;
  answer: string | React.ReactNode;
}

const FAQ_ITEMS: FAQItem[] = [
  {
    id: "what-is-rosetta",
    category: "Architecture",
    question: "What is ROSETTA and how is it different from AI code generators?",
    answer: (
      <div className="space-y-3">
        <p>
          <strong>ROSETTA is a deterministic, compiler-grade source-to-source transpiler</strong> that operates directly on <strong>Abstract Syntax Trees (ASTs)</strong> rather than probabilistic next-token text prediction.
        </p>
        <p>
          Unlike LLMs (like ChatGPT or Claude) which can hallucinate non-existent syntax, drop critical edge cases, or introduce subtle logic bugs, ROSETTA uses a formal three-stage compiler architecture:
        </p>
        <ul className="list-disc pl-5 space-y-1 text-sm">
          <li><strong>BABEL Frontends:</strong> Formally parse source code into canonical Rosetta Intermediate Representation (IR).</li>
          <li><strong>HERMES Pipeline:</strong> Applies deterministic semantic normalization passes (type inference, memory safety, indexing resolution).</li>
          <li><strong>CIPHER Backends:</strong> Emits target code adhering to strict language-idiomatic standards.</li>
        </ul>
      </div>
    ),
  },
  {
    id: "zero-hallucinations",
    category: "Architecture",
    question: "Does ROSETTA produce hallucinations or broken imports?",
    answer: (
      <p>
        <strong>Zero hallucinations.</strong> Because every parse and emission stage is governed by formal grammar visitors and concrete AST data structures, the syntax is guaranteed to be syntactically valid in the target language. Library mapping tables deterministically resolve standard library equivalents (such as COBOL display statements to Python <code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">print()</code> or C++ vectors to Rust <code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">Vec&lt;T&gt;</code>).
      </p>
    ),
  },
  {
    id: "angular-support",
    category: "Languages",
    question: "Does ROSETTA support Angular, React, and modern UI frameworks?",
    answer: (
      <div className="space-y-3">
        <p>
          <strong>Yes, at the core language level!</strong> Angular applications are built entirely using <strong>TypeScript (<code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">.ts</code>)</strong> and HTML/CSS templates.
        </p>
        <p>
          ROSETTA includes full bidirectional AST parsing and code emission for TypeScript. Any Angular service, data model, state logic, calculation algorithm, or utility class can be pasted into ROSETTA and transpiled into <strong>Python, Go, C#, Rust, Java, C++, etc.</strong>
        </p>
        <p className="text-sm text-[#57534E] dark:text-[#A1A1AA]">
          <em>Note:</em> Framework component translation (e.g. converting Angular <code className="font-mono text-xs">@Component</code> decorators into React JSX) is a UI-level AST transform built directly on top of ROSETTA's TypeScript engine.
        </p>
      </div>
    ),
  },
  {
    id: "legacy-migration",
    category: "Languages",
    question: "Which legacy mainframe and enterprise languages can ROSETTA modernize?",
    answer: (
      <div className="space-y-2">
        <p>
          ROSETTA specializes in automating the migration of decades of legacy enterprise codebases into modern cloud-native architectures:
        </p>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 pt-2 text-xs font-mono">
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">COBOL (.cbl)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">Fortran (.f90, .f)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">Ada (.adb)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">Pascal &amp; Delphi (.pas)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">PL/I (.pli)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">RPG (.rpg, .rpgle)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">Visual Basic (.vb, .vba)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">Modula-2 (.mod)</span>
          <span className="p-2 rounded-lg bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] font-semibold">SNOBOL4 (.sno)</span>
        </div>
      </div>
    ),
  },
  {
    id: "hermes-passes",
    category: "HERMES",
    question: "What are HERMES Optimization Passes and what do they do?",
    answer: (
      <div className="space-y-3">
        <p>
          HERMES is ROSETTA&apos;s modular AST optimization pipeline. Before code is emitted in the target dialect, HERMES executes specialized normalization passes:
        </p>
        <ul className="list-disc pl-5 space-y-1.5 text-sm">
          <li><strong>TypeInferencePass:</strong> Infers strong static types across weakly typed or implicit variables.</li>
          <li><strong>LegacyIndexingPass:</strong> Converts 1-based array indexes (Fortran, Julia, MATLAB) to 0-based memory models.</li>
          <li><strong>MemorySafetyNormalizationPass:</strong> Converts raw pointers and unsafe memory allocations into safe constructs, such as Rust borrow-checked references or Go pointers.</li>
          <li><strong>LibraryMappingPass:</strong> Translates native runtime APIs (e.g., standard I/O, string formatting, file system calls) into the target language&apos;s standard library.</li>
          <li><strong>IdiomNormalizationPass:</strong> Transforms procedural paradigms into idiomatic structures (e.g., list comprehensions, match expressions, or async tasks).</li>
        </ul>
      </div>
    ),
  },
  {
    id: "memory-safety",
    category: "HERMES",
    question: "How does ROSETTA ensure memory safety when migrating C/C++ to Rust?",
    answer: (
      <p>
        When converting from C or C++ to Rust, the HERMES <code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">MemorySafetyNormalizationPass</code> identifies pointer lifetimes and mutability. It replaces raw pointer arithmetic with safe slice indexing (<code className="font-mono text-xs">&amp;[T]</code>), converts heap allocations to <code className="font-mono text-xs">Box&lt;T&gt;</code> or <code className="font-mono text-xs">Vec&lt;T&gt;</code>, and ensures all emitted Rust conforms to the borrow checker without requiring unsafe blocks.
      </p>
    ),
  },
  {
    id: "on-premise-security",
    category: "Enterprise",
    question: "Can ROSETTA run 100% on-premises without cloud access?",
    answer: (
      <div className="space-y-2">
        <p>
          <strong>Yes.</strong> ROSETTA can be deployed completely air-gapped on your private infrastructure. We provide:
        </p>
        <ul className="list-disc pl-5 space-y-1 text-sm">
          <li>A self-contained Python CLI tool (<code className="font-mono text-xs">pip install .</code>).</li>
          <li>A standalone Docker container (<code className="font-mono text-xs">docker run -p 8008:8008 rosetta-compiler</code>).</li>
          <li>A local Model Context Protocol (MCP) server for IDE integrations.</li>
        </ul>
        <p className="text-sm">
          No source code, telemetry, or intellectual property ever leaves your secure firewall.
        </p>
      </div>
    ),
  },
  {
    id: "continuous-autolearn",
    category: "AutoLearn",
    question: "How does the Continuous Auto-Learning engine work?",
    answer: (
      <div className="space-y-2">
        <p>
          With the <code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">rosetta learn</code> CLI command or the <code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">/api/learn</code> endpoint, you can teach ROSETTA proprietary, internal, or domain-specific languages (DSLs) on the fly.
        </p>
        <p>
          You provide an EBNF grammar or a sample code corpus. ROSETTA&apos;s dynamic synthesis engine compiles a new BABEL Lexer/Parser pair and a CIPHER emitter at runtime, storing them under <code className="font-mono text-xs">rosetta/autolearn/generated</code>. The new language immediately becomes available in both the CLI and Web Studio without restarting the server.
        </p>
      </div>
    ),
  },
  {
    id: "cli-vs-web",
    category: "Enterprise",
    question: "What is the difference between the Web Studio Workbench and the CLI?",
    answer: (
      <div className="space-y-2">
        <p>
          <strong>Web Studio:</strong> Built for fast interactive experimentation, syntax testing, real-time AST inspection, and side-by-side code diffing directly in your browser.
        </p>
        <p>
          <strong>ROSETTA CLI:</strong> Built for large-scale production workflows. It handles recursive directory scans, automated batch repository transpilation, CI/CD pipeline verification, and custom AST pass configurations.
        </p>
      </div>
    ),
  },
  {
    id: "mcp-server",
    category: "Architecture",
    question: "Can I use ROSETTA with Cursor, Claude Desktop, or AI Agents via MCP?",
    answer: (
      <p>
        <strong>Yes.</strong> ROSETTA has a built-in FastMCP server. By running <code className="font-mono text-xs bg-[#141413]/5 dark:bg-white/10 px-1 py-0.5 rounded">rosetta mcp</code> or pointing your agent to ROSETTA&apos;s MCP entry point, AI agents can invoke <code className="font-mono text-xs">transpile</code>, <code className="font-mono text-xs">inspect_ir</code>, and <code className="font-mono text-xs">get_supported_languages</code> as native tool calls with 100% determinism.
      </p>
    ),
  },
];

const CATEGORIES = [
  "All",
  "Architecture",
  "Languages",
  "HERMES",
  "Enterprise",
  "AutoLearn",
] as const;

export default function FAQPage() {
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState<typeof CATEGORIES[number]>("All");
  const [openIds, setOpenIds] = useState<Set<string>>(new Set(["what-is-rosetta", "zero-hallucinations", "angular-support"]));

  const toggleItem = (id: string) => {
    setOpenIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  const filteredItems = useMemo(() => {
    return FAQ_ITEMS.filter((item) => {
      const matchesCategory = selectedCategory === "All" || item.category === selectedCategory;
      const qText = item.question.toLowerCase();
      const s = search.toLowerCase();
      const matchesSearch = !s || qText.includes(s) || (typeof item.answer === "string" && item.answer.toLowerCase().includes(s));
      return matchesCategory && matchesSearch;
    });
  }, [search, selectedCategory]);

  return (
    <div className="py-12 md:py-20 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto mb-12">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold tracking-wider uppercase bg-[#F40009]/10 text-[#F40009] border border-[#F40009]/20 mb-4">
          <HelpCircle className="w-3.5 h-3.5" />
          Frequently Asked Questions
        </div>
        <h1 className="font-space text-3xl sm:text-5xl font-black tracking-tight text-[#141413] dark:text-[#FAF6F0] mb-4">
          Everything You Need to Know About ROSETTA
        </h1>
        <p className="font-sans text-base sm:text-lg text-[#57534E] dark:text-[#A1A1AA] leading-relaxed">
          Explore how deterministic AST compiler pipelines work, how 45+ languages are parsed and optimized, and how enterprise migrations are conducted with zero hallucinations.
        </p>
      </div>

      {/* Search & Category Filter */}
      <div className="mb-10 space-y-4">
        <div className="relative max-w-2xl mx-auto">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-[#A8A29E]" />
          <input
            type="text"
            placeholder="Search questions (e.g., Angular, COBOL, memory safety, hallucination)..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-12 pr-4 py-3.5 rounded-2xl bg-white dark:bg-[#1C1C1A] border border-[#E5DEC9] dark:border-[#27272A] text-sm font-sans text-[#141413] dark:text-[#FAF6F0] placeholder-[#A8A29E] focus:outline-none focus:border-[#F40009] focus:ring-2 focus:ring-[#F40009]/10 transition-all shadow-sm"
          />
        </div>

        {/* Category Pills */}
        <div className="flex flex-wrap items-center justify-center gap-2 pt-2">
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-4 py-1.5 rounded-full text-xs font-mono font-bold transition-all ${
                selectedCategory === cat
                  ? "bg-[#F40009] text-white shadow-sm"
                  : "bg-white dark:bg-[#1C1C1A] text-[#57534E] dark:text-[#A1A1AA] border border-[#E5DEC9] dark:border-[#27272A] hover:border-[#F40009]/40"
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {/* FAQ Accordion List */}
      <div className="space-y-4">
        {filteredItems.length === 0 ? (
          <div className="text-center py-16 bg-white dark:bg-[#1C1C1A] rounded-2xl border border-[#E5DEC9] dark:border-[#27272A] p-8">
            <HelpCircle className="w-10 h-10 text-[#A8A29E] mx-auto mb-3" />
            <h3 className="font-space text-lg font-bold text-[#141413] dark:text-[#FAF6F0] mb-1">
              No matching questions found
            </h3>
            <p className="text-sm text-[#57534E] dark:text-[#A1A1AA] mb-4">
              Try a different keyword or contact our engineering team directly on the Support page.
            </p>
            <Link
              href="/support"
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-[#F40009] text-white text-xs font-mono font-bold hover:bg-[#d00008] transition-all"
            >
              Contact Support
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        ) : (
          filteredItems.map((item) => {
            const isOpen = openIds.has(item.id);
            return (
              <div
                key={item.id}
                className="bg-white dark:bg-[#1C1C1A] border border-[#E5DEC9] dark:border-[#27272A] rounded-2xl overflow-hidden transition-all shadow-sm hover:border-[#F40009]/30"
              >
                <button
                  onClick={() => toggleItem(item.id)}
                  className="w-full text-left px-6 py-5 flex items-center justify-between gap-4 cursor-pointer"
                >
                  <div className="flex items-center gap-3">
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase tracking-wider bg-[#F40009]/10 text-[#F40009] shrink-0">
                      {item.category}
                    </span>
                    <span className="font-space text-base sm:text-lg font-bold text-[#141413] dark:text-[#FAF6F0]">
                      {item.question}
                    </span>
                  </div>
                  <ChevronDown
                    className={`w-5 h-5 text-[#57534E] dark:text-[#A1A1AA] transition-transform duration-200 shrink-0 ${
                      isOpen ? "rotate-180 text-[#F40009]" : ""
                    }`}
                  />
                </button>

                <AnimatePresence>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                      className="overflow-hidden"
                    >
                      <div className="px-6 pb-6 pt-1 text-sm sm:text-base text-[#57534E] dark:text-[#D4D4D8] leading-relaxed border-t border-[#E5DEC9]/40 dark:border-[#27272A]/40 font-sans">
                        {item.answer}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            );
          })
        )}
      </div>

      {/* Still Have Questions CTA Banner */}
      <div className="mt-16 rounded-3xl border border-[#E5DEC9] dark:border-[#27272A] bg-gradient-to-br from-[#F3EDE2] via-white to-[#F3EDE2] dark:from-[#1C1C1A] dark:via-[#141413] dark:to-[#1C1C1A] p-8 sm:p-10 text-center relative overflow-hidden shadow-sm">
        <h3 className="font-space text-2xl font-black text-[#141413] dark:text-[#FAF6F0] mb-2">
          Still have questions or custom language needs?
        </h3>
        <p className="text-sm sm:text-base text-[#57534E] dark:text-[#A1A1AA] max-w-xl mx-auto mb-6">
          Our compiler engineering team is ready to assist with enterprise mainframe architectures, grammar syntheses, or dedicated SLAs.
        </p>
        <div className="flex flex-wrap items-center justify-center gap-4">
          <Link
            href="/support"
            className="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#F40009] text-white text-sm font-semibold hover:bg-[#d00008] transition-all shadow-sm"
          >
            Visit Support &amp; Help Desk
            <ArrowRight className="w-4 h-4" />
          </Link>
          <Link
            href="/transpile"
            className="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-white dark:bg-[#27272A] text-[#141413] dark:text-[#FAF6F0] border border-[#E5DEC9] dark:border-[#3F3F46] text-sm font-semibold hover:border-[#F40009] transition-all"
          >
            Open Interactive Workbench
          </Link>
        </div>
      </div>
    </div>
  );
}
