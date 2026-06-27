"use client";

import { motion } from "framer-motion";
import { Award, ScrollText, Presentation } from "lucide-react";
import { achievements } from "@/lib/data";
import { Section } from "@/components/ui/section";

const iconMap = {
  award: Award,
  scroll: ScrollText,
  presentation: Presentation,
};

export function Achievements() {
  return (
    <Section
      id="achievements"
      eyebrow="Achievements"
      title={<>Recognition &amp; <span className="gradient-text">milestones</span></>}
      description="Moments that mark progress along the way."
    >
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {achievements.map((item, i) => {
          const Icon = iconMap[item.icon];
          return (
            <motion.div
              key={item.title}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              whileHover={{ y: -6 }}
              className="card-surface glow-border relative overflow-hidden p-6"
            >
              <div className="absolute -right-6 -top-6 h-24 w-24 rounded-full bg-primary/10 blur-2xl" />
              <span className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-primary to-accent text-white shadow-lg">
                <Icon className="h-6 w-6" />
              </span>
              <h3 className="text-base font-bold">{item.title}</h3>
              <p className="mt-2 text-sm text-muted-foreground">{item.detail}</p>
            </motion.div>
          );
        })}
      </div>
    </Section>
  );
}
