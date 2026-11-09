"use client";

import React, { useEffect, useState, useRef, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { CheckCircle2, ShieldCheck, Terminal, Copy, Check, ArrowRight } from "lucide-react";
import Link from "next/link";
import confetti from "canvas-confetti";

function BillingSuccessContent() {
  const searchParams = useSearchParams();
  const tier = searchParams.get("tier") || "pro";
  const cycle = searchParams.get("cycle") || "monthly";

  const [copied, setCopied] = useState(false);
  const [logs, setLogs] = useState<string[]>([]);
  const consoleBottomRef = useRef<HTMLDivElement | null>(null);

  const mockApiKey = "RSTA-PRO-8c7a-42d4-8902-8491e78287d1";

  // Spectacular confetti trigger
  useEffect(() => {
    confetti({
      particleCount: 200,
      spread: 100,
      origin: { y: 0.4 },
      colors: ["#10B981", "#06B6D4", "#7C3AED", "#FFFFFF"],
    });

    const timer = setTimeout(() => {
      confetti({
        particleCount: 100,
        spread: 60,
        origin: { x: 0.3, y: 0.6 },
        colors: ["#10B981", "#06B6D4"],
      });
      confetti({
        particleCount: 100,
        spread: 60,
        origin: { x: 0.7, y: 0.6 },
        colors: ["#10B981", "#7C3AED"],
      });
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  // Animate mock systems telemetry loading
  useEffect(() => {
    const diagnosticSequence = [
      "SYS_AUTH :: Secure signature received from Lemon Squeezy gateway.",
      `SYS_LICENSE :: Verifying plan credentials [Plan: ${tier.toUpperCase()} | Cycle: ${cycle.toUpperCase()}].`,
      "SYS_LICENSE :: License bound successfully to chideradaniel40@gmail.com.",
      "HERMES_PIPELINE :: High-pass compiler token throughput set to 10,000/mo.",
      "CIPHER_BACKEND :: Priority cluster parallel queues assigned.",
      "OPTIMIZER_PASS :: Multi-pass AST desugaring algorithms enabled.",
      `API_KEY :: Provisioning Pro Node endpoint gateway...`,
      `SUCCESS :: API key [${mockApiKey}] successfully activated.`,
      "SYS_ACTIVATE :: Premium workstation synchronization complete. Systems active."
    ];

    let currentStep = 0;
    const interval = setInterval(() => {
      if (currentStep < diagnosticSequence.length) {
        setLogs(prev => [...prev, `${new Date().toLocaleTimeString()} :: ${diagnosticSequence[currentStep]}`]);
        currentStep++;
      } else {
        clearInterval(interval);
      }
    }, 800);

    return () => clearInterval(interval);
  }, [tier, cycle]);

  useEffect(() => {
    if (consoleBottomRef.current) {
      consoleBottomRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [logs]);

  const handleCopy = () => {
    navigator.clipboard.writeText(mockApiKey);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="min-h-screen bg-[#FAF6F0] text-[#141413] pt-24 pb-16 px-4 md:px-8 relative flex items-center justify-center">
      <div className="max-w-2xl mx-auto w-full relative z-10">
        
        <motion.div
          initial={{ opacity: 0, scale: 0.96 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5 }}
          className="editorial-card rounded-3xl p-8 md:p-10 bg-white border-2 border-[#141413] shadow-[8px_8px_0px_#F40009] relative"
        >
          {/* Header Icon Checkmark */}
          <div className="flex flex-col items-center text-center mb-8 select-none">
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ type: "spring", stiffness: 100, delay: 0.2 }}
              className="w-16 h-16 rounded-2xl bg-[#F40009] text-white flex items-center justify-center mb-4 shadow-md"
            >
              <ShieldCheck className="w-8 h-8" />
            </motion.div>
            
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#F40009]/10 text-[#F40009] font-mono text-xs font-bold mb-2 uppercase">
              <CheckCircle2 className="w-3.5 h-3.5" />
              PLAN ACTIVATED: {tier.toUpperCase()} ({cycle.toUpperCase()})
            </div>

            <h1 className="font-space font-extrabold text-3xl tracking-tight text-[#141413]">
              Welcome to Rosetta Pro
            </h1>
            <p className="mt-2 text-[#57534E] font-sans text-sm max-w-md">
              Your high-throughput compiler pipeline is active. 10,000 translations/month and full AST optimization passes have been unlocked.
            </p>
          </div>

          {/* Copyable API key panel */}
          <div className="rounded-2xl border border-[#E5DEC9] bg-[#FAF6F0] p-5 mb-6">
            <div className="flex items-center justify-between mb-2">
              <span className="font-mono text-xs text-[#141413] uppercase tracking-wider font-bold">
                YOUR PRO DEVELOPER API KEY:
              </span>
              <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-[#F40009]/10 text-[#F40009]">
                ACTIVE
              </span>
            </div>

            <div className="flex items-center justify-between gap-3 bg-white border border-[#D6CFC2] rounded-xl px-4 py-3">
              <code className="font-mono text-xs text-[#141413] font-bold select-all truncate">
                {mockApiKey}
              </code>
              <button
                onClick={handleCopy}
                className="p-2 rounded-lg border border-[#D6CFC2] bg-[#FAF6F0] hover:bg-[#F40009] hover:text-white hover:border-[#F40009] text-[#141413] transition-all cursor-pointer shrink-0"
                title="Copy API Key"
              >
                {copied ? <Check className="w-4 h-4 text-emerald-600" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>
            <p className="text-[11px] text-[#78716C] font-mono mt-2">
              Pass as header: <code className="text-[#F40009]">Authorization: Bearer {mockApiKey}</code> or in CLI config.
            </p>
          </div>

          {/* System Activation Logs Terminal */}
          <div className="rounded-2xl border border-[#141413] bg-[#141413] p-5 font-mono text-[11px] text-[#A8A29E] h-48 overflow-hidden flex flex-col mb-8 select-none">
            <div className="flex items-center justify-between border-b border-[#2A2620] pb-2 mb-3 uppercase tracking-wider text-xs font-bold text-white shrink-0">
              <span className="flex items-center gap-2">
                <Terminal className="w-3.5 h-3.5 text-[#F40009]" />
                ACTIVATION TELEMETRY
              </span>
              <span className="text-emerald-400">● VERIFIED</span>
            </div>
            
            <div className="flex-grow overflow-y-auto space-y-1.5 pr-2">
              {logs.map((log, idx) => (
                <div key={idx} className="flex gap-2">
                  <span className="text-[#57534E]">[{idx.toString().padStart(2, "0")}]</span>
                  <span className={log.includes("SUCCESS") ? "text-emerald-400 font-bold" : log.includes("API_KEY") ? "text-[#F40009] font-bold" : "text-[#D6CFC2]"}>
                    {log}
                  </span>
                </div>
              ))}
              <div ref={consoleBottomRef} />
            </div>
          </div>

          {/* Action redirects */}
          <div className="flex flex-col sm:flex-row gap-3 items-center justify-center">
            <Link
              href="/transpile"
              className="w-full sm:w-auto h-11 px-8 rounded-full bg-[#F40009] hover:bg-[#d00008] text-white font-space font-bold text-xs uppercase tracking-wider flex items-center justify-center gap-2 shadow-sm transition-all"
            >
              LAUNCH WORKBENCH
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              href="/docs"
              className="w-full sm:w-auto h-11 px-6 rounded-full border border-[#D6CFC2] bg-white text-[#141413] hover:border-[#F40009] font-space font-bold text-xs uppercase tracking-wider flex items-center justify-center transition-all"
            >
              VIEW CLI &amp; MCP DOCS
            </Link>
          </div>

        </motion.div>

      </div>
    </div>
  );
}

export default function BillingSuccessPage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen bg-[#FAF6F0] text-[#141413] flex items-center justify-center font-mono text-xs">
        &gt; CONNECTING SECURE GATEWAY DATA NODE...
      </div>
    }>
      <BillingSuccessContent />
    </Suspense>
  );
}
