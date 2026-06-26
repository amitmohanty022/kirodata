"use client";

import Image from "next/image";
import { motion } from "framer-motion";
import { Github } from "lucide-react";
import { techStack, profile } from "@/lib/data";
import { Reveal } from "@/components/ui/reveal";

export function TechStack() {
  // Duplicate the list so the marquee can loop seamlessly.
  const row = [...techStack, ...techStack];

  return (
    <section
      id="tech-stack"
      className="scroll-mt-24 border-y border-border bg-muted/20 py-20 sm:py-24"
      aria-labelledby="tech-stack-heading"
    >
      <div className="container-px">
        <Reveal className="mx-auto mb-12 max-w-2xl text-center">
          <span className="mb-3 inline-block rounded-full border border-primary/30 bg-primary/10 px-4 py-1 font-mono text-xs uppercase tracking-widest text-primary">
            Tech Stack
          </span>
          <h2 id="tech-stack-heading" className="section-heading text-balance">
            Tools I work with <span className="gradient-text">daily</span>
          </h2>
        </Reveal>
      </div>

      {/* Marquee */}
      <div className="relative flex overflow-hidden mask-fade-x py-2">
        <div className="flex shrink-0 animate-marquee items-center gap-4 pr-4">
          {row.map((tech, i) => (
            <span
              key={`${tech}-${i}`}
              className="whitespace-nowrap rounded-full border border-border bg-card/70 px-5 py-2.5 text-sm font-medium text-foreground/80 backdrop-blur"
            >
              {tech}
            </span>
          ))}
        </div>
      </div>

      {/* GitHub activity */}
      <div className="container-px mt-14">
        <Reveal className="mx-auto max-w-3xl">
          <div className="card-surface glow-border overflow-hidden p-6 text-center">
            <h3 className="mb-1 flex items-center justify-center gap-2 text-lg font-semibold">
              <Github className="h-5 w-5" />
              GitHub Activity
            </h3>
            <p className="mb-6 text-sm text-muted-foreground">
              Live contribution stats from{" "}
              <a
                href={`https://github.com/${profile.githubUsername}`}
                target="_blank"
                rel="noopener noreferrer"
                className="text-primary hover:underline"
              >
                @{profile.githubUsername}
              </a>
            </p>
            <div className="mx-auto w-full max-w-md overflow-hidden rounded-xl">
              <Image
                src={`https://github-readme-stats.vercel.app/api?username=${profile.githubUsername}&show_icons=true&hide_border=true&bg_color=00000000&title_color=8b5cf6&icon_color=06b6d4&text_color=9ca3af`}
                alt={`${profile.name} GitHub statistics`}
                width={500}
                height={200}
                unoptimized
                className="h-auto w-full"
              />
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
