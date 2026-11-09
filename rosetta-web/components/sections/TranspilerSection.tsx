"use client";

import React, { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Copy, Download, Zap, RefreshCw, ChevronDown, Check, Play, Info } from "lucide-react";
import CodeEditor from "../ui/CodeEditor";

interface LanguageOption {
  name: string;
  ext: string;
  phase: number;
  badgeColor: string;
  type: "source" | "target" | "both";
}

const LANGUAGES: LanguageOption[] = [
  { name: "Python", ext: ".py", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "JavaScript", ext: ".js", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "TypeScript", ext: ".ts", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Java", ext: ".java", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "C++", ext: ".cpp", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "C", ext: ".c", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Rust", ext: ".rs", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Go", ext: ".go", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Swift", ext: ".swift", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Kotlin", ext: ".kt", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Ruby", ext: ".rb", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "PHP", ext: ".php", phase: 1, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "COBOL", ext: ".cbl", phase: 2, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Fortran", ext: ".f90", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Visual Basic", ext: ".vb", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Delphi", ext: ".delphi", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "BASIC", ext: ".bas", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Pascal", ext: ".pas", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Ada", ext: ".adb", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "LISP", ext: ".lisp", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Algol", ext: ".alg", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Smalltalk", ext: ".st", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Prolog", ext: ".pl", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "SNOBOL4", ext: ".sno", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "PL/I", ext: ".pli", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Modula-2", ext: ".mod", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "RPG", ext: ".rpg", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Eiffel", ext: ".e", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Forth", ext: ".fs", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "ML", ext: ".ml", phase: 4, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Solidity", ext: ".sol", phase: 5, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Mojo", ext: ".mojo", phase: 5, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Zig", ext: ".zig", phase: 5, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Carbon", ext: ".carbon", phase: 5, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "C#", ext: ".cs", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Dart", ext: ".dart", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Lua", ext: ".lua", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "R", ext: ".r", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Julia", ext: ".jl", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Scala", ext: ".scala", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Haskell", ext: ".hs", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Elixir", ext: ".ex", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Bash", ext: ".sh", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "PowerShell", ext: ".ps1", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Arduino", ext: ".ino", phase: 5, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "SQL", ext: ".sql", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Objective-C", ext: ".m", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Move", ext: ".move", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "Perl", ext: ".pm", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Matlab", ext: ".matlab", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" },
  { name: "VBA", ext: ".vba", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "Assembly", ext: ".asm", phase: 3, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "HCL", ext: ".tf", phase: 6, badgeColor: "bg-[#F3EDE2] text-[#44403C] border-[#D6CFC2]", type: "both" },
  { name: "GraphQL", ext: ".gql", phase: 6, badgeColor: "bg-[#F40009]/10 text-[#F40009] border-[#F40009]/25", type: "both" }
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

export default function TranspilerSection() {
  const [sourceCode, setSourceCode] = useState(SAMPLE_CODES.COBOL.code);
  const [targetCode, setTargetCode] = useState("");
  const [typedTargetCode, setTypedTargetCode] = useState("");
  
  const [sourceLang, setSourceLang] = useState<LanguageOption>(LANGUAGES.find(l => l.ext === ".cbl")!);
  const [targetLang, setTargetLang] = useState<LanguageOption>(LANGUAGES.find(l => l.ext === ".py")!);
  
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);
  
  const [searchSource, setSearchSource] = useState("");
  const [searchTarget, setSearchTarget] = useState("");
  
  const [openSourceDropdown, setOpenSourceDropdown] = useState(false);
  const [openTargetDropdown, setOpenTargetDropdown] = useState(false);
  
  const [tokensUsed, setTokensUsed] = useState(0);
  const [timeMs, setTimeMs] = useState(0);

  const typewriterIntervalRef = useRef<NodeJS.Timeout | null>(null);
  const sourceLangRef = useRef<LanguageOption>(sourceLang);
  useEffect(() => {
    sourceLangRef.current = sourceLang;
  }, [sourceLang]);

  useEffect(() => {
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
            if (detected && detected.ext !== sourceLangRef.current.ext) {
              setSourceLang(detected);
            }
          }
        }
      } catch (err) {}
    }, 400);

    return () => clearTimeout(delayDebounceFn);
  }, [sourceCode]);

  const loadSample = (key: keyof typeof SAMPLE_CODES) => {
    const sample = SAMPLE_CODES[key];
    setSourceCode(sample.code);
    const src = LANGUAGES.find(l => l.ext === sample.ext);
    const tgt = LANGUAGES.find(l => l.ext === `.${sample.target}` || l.ext === sample.target);
    if (src) setSourceLang(src);
    if (tgt) setTargetLang(tgt);
    setTargetCode("");
    setTypedTargetCode("");
  };

  const handleTranslate = async () => {
    if (!sourceCode.trim()) return;
    setLoading(true);
    setTargetCode("");
    setTypedTargetCode("");
    if (typewriterIntervalRef.current) clearInterval(typewriterIntervalRef.current);

    try {
      const fromExt = sourceLang.ext;
      const toExt = targetLang.ext.replace(".", "");

      const res = await fetch("/api/transpile", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ source: sourceCode, from_lang: fromExt, to_lang: toExt })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || "Transpilation engine failure");
      }

      const data = await res.json();
      const output = (data.result && data.result.trim())
        ? data.result
        : `// [ROSETTA COMPILER NOTICE]\n// 0 statements were produced by the ${sourceLang.name} parser.\n// Please select the matching Source language above.`;
      setTargetCode(output);
      setTokensUsed(data.tokens_used);
      setTimeMs(data.time_ms);

      let currentIndex = 0;
      const increment = Math.max(1, Math.ceil(output.length / 50));

      typewriterIntervalRef.current = setInterval(() => {
        if (currentIndex < output.length) {
          currentIndex += increment;
          setTypedTargetCode(output.slice(0, currentIndex));
        } else {
          setTypedTargetCode(output);
          if (typewriterIntervalRef.current) clearInterval(typewriterIntervalRef.current);
        }
      }, 15);
    } catch (err: any) {
      setTargetCode(`// Error: ${err.message || "Failed to compile. Please check connection."}`);
      setTypedTargetCode(`// Error: ${err.message || "Failed to compile. Please check connection."}`);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(targetCode || typedTargetCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const element = document.createElement("a");
    const file = new Blob([targetCode || typedTargetCode], { type: "text/plain" });
    element.href = URL.createObjectURL(file);
    element.download = `translated_code${targetLang.ext}`;
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  const filteredSourceLanguages = LANGUAGES.filter(
    (l) => l.type !== "target" && l.name.toLowerCase().includes(searchSource.toLowerCase())
  );
  const filteredTargetLanguages = LANGUAGES.filter(
    (l) => l.type !== "source" && l.name.toLowerCase().includes(searchTarget.toLowerCase())
  );

  return (
    <section id="workbench" className="py-20 bg-[#FAF6F0]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header Block */}
        <div className="text-center max-w-3xl mx-auto mb-12">
          <h2 className="font-space text-3xl md:text-4xl font-extrabold tracking-tight text-[#141413]">
            Interactive Compiler Studio
          </h2>
          <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base">
            Paste any source program below, choose your target language, and run the Rosetta compiler in real time.
          </p>
        </div>

        {/* Quick Sample Selector Bar */}
        <div className="flex flex-wrap items-center justify-center gap-2.5 mb-8">
          <span className="font-mono text-xs text-[#57534E] font-semibold uppercase mr-1">
            Load Sample:
          </span>
          {Object.keys(SAMPLE_CODES).map((key) => (
            <button
              key={key}
              onClick={() => loadSample(key as any)}
              className="px-4 py-1.5 rounded-full border border-[#D6CFC2] bg-white text-xs font-bold text-[#141413] hover:border-[#F40009] hover:text-[#F40009] transition-all cursor-pointer"
            >
              {key}
            </button>
          ))}
        </div>

        {/* Core Double Editor Workbench */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 items-stretch min-h-[480px]">
          
          {/* LEFT: SOURCE PANEL */}
          <div className="editorial-card rounded-2xl flex flex-col overflow-hidden bg-white relative">
            <div className="h-14 px-4 border-b border-[#E5DEC9] bg-[#FAF6F0] flex items-center justify-between z-20">
              <div className="relative">
                <button
                  onClick={() => {
                    setOpenSourceDropdown(!openSourceDropdown);
                    setOpenTargetDropdown(false);
                  }}
                  className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white border border-[#D6CFC2] text-xs font-bold text-[#141413] hover:border-[#F40009] transition-all cursor-pointer"
                >
                  <span>Source: {sourceLang.name}</span>
                  <span className={`px-1.5 py-0.5 rounded text-[9px] font-mono border ${sourceLang.badgeColor}`}>
                    P{sourceLang.phase}
                  </span>
                  <ChevronDown className="w-3.5 h-3.5 opacity-60" />
                </button>

                <AnimatePresence>
                  {openSourceDropdown && (
                    <motion.div
                      initial={{ opacity: 0, y: 8 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: 8 }}
                      className="absolute left-0 mt-2 w-64 bg-white border-2 border-[#141413] rounded-xl overflow-hidden shadow-xl z-30 max-h-80 flex flex-col"
                    >
                      <div className="p-2 border-b border-[#E5DEC9] bg-[#FAF6F0]">
                        <input
                          type="text"
                          placeholder="Search languages..."
                          value={searchSource}
                          onChange={(e) => setSearchSource(e.target.value)}
                          className="w-full px-3 py-1.5 rounded-lg bg-white border border-[#D6CFC2] text-xs text-[#141413] placeholder-[#78716C] focus:outline-none focus:border-[#F40009]"
                        />
                      </div>
                      <div className="overflow-y-auto flex-grow p-1">
                        {filteredSourceLanguages.map((lang) => (
                          <button
                            key={lang.name}
                            onClick={() => {
                              setSourceLang(lang);
                              setOpenSourceDropdown(false);
                            }}
                            className={`w-full text-left px-3 py-2 rounded-lg text-xs font-semibold hover:bg-[#FAF6F0] transition-all flex items-center justify-between cursor-pointer ${
                              sourceLang.ext === lang.ext ? "bg-[#F40009]/10 text-[#F40009]" : "text-[#141413]"
                            }`}
                          >
                            <span>{lang.name} ({lang.ext})</span>
                            <span className={`px-1.5 py-0.5 rounded text-[9px] font-mono border ${lang.badgeColor}`}>
                              P{lang.phase}
                            </span>
                          </button>
                        ))}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>

              <div className="flex items-center gap-3">
                <span className="font-mono text-xs text-[#57534E] hidden sm:inline">
                  {sourceCode.length} chars
                </span>
                <span className="h-2.5 w-2.5 rounded-full bg-[#F40009]"></span>
              </div>
            </div>

            <div className="flex-grow min-h-[380px] p-4 bg-white">
              <CodeEditor
                value={sourceCode}
                onChange={(val) => setSourceCode(val || "")}
                language={sourceLang.ext}
              />
            </div>
          </div>

          {/* RIGHT: TARGET OUTPUT PANEL */}
          <div className="editorial-card rounded-2xl flex flex-col overflow-hidden bg-white relative">
            <div className="h-14 px-4 border-b border-[#E5DEC9] bg-[#FAF6F0] flex items-center justify-between z-20">
              <div className="relative">
                <button
                  onClick={() => {
                    setOpenTargetDropdown(!openTargetDropdown);
                    setOpenSourceDropdown(false);
                  }}
                  className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-white border border-[#D6CFC2] text-xs font-bold text-[#141413] hover:border-[#F40009] transition-all cursor-pointer"
                >
                  <span>Target: {targetLang.name}</span>
                  <span className={`px-1.5 py-0.5 rounded text-[9px] font-mono border ${targetLang.badgeColor}`}>
                    P{targetLang.phase}
                  </span>
                  <ChevronDown className="w-3.5 h-3.5 opacity-60" />
                </button>

                <AnimatePresence>
                  {openTargetDropdown && (
                    <motion.div
                      initial={{ opacity: 0, y: 8 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: 8 }}
                      className="absolute left-0 mt-2 w-64 bg-white border-2 border-[#141413] rounded-xl overflow-hidden shadow-xl z-30 max-h-80 flex flex-col"
                    >
                      <div className="p-2 border-b border-[#E5DEC9] bg-[#FAF6F0]">
                        <input
                          type="text"
                          placeholder="Search targets..."
                          value={searchTarget}
                          onChange={(e) => setSearchTarget(e.target.value)}
                          className="w-full px-3 py-1.5 rounded-lg bg-white border border-[#D6CFC2] text-xs text-[#141413] placeholder-[#78716C] focus:outline-none focus:border-[#F40009]"
                        />
                      </div>
                      <div className="overflow-y-auto flex-grow p-1">
                        {filteredTargetLanguages.map((lang) => (
                          <button
                            key={lang.name}
                            onClick={() => {
                              setTargetLang(lang);
                              setOpenTargetDropdown(false);
                            }}
                            className={`w-full text-left px-3 py-2 rounded-lg text-xs font-semibold hover:bg-[#FAF6F0] transition-all flex items-center justify-between cursor-pointer ${
                              targetLang.ext === lang.ext ? "bg-[#F40009]/10 text-[#F40009]" : "text-[#141413]"
                            }`}
                          >
                            <span>{lang.name} ({lang.ext})</span>
                            <span className={`px-1.5 py-0.5 rounded text-[9px] font-mono border ${lang.badgeColor}`}>
                              P{lang.phase}
                            </span>
                          </button>
                        ))}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>

              <div className="flex items-center gap-2">
                <button
                  disabled={!targetCode}
                  onClick={handleCopy}
                  className={`p-2 rounded-lg border transition-all ${
                    targetCode 
                      ? "border-[#D6CFC2] bg-white hover:border-[#F40009] text-[#141413] cursor-pointer" 
                      : "border-transparent opacity-30 cursor-not-allowed"
                  }`}
                  title="Copy to Clipboard"
                >
                  {copied ? <Check className="w-4 h-4 text-[#F40009]" /> : <Copy className="w-4 h-4" />}
                </button>
                <button
                  disabled={!targetCode}
                  onClick={handleDownload}
                  className={`p-2 rounded-lg border transition-all ${
                    targetCode 
                      ? "border-[#D6CFC2] bg-white hover:border-[#F40009] text-[#141413] cursor-pointer" 
                      : "border-transparent opacity-30 cursor-not-allowed"
                  }`}
                  title="Download File"
                >
                  <Download className="w-4 h-4" />
                </button>
              </div>
            </div>

            <div className="flex-grow min-h-[380px] p-4 bg-white">
              <CodeEditor
                value={typedTargetCode}
                language={targetLang.ext}
                readOnly
              />
            </div>

            {typedTargetCode && (
              <div className="px-4 py-2.5 border-t border-[#E5DEC9] bg-[#FAF6F0] flex items-center justify-between text-xs font-mono text-[#57534E]">
                <div className="flex items-center gap-2 font-bold text-[#F40009]">
                  <Zap className="w-3.5 h-3.5" />
                  <span>TRANSPILATION COMPLETE</span>
                </div>
                <div className="flex items-center gap-4">
                  <span>TIME: <strong className="text-[#141413]">{timeMs} ms</strong></span>
                  <span>TOKENS: <strong className="text-[#141413]">{tokensUsed}</strong></span>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* COMPILATION TRIGGER BUTTON */}
        <div className="mt-8 flex flex-col items-center gap-2">
          <button
            onClick={handleTranslate}
            disabled={loading || !sourceCode.trim()}
            className={`px-9 py-4 rounded-full font-space font-bold tracking-wider text-sm flex items-center justify-center gap-3 transition-all shadow-md ${
              loading 
                ? "bg-[#F40009]/50 text-white cursor-wait" 
                : "bg-[#F40009] hover:bg-[#d00008] text-white cursor-pointer"
            }`}
          >
            {loading ? (
              <>
                <RefreshCw className="w-4 h-4 animate-spin" />
                <span>COMPILING IN ROSETTA...</span>
              </>
            ) : (
              <>
                <Play className="w-4 h-4 fill-current" />
                <span>TRANSLATE CODE NOW</span>
              </>
            )}
          </button>
          <div className="flex items-center gap-1.5 text-xs text-[#57534E] font-mono">
            <Info className="w-3.5 h-3.5 text-[#F40009]" />
            <span>Auto-detection active across all 45+ languages</span>
          </div>
        </div>

      </div>
    </section>
  );
}
