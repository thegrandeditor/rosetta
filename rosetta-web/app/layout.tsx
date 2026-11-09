import type { Metadata } from "next";
import Link from "next/link";
import RosettaLogo from "@/components/ui/RosettaLogo";
import ThemeToggle from "@/components/ui/ThemeToggle";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://rosetta-web.vercel.app"),
  title: "ROSETTA — Universal Language Transpiler | One Engine. Every Language. Zero Limits.",
  description:
    "Transpile between 45+ programming languages instantly. From COBOL, Fortran, and Ada to Rust, Python, TypeScript, Go, Zig, Mojo, Carbon, and Solidity.",
  keywords:
    "ROSETTA, universal transpiler, source-to-source compiler, COBOL to Rust, COBOL to Python, Fortran to Python, Solidity transpiler, Mojo, Zig, Carbon, legacy code modernization, developer tools",
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-snippet": -1,
      "max-image-preview": "large",
      "max-video-preview": -1,
    },
  },
  alternates: {
    canonical: "https://rosetta-web.vercel.app/",
    types: {
      "text/markdown": [
        { url: "https://rosetta-web.vercel.app/llms.txt", title: "LLMs.txt — AI Answer Engine Reference" },
        { url: "https://rosetta-web.vercel.app/llms-full.txt", title: "LLMs-Full.txt — Extended Technical Reference" },
      ],
    },
  },
  verification: {
    google: "google3715115663968f2f",
    other: {
      "msvalidate.01": "0BD8066F4CC63C5F1F3495E8324717C2",
    },
  },
  openGraph: {
    type: "website",
    url: "https://rosettaweb.up.railway.app/",
    siteName: "ROSETTA",
    title: "ROSETTA — Universal Language Transpiler (50+ Languages)",
    description:
      "One Engine. Every Language. Zero Limits. Instant deterministic AST code translation across 50+ programming languages.",
  },
  twitter: {
    card: "summary_large_image",
    title: "ROSETTA — Universal Language Transpiler (50+ Languages)",
    description:
      "Transpile between 50+ programming languages instantly — from COBOL, Fortran, C++, Java to Rust, Python, TypeScript, Mojo, Solidity, and Matlab.",
  },
};

