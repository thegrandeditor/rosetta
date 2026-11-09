"use client";

import React, { useState } from "react";
import {
  Terminal,
  Cpu,
  Server,
  Sparkles,
  Copy,
  Check,
  BookOpen,
  Code2,
  ShieldCheck,
  ArrowRight,
  Layers,
} from "lucide-react";
import Link from "next/link";

interface CodeBlockProps {
  title: string;
  code: string;
  badge?: string;
}

function CopyableCodeBlock({ title, code, badge = "SHELL" }: CodeBlockProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="rounded-xl border border-[#E5DEC9] bg-[#FAF6F0] overflow-hidden">
      <div className="px-4 py-2.5 border-b border-[#E5DEC9] bg-white flex items-center justify-between">
        <span className="font-mono text-xs font-bold text-[#141413]">
          {title}
        </span>
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
            {badge}
          </span>
          <button
            onClick={handleCopy}
            className="p-1.5 rounded-lg border border-[#D6CFC2] bg-white text-[#57534E] hover:text-[#141413] hover:border-[#F40009] transition-all cursor-pointer"
            title="Copy snippet"
          >
            {copied ? (
              <Check className="w-3.5 h-3.5 text-[#F40009]" />
            ) : (
              <Copy className="w-3.5 h-3.5" />
            )}
          </button>
        </div>
      </div>
      <pre className="p-4 font-mono text-xs text-[#141413] overflow-x-auto leading-relaxed">
        {code}
      </pre>
    </div>
  );
}

