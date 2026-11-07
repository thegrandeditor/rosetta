"use client";

import React, { useState } from "react";
import { Check, Shield, Zap, Activity } from "lucide-react";

export default function PricingSection() {
  const [isAnnual, setIsAnnual] = useState(false);

  const tiers = [
    {
      name: "FREE",
      priceMonthly: 0,
      priceAnnually: 0,
      description: "Ideal for individual developers, students, and quick code translations.",
      features: [
        "100 translations / month",
        "Web Studio & CLI access",
        "All 45+ languages supported",
        "Standard HERMES passes",
      ],
      icon: <Activity className="w-5 h-5 text-[#141413]" />,
      buttonText: "Open Workbench",
      href: "/transpile",
      featured: false,
    },
    {
      name: "PRO",
      priceMonthly: 29,
      priceAnnually: 23,
      description: "For software engineers, consultants, and AI IDE (MCP) workflows.",
      badge: "MOST POPULAR",
      features: [
        "10,000 translations / month",
        "Full CLI & MCP Server access",
        "Auto-Learn Custom Grammar Engine",
        "Advanced memory & stdlib passes",
      ],
      icon: <Zap className="w-5 h-5 text-[#F40009]" />,
      buttonText: "Start Pro Trial",
      href: "/transpile",
      featured: true,
    },
    {
      name: "ENTERPRISE",
      priceMonthly: 999,
      priceAnnually: 799,
      description: "For banks, governments, and teams migrating legacy mainframes.",
      features: [
        "Unlimited local & cluster execution",
        "Air-gapped Docker Compose deployment",
        "COBOL, PL/I & RPG priority support",
        "99.99% uptime SLA & dedicated engineer",
      ],
      icon: <Shield className="w-5 h-5 text-[#141413]" />,
      buttonText: "View Enterprise Docs",
      href: "/docs",
      featured: false,
    },
  ];

  return (
    <section id="pricing" className="py-20 bg-[#FAF6F0] border-t border-[#E5DEC9]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[#D6CFC2] bg-white text-xs font-mono font-bold text-[#F40009] uppercase tracking-widest mb-3">
            SIMPLE PRICING
          </div>
          <h2 className="font-space text-3xl md:text-4xl font-extrabold tracking-tight text-[#141413]">
            One Engine. Flexible Access.
          </h2>
          <p className="mt-3 text-[#57534E] font-sans text-sm md:text-base">
            Start free in the browser or terminal, or deploy an air-gapped cluster for your organization.
          </p>

          <div className="mt-7 flex items-center justify-center gap-3">
            <span className={`text-xs font-bold ${!isAnnual ? "text-[#141413]" : "text-[#78716C]"}`}>
              Monthly
            </span>
            <button
              onClick={() => setIsAnnual(!isAnnual)}
              className="relative w-12 h-6 rounded-full bg-white border border-[#D6CFC2] flex items-center p-1 cursor-pointer"
              aria-label="Toggle billing cycle"
            >
              <div
                className={`w-4 h-4 rounded-full bg-[#F40009] transition-transform ${
                  isAnnual ? "translate-x-6" : "translate-x-0"
                }`}
              />
            </button>
            <span className={`text-xs font-bold ${isAnnual ? "text-[#141413]" : "text-[#78716C]"}`}>
              Annual <span className="text-[#F40009]">(Save 20%)</span>
            </span>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {tiers.map((tier) => {
            const price = isAnnual ? tier.priceAnnually : tier.priceMonthly;
            return (
              <div
                key={tier.name}
                className={`rounded-2xl p-8 bg-white flex flex-col justify-between relative ${
                  tier.featured
                    ? "border-2 border-[#141413] shadow-[6px_6px_0px_#F40009]"
                    : "border border-[#E5DEC9]"
                }`}
              >
                {tier.badge && (
                  <div className="absolute top-0 right-6 -translate-y-1/2 px-3 py-1 rounded-full bg-[#F40009] text-[10px] font-mono font-bold text-white">
                    {tier.badge}
                  </div>
                )}

                <div>
                  <div className="flex items-center justify-between mb-4">
                    <span className="font-space font-black text-sm text-[#57534E] uppercase tracking-wider">
                      {tier.name}
                    </span>
                    <div className="w-9 h-9 rounded-lg bg-[#FAF6F0] border border-[#E5DEC9] flex items-center justify-center">
                      {tier.icon}
                    </div>
                  </div>

                  <div className="flex items-baseline gap-1 mb-3">
                    <span className="font-space font-extrabold text-4xl text-[#141413]">
                      ${price}
                    </span>
                    <span className="text-xs text-[#78716C] font-mono">
                      {tier.name === "FREE" ? "forever" : "/month"}
                    </span>
                  </div>

                  <p className="text-xs text-[#57534E] mb-6 leading-relaxed">
                    {tier.description}
                  </p>

                  <ul className="space-y-3 border-t border-[#F3EDE2] pt-5 mb-8">
                    {tier.features.map((feat) => (
                      <li key={feat} className="flex items-center gap-2.5 text-xs text-[#141413]">
                        <Check className="w-4 h-4 text-[#F40009] shrink-0" />
                        <span>{feat}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <a
                  href={tier.href}
                  className={`w-full py-3 rounded-full text-xs font-bold text-center transition-all ${
                    tier.featured
                      ? "bg-[#F40009] hover:bg-[#d00008] text-white"
                      : "bg-[#FAF6F0] hover:bg-[#E5DEC9] text-[#141413] border border-[#D6CFC2]"
                  }`}
                >
                  {tier.buttonText}
                </a>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
