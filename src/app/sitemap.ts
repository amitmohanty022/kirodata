import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/utils";

// Required for `output: "export"` (GitHub Pages); the route is static anyway.
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: SITE_URL,
      lastModified: new Date(),
      changeFrequency: "monthly",
      priority: 1,
    },
  ];
}
