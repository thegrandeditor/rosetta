"use client";

import React, { useEffect, useRef } from "react";

interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  color: string;
}

export default function ParticleField() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const mouseRef = useRef({ x: 0, y: 0, targetX: 0, targetY: 0 });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animationFrameId: number;
    let particles: Particle[] = [];

    // Scale particle count for fast, buttery smooth 60fps rendering
    const isMobile = typeof window !== "undefined" && window.innerWidth < 768;
    const particleCount = isMobile ? 35 : 70;

    const resizeCanvas = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);

    // Initialize Particles
    const colors = ["#F40009", "#FFFFFF", "#B80007", "#FF4D54"];
    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        radius: Math.random() * 1.5 + 1,
        color: colors[Math.floor(Math.random() * colors.length)],
      });
    }

    // Mouse movement tracker for parallax
    const handleMouseMove = (e: MouseEvent) => {
      mouseRef.current.targetX = (e.clientX - window.innerWidth / 2) * 0.03;
      mouseRef.current.targetY = (e.clientY - window.innerHeight / 2) * 0.03;
    };
    window.addEventListener("mousemove", handleMouseMove, { passive: true });

    // Loop
    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const mouse = mouseRef.current;
      mouse.x += (mouse.targetX - mouse.x) * 0.05;
      mouse.y += (mouse.targetY - mouse.y) * 0.05;

      const maxDistance = 95;
      const n = particles.length;

      // Draw connection lines
      for (let i = 0; i < n; i++) {
        const p1 = particles[i];
        const currentX = p1.x + mouse.x * (p1.radius * 0.3);
        const currentY = p1.y + mouse.y * (p1.radius * 0.3);

        for (let j = i + 1; j < n; j++) {
          const p2 = particles[j];
          const otherX = p2.x + mouse.x * (p2.radius * 0.3);
          const otherY = p2.y + mouse.y * (p2.radius * 0.3);

          const dx = currentX - otherX;
          const dy = currentY - otherY;
          const distSq = dx * dx + dy * dy;

          if (distSq < maxDistance * maxDistance) {
            const dist = Math.sqrt(distSq);
            const alpha = (1 - dist / maxDistance) * 0.1;
            ctx.beginPath();
            ctx.strokeStyle = `rgba(244, 0, 9, ${alpha})`;
            ctx.lineWidth = 0.5;
            ctx.moveTo(currentX, currentY);
            ctx.lineTo(otherX, otherY);
            ctx.stroke();
          }
        }
      }

      // Render individual particles
      for (let i = 0; i < n; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        const px = p.x + mouse.x * (p.radius * 0.3);
        const py = p.y + mouse.y * (p.radius * 0.3);

        ctx.beginPath();
        ctx.arc(px, py, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
      }

      animationFrameId = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="absolute inset-0 w-full h-full pointer-events-none z-0 bg-[#050508]"
    />
  );
}
