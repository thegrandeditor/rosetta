import React from "react";
import HeroSection from "@/components/sections/HeroSection";
import TranspilerSection from "@/components/sections/TranspilerSection";
import HowItWorksSection from "@/components/sections/HowItWorksSection";
import LanguagesSection from "@/components/sections/LanguagesSection";
import EnterpriseSection from "@/components/sections/EnterpriseSection";
import PricingSection from "@/components/sections/PricingSection";
import CTASection from "@/components/sections/CTASection";

export const unstable_instant = false;

export default function Home() {
  return (
    <div className="flex flex-col w-full bg-[#FAF6F0] relative">
      <HeroSection />
      <TranspilerSection />
      <HowItWorksSection />
      <LanguagesSection />
      <EnterpriseSection />
      <PricingSection />
      <CTASection />
    </div>
  );
}
