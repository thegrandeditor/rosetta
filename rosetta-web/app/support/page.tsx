"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  LifeBuoy,
  MessageSquare,
  ShieldAlert,
  Server,
  Terminal,
  Send,
  CheckCircle2,
  FileCode,
  Mail,
  Clock,
  Sparkles,
  ArrowRight,
  ExternalLink,
  AlertCircle,
  GitBranch
} from "lucide-react";
import Link from "next/link";

export default function SupportPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    organization: "",
    category: "legacy-modernization",
    codeSnippet: "",
    message: "",
  });

  const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
  const [feedbackMsg, setFeedbackMsg] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.name.trim() || !formData.email.trim() || !formData.message.trim()) {
      setStatus("error");
      setFeedbackMsg("Please provide your name, email, and inquiry details.");
      return;
    }

    setStatus("submitting");

    // Simulate sending ticket / logging support request
    setTimeout(() => {
      setStatus("success");
      setFeedbackMsg(
        `Thank you, ${formData.name}! Your support ticket has been received. Our compiler engineering team will follow up at ${formData.email} within 4 business hours.`
      );
      setFormData({
        name: "",
        email: "",
        organization: "",
        category: "legacy-modernization",
        codeSnippet: "",
        message: "",
      });
    }, 1200);
  };

  return (
    <div className="py-12 md:py-20 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto mb-14">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold tracking-wider uppercase bg-[#F40009]/10 text-[#F40009] border border-[#F40009]/20 mb-4">
          <LifeBuoy className="w-3.5 h-3.5" />
          ROSETTA Help Desk &amp; Engineering Support
        </div>
        <h1 className="font-space text-3xl sm:text-5xl font-black tracking-tight text-[#141413] dark:text-[#FAF6F0] mb-4">
          How Can Our Compiler Team Help You?
        </h1>
        <p className="font-sans text-base sm:text-lg text-[#57534E] dark:text-[#A1A1AA] leading-relaxed">
          From legacy mainframe codebases (COBOL, Fortran, Ada) to custom language grammars and private VPC deployments, our engineering team is here to assist.
        </p>

        {/* Live Engine Status Pill */}
        <div className="flex flex-wrap items-center justify-center gap-4 mt-6 text-xs font-mono">
          <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 font-bold">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            Live Cloud Engine: Operational
          </div>
          <div className="px-3.5 py-1.5 rounded-full bg-white dark:bg-[#1C1C1A] text-[#57534E] dark:text-[#A1A1AA] border border-[#E5DEC9] dark:border-[#27272A]">
            Response Time: ~0.36 ms
          </div>
          <div className="px-3.5 py-1.5 rounded-full bg-white dark:bg-[#1C1C1A] text-[#57534E] dark:text-[#A1A1AA] border border-[#E5DEC9] dark:border-[#27272A]">
            Catalog: 48 Languages Active
          </div>
        </div>
      </div>

      {/* Support Channels Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
        {/* Channel 1: Enterprise SLA */}
        <div className="bg-white dark:bg-[#1C1C1A] rounded-2xl border border-[#E5DEC9] dark:border-[#27272A] p-6 flex flex-col justify-between shadow-sm hover:border-[#F40009]/40 transition-all">
          <div>
            <div className="w-10 h-10 rounded-xl bg-[#F40009]/10 text-[#F40009] flex items-center justify-center mb-4">
              <Server className="w-5 h-5" />
            </div>
            <h3 className="font-space text-lg font-bold text-[#141413] dark:text-[#FAF6F0] mb-2">
              Enterprise Mainframe SLAs
            </h3>
            <p className="text-sm text-[#57534E] dark:text-[#A1A1AA] leading-relaxed mb-4">
              Dedicated engineering support for financial cores, banking systems, insurance backbones, and defense infrastructure migrating from COBOL, Fortran, and PL/I.
            </p>
          </div>
          <div className="text-xs font-mono font-bold text-[#F40009] flex items-center gap-1.5 pt-2 border-t border-[#E5DEC9]/40 dark:border-[#27272A]/40">
            <Clock className="w-3.5 h-3.5" />
            4-Hour Priority SLA
          </div>
        </div>

        {/* Channel 2: Open Source Community */}
        <div className="bg-white dark:bg-[#1C1C1A] rounded-2xl border border-[#E5DEC9] dark:border-[#27272A] p-6 flex flex-col justify-between shadow-sm hover:border-[#F40009]/40 transition-all">
          <div>
            <div className="w-10 h-10 rounded-xl bg-[#141413]/10 dark:bg-white/10 text-[#141413] dark:text-white flex items-center justify-center mb-4">
              <svg className="w-5 h-5 fill-current" viewBox="0 0 24 24">
                <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
              </svg>
            </div>
            <h3 className="font-space text-lg font-bold text-[#141413] dark:text-[#FAF6F0] mb-2">
              GitHub Community &amp; Issues
            </h3>
            <p className="text-sm text-[#57534E] dark:text-[#A1A1AA] leading-relaxed mb-4">
              Submit reproducible grammar bugs, request language frontends or backends, and collaborate directly with the core Rosetta development team.
            </p>
          </div>
          <a
            href="https://github.com/thegrandeditor/rosetta/issues"
            target="_blank"
            rel="noopener noreferrer"
            className="text-xs font-mono font-bold text-[#141413] dark:text-white hover:text-[#F40009] flex items-center gap-1.5 pt-2 border-t border-[#E5DEC9]/40 dark:border-[#27272A]/40 transition-colors"
          >
            Open GitHub Issues
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>

        {/* Channel 3: Documentation & Guides */}
        <div className="bg-white dark:bg-[#1C1C1A] rounded-2xl border border-[#E5DEC9] dark:border-[#27272A] p-6 flex flex-col justify-between shadow-sm hover:border-[#F40009]/40 transition-all">
          <div>
            <div className="w-10 h-10 rounded-xl bg-[#F40009]/10 text-[#F40009] flex items-center justify-center mb-4">
              <Terminal className="w-5 h-5" />
            </div>
            <h3 className="font-space text-lg font-bold text-[#141413] dark:text-[#FAF6F0] mb-2">
              CLI &amp; FastMCP Integration
            </h3>
            <p className="text-sm text-[#57534E] dark:text-[#A1A1AA] leading-relaxed mb-4">
              Step-by-step setup guides for integrating Rosetta with Cursor, Claude Desktop, local terminal pipelines, and custom CI/CD build scripts.
            </p>
          </div>
          <Link
            href="/docs"
            className="text-xs font-mono font-bold text-[#F40009] hover:underline flex items-center gap-1.5 pt-2 border-t border-[#E5DEC9]/40 dark:border-[#27272A]/40"
          >
            Read CLI Documentation
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>
      </div>

      {/* Main Support Ticket Form & FAQ Quick Reference */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Left Column: Direct Ticket Form */}
        <div className="lg:col-span-7 bg-white dark:bg-[#1C1C1A] border border-[#E5DEC9] dark:border-[#27272A] rounded-3xl p-6 sm:p-8 shadow-sm">
          <div className="mb-6">
            <h2 className="font-space text-2xl font-black text-[#141413] dark:text-[#FAF6F0] mb-1">
              Submit a Support Ticket
            </h2>
            <p className="text-sm text-[#57534E] dark:text-[#A1A1AA]">
              Have a syntax question, unexpected compiler output, or enterprise inquiry? Fill out the form below.
            </p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-mono font-bold text-[#141413] dark:text-[#FAF6F0] uppercase tracking-wider mb-1.5">
                  Your Name *
                </label>
                <input
                  type="text"
                  required
                  placeholder="Ada Lovelace"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] text-sm text-[#141413] dark:text-[#FAF6F0] focus:outline-none focus:border-[#F40009] transition-all"
                />
              </div>

              <div>
                <label className="block text-xs font-mono font-bold text-[#141413] dark:text-[#FAF6F0] uppercase tracking-wider mb-1.5">
                  Email Address *
                </label>
                <input
                  type="email"
                  required
                  placeholder="ada@enterprise.com"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] text-sm text-[#141413] dark:text-[#FAF6F0] focus:outline-none focus:border-[#F40009] transition-all"
                />
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-mono font-bold text-[#141413] dark:text-[#FAF6F0] uppercase tracking-wider mb-1.5">
                  Organization / Team
                </label>
                <input
                  type="text"
                  placeholder="Global Bank Systems"
                  value={formData.organization}
                  onChange={(e) => setFormData({ ...formData, organization: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] text-sm text-[#141413] dark:text-[#FAF6F0] focus:outline-none focus:border-[#F40009] transition-all"
                />
              </div>

              <div>
                <label className="block text-xs font-mono font-bold text-[#141413] dark:text-[#FAF6F0] uppercase tracking-wider mb-1.5">
                  Inquiry Category
                </label>
                <select
                  value={formData.category}
                  onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] text-sm text-[#141413] dark:text-[#FAF6F0] focus:outline-none focus:border-[#F40009] transition-all"
                >
                  <option value="legacy-modernization">Legacy Migration (COBOL, Fortran, PL/I, RPG)</option>
                  <option value="compiler-bug">Compiler Bug or Grammar Parse Failure</option>
                  <option value="custom-grammar">Custom Grammar Synthesis (rosetta learn)</option>
                  <option value="enterprise-sla">Enterprise SLA &amp; Air-Gapped Deployment</option>
                  <option value="general-inquiry">General Technical Question</option>
                </select>
              </div>
            </div>

            <div>
              <label className="block text-xs font-mono font-bold text-[#141413] dark:text-[#FAF6F0] uppercase tracking-wider mb-1.5">
                Code Snippet or Compiler Trace (Optional)
              </label>
              <textarea
                rows={4}
                placeholder="Paste snippet, compiler exception, or HERMES pass trace here..."
                value={formData.codeSnippet}
                onChange={(e) => setFormData({ ...formData, codeSnippet: e.target.value })}
                className="w-full px-4 py-2.5 rounded-xl bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] text-xs font-mono text-[#141413] dark:text-[#FAF6F0] focus:outline-none focus:border-[#F40009] transition-all"
              />
            </div>

            <div>
              <label className="block text-xs font-mono font-bold text-[#141413] dark:text-[#FAF6F0] uppercase tracking-wider mb-1.5">
                Message &amp; Detailed Explanation *
              </label>
              <textarea
                rows={4}
                required
                placeholder="Describe your current setup, expected output, and any specific language requirements..."
                value={formData.message}
                onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                className="w-full px-4 py-2.5 rounded-xl bg-[#FAF6F0] dark:bg-[#141413] border border-[#E5DEC9] dark:border-[#27272A] text-sm text-[#141413] dark:text-[#FAF6F0] focus:outline-none focus:border-[#F40009] transition-all"
              />
            </div>

            {/* Error or Success notification */}
            {status === "error" && (
              <div className="p-3.5 rounded-xl bg-red-500/10 border border-red-500/20 text-red-600 dark:text-red-400 text-xs font-mono flex items-center gap-2">
                <AlertCircle className="w-4 h-4 shrink-0" />
                {feedbackMsg}
              </div>
            )}

            {status === "success" && (
              <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-700 dark:text-emerald-300 text-xs font-mono flex items-start gap-2.5">
                <CheckCircle2 className="w-5 h-5 shrink-0 text-emerald-500 mt-0.5" />
                <span>{feedbackMsg}</span>
              </div>
            )}

            <button
              type="submit"
              disabled={status === "submitting"}
              className="w-full py-3.5 px-6 rounded-xl bg-[#F40009] hover:bg-[#d00008] text-white font-space font-bold text-sm flex items-center justify-center gap-2 transition-all cursor-pointer shadow-sm disabled:opacity-50"
            >
              {status === "submitting" ? (
                <>
                  <span className="w-4 h-4 border-2 border-white/40 border-t-white rounded-full animate-spin" />
                  Routing Ticket to Compiler Team...
                </>
              ) : (
                <>
                  <Send className="w-4 h-4" />
                  Submit Engineering Ticket
                </>
              )}
            </button>
          </form>
        </div>

        {/* Right Column: Quick Diagnostics & FAQ Links */}
        <div className="lg:col-span-5 space-y-6">
          {/* Box 1: Quick Diagnostics */}
          <div className="bg-[#FAF6F0] dark:bg-[#1C1C1A] border border-[#E5DEC9] dark:border-[#27272A] rounded-3xl p-6 sm:p-7">
            <h3 className="font-space text-lg font-bold text-[#141413] dark:text-[#FAF6F0] mb-3 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-[#F40009]" />
              Quick Diagnostics Checklist
            </h3>
            <ul className="space-y-3 text-xs font-sans text-[#57534E] dark:text-[#A1A1AA] leading-relaxed">
              <li className="flex items-start gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#F40009] mt-1.5 shrink-0" />
                <span>
                  <strong>Dialect Override:</strong> If auto-detection chooses the wrong dialect, explicitly set the Source dropdown in the Workbench or pass <code className="font-mono bg-white dark:bg-[#141413] px-1 py-0.5 rounded border border-[#E5DEC9] dark:border-[#27272A]">--from .cbl</code> in the CLI.
                </span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#F40009] mt-1.5 shrink-0" />
                <span>
                  <strong>AST Verification:</strong> You can inspect the full normalized abstract syntax tree by toggling the <strong>IR AST</strong> button in the Workbench right editor.
                </span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-[#F40009] mt-1.5 shrink-0" />
                <span>
                  <strong>Air-Gapped Setup:</strong> For zero-internet deployments, set <code className="font-mono bg-white dark:bg-[#141413] px-1 py-0.5 rounded border border-[#E5DEC9] dark:border-[#27272A]">ROSETTA_API_URL</code> to point to your local container instance.
                </span>
              </li>
            </ul>
          </div>

          {/* Box 2: Have you checked the FAQ? */}
          <div className="bg-white dark:bg-[#1C1C1A] border border-[#E5DEC9] dark:border-[#27272A] rounded-3xl p-6 sm:p-7 shadow-sm">
            <h3 className="font-space text-lg font-bold text-[#141413] dark:text-[#FAF6F0] mb-2">
              Have you checked our FAQ?
            </h3>
            <p className="text-xs text-[#57534E] dark:text-[#A1A1AA] leading-relaxed mb-4">
              Answers to common architecture questions, Angular/React framework transforms, memory safety invariants, and continuous learning are documented.
            </p>
            <Link
              href="/faq"
              className="inline-flex items-center gap-2 text-xs font-mono font-bold text-[#F40009] hover:underline"
            >
              Browse Complete FAQ
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          {/* Box 3: Security & Privacy Guarantee */}
          <div className="bg-emerald-500/5 dark:bg-emerald-950/10 border border-emerald-500/20 rounded-3xl p-6 sm:p-7">
            <div className="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-mono text-xs font-bold mb-2">
              <ShieldAlert className="w-4 h-4" />
              Enterprise Privacy Guarantee
            </div>
            <p className="text-xs text-[#57534E] dark:text-[#A1A1AA] leading-relaxed">
              ROSETTA does not store, log, or use proprietary customer code for model training. Deterministic compiler passes execute in isolated memory sandboxes.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
