import type { MetadataRoute } from "next";
import { profile } from "@/lib/data";
import { withBasePath } from "@/lib/utils";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: `${profile.name} — Portfolio`,
    short_name: profile.firstName,
    description:
      "AI/ML Engineer, Data Scientist & Full-Stack Developer portfolio.",
    start_url: withBasePath("/"),
    display: "standalone",
    background_color: "#0a0e1a",
    theme_color: "#0a0e1a",
    icons: [
      {
        src: withBasePath("/icon"),
        sizes: "64x64",
        type: "image/png",
      },
      {
        src: withBasePath("/apple-icon"),
        sizes: "180x180",
        type: "image/png",
      },
    ],
  };
}
