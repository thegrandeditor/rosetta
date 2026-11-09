"use client";

import React, { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Play, Copy, Download, RefreshCw, Sliders, ChevronDown, Check } from "lucide-react";
import CodeEditor from "@/components/ui/CodeEditor";

interface LanguageOption {
  name: string;
  ext: string;
  phase: number;
  type: "source" | "target" | "both";
}

const LANGUAGES: LanguageOption[] = [
  { name: "Python", ext: ".py", phase: 1, type: "both" },
  { name: "JavaScript", ext: ".js", phase: 1, type: "both" },
  { name: "TypeScript", ext: ".ts", phase: 1, type: "both" },
  { name: "Java", ext: ".java", phase: 1, type: "both" },
  { name: "C++", ext: ".cpp", phase: 1, type: "both" },
  { name: "C", ext: ".c", phase: 1, type: "both" },
  { name: "Rust", ext: ".rs", phase: 1, type: "both" },
  { name: "Go", ext: ".go", phase: 1, type: "both" },
  { name: "Swift", ext: ".swift", phase: 1, type: "both" },
  { name: "Kotlin", ext: ".kt", phase: 1, type: "both" },
  { name: "Ruby", ext: ".rb", phase: 1, type: "both" },
  { name: "PHP", ext: ".php", phase: 1, type: "both" },
  { name: "COBOL", ext: ".cbl", phase: 2, type: "both" },
  { name: "Fortran", ext: ".f90", phase: 3, type: "both" },
  { name: "Visual Basic", ext: ".vb", phase: 3, type: "both" },
  { name: "Delphi", ext: ".delphi", phase: 3, type: "both" },
  { name: "BASIC", ext: ".bas", phase: 3, type: "both" },
  { name: "Pascal", ext: ".pas", phase: 3, type: "both" },
  { name: "Ada", ext: ".adb", phase: 3, type: "both" },
  { name: "LISP", ext: ".lisp", phase: 3, type: "both" },
  { name: "Algol", ext: ".alg", phase: 3, type: "both" },
  { name: "Smalltalk", ext: ".st", phase: 3, type: "both" },
  { name: "Prolog", ext: ".pl", phase: 3, type: "both" },
  { name: "SNOBOL4", ext: ".sno", phase: 4, type: "both" },
  { name: "PL/I", ext: ".pli", phase: 4, type: "both" },
  { name: "Modula-2", ext: ".mod", phase: 4, type: "both" },
  { name: "RPG", ext: ".rpg", phase: 4, type: "both" },
  { name: "Eiffel", ext: ".e", phase: 4, type: "both" },
  { name: "Forth", ext: ".fs", phase: 4, type: "both" },
  { name: "ML", ext: ".ml", phase: 4, type: "both" },
  { name: "Solidity", ext: ".sol", phase: 5, type: "both" },
  { name: "Mojo", ext: ".mojo", phase: 5, type: "both" },
  { name: "Zig", ext: ".zig", phase: 5, type: "both" },
  { name: "Carbon", ext: ".carbon", phase: 5, type: "both" },
  { name: "C#", ext: ".cs", phase: 6, type: "both" },
  { name: "Dart", ext: ".dart", phase: 6, type: "both" },
  { name: "Lua", ext: ".lua", phase: 6, type: "both" },
  { name: "R", ext: ".r", phase: 6, type: "both" },
  { name: "Julia", ext: ".jl", phase: 6, type: "both" },
  { name: "Scala", ext: ".scala", phase: 6, type: "both" },
  { name: "Haskell", ext: ".hs", phase: 6, type: "both" },
  { name: "Elixir", ext: ".ex", phase: 6, type: "both" },
  { name: "Bash", ext: ".sh", phase: 6, type: "both" },
  { name: "PowerShell", ext: ".ps1", phase: 6, type: "both" },
  { name: "Arduino", ext: ".ino", phase: 5, type: "both" },
  { name: "SQL", ext: ".sql", phase: 6, type: "both" },
  { name: "Objective-C", ext: ".m", phase: 6, type: "both" },
  { name: "Move", ext: ".move", phase: 6, type: "both" },
  { name: "Perl", ext: ".pm", phase: 6, type: "both" },
  { name: "Matlab", ext: ".matlab", phase: 6, type: "both" },
  { name: "VBA", ext: ".vba", phase: 3, type: "both" },
  { name: "Assembly", ext: ".asm", phase: 3, type: "both" },
  { name: "HCL", ext: ".tf", phase: 6, type: "both" },
  { name: "GraphQL", ext: ".gql", phase: 6, type: "both" }
];

