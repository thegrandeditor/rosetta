"use client";

import React, { useRef, useState } from "react";
import { useFrame } from "@react-three/fiber";
import { Html } from "@react-three/drei";
import * as THREE from "three";

interface LanguageOrbData {
  name: string;
  phase: number;
  color: string;
  paradigm: string;
  featured?: boolean;
}

// 32 Languages classified by phase
const ORB_LANGUAGES: LanguageOrbData[] = [
  // Phase 1 & 2: Foundation & Modern
  { name: "Python", phase: 1, color: "#F40009", paradigm: "Multi-paradigm", featured: true },
  { name: "JavaScript", phase: 1, color: "#FFFFFF", paradigm: "Event-driven", featured: true },
  { name: "TypeScript", phase: 1, color: "#F40009", paradigm: "Static OOP" },
  { name: "Java", phase: 1, color: "#FFFFFF", paradigm: "OOP" },
  { name: "C++", phase: 1, color: "#F40009", paradigm: "Systems OOP", featured: true },
  { name: "C", phase: 1, color: "#FFFFFF", paradigm: "Procedural" },
  { name: "Rust", phase: 1, color: "#F40009", paradigm: "Safe Systems", featured: true },
  { name: "Go", phase: 1, color: "#FFFFFF", paradigm: "Concurrent" },
  { name: "Swift", phase: 1, color: "#F40009", paradigm: "Multi-paradigm" },
  { name: "Kotlin", phase: 1, color: "#FFFFFF", paradigm: "Functional OOP" },
  { name: "Ruby", phase: 1, color: "#F40009", paradigm: "Dynamic OOP" },
  { name: "PHP", phase: 1, color: "#FFFFFF", paradigm: "Web Scripting" },
  { name: "COBOL", phase: 2, color: "#F40009", paradigm: "Legacy Business", featured: true },

  // Phase 3: Legacy & Lost
  { name: "Fortran", phase: 3, color: "#FF4D54", paradigm: "Scientific" },
  { name: "BASIC", phase: 3, color: "#FFFFFF", paradigm: "Structured" },
  { name: "Pascal", phase: 3, color: "#FF4D54", paradigm: "Structured" },
  { name: "Ada", phase: 3, color: "#FFFFFF", paradigm: "Real-time" },
  { name: "LISP", phase: 3, color: "#FF4D54", paradigm: "Functional" },
  { name: "Algol", phase: 3, color: "#FFFFFF", paradigm: "Procedural" },
  { name: "Smalltalk", phase: 3, color: "#FF4D54", paradigm: "Pure OOP" },
  { name: "Prolog", phase: 3, color: "#FFFFFF", paradigm: "Logic Rules" },

  // Phase 4: Declarative & Specialized
  { name: "SNOBOL4", phase: 4, color: "#F40009", paradigm: "Pattern Match" },
  { name: "PL/I", phase: 4, color: "#FFFFFF", paradigm: "Structured" },
  { name: "Modula-2", phase: 4, color: "#F40009", paradigm: "Modular" },
  { name: "RPG", phase: 4, color: "#FFFFFF", paradigm: "Business Reports" },
  { name: "Eiffel", phase: 4, color: "#F40009", paradigm: "Design Contract" },
  { name: "Forth", phase: 4, color: "#FFFFFF", paradigm: "Stack-based" },
  { name: "ML", phase: 4, color: "#F40009", paradigm: "Functional" },

  // Phase 5: Emerging & Future
  { name: "Solidity", phase: 5, color: "#FFFFFF", paradigm: "Blockchain", featured: true },
  { name: "Mojo", phase: 5, color: "#F40009", paradigm: "AI Hardware" },
  { name: "Zig", phase: 5, color: "#FFFFFF", paradigm: "General Systems" },
  { name: "Carbon", phase: 5, color: "#F40009", paradigm: "C++ Successor", featured: true },
];

function Orb({ data, index, count }: { data: LanguageOrbData; index: number; count: number }) {
  const meshRef = useRef<THREE.Mesh>(null);
  const [hovered, setHovered] = useState(false);

  const getRadius = (phase: number) => {
    switch (phase) {
      case 1:
      case 2:
        return 2.5;
      case 3:
        return 3.4;
      case 4:
        return 4.3;
      case 5:
        return 5.2;
      default:
        return 3.0;
    }
  };

  const radius = getRadius(data.phase);
  const angleOffset = (index / count) * Math.PI * 2;
  const speed = 0.15 + (5 - data.phase) * 0.03;

  useFrame((state) => {
    if (!meshRef.current) return;
    const time = state.clock.getElapsedTime();
    const currentAngle = time * speed + angleOffset;

    meshRef.current.position.x = Math.cos(currentAngle) * radius;
    meshRef.current.position.z = Math.sin(currentAngle) * radius;
    meshRef.current.position.y = Math.sin(time * 1.2 + index) * 0.12;
  });

  // Only render HTML tag when hovered or for a small set of featured key languages to prevent DOM thrashing
  const showLabel = hovered || data.featured;

  return (
    <mesh
      ref={meshRef}
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
    >
      <sphereGeometry args={[hovered ? 0.14 : 0.08, 12, 12]} />
      <meshBasicMaterial color={data.color} />

      <mesh>
        <sphereGeometry args={[hovered ? 0.26 : 0.14, 6, 6]} />
        <meshBasicMaterial
          color={data.color}
          transparent
          opacity={hovered ? 0.5 : 0.15}
          wireframe
        />
      </mesh>

      {showLabel && (
        <Html distanceFactor={10} position={[0, hovered ? 0.28 : 0.2, 0]} center>
          <div
            className={`px-2 py-0.5 rounded-full border text-[9px] font-space font-medium tracking-wide transition-all pointer-events-none select-none backdrop-blur-md shadow-lg ${
              hovered
                ? "bg-[#0a0a0f] text-white opacity-100 scale-110"
                : "bg-[#050508]/85 text-white/60 border-white/10 opacity-80"
            }`}
            style={{
              borderColor: data.color + (hovered ? "80" : "30"),
              boxShadow: hovered ? `0 0 12px ${data.color}40` : "none",
              color: hovered ? data.color : "",
            }}
          >
            {data.name}
            {hovered && (
              <div className="text-[7px] text-white/40 mt-0.5 whitespace-nowrap">
                {data.paradigm} (P{data.phase})
              </div>
            )}
          </div>
        </Html>
      )}
    </mesh>
  );
}

export default function LanguageOrbs() {
  return (
    <group>
      {ORB_LANGUAGES.map((lang, idx) => (
        <Orb
          key={lang.name}
          data={lang}
          index={idx}
          count={ORB_LANGUAGES.length}
        />
      ))}
    </group>
  );
}