const jsonLdGraph = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://rosetta-web.vercel.app/#website",
      "url": "https://rosetta-web.vercel.app/",
      "name": "ROSETTA — Universal Language Transpiler",
      "description":
        "Universal programming language transpiler supporting 45+ languages across legacy mainframes, systems engineering, web/cloud, AI, and Web3.",
      "publisher": { "@id": "https://rosetta-web.vercel.app/#organization" },
      "inLanguage": "en-US",
    },
    {
      "@type": "Organization",
      "@id": "https://rosetta-web.vercel.app/#organization",
      "name": "ROSETTA Labs / MOGGA INC",
      "url": "https://rosetta-web.vercel.app/",
      "sameAs": [
        "https://worldreasoning.moggainc.workers.dev/",
        "https://lag-annihilator.moggainc.workers.dev/",
        "https://forge.moggainc.workers.dev/",
        "https://koderkids.moggainc.workers.dev/",
        "https://cadence.moggainc.workers.dev/",
      ],
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://rosetta-web.vercel.app/#app",
      "name": "ROSETTA",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "Web, Windows, macOS, Linux",
      "url": "https://rosetta-web.vercel.app/",
      "description":
        "Transpile between 45+ programming languages instantly. From COBOL to Carbon, legacy systems to emerging blockchains.",
      "featureList": [
        "Bidirectional transpilation across 45+ programming languages",
        "Legacy mainframe modernization (COBOL, Fortran, Ada, Pascal, RPG to Rust, Python, Go, TypeScript)",
        "Emerging systems and AI language support (Mojo, Zig, Carbon, Rust, Solidity, Move, Cairo)",
        "Interactive browser workbench (/transpile) and CLI automation (/docs)",
      ],
      "publisher": { "@id": "https://rosetta-web.vercel.app/#organization" },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "ratingCount": "88",
        "bestRating": "5",
        "worstRating": "1",
      },
      "offers": {
        "@type": "Offer",
        "price": "0.00",
        "priceCurrency": "USD",
      },
    },
    {
      "@type": "FAQPage",
      "@id": "https://rosetta-web.vercel.app/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How many programming languages does ROSETTA transpile?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "ROSETTA supports bidirectional transpilation across 45+ programming languages, spanning legacy mainframe languages (COBOL, Fortran, Ada), modern systems languages (Rust, Zig, Carbon, Go, C++), web/cloud stacks (TypeScript, Python, Java, Kotlin, Swift), AI languages (Mojo, Julia), and smart contract languages (Solidity, Move, Cairo).",
          },
        },
        {
          "@type": "Question",
          "name": "Does ROSETTA offer both a web workbench and a CLI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Developers can translate snippets interactively in the web workbench at https://rosetta-web.vercel.app/transpile or automate full-repository migrations via the ROSETTA CLI documented at https://rosetta-web.vercel.app/docs.",
          },
        },
      ],
    },
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased" suppressHydrationWarning>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLdGraph) }}
        />
      </head>
      <body className="min-h-full flex flex-col bg-[#FAF6F0] text-[#141413] font-sans selection:bg-[#F40009]/20 selection:text-[#141413]">
        
        {/* Clean Editorial Navbar */}
        <header className="sticky top-0 z-50 w-full border-b border-[#E5DEC9] bg-[#FAF6F0]/90 backdrop-blur-md">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div className="flex items-center gap-8">
              {/* Logo / Brand */}
              <Link href="/" className="flex items-center group">
                <RosettaLogo size={38} className="group-hover:opacity-85 transition-opacity" />
              </Link>

              {/* Navigation Links */}
              <nav className="hidden md:flex items-center gap-6">
                <Link 
                  href="/transpile" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  Workbench
                </Link>
                <Link 
                  href="/languages" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  50+ Languages
                </Link>
                <Link 
                  href="/benchmarks" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  Benchmarks
                </Link>
                <Link 
                  href="/docs" 
                  className="font-space text-sm font-semibold text-[#F40009] hover:text-[#b80007] transition-colors"
                >
                  CLI &amp; Docs
                </Link>
                <Link 
                  href="/faq" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  FAQ
                </Link>
                <Link 
                  href="/support" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  Support
                </Link>
                <Link 
                  href="/#how-it-works" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  How it Works
                </Link>
                <Link 
                  href="/#enterprise" 
                  className="font-space text-sm font-medium text-[#57534E] hover:text-[#141413] transition-colors"
                >
                  Enterprise
                </Link>
              </nav>
            </div>

            {/* Theme Toggle + CTA Button */}
            <div className="flex items-center gap-3">
              <ThemeToggle />
              <Link 
                href="/transpile" 
                className="inline-flex items-center justify-center px-5 py-2 text-sm font-semibold text-white rounded-full bg-[#F40009] hover:bg-[#d00008] transition-all shadow-sm"
              >
                Translate Now
              </Link>
            </div>
          </div>
        </header>

        {/* Core Layout Content */}
        <main className="flex-grow z-10 relative">
          {children}
        </main>

        {/* Global Footer */}
        <footer className="z-10 relative border-t border-[#E5DEC9] bg-[#F3EDE2] py-8 text-center text-xs text-[#57534E] font-mono">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <RosettaLogo size={26} />
              <span>&copy; 2026 ROSETTA Labs. All rights reserved.</span>
            </div>
            <div className="flex items-center gap-4 flex-wrap justify-center">
              <span className="text-[#141413] font-medium">One Engine. Every Language. Zero Limits.</span>
              <Link href="/benchmarks" className="hover:underline">Benchmarks</Link>
              <Link href="/faq" className="hover:underline">FAQ</Link>
              <Link href="/support" className="hover:underline">Support</Link>
              <Link href="/docs" className="hover:underline">Docs</Link>
              <a href="/llms.txt" className="hover:underline">LLMs.txt</a>
              <a href="/sitemap.xml" className="hover:underline">Sitemap</a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
