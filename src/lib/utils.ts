import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

/** Merge Tailwind class names safely, resolving conflicts. */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/** Site URL used for SEO / Open Graph. */
export const SITE_URL =
  process.env.NEXT_PUBLIC_SITE_URL?.replace(/\/$/, "") ||
  "https://amitmohanty.vercel.app";

/**
 * Base path the app is served from (empty on Vercel, "/<repo>" on GitHub Pages).
 * Use `withBasePath` for plain <a href> / static asset links so they resolve
 * correctly when the site is hosted under a sub-path.
 */
export const BASE_PATH = process.env.NEXT_PUBLIC_BASE_PATH || "";

export function withBasePath(path: string) {
  if (!path.startsWith("/")) return path;
  return `${BASE_PATH}${path}`;
}