export default function DocsPage() {
  const [activeTab, setActiveTab] = useState<"cli" | "mcp" | "autolearn" | "enterprise">("cli");

  const tabs = [
    { id: "cli", label: "1. CLI & Terminal", icon: <Terminal className="w-4 h-4" /> },
    { id: "mcp", label: "2. AI IDE / MCP Server", icon: <Cpu className="w-4 h-4" /> },
    { id: "autolearn", label: "3. Auto-Learn Engine", icon: <Sparkles className="w-4 h-4" /> },
    { id: "enterprise", label: "4. Enterprise Docker & API", icon: <Server className="w-4 h-4" /> },
  ] as const;

  return (
    <div className="min-h-screen bg-[#FAF6F0] text-[#141413] py-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-6xl mx-auto">
        
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#D6CFC2] bg-white text-xs font-mono font-bold text-[#F40009] uppercase tracking-widest mb-3">
            <BookOpen className="w-3.5 h-3.5" />
            DEVELOPER &amp; ENTERPRISE DOCUMENTATION
          </div>
          <h1 className="font-space font-extrabold text-4xl md:text-5xl tracking-tight text-[#141413]">
            Run <span className="text-[#F40009]">Rosetta</span> Anywhere
          </h1>
          <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base leading-relaxed">
            Install the native CLI, connect Rosetta to your AI IDE via Model Context Protocol (MCP), ingest custom grammars, or deploy an air-gapped Docker cluster.
          </p>
        </div>

        {/* Beginner Learner Callout Banner */}
        <div className="mb-10 p-5 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200/80 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#F40009] text-white flex items-center justify-center shrink-0 shadow-xs">
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <div className="font-space font-bold text-sm text-[#141413]">
                New to AST Compilers or the Web Studio?
              </div>
              <p className="text-xs text-[#57534E] font-sans mt-0.5">
                Read our beginner-friendly visual guide to understanding the Workbench, HERMES passes, and AST transpilation.
              </p>
            </div>
          </div>
          <Link
            href="/workbench-guide"
            className="shrink-0 px-4 py-2 rounded-full bg-[#141413] hover:bg-[#F40009] text-white font-space font-bold text-xs uppercase tracking-wider transition-colors shadow-xs"
          >
            Learner&apos;s Guide &rarr;
          </Link>
        </div>

        {/* Navigation Pills */}
        <div className="flex flex-wrap items-center justify-center gap-2.5 mb-10">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-5 py-2.5 rounded-full font-space text-xs font-bold flex items-center gap-2 border transition-all cursor-pointer ${
                activeTab === tab.id
                  ? "bg-[#F40009] text-white border-[#F40009] shadow-sm"
                  : "bg-white border-[#D6CFC2] text-[#57534E] hover:text-[#141413]"
              }`}
            >
              {tab.icon}
              <span>{tab.label}</span>
            </button>
          ))}
        </div>

        {/* Tab 1: CLI & Terminal */}
        {activeTab === "cli" && (
          <div className="editorial-card rounded-3xl p-8 md:p-10 bg-white space-y-8">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#E5DEC9] pb-6">
              <div>
                <span className="font-mono text-xs font-bold text-[#F40009] uppercase">
                  COMMAND-LINE COMPILER
                </span>
                <h2 className="font-space text-2xl md:text-3xl font-extrabold mt-1 text-[#141413]">
                  Rosetta CLI (`rosetta`)
                </h2>
                <p className="text-[#57534E] text-sm mt-1 max-w-2xl">
                  Install the Python package to transpile files in your terminal or CI/CD pipelines.
                </p>
              </div>
              <div className="px-4 py-1.5 rounded-full border border-[#F40009]/30 bg-[#F40009]/10 font-mono text-xs font-bold text-[#F40009] shrink-0">
                Python &gt;= 3.10 Ready
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <CopyableCodeBlock
                title="1. Install Package Locally"
                badge="SHELL"
                code={`# Install directly from repository root
pip install -e .

# Verify CLI entrypoints
rosetta --help`}
              />

              <CopyableCodeBlock
                title="2. Cross-Compile Any of the 45+ Languages"
                badge="SHELL"
                code={`# Legacy COBOL Mainframe -> Modern Python
rosetta company_cobol_standard.cbl --to py

# Python Financial Engine -> Rust Safe Systems
rosetta complex_test.py --to rs

# Solidity Smart Contract -> TypeScript SDK
rosetta vault.sol --to ts`}
              />

              <CopyableCodeBlock
                title="3. Inspect Canonical Rosetta IR & Select Passes"
                badge="SHELL"
                code={`# Print intermediate RosettaNode AST before code emission
rosetta app.js --to go --show-ir

# Run specific HERMES passes explicitly
rosetta app.py --to cpp --passes stdlib_normalization,type_inference,idiom_normalization`}
              />

              <div className="rounded-xl border border-[#E5DEC9] bg-[#FAF6F0] p-6 flex flex-col justify-between">
                <div>
                  <h3 className="font-space font-bold text-base text-[#141413] flex items-center gap-2 mb-3">
                    <Layers className="w-4 h-4 text-[#F40009]" />
                    Active HERMES Passes
                  </h3>
                  <ul className="space-y-2 text-xs text-[#44403C] font-mono">
                    <li>&bull; <strong className="text-[#141413]">StdlibNormalizationPass</strong>: Cross-language I/O &amp; collections</li>
                    <li>&bull; <strong className="text-[#141413]">LibraryMappingPass</strong>: fetch/requests/http, JSON, Math, Date</li>
                    <li>&bull; <strong className="text-[#141413]">MemorySafetyNormalizationPass</strong>: Pointers, malloc &amp; GC free</li>
                    <li>&bull; <strong className="text-[#141413]">TypeInferencePass</strong>: Static type deduction</li>
                    <li>&bull; <strong className="text-[#141413]">LegacyIndexingPass</strong>: 1-based (Fortran/COBOL) to 0-based</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tab 2: MCP Server */}
        {activeTab === "mcp" && (
          <div className="editorial-card rounded-3xl p-8 md:p-10 bg-white space-y-8">
            <div className="border-b border-[#E5DEC9] pb-6">
              <span className="font-mono text-xs font-bold text-[#F40009] uppercase">
                MODEL CONTEXT PROTOCOL (STDIO)
              </span>
              <h2 className="font-space text-2xl md:text-3xl font-extrabold mt-1 text-[#141413]">
                AI Coding Agent Integration (`rosetta-mcp`)
              </h2>
              <p className="text-[#57534E] text-sm mt-1 max-w-2xl">
                Connect Rosetta directly into Cursor, Claude Desktop, Windsurf, or Antigravity for deterministic AST transpilation.
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <CopyableCodeBlock
                title="1. Add to mcp_config.json / claude_desktop_config.json"
                badge="JSON"
                code={`{
  "mcpServers": {
    "rosetta-transpiler": {
      "command": "python",
      "args": ["-m", "rosetta.cli.mcp_server"],
      "env": {
        "PYTHONPATH": "/path/to/Rosetta"
      }
    }
  }
}`}
              />

              <CopyableCodeBlock
                title="2. Exposed MCP Tools for AI Agents"
                badge="PYTHON"
                code={`# 1. Deterministic Universal Transpilation across 45+ Languages
transpile(source: str, input_ext: str, target_lang: str) -> str

# 2. Full AST + HERMES Pass Telemetry Inspection
inspect_ir(source: str, input_ext: str, target_lang: str = "py") -> dict

# 3. Query Supported Frontends & Backends
get_supported_languages() -> dict`}
              />
            </div>
          </div>
        )}

        {/* Tab 3: Auto-Learn Engine */}
        {activeTab === "autolearn" && (
          <div className="editorial-card rounded-3xl p-8 md:p-10 bg-white space-y-8">
            <div className="border-b border-[#E5DEC9] pb-6">
              <span className="font-mono text-xs font-bold text-[#F40009] uppercase">
                PHASE 5 AUTO-LEARN ENGINE
              </span>
              <h2 className="font-space text-2xl md:text-3xl font-extrabold mt-1 text-[#141413]">
                Ingest Custom Languages (`rosetta learn`)
              </h2>
              <p className="text-[#57534E] text-sm mt-1 max-w-2xl">
                Point Rosetta at an ANTLR4 `.g4` grammar, BNF specification, or sample code corpus to automatically scaffold a new parser and emitter.
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              <CopyableCodeBlock
                title="From ANTLR4 Grammar (.g4)"
                badge="SHELL"
                code={`rosetta learn \\
  --grammar ./grammars/MyDSL.g4 \\
  --name MyDSL`}
              />

              <CopyableCodeBlock
                title="From BNF / EBNF Spec (.bnf)"
                badge="SHELL"
                code={`rosetta learn \\
  --bnf ./specs/LegacyBank.bnf \\
  --name LegacyBank`}
              />

              <CopyableCodeBlock
                title="From Code Corpus Directory"
                badge="SHELL"
                code={`rosetta learn \\
  --corpus ./samples/custom_lang/ \\
  --name CustomLang`}
              />
            </div>
          </div>
        )}

        {/* Tab 4: Enterprise Docker & API */}
        {activeTab === "enterprise" && (
          <div className="editorial-card rounded-3xl p-8 md:p-10 bg-white space-y-8">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#E5DEC9] pb-6">
              <div>
                <span className="font-mono text-xs font-bold text-[#F40009] uppercase">
                  ON-PREMISE / AIR-GAPPED VPC DEPLOYMENT
                </span>
                <h2 className="font-space text-2xl md:text-3xl font-extrabold mt-1 text-[#141413]">
                  Enterprise Docker &amp; REST API Bridge
                </h2>
                <p className="text-[#57534E] text-sm mt-1 max-w-2xl">
                  Deploy Rosetta inside your private corporate network so sensitive COBOL or financial code never leaves your infrastructure.
                </p>
              </div>
              <div className="flex items-center gap-2 px-4 py-1.5 rounded-full border border-[#F40009]/30 bg-[#F40009]/10 font-mono text-xs font-bold text-[#F40009] shrink-0">
                <ShieldCheck className="w-4 h-4" />
                <span>Zero External Data Egress</span>
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <CopyableCodeBlock
                title="1. Self-Hosted Docker Compose Cluster"
                badge="DOCKER"
                code={`# Build and start both FastAPI Engine (8008) & Web Studio (3000)
docker-compose up -d --build

# Or run the headless compiler API container standalone
docker build -t rosetta-engine .
docker run -p 8008:8008 rosetta-engine`}
              />

              <CopyableCodeBlock
                title="2. Programmatic REST API Integration"
                badge="CURL"
                code={`curl -X POST http://localhost:8008/api/transpile \\
  -H "Content-Type: application/json" \\
  -d '{
    "source": "IDENTIFICATION DIVISION.\\nPROGRAM-ID. PAYROLL.\\nPROCEDURE DIVISION.\\nDISPLAY \\"OK\\".\\nSTOP RUN.",
    "from_lang": ".cbl",
    "to_lang": "py"
  }'`}
              />
            </div>
          </div>
        )}

        {/* Bottom CTA */}
        <div className="mt-12 flex flex-col sm:flex-row items-center justify-center gap-4">
          <Link
            href="/transpile"
            className="px-7 py-3.5 rounded-full bg-[#F40009] hover:bg-[#d00008] text-white font-space font-bold text-sm flex items-center gap-2 shadow-sm transition-all"
          >
            <Code2 className="w-4 h-4" />
            <span>Open Interactive Workbench</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
          <Link
            href="/languages"
            className="px-7 py-3.5 rounded-full border-2 border-[#141413] bg-white hover:bg-[#F3EDE2] text-[#141413] font-space font-bold text-sm transition-all"
          >
            Explore 45+ Languages
          </Link>
        </div>

      </div>
    </div>
  );
}
