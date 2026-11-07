"use client";

import React, { useEffect, useState } from "react";
import { Sun, Moon } from "lucide-react";

export default function ThemeToggle() {
  const [isDark, setIsDark] = useState(false);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const saved = localStorage.getItem("rosetta-theme");
    if (saved === "dark") {
      document.documentElement.classList.add("dark");
      setIsDark(true);
    } else {
      document.documentElement.classList.remove("dark");
      setIsDark(false);
    }
    window.dispatchEvent(new CustomEvent("rosetta-theme-change", { detail: saved === "dark" ? "dark" : "light" }));
  }, []);

  const toggleTheme = () => {
    const nextDark = !isDark;
    setIsDark(nextDark);
    if (nextDark) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("rosetta-theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("rosetta-theme", "light");
    }
    window.dispatchEvent(new CustomEvent("rosetta-theme-change", { detail: nextDark ? "dark" : "light" }));
  };

  if (!mounted) {
    return (
      <div className="w-9 h-9 rounded-full border border-[#E5DEC9] bg-white flex items-center justify-center opacity-50" />
    );
  }

  return (
    <button
      onClick={toggleTheme}
      className="w-9 h-9 rounded-full border border-[#E5DEC9] bg-white text-[#141413] hover:border-[#F40009] flex items-center justify-center transition-all cursor-pointer"
      title={isDark ? "Switch to Warm Cream Light Mode" : "Switch to Dark Mode"}
      aria-label="Toggle Light and Dark Mode"
    >
      {isDark ? (
        <Sun className="w-4 h-4 text-[#F40009]" />
      ) : (
        <Moon className="w-4 h-4 text-[#141413]" />
      )}
    </button>
  );
}
