"use client";

import React, { useRef, useEffect, useState } from "react";
import Editor, { Monaco } from "@monaco-editor/react";

interface CodeEditorProps {
  value: string;
  onChange?: (val: string | undefined) => void;
  language: string;
  readOnly?: boolean;
  onMount?: (editor: any, monaco: Monaco) => void;
}

export default function CodeEditor({
  value,
  onChange,
  language,
  readOnly = false,
  onMount,
}: CodeEditorProps) {
  const editorRef = useRef<any>(null);
  const monacoRef = useRef<Monaco | null>(null);
  const [editorTheme, setEditorTheme] = useState<"rosetta-cream" | "rosetta-dark">("rosetta-cream");

  const getMonacoLanguage = (lang: string) => {
    const ext = lang.toLowerCase().trim();
    if (ext === ".py" || ext === "py" || ext === "python") return "python";
    if (ext === ".js" || ext === "js" || ext === "javascript") return "javascript";
    if (ext === ".ts" || ext === "ts" || ext === "typescript") return "typescript";
    if (ext === ".java" || ext === "java") return "java";
    if (ext === ".cpp" || ext === "cpp" || ext === "c++") return "cpp";
    if (ext === ".c" || ext === "c") return "c";
    if (ext === ".rs" || ext === "rs" || ext === "rust") return "rust";
    if (ext === ".go" || ext === "go") return "go";
    if (ext === ".sol" || ext === "solidity" || ext === "sol") return "solidity";
    if (ext === ".cbl" || ext === ".cob" || ext === "cobol") return "plaintext"; // COBOL does not have default monaco syntax and marks everything red
    if (ext === ".f90" || ext === ".f" || ext === "fortran") return "fortran";
    if (ext === ".pas" || ext === "pascal") return "pascal";
    if (ext === ".bas" || ext === "basic") return "basic";
    if (ext === ".lisp" || ext === "lisp") return "lisp";
    if (ext === ".rb" || ext === "ruby") return "ruby";
    if (ext === ".php" || ext === "php") return "php";
    if (ext === ".swift" || ext === "swift") return "swift";
    if (ext === ".kt" || ext === "kotlin") return "kotlin";
    if (ext === ".cs" || ext === "csharp" || ext === "cs") return "csharp";
    if (ext === ".dart" || ext === "dart") return "dart";
    if (ext === ".lua" || ext === "lua") return "lua";
    if (ext === ".r" || ext === "r") return "r";
    if (ext === ".jl" || ext === "julia") return "julia";
    if (ext === ".scala" || ext === "scala") return "scala";
    if (ext === ".hs" || ext === "haskell") return "haskell";
    if (ext === ".ex" || ext === ".exs" || ext === "elixir") return "elixir";
    if (ext === ".sh" || ext === ".bash" || ext === "bash") return "shell";
    if (ext === ".sql" || ext === "sql") return "sql";
    if (ext === ".m" || ext === "objc" || ext === "objective-c") return "objective-c";
    if (ext === ".move" || ext === "move") return "rust";
    if (ext === ".pm" || ext === ".plx" || ext === "perl") return "perl";
    return "plaintext";
  };

  useEffect(() => {
    const syncTheme = () => {
      const isDark = document.documentElement.classList.contains("dark");
      const targetTheme = isDark ? "rosetta-dark" : "rosetta-cream";
      setEditorTheme(targetTheme);
      if (monacoRef.current) {
        monacoRef.current.editor.setTheme(targetTheme);
      }
    };

    syncTheme();
    window.addEventListener("rosetta-theme-change", syncTheme);
    return () => window.removeEventListener("rosetta-theme-change", syncTheme);
  }, []);

  const handleEditorDidMount = (editor: any, monaco: Monaco) => {
    editorRef.current = editor;
    monacoRef.current = monaco;

    // 1. Warm Cream & Crimson Editorial Light Theme
    monaco.editor.defineTheme("rosetta-cream", {
      base: "vs",
      inherit: true,
      rules: [
        { token: "comment", foreground: "78716C", fontStyle: "italic" },
        { token: "keyword", foreground: "F40009", fontStyle: "bold" },
        { token: "string", foreground: "9A3412" },
        { token: "number", foreground: "B91C1C" },
        { token: "type", foreground: "141413", fontStyle: "bold" },
        { token: "class", foreground: "F40009", fontStyle: "bold" },
        { token: "function", foreground: "141413", fontStyle: "bold" },
      ],
      colors: {
        "editor.background": "#FAF6F0",
        "editor.foreground": "#141413",
        "editor.lineHighlightBackground": "#F3EDE2",
        "editorLineNumber.foreground": "#A8A29E",
        "editorLineNumber.activeForeground": "#F40009",
        "editor.selectionBackground": "#F4000920",
        "editorCursor.foreground": "#F40009",
      },
    });

    // 2. Deep Charcoal & Crimson Dark Theme
    monaco.editor.defineTheme("rosetta-dark", {
      base: "vs-dark",
      inherit: true,
      rules: [
        { token: "comment", foreground: "71717A", fontStyle: "italic" },
        { token: "keyword", foreground: "FF4D54", fontStyle: "bold" },
        { token: "string", foreground: "FCA5A5" },
        { token: "number", foreground: "F87171" },
        { token: "type", foreground: "F5F5F4", fontStyle: "bold" },
        { token: "class", foreground: "FF4D54", fontStyle: "bold" },
        { token: "function", foreground: "FFFFFF", fontStyle: "bold" },
      ],
      colors: {
        "editor.background": "#0B0B0E",
        "editor.foreground": "#F5F5F4",
        "editor.lineHighlightBackground": "#16161D",
        "editorLineNumber.foreground": "#52525B",
        "editorLineNumber.activeForeground": "#F40009",
        "editor.selectionBackground": "#F4000935",
        "editorCursor.foreground": "#F40009",
      },
    });

    const isDark = document.documentElement.classList.contains("dark");
    const initialTheme = isDark ? "rosetta-dark" : "rosetta-cream";
    setEditorTheme(initialTheme);
    monaco.editor.setTheme(initialTheme);

    if (onMount) {
      onMount(editor, monaco);
    }
  };

  return (
    <div className="w-full h-full border border-[#E5DEC9] bg-[#FAF6F0] rounded-xl overflow-hidden">
      <Editor
        height="100%"
        width="100%"
        theme={editorTheme}
        language={getMonacoLanguage(language)}
        value={value}
        onChange={onChange}
        onMount={handleEditorDidMount}
        loading={
          <div className="w-full h-full flex flex-col items-center justify-center bg-[#FAF6F0] text-[#57534E] gap-3">
            <div className="w-8 h-8 rounded-full border-2 border-t-[#F40009] border-[#E5DEC9] animate-spin"></div>
            <span className="font-mono text-xs tracking-wider">LOADING EDITOR...</span>
          </div>
        }
        options={{
          readOnly,
          fontSize: 13.5,
          fontFamily: "'IBM Plex Mono', monospace",
          fontLigatures: true,
          lineHeight: 22,
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          lineNumbersMinChars: 3,
          padding: { top: 12, bottom: 12 },
          smoothScrolling: true,
          cursorBlinking: "smooth",
          renderLineHighlight: "all",
          wordWrap: "on",
          automaticLayout: true,
        }}
      />
    </div>
  );
}
