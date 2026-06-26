"use client";

import { motion } from "framer-motion";
import { skillGroups } from "@/lib/data";
import { Section } from "@/components/ui/section";

export function Skills() {
  return (
    <Section
      id="skills"
      eyebrow="Skills"
      title={<>My technical <span className="gradient-text">toolkit</span></>}
      description="The languages, frameworks, and platforms I use to build intelligent systems end to end."
    >
      <div className="grid gap-6 md:grid-cols-2">
        {skillGroups.map((group, gi) => {
          const Icon = group.icon;
          return (
            <motion.div
              key={group.title}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.5, delay: gi * 0.08 }}
              className="card-surface glow-border p-6"
            >
              <div className="mb-5 flex items-center gap-3">
                <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-primary/10 text-primary">
                  <Icon className="h-5 w-5" />
                </span>
                <h3 className="text-lg font-semibold">{group.title}</h3>
              </div>
              <ul className="flex flex-wrap gap-2">
                {group.skills.map((skill, si) => (
                  <motion.li
                    key={skill}
                    initial={{ opacity: 0, scale: 0.8 }}
                    whileInView={{ opacity: 1, scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.3, delay: 0.1 + si * 0.03 }}
                    whileHover={{ y: -3, scale: 1.05 }}
                    className="cursor-default rounded-lg border border-border bg-muted/50 px-3 py-1.5 text-sm font-medium text-foreground/90 transition-colors hover:border-primary/50 hover:bg-primary/10 hover:text-primary"
                  >
                    {skill}
                  </motion.li>
                ))}
              </ul>
            </motion.div>
          );
        })}
      </div>
    </Section>
  );
}
