import React from "react";

interface RosettaLogoProps {
  className?: string;
  size?: number;
}

/**
 * Simple, clean Coca-Cola style script wordmark + single ribbon wave for Rosetta.
 */
export default function RosettaLogo({
  className = "",
  size = 36,
}: RosettaLogoProps) {
  const height = size;
  const width = Math.round(size * 3.1);

  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 280 90"
      width={width}
      height={height}
      fill="none"
      className={className}
      aria-label="Rosetta"
    >
      {/* Clean Flowing Script Wordmark in Classic Crimson Red */}
      <text
        x="140"
        y="58"
        textAnchor="middle"
        fill="#F40009"
        style={{
          fontFamily: "'Lobster Two', 'Brush Script MT', cursive",
          fontStyle: "italic",
          fontWeight: 700,
          fontSize: "58px",
          letterSpacing: "0.5px",
        }}
      >
        Rosetta
      </text>

      {/* Single Clean Ribbon Wave */}
      <path
        d="M 28 74 C 95 54, 185 88, 254 64 C 188 82, 98 62, 34 79 Z"
        fill="#F40009"
      />
    </svg>
  );
}
