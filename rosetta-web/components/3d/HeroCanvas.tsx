"use client";

import React from "react";
import { Canvas } from "@react-three/fiber";
import RosettaStone from "./RosettaStone";
import LanguageOrbs from "./LanguageOrbs";

export default function HeroCanvas() {
  return (
    <div className="w-full h-full relative">
      <Canvas
        camera={{ position: [0, 0, 7.5], fov: 45 }}
        gl={{ antialias: true, alpha: true }}
        style={{ background: "transparent" }}
      >
        {/* Futuristic Space Studio Lighting Setup */}
        <ambientLight intensity={0.65} />
        <directionalLight position={[5, 10, 5]} intensity={1.5} />
        <directionalLight position={[-5, -10, -5]} intensity={0.5} color="#F40009" />
        
        {/* Core 3D objects */}
        <RosettaStone />
        <LanguageOrbs />
      </Canvas>
    </div>
  );
}
