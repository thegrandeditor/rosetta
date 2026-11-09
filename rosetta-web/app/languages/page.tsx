import React, { Suspense } from "react";
import LanguagesClient from "@/components/sections/LanguagesClient";

export const unstable_instant = false;

export default function LanguagesMatrixPage() {
  return (
    <Suspense 
      fallback={
        <div className="min-h-screen bg-[#FAF6F0] text-[#141413] flex items-center justify-center font-mono text-xs">
          &gt; LOADING 50+ LANGUAGES CATALOG...
        </div>
      }
    >
      <LanguagesClient />
    </Suspense>
  );
}
