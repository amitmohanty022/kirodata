import Link from "next/link";
import type { Metadata } from "next";
import { Home, Compass } from "lucide-react";

export const metadata: Metadata = {
  title: "404 — Page Not Found",
  robots: { index: false, follow: false },
};

export default function NotFound() {
  return (
    <main className="relative flex min-h-screen flex-col items-center justify-center overflow-hidden px-6 text-center">
      {/* decorative glow */}
      <div
        aria-hidden
        className="pointer-events-none absolute left-1/2 top-1/2 h-[30rem] w-[30rem] -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary/15 blur-[120px]"
      />
      <p className="font-mono text-[6rem] font-extrabold leading-none gradient-text sm:text-[9rem]">
        404
      </p>
      <h1 className="mt-2 text-2xl font-bold sm:text-3xl">
        This page wandered off
      </h1>
      <p className="mt-3 max-w-md text-muted-foreground">
        The page you&apos;re looking for doesn&apos;t exist or has been moved.
        Let&apos;s get you back on track.
      </p>
      <div className="mt-8 flex flex-col gap-3 sm:flex-row">
        <Link
          href="/"
          className="inline-flex items-center justify-center gap-2 rounded-full bg-primary px-6 py-3 font-semibold text-primary-foreground shadow-lg shadow-primary/30 transition-transform hover:scale-105"
        >
          <Home className="h-4 w-4" />
          Back home
        </Link>
        <Link
          href="/#projects"
          className="inline-flex items-center justify-center gap-2 rounded-full border border-border bg-card/60 px-6 py-3 font-semibold backdrop-blur transition-colors hover:border-primary/50 hover:text-primary"
        >
          <Compass className="h-4 w-4" />
          Explore projects
        </Link>
      </div>
    </main>
  );
}