const SAMPLE_CODES: Record<string, { ext: string; code: string; target: string }> = {
  COBOL: {
    ext: ".cbl",
    target: "py",
    code: `       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 GREETING PIC X(12) VALUE 'HELLO ROSETTA'.
       PROCEDURE DIVISION.
           DISPLAY GREETING.
           STOP RUN.`
  },
  FORTRAN: {
    ext: ".f90",
    target: "py",
    code: `PROGRAM HELLO
    PRINT *, 'Hello, World!'
    CALL GREET('Rosetta')
END PROGRAM HELLO

SUBROUTINE GREET(NAME)
    CHARACTER(LEN=*) :: NAME
    PRINT *, 'Greetings, ', NAME
END SUBROUTINE GREET`
  },
  Python: {
    ext: ".py",
    target: "js",
    code: `def calculate_primes(limit: int):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(calculate_primes(20))`
  },
  Rust: {
    ext: ".rs",
    target: "js",
    code: `fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    let sum: i32 = numbers.iter().sum();
    println!("Sum is {}", sum);
}`
  },
  Solidity: {
    ext: ".sol",
    target: "py",
    code: `contract SimpleBank {
    mapping(address => uint) balances;
    event Transfer(address indexed from, address indexed to, uint amount);
    
    function deposit(uint amount) public payable {
        balances[msg.sender] = balances[msg.sender] + amount;
        emit Transfer(address(0), msg.sender, amount);
    }
}`
  }
};

