"use client";

import { motion } from "framer-motion";
import { profile } from "@/lib/data";
import { Section } from "@/components/ui/section";
import { Reveal } from "@/components/ui/reveal";

export function About() {
  return (
    <Section
      id="about"
      eyebrow="About Me"
      title={<>Turning research into <span className="gradient-text">production</span></>}
      description="A quick look at who I am and what drives my work."
    >
      <div className="grid items-start gap-12 lg:grid-cols-[1.4fr_1fr]">
        <div className="space-y-5">
          {profile.about.map((paragraph, i) => (
            <Reveal key={i} delay={i} className="text-pretty leading-relaxed text-muted-foreground">
              <p>{paragraph}</p>
            </Reveal>
          ))}
        </div>

        <div className="grid grid-cols-2 gap-4">
          {profile.stats.map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              className="card-surface glow-border flex flex-col items-center justify-center p-6 text-center"
            >
              <span className="gradient-text text-2xl font-extrabold sm:text-3xl">
                {stat.value}
              </span>
              <span className="mt-1 text-xs text-muted-foreground">
                {stat.label}
              </span>
            </motion.div>
          ))}
        </div>
      </div>
    </Section>
  );
}
