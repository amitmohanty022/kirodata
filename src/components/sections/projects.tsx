"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { ArrowUpRight, Github, Calendar } from "lucide-react";
import { projects } from "@/lib/data";
import { Section } from "@/components/ui/section";
import { cn } from "@/lib/utils";

const categories = ["All", ...Array.from(new Set(projects.map((p) => p.category)))];

export function Projects() {
  const [filter, setFilter] = useState("All");

  const filtered =
    filter === "All" ? projects : projects.filter((p) => p.category === filter);

  return (
    <Section
      id="projects"
      eyebrow="Projects"
      title={<>Things I&apos;ve <span className="gradient-text">built</span></>}
      description="Selected projects spanning generative AI, computer vision, and accessible deep learning."
    >
      {/* filters */}
      <div className="mb-10 flex flex-wrap justify-center gap-2">
        {categories.map((cat) => (
          <button
            key={cat}
            type="button"
            onClick={() => setFilter(cat)}
            className={cn(
              "rounded-full border px-4 py-1.5 text-sm font-medium transition-all",
              filter === cat
                ? "border-primary bg-primary text-primary-foreground"
                : "border-border bg-card/60 text-muted-foreground hover:border-primary/50 hover:text-foreground"
            )}
          >
            {cat}
          </button>
        ))}
      </div>

      <motion.div layout className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        <AnimatePresence mode="popLayout">
          {filtered.map((project) => (
            <motion.article
              key={project.title}
              layout
              initial={{ opacity: 0, scale: 0.92 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.92 }}
              transition={{ duration: 0.4 }}
              whileHover={{ y: -6 }}
              className="card-surface glow-border group flex flex-col overflow-hidden p-6"
            >
              {/* gradient top accent */}
              <div className="mb-4 flex items-center justify-between">
                <span className="rounded-full bg-accent/10 px-3 py-1 font-mono text-xs text-accent">
                  {project.category}
                </span>
                <div className="flex gap-1.5">
                  {project.github && (
                    <a
                      href={project.github}
                      target="_blank"
                      rel="noopener noreferrer"
                      aria-label={`${project.title} GitHub repository`}
                      className="flex h-8 w-8 items-center justify-center rounded-lg border border-border text-muted-foreground transition-colors hover:border-primary/50 hover:text-primary"
                    >
                      <Github className="h-4 w-4" />
                    </a>
                  )}
                  {project.demo && (
                    <a
                      href={project.demo}
                      target="_blank"
                      rel="noopener noreferrer"
                      aria-label={`${project.title} live demo`}
                      className="flex h-8 w-8 items-center justify-center rounded-lg border border-border text-muted-foreground transition-colors hover:border-primary/50 hover:text-primary"
                    >
                      <ArrowUpRight className="h-4 w-4" />
                    </a>
                  )}
                </div>
              </div>

              <h3 className="text-lg font-bold transition-colors group-hover:text-primary">
                {project.title}
              </h3>
              <p className="mt-0.5 inline-flex items-center gap-1.5 font-mono text-xs text-muted-foreground">
                <Calendar className="h-3 w-3" />
                {project.period}
              </p>
              <p className="mt-3 text-sm font-medium text-foreground/80">
                {project.tagline}
              </p>

              <ul className="mt-3 space-y-2 text-sm text-muted-foreground">
                {project.description.map((d, di) => (
                  <li key={di} className="flex gap-2">
                    <span className="mt-1.5 h-1 w-1 shrink-0 rounded-full bg-primary" />
                    <span className="text-pretty">{d}</span>
                  </li>
                ))}
              </ul>

              <div className="mt-auto flex flex-wrap gap-1.5 pt-5">
                {project.tech.map((t) => (
                  <span
                    key={t}
                    className="rounded-md border border-border bg-muted/40 px-2 py-0.5 text-xs text-muted-foreground"
                  >
                    {t}
                  </span>
                ))}
              </div>
            </motion.article>
          ))}
        </AnimatePresence>
      </motion.div>
    </Section>
  );
}