export default function TranspileClient() {
  const [sourceCode, setSourceCode] = useState(SAMPLE_CODES.COBOL.code);
  const [targetCode, setTargetCode] = useState("");
  const [typedTargetCode, setTypedTargetCode] = useState("");
  const [astTree, setAstTree] = useState<string>("");
  const [outputView, setOutputView] = useState<"code" | "ast">("code");
  
  const [sourceLang, setSourceLang] = useState<LanguageOption>(
    LANGUAGES.find(l => l.ext === ".cbl") || LANGUAGES[0]
  );
  const [targetLang, setTargetLang] = useState<LanguageOption>(
    LANGUAGES.find(l => l.ext === ".py") || LANGUAGES[1]
  );
  
  const sourceLangRef = useRef(sourceLang);
  useEffect(() => {
    sourceLangRef.current = sourceLang;
  }, [sourceLang]);

  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);
  const [detectedLabel, setDetectedLabel] = useState<string>("");
  const [detectedLangObj, setDetectedLangObj] = useState<LanguageOption | null>(null);
  const [detectedConfidence, setDetectedConfidence] = useState<number>(0);
  
  const [loopUnrolling, setLoopUnrolling] = useState(true);
  const [inlining, setInlining] = useState(true);
  const [safeGuard, setSafeGuard] = useState(true);
  const [deadCodeElim, setDeadCodeElim] = useState(false);

  const [searchSource, setSearchSource] = useState("");
  const [searchTarget, setSearchTarget] = useState("");
  const [openSource, setOpenSource] = useState(false);
  const [openTarget, setOpenTarget] = useState(false);

  const [logs, setLogs] = useState<string[]>([
    "SYS_INIT :: Rosetta Compiler Workbench ready.",
    "Awaiting source code payload..."
  ]);
  const consoleBottomRef = useRef<HTMLDivElement | null>(null);

  const [tokensUsed, setTokensUsed] = useState(0);
  const [timeMs, setTimeMs] = useState(0);

  const typewriterIntervalRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (!sourceCode.trim()) {
      setDetectedLabel("");
      setDetectedLangObj(null);
      setDetectedConfidence(0);
      return;
    }

    const delayDebounceFn = setTimeout(async () => {
      if (sourceCode.trim().length < 8) return;
      try {
        const res = await fetch("/api/detect", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ source: sourceCode }),
        });
        if (res.ok) {
          const data = await res.json();
          if (data.confidence >= 0.2) {
            const detected = LANGUAGES.find(l => l.ext === data.language);
            if (detected) {
              setDetectedLabel(`${detected.name} (${Math.round(data.confidence * 100)}%)`);
              setDetectedLangObj(detected);
              setDetectedConfidence(data.confidence);
              if (detected.ext !== sourceLangRef.current.ext && data.confidence >= 0.4) {
                setSourceLang(detected);
                addLog(`AUTO_DETECT :: Switched source language to ${detected.name}`);
              }
            }
          }
        }
      } catch (err) {}
    }, 400);

    return () => clearTimeout(delayDebounceFn);
  }, [sourceCode]);

  useEffect(() => {
    if (consoleBottomRef.current) {
      consoleBottomRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [logs]);

  const addLog = (message: string) => {
    setLogs(prev => [...prev, `${new Date().toLocaleTimeString()} :: ${message}`]);
  };

  const loadSample = (key: keyof typeof SAMPLE_CODES) => {
    const sample = SAMPLE_CODES[key];
    setSourceCode(sample.code);
    const src = LANGUAGES.find(l => l.ext === sample.ext);
    const tgt = LANGUAGES.find(l => l.ext === `.${sample.target}` || l.ext === sample.target);
    if (src) setSourceLang(src);
    if (tgt) setTargetLang(tgt);
    setTargetCode("");
    setTypedTargetCode("");
    setDetectedLabel("");
    addLog(`PRESET :: Loaded ${key} sample`);
  };

  const executeTranspilation = async () => {
    if (!sourceCode.trim()) return;
    setLoading(true);
    setTargetCode("");
    setTypedTargetCode("");
    if (typewriterIntervalRef.current) clearInterval(typewriterIntervalRef.current);

    let effectiveSource = sourceLang;
    if (detectedLangObj && detectedConfidence >= 0.8 && detectedLangObj.ext !== sourceLang.ext) {
      effectiveSource = detectedLangObj;
      setSourceLang(detectedLangObj);
      addLog(`AUTO_ALIGN :: Synchronized Source from ${sourceLang.name} -> ${detectedLangObj.name}`);
    }

    addLog(`COMPILE :: ${effectiveSource.name} -> ${targetLang.name}`);

    try {
      const fromExt = effectiveSource.ext;
      const toExt = targetLang.ext.replace(".", "");

      const startTime = performance.now();
      const res = await fetch("/api/transpile", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          source: sourceCode,
          from_lang: fromExt,
          to_lang: toExt
        }),
      });
      const endTime = performance.now();

      if (!res.ok) throw new Error("Transpilation bridge error.");

      const data = await res.json();
      const finalCode = data.result;
      
      if (!finalCode || !finalCode.trim()) {
        const warning = `// [ROSETTA COMPILER NOTICE]\n// 0 statements were produced by the ${effectiveSource.name} parser.\n// Select the matching source language above.`;
        setTargetCode(warning);
        setTypedTargetCode(warning);
        addLog(`NOTICE :: 0 statements produced using ${effectiveSource.name} grammar.`);
      } else {
        setTargetCode(finalCode);
        setTypedTargetCode(finalCode);
        addLog("SUCCESS :: Target code emitted.");
      }

      if (data.ast) {
        setAstTree(JSON.stringify(data.ast, null, 2));
      } else {
        setAstTree(JSON.stringify({ node_type: "Program", source: sourceLang.name, target: targetLang.name }, null, 2));
      }
      if (data.passes && Array.isArray(data.passes)) {
        addLog(`HERMES_PASSES :: [${data.passes.join(" -> ")}]`);
      }
      setTokensUsed(data.tokens_used || Math.floor(sourceCode.length / 4));
      setTimeMs(data.time_ms || Math.round(endTime - startTime));
    } catch (err: any) {
      const finalCode = `// Backend Error:\n${err.message}`;
      setTargetCode(finalCode);
      setTypedTargetCode(finalCode);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(targetCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const element = document.createElement("a");
    const file = new Blob([targetCode], { type: "text/plain" });
    element.href = URL.createObjectURL(file);
    element.download = `rosetta_${sourceLang.name.toLowerCase()}_to_${targetLang.name.toLowerCase()}${targetLang.ext}`;
    document.body.appendChild(element);
    element.click();
  };

  const filteredSource = LANGUAGES.filter(l => 
    l.name.toLowerCase().includes(searchSource.toLowerCase()) && l.type !== "target"
  );
  const filteredTarget = LANGUAGES.filter(l => 
    l.name.toLowerCase().includes(searchTarget.toLowerCase()) && l.type !== "source"
  );

  return (
    <div className="min-h-screen bg-[#FAF6F0] text-[#141413] flex flex-col">
      {/* Top Bar */}
      <div className="border-b border-[#E5DEC9] bg-white px-6 py-4 flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-[#F40009] flex items-center justify-center font-serif italic font-bold text-base text-white">
            R
          </div>
          <div>
            <h1 className="font-space font-bold text-sm text-[#141413] flex items-center gap-2">
              Rosetta Compiler Workbench
              <span className="h-2 w-2 rounded-full bg-[#F40009]"></span>
            </h1>
            <p className="text-[11px] text-[#57534E] font-mono">
              45+ &times; 45+ Universal Deterministic AST Transpiler
            </p>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <span className="font-mono text-xs text-[#57534E] font-semibold mr-1">PRESETS:</span>
          {Object.keys(SAMPLE_CODES).map((key) => (
            <button
              key={key}
              onClick={() => loadSample(key)}
              className="px-3.5 py-1 rounded-full bg-[#FAF6F0] border border-[#D6CFC2] font-mono text-xs font-bold text-[#141413] hover:border-[#F40009] hover:text-[#F40009] transition-all cursor-pointer"
            >
              {key}
            </button>
          ))}
        </div>
      </div>

      {/* Main Split Grid */}
      <div className="flex-grow grid grid-cols-1 lg:grid-cols-12">
        
        {/* Left Sidebar: HERMES Passes */}
        <div className="lg:col-span-2 border-r border-[#E5DEC9] p-5 flex flex-col gap-6 bg-[#F3EDE2]/60">
          <div className="flex items-center gap-2 font-space font-bold text-xs text-[#141413] uppercase border-b border-[#E5DEC9] pb-2">
            <Sliders className="w-4 h-4 text-[#F40009]" />
            HERMES Passes
          </div>

          <div className="space-y-4">
            <label className="flex items-center justify-between text-xs font-semibold text-[#141413] cursor-pointer">
              <span>Loop Unrolling</span>
              <input
                type="checkbox"
                checked={loopUnrolling}
                onChange={(e) => setLoopUnrolling(e.target.checked)}
                className="accent-[#F40009]"
              />
            </label>
            <label className="flex items-center justify-between text-xs font-semibold text-[#141413] cursor-pointer">
              <span>Function Inlining</span>
              <input
                type="checkbox"
                checked={inlining}
                onChange={(e) => setInlining(e.target.checked)}
                className="accent-[#F40009]"
              />
            </label>
            <label className="flex items-center justify-between text-xs font-semibold text-[#141413] cursor-pointer">
              <span>Safe Allocator</span>
              <input
                type="checkbox"
                checked={safeGuard}
                onChange={(e) => setSafeGuard(e.target.checked)}
                className="accent-[#F40009]"
              />
            </label>
            <label className="flex items-center justify-between text-xs font-semibold text-[#141413] cursor-pointer">
              <span>Dead Code Elim</span>
              <input
                type="checkbox"
                checked={deadCodeElim}
                onChange={(e) => setDeadCodeElim(e.target.checked)}
                className="accent-[#F40009]"
              />
            </label>
          </div>

          <div className="mt-auto border-t border-[#E5DEC9] pt-4 space-y-2 font-mono text-xs text-[#57534E]">
            <div className="flex items-center justify-between">
              <span>LEXER:</span>
              <span className="text-[#F40009] font-bold">READY</span>
            </div>
            {tokensUsed > 0 && (
              <div className="flex items-center justify-between">
                <span>TOKENS:</span>
                <span className="text-[#141413] font-bold">{tokensUsed}</span>
              </div>
            )}
            {timeMs > 0 && (
              <div className="flex items-center justify-between">
                <span>LATENCY:</span>
                <span className="text-[#F40009] font-bold">{timeMs} ms</span>
              </div>
            )}
          </div>
        </div>

        {/* Center/Main Editors Frame */}
        <div className="lg:col-span-10 flex flex-col">
          <div className="flex-grow grid grid-cols-1 md:grid-cols-2 min-h-[480px]">
            
            {/* Source Column */}
            <div className="border-r border-b border-[#E5DEC9] flex flex-col bg-white">
              <div className="px-5 py-3 border-b border-[#E5DEC9] bg-[#FAF6F0] flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold text-[#57534E]">SOURCE:</span>
                  <div className="relative">
                    <button
                      onClick={() => setOpenSource(!openSource)}
                      className="px-3 py-1 rounded-lg border border-[#D6CFC2] bg-white flex items-center gap-2 hover:border-[#F40009] font-space font-bold text-xs text-[#141413] cursor-pointer"
                    >
                      {sourceLang.name} ({sourceLang.ext})
                      <ChevronDown className="w-3.5 h-3.5 opacity-60" />
                    </button>

                    <AnimatePresence>
                      {openSource && (
                        <motion.div
                          initial={{ opacity: 0, y: 8 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: 8 }}
                          className="absolute left-0 mt-2 w-56 rounded-xl border-2 border-[#141413] bg-white p-2 shadow-xl z-30"
                        >
                          <input
                            type="text"
                            value={searchSource}
                            onChange={(e) => setSearchSource(e.target.value)}
                            placeholder="Search language..."
                            className="w-full h-8 px-3 rounded-lg bg-[#FAF6F0] border border-[#D6CFC2] text-xs text-[#141413] mb-2 focus:outline-none focus:border-[#F40009]"
                          />
                          <div className="max-h-52 overflow-y-auto space-y-0.5">
                            {filteredSource.map((lang) => (
                              <button
                                key={lang.name}
                                onClick={() => {
                                  setSourceLang(lang);
                                  setOpenSource(false);
                                }}
                                className="w-full text-left px-3 py-1.5 rounded-lg text-xs font-semibold text-[#141413] hover:bg-[#FAF6F0] flex items-center justify-between cursor-pointer"
                              >
                                <span>{lang.name}</span>
                                <span className="font-mono text-[10px] text-[#78716C]">P{lang.phase}</span>
                              </button>
                            ))}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                </div>

                {detectedLabel && detectedLangObj && (
                  <button
                    onClick={() => {
                      setSourceLang(detectedLangObj);
                      addLog(`ALIGN :: Switched source to detected ${detectedLangObj.name}`);
                    }}
                    title="Click to switch source language to detected dialect"
                    className="font-mono text-xs px-2.5 py-0.5 rounded-full bg-[#F40009]/10 hover:bg-[#F40009]/20 text-[#F40009] font-semibold transition-colors cursor-pointer"
                  >
                    Auto: {detectedLabel}
                  </button>
                )}
              </div>

              <div className="flex-grow p-4 min-h-[340px]">
                <CodeEditor
                  value={sourceCode}
                  onChange={(val) => setSourceCode(val || "")}
                  language={sourceLang.name.toLowerCase()}
                />
              </div>
            </div>

            {/* Target Column */}
            <div className="border-b border-[#E5DEC9] flex flex-col bg-white">
              <div className="px-5 py-3 border-b border-[#E5DEC9] bg-[#FAF6F0] flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold text-[#57534E]">TARGET:</span>
                  <div className="relative">
                    <button
                      onClick={() => setOpenTarget(!openTarget)}
                      className="px-3 py-1 rounded-lg border border-[#D6CFC2] bg-white flex items-center gap-2 hover:border-[#F40009] font-space font-bold text-xs text-[#141413] cursor-pointer"
                    >
                      {targetLang.name} ({targetLang.ext})
                      <ChevronDown className="w-3.5 h-3.5 opacity-60" />
                    </button>

                    <AnimatePresence>
                      {openTarget && (
                        <motion.div
                          initial={{ opacity: 0, y: 8 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: 8 }}
                          className="absolute left-0 mt-2 w-56 rounded-xl border-2 border-[#141413] bg-white p-2 shadow-xl z-30"
                        >
                          <input
                            type="text"
                            value={searchTarget}
                            onChange={(e) => setSearchTarget(e.target.value)}
                            placeholder="Search target..."
                            className="w-full h-8 px-3 rounded-lg bg-[#FAF6F0] border border-[#D6CFC2] text-xs text-[#141413] mb-2 focus:outline-none focus:border-[#F40009]"
                          />
                          <div className="max-h-52 overflow-y-auto space-y-0.5">
                            {filteredTarget.map((lang) => (
                              <button
                                key={lang.name}
                                onClick={() => {
                                  setTargetLang(lang);
                                  setOpenTarget(false);
                                }}
                                className="w-full text-left px-3 py-1.5 rounded-lg text-xs font-semibold text-[#141413] hover:bg-[#FAF6F0] flex items-center justify-between cursor-pointer"
                              >
                                <span>{lang.name}</span>
                                <span className="font-mono text-[10px] text-[#78716C]">P{lang.phase}</span>
                              </button>
                            ))}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <div className="flex items-center rounded-full border border-[#D6CFC2] bg-white p-0.5 font-mono text-xs">
                    <button
                      onClick={() => setOutputView("code")}
                      className={`px-2.5 py-0.5 rounded-full font-bold transition-all cursor-pointer ${
                        outputView === "code" ? "bg-[#F40009] text-white" : "text-[#57534E]"
                      }`}
                    >
                      CODE
                    </button>
                    <button
                      onClick={() => setOutputView("ast")}
                      className={`px-2.5 py-0.5 rounded-full font-bold transition-all cursor-pointer ${
                        outputView === "ast" ? "bg-[#F40009] text-white" : "text-[#57534E]"
                      }`}
                    >
                      IR AST
                    </button>
                  </div>
                  {targetCode && (
                    <>
                      <button
                        onClick={handleCopy}
                        className="p-1.5 rounded-lg border border-[#D6CFC2] bg-white text-[#141413] hover:border-[#F40009] cursor-pointer"
                        title="Copy"
                      >
                        {copied ? <Check className="w-3.5 h-3.5 text-[#F40009]" /> : <Copy className="w-3.5 h-3.5" />}
                      </button>
                      <button
                        onClick={handleDownload}
                        className="p-1.5 rounded-lg border border-[#D6CFC2] bg-white text-[#141413] hover:border-[#F40009] cursor-pointer"
                        title="Download"
                      >
                        <Download className="w-3.5 h-3.5" />
                      </button>
                    </>
                  )}
                </div>
              </div>

              <div className="flex-grow p-4 min-h-[340px]">
                <CodeEditor
                  value={outputView === "ast" ? (astTree || "// Compile source to inspect Rosetta IR AST...") : typedTargetCode}
                  language={outputView === "ast" ? "json" : targetLang.name.toLowerCase()}
                  readOnly
                />
              </div>
            </div>
          </div>

          {/* Bottom Console & Translate Action */}
          <div className="grid grid-cols-1 lg:grid-cols-12 bg-[#FAF6F0]">
            <div className="lg:col-span-8 p-4 font-mono text-xs text-[#57534E] flex flex-col h-36 border-r border-[#E5DEC9] overflow-hidden">
              <div className="flex items-center justify-between border-b border-[#E5DEC9] pb-1 mb-2 uppercase text-[11px] font-bold text-[#141413]">
                <span>COMPILER LOG STREAM</span>
                <span className="text-[#F40009]">● READY</span>
              </div>
              <div className="flex-grow overflow-y-auto space-y-1">
                {logs.map((log, idx) => (
                  <div key={idx} className="flex gap-2">
                    <span className="text-[#A8A29E]">[{idx.toString().padStart(2, "0")}]</span>
                    <span className={log.includes("SUCCESS") ? "text-[#F40009] font-semibold" : "text-[#44403C]"}>
                      {log}
                    </span>
                  </div>
                ))}
                <div ref={consoleBottomRef} />
              </div>
            </div>

            <div className="lg:col-span-4 p-5 flex flex-col justify-center items-center gap-2 bg-white">
              <button
                onClick={executeTranspilation}
                disabled={loading || !sourceCode.trim()}
                className="w-full h-12 rounded-full bg-[#F40009] hover:bg-[#d00008] text-white font-space font-bold tracking-wider text-sm flex items-center justify-center gap-2 shadow-md transition-all cursor-pointer disabled:opacity-50"
              >
                {loading ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    COMPILING...
                  </>
                ) : (
                  <>
                    <Play className="w-4 h-4 fill-current" />
                    TRANSLATE CODE
                  </>
                )}
              </button>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
