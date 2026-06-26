"use client";

import { motion } from "framer-motion";
import { GraduationCap, BadgeCheck } from "lucide-react";
import { education, certifications } from "@/lib/data";
import { Section } from "@/components/ui/section";

export function Education() {
  return (
    <Section
      id="education"
      eyebrow="Education & Certifications"
      title={<>Academic <span className="gradient-text">foundation</span></>}
      description="Formal education and continued professional training."
    >
      <div className="grid gap-8 lg:grid-cols-2">
        {/* Education */}
        <div>
          <h3 className="mb-5 flex items-center gap-2 text-lg font-semibold">
            <GraduationCap className="h-5 w-5 text-primary" />
            Education
          </h3>
          <div className="space-y-5">
            {education.map((edu, i) => (
              <motion.div
                key={edu.institution}
                initial={{ opacity: 0, x: -24 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true, margin: "-60px" }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                className="card-surface glow-border p-6"
              >
                <span className="font-mono text-xs uppercase tracking-wider text-primary">
                  {edu.period}
                </span>
                <h4 className="mt-1 text-base font-bold">{edu.institution}</h4>
                <p className="mt-1 text-sm text-foreground/80">{edu.degree}</p>
                <p className="mt-1 text-sm text-muted-foreground">
                  {edu.location} · {edu.detail}
                </p>
                <div className="mt-4">
                  <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                    Relevant Coursework
                  </p>
                  <div className="flex flex-wrap gap-1.5">
                    {edu.coursework.map((c) => (
                      <span
                        key={c}
                        className="rounded-md border border-border bg-muted/40 px-2 py-0.5 text-xs text-muted-foreground"
                      >
                        {c}
                      </span>
                    ))}
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* Certifications */}
        <div>
          <h3 className="mb-5 flex items-center gap-2 text-lg font-semibold">
            <BadgeCheck className="h-5 w-5 text-accent" />
            Certifications
          </h3>
          <div className="space-y-5">
            {certifications.map((cert, i) => (
              <motion.div
                key={cert.title}
                initial={{ opacity: 0, x: 24 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true, margin: "-60px" }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                className="card-surface glow-border p-6"
              >
                {cert.period && (
                  <span className="font-mono text-xs uppercase tracking-wider text-accent">
                    {cert.period}
                  </span>
                )}
                <h4 className="mt-1 text-base font-bold">{cert.title}</h4>
                <p className="mt-1 text-sm font-medium text-foreground/80">
                  {cert.issuer}
                </p>
                <p className="mt-2 text-sm text-muted-foreground">
                  {cert.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </Section>
  );
}
