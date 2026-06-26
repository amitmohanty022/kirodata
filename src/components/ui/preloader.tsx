"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { profile } from "@/lib/data";

export function Preloader() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Respect users who prefer reduced motion — skip the intro quickly.
    const reduced = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;
    const timer = setTimeout(() => setLoading(false), reduced ? 200 : 1700);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    document.body.style.overflow = loading ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [loading]);

  const initials = profile.name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .slice(0, 3);

  return (
    <AnimatePresence>
      {loading && (
        <motion.div
          key="preloader"
          className="fixed inset-0 z-[100] flex flex-col items-center justify-center bg-background"
          exit={{ opacity: 0 }}
          transition={{ duration: 0.6, ease: "easeInOut" }}
        >
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="relative flex h-24 w-24 items-center justify-center"
          >
            <motion.span
              className="absolute inset-0 rounded-full border-2 border-transparent border-t-primary border-r-accent"
              animate={{ rotate: 360 }}
              transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
            />
            <span className="font-mono text-2xl font-bold gradient-text">
              {initials}
            </span>
          </motion.div>
          <motion.p
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="mt-6 font-mono text-xs uppercase tracking-[0.3em] text-muted-foreground"
          >
            Loading portfolio
          </motion.p>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
