import type { ReactNode } from "react";
import { cn } from "@/lib/utils";
import { Reveal } from "./reveal";

type SectionProps = {
  id: string;
  eyebrow?: string;
  title: ReactNode;
  description?: ReactNode;
  children: ReactNode;
  className?: string;
};

export function Section({
  id,
  eyebrow,
  title,
  description,
  children,
  className,
}: SectionProps) {
  return (
    <section
      id={id}
      className={cn("scroll-mt-24 py-20 sm:py-28", className)}
      aria-labelledby={`${id}-heading`}
    >
      <div className="container-px">
        <Reveal className="mx-auto mb-14 max-w-2xl text-center">
          {eyebrow && (
            <span className="mb-3 inline-block rounded-full border border-primary/30 bg-primary/10 px-4 py-1 font-mono text-xs uppercase tracking-widest text-primary">
              {eyebrow}
            </span>
          )}
          <h2 id={`${id}-heading`} className="section-heading text-balance">
            {title}
          </h2>
          {description && (
            <p className="mx-auto mt-4 max-w-xl text-pretty text-muted-foreground">
              {description}
            </p>
          )}
        </Reveal>
        {children}
      </div>
    </section>
  );
}
