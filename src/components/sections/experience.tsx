"use client";

import { motion } from "framer-motion";
import { Briefcase, MapPin } from "lucide-react";
import { experiences } from "@/lib/data";
import { Section } from "@/components/ui/section";

export function Experience() {
  return (
    <Section
      id="experience"
      eyebrow="Experience"
      title={<>Where I&apos;ve <span className="gradient-text">made impact</span></>}
      description="From data analytics to shipping enterprise Agentic AI in production."
    >
      <div className="relative mx-auto max-w-3xl">
        {/* vertical line */}
        <div className="absolute left-4 top-2 h-full w-px bg-gradient-to-b from-primary/60 via-border to-transparent md:left-1/2" />

        <div className="space-y-10">
          {experiences.map((exp, i) => {
            const isLeft = i % 2 === 0;
            return (
              <motion.div
                key={`${exp.company}-${exp.period}`}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-80px" }}
                transition={{ duration: 0.6 }}
                className={`relative pl-12 md:w-1/2 md:pl-0 ${
                  isLeft ? "md:pr-12 md:text-right" : "md:ml-auto md:pl-12"
                }`}
              >
                {/* node */}
                <span
                  className={`absolute left-4 top-2 z-10 flex h-3 w-3 -translate-x-1/2 items-center justify-center rounded-full bg-primary ring-4 ring-background md:left-auto ${
                    isLeft ? "md:-right-1.5 md:left-auto" : "md:-left-1.5"
                  }`}
                >
                  {exp.current && (
                    <span className="absolute h-full w-full animate-ping rounded-full bg-primary opacity-60" />
                  )}
                </span>

                <div className="card-surface glow-border p-6">
                  <span className="font-mono text-xs uppercase tracking-wider text-primary">
                    {exp.period}
                  </span>
                  <h3 className="mt-1 text-lg font-bold">{exp.role}</h3>
                  <div
                    className={`mt-1 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-muted-foreground ${
                      isLeft ? "md:justify-end" : ""
                    }`}
                  >
                    <span className="inline-flex items-center gap-1.5 font-medium text-foreground/90">
                      <Briefcase className="h-3.5 w-3.5" />
                      {exp.company}
                    </span>
                    <span className="inline-flex items-center gap-1.5">
                      <MapPin className="h-3.5 w-3.5" />
                      {exp.location}
                    </span>
                  </div>
                  <ul
                    className={`mt-4 space-y-2 text-sm text-muted-foreground ${
                      isLeft ? "md:text-left" : ""
                    }`}
                  >
                    {exp.highlights.map((h, hi) => (
                      <li key={hi} className="flex gap-2">
                        <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-accent" />
                        <span className="text-pretty">{h}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </motion.div>
            );
          })}
        </div>
      </div>
    </Section>
  );
}
