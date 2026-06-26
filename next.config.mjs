/**
 * When building for GitHub Pages we produce a fully static export and serve the
 * site from a sub-path (https://<user>.github.io/<repo>/). On Vercel (or any
 * Node host) none of this applies and the app runs as a normal Next.js app.
 */
const isGithubPages = process.env.GITHUB_PAGES === "true";
const basePath = process.env.NEXT_PUBLIC_BASE_PATH || "";

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  compress: true,
  ...(isGithubPages
    ? {
        output: "export",
        basePath,
        trailingSlash: true,
        images: { unoptimized: true },
      }
    : {
        images: {
          formats: ["image/avif", "image/webp"],
          remotePatterns: [
            {
              protocol: "https",
              hostname: "avatars.githubusercontent.com",
            },
            {
              protocol: "https",
              hostname: "github-readme-stats.vercel.app",
            },
          ],
        },
      }),
};

export default nextConfig;
