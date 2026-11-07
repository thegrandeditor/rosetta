"use client";

import React, { useEffect, useState, useRef, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { CheckCircle2, ShieldCheck, Terminal, Copy, Check, ArrowRight } from "lucide-react";
import Link from "next/link";
import confetti from "canvas-confetti";
import ParticleField from "@/components/3d/ParticleField";

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
    <div className="min-h-screen bg-[#050508] text-white pt-28 pb-16 px-4 md:px-8 relative overflow-hidden flex items-center">
      <ParticleField />
      
      {/* Premium Emerald/Cyan Background Glows */}
      <div className="absolute top-[15%] left-[20%] w-[350px] h-[350px] rounded-full bg-[#10B981]/5 blur-[120px] pointer-events-none"></div>
      <div className="absolute bottom-[20%] right-[20%] w-[450px] h-[450px] rounded-full bg-[#06B6D4]/5 blur-[150px] pointer-events-none"></div>

      <div className="max-w-3xl mx-auto w-full relative z-10">
        
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.6 }}
          className="glass-panel border-white/[0.04] rounded-3xl p-8 md:p-10 shadow-[0_30px_60px_rgba(0,0,0,0.8)] relative"
          style={{
            boxShadow: "0 30px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(16, 185, 129, 0.1)",
            border: "1px solid rgba(16, 185, 129, 0.15)"
          }}
        >
          {/* Header Icon Checkmark */}
          <div className="flex flex-col items-center text-center mb-8 select-none">
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ type: "spring", stiffness: 100, delay: 0.3 }}
              className="w-16 h-16 rounded-full bg-[#10B981]/15 border border-[#10B981]/30 flex items-center justify-center mb-4 shadow-[0_0_20px_rgba(16,185,129,0.3)]"
            >
              <ShieldCheck className="w-8 h-8 text-[#10B981]" />
            </motion.div>
            
            <h1 className="font-space font-black text-3xl tracking-tight bg-gradient-to-r from-white via-white to-white/70 bg-clip-text text-transparent">
              Node Activated Successfully
            </h1>
            <p className="mt-2 text-white/50 font-sans text-sm font-light">
              Your secure compiler pipeline is active and synched with Vercel serverless.
            </p>
          </div>

          {/* Copyable API key panel */}
          <div className="glass-panel border-white/[0.04] bg-black/40 rounded-xl p-5 mb-8">
            <span className="font-mono text-[9px] text-[#10B981] uppercase tracking-widest block mb-2 font-bold">
              PRO DEVELOPER API KEY:
            </span>
            <div className="flex items-center justify-between gap-4 bg-white/[0.02] border border-white/5 rounded-lg px-4 py-3">
              <code className="font-mono text-xs text-white/80 select-all select-none truncate">
                {mockApiKey}
              </code>
              <button
                onClick={handleCopy}
                className="p-2 rounded border border-white/5 bg-white/[0.02] hover:bg-white/5 hover:border-white/15 text-white/60 hover:text-white transition-all duration-200 shrink-0"
              >
                {copied ? <Check className="w-4 h-4 text-[#10B981]" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>
            <p className="text-[10px] text-white/30 font-sans mt-2">
              Pass this key inside your SDK or REST compiler headers as `X-Rosetta-Key`.
            </p>
          </div>

          {/* System Activation Logs Terminal */}
          <div className="glass-panel border-white/[0.04] bg-[#07070a]/90 rounded-2xl p-5 font-mono text-[10px] text-white/40 h-52 overflow-hidden flex flex-col mb-8 select-none">
            <div className="flex items-center justify-between border-b border-white/[0.03] pb-2 mb-3 uppercase text-white/30 tracking-widest shrink-0">
              <span className="flex items-center gap-2">
                <Terminal className="w-3.5 h-3.5 text-[#10B981]" />
                TELEMETRY DECK SIGNALS
              </span>
              <span className="text-[#10B981] animate-pulse">● SIGNAL_ESTABLISHED</span>
            </div>
            
            <div className="flex-grow overflow-y-auto space-y-1.5 pr-2">
              {logs.map((log, idx) => (
                <div key={idx} className="flex gap-2">
                  <span className="text-white/20">[{idx.toString().padStart(3, "0")}]</span>
                  <span className={log.includes("SUCCESS") || log.includes("established") ? "text-[#10B981]" : log.includes("LICENSE") ? "text-[#06B6D4]" : "text-white/60"}>
                    {log}
                  </span>
                </div>
              ))}
              <div ref={consoleBottomRef} />
            </div>
          </div>

          {/* Action redirects */}
          <div className="flex flex-col sm:flex-row gap-4 items-center justify-center">
            <Link
              href="/transpile"
              className="w-full sm:w-auto h-12 px-8 rounded-xl bg-gradient-to-r from-[#10B981] to-[#06B6D4] text-white font-mono font-bold tracking-widest text-xs flex items-center justify-center gap-2 shadow-[0_0_15px_rgba(16,185,129,0.3)] hover:shadow-[0_0_25px_rgba(6,182,212,0.5)] hover:scale-[1.01] transition-all duration-300"
            >
              LAUNCH PRO WORKBENCH
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              href="/"
              className="w-full sm:w-auto h-12 px-8 rounded-xl border border-white/10 bg-white/[0.02] text-white/60 hover:text-white hover:bg-white/5 hover:border-white/20 font-mono text-xs flex items-center justify-center transition-all duration-300"
            >
              RETURN TO CONTROL COCKPIT
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
      <div className="min-h-screen bg-[#050508] text-white flex items-center justify-center font-mono text-xs">
        &gt; CONNECTING SECURE GATEWAY DATA NODE...
      </div>
    }>
      <BillingSuccessContent />
    </Suspense>
  );
}
