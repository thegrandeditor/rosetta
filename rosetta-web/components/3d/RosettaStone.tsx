"use client";

import React, { useRef, useState } from "react";
import { useFrame } from "@react-three/fiber";
import { MeshDistortMaterial, Stars } from "@react-three/drei";
import * as THREE from "three";

export default function RosettaStone() {
  const meshRef = useRef<THREE.Mesh>(null);
  const [hovered, setHovered] = useState(false);

  // Animate rotation and floating (up/down)
  useFrame((state) => {
    if (!meshRef.current) return;
    
    // Slow Y-axis rotation
    meshRef.current.rotation.y = state.clock.getElapsedTime() * 0.25;
    
    // Float up and down using a sine wave
    meshRef.current.position.y = Math.sin(state.clock.getElapsedTime() * 1.2) * 0.15;
    
    // Gentle rocking
    meshRef.current.rotation.x = Math.sin(state.clock.getElapsedTime() * 0.6) * 0.05;
    meshRef.current.rotation.z = Math.cos(state.clock.getElapsedTime() * 0.6) * 0.03;
  });

  return (
    <group>
      {/* Decorative background stars inside the canvas container */}
      <Stars radius={100} depth={50} count={300} factor={4} saturation={0} fade speed={1} />
      
      {/* Primary 3D Monolith Mesh */}
      <mesh
        ref={meshRef}
        onPointerOver={() => setHovered(true)}
        onPointerOut={() => setHovered(false)}
        scale={hovered ? [1.08, 1.08, 1.08] : [1, 1, 1]}
        transition-all="true"
      >
        {/* Monolith geometric block */}
        <boxGeometry args={[1.8, 2.8, 0.45]} />
        
        {/* Futuristic dark glossy obsidian-like material with slight distortion */}
        <MeshDistortMaterial
          color={hovered ? "#4a0409" : "#14080a"}
          roughness={0.15}
          metalness={0.9}
          clearcoat={1.0}
          clearcoatRoughness={0.1}
          distort={0.1}
          speed={1.5}
        />

        {/* Glowing holographic inner core wireframe */}
        <mesh scale={[1.02, 1.02, 1.02]}>
          <boxGeometry args={[1.8, 2.8, 0.45]} />
          <meshBasicMaterial
            color={hovered ? "#FFFFFF" : "#F40009"}
            wireframe
            transparent
            opacity={hovered ? 0.6 : 0.3}
          />
        </mesh>

        {/* Embedded symbolic carved glowing lights */}
        <mesh position={[0, 0, 0.23]}>
          <planeGeometry args={[1.4, 2.2]} />
          <meshBasicMaterial
            color={hovered ? "#FFFFFF" : "#F40009"}
            transparent
            opacity={hovered ? 0.15 : 0.08}
          />
        </mesh>
      </mesh>

      {/* Ambient glowing spotlight behind the stone */}
      <pointLight 
        position={[0, 0, 2]} 
        intensity={hovered ? 4.5 : 2.5} 
        color={hovered ? "#FFFFFF" : "#F40009"} 
        distance={8}
      />
    </group>
  );
}
