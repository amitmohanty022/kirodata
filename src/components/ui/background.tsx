"use client";

import { motion } from "framer-motion";

/**
 * Fixed, decorative background: subtle grid + animated aurora blobs.
 * Pointer-events disabled so it never blocks interaction.
 */
export function Background() {
  return (
    <div
      aria-hidden
      className="pointer-events-none fixed inset-0 -z-10 overflow-hidden"
    >
      {/* grid */}
      <div className="absolute inset-0 bg-grid-pattern bg-[size:64px_64px] opacity-[0.15] [mask-image:radial-gradient(ellipse_at_center,black,transparent_75%)]" />

      {/* aurora blobs */}
      <motion.div
        className="absolute -left-32 top-[-10%] h-[36rem] w-[36rem] rounded-full bg-[hsl(var(--glow-1))] opacity-20 blur-[120px]"
        animate={{ x: [0, 60, 0], y: [0, 40, 0] }}
        transition={{ duration: 18, repeat: Infinity, ease: "easeInOut" }}
      />
      <motion.div
        className="absolute right-[-10%] top-1/3 h-[30rem] w-[30rem] rounded-full bg-[hsl(var(--glow-2))] opacity-[0.18] blur-[120px]"
        animate={{ x: [0, -50, 0], y: [0, 60, 0] }}
        transition={{ duration: 22, repeat: Infinity, ease: "easeInOut" }}
      />
      <motion.div
        className="absolute bottom-[-10%] left-1/3 h-[28rem] w-[28rem] rounded-full bg-[hsl(var(--glow-3))] opacity-[0.16] blur-[120px]"
        animate={{ x: [0, 40, 0], y: [0, -40, 0] }}
        transition={{ duration: 20, repeat: Infinity, ease: "easeInOut" }}
      />
    </div>
  );
}
