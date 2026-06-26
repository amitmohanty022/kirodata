import { ImageResponse } from "next/og";
import { profile } from "@/lib/data";

export const runtime = "edge";
export const alt = `${profile.name} — AI/ML Engineer Portfolio`;
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function OpenGraphImage() {
  return new ImageResponse(
    (
      <div
        style={{
          height: "100%",
          width: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          padding: "80px",
          background:
            "linear-gradient(135deg, #0a0e1a 0%, #131a2e 55%, #1a1030 100%)",
          color: "white",
          fontFamily: "sans-serif",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: "16px",
            fontSize: 26,
            color: "#9ca3af",
            marginBottom: 24,
          }}
        >
          <div
            style={{
              width: 14,
              height: 14,
              borderRadius: 999,
              background: "#34d399",
            }}
          />
          Portfolio
        </div>
        <div
          style={{
            fontSize: 76,
            fontWeight: 800,
            lineHeight: 1.05,
            letterSpacing: "-0.02em",
            display: "flex",
            flexWrap: "wrap",
          }}
        >
          {profile.name}
        </div>
        <div
          style={{
            fontSize: 40,
            fontWeight: 700,
            marginTop: 18,
            background: "linear-gradient(90deg, #8b5cf6, #06b6d4)",
            backgroundClip: "text",
            color: "transparent",
          }}
        >
          AI/ML Engineer · Data Scientist · Full-Stack Developer
        </div>
        <div
          style={{
            fontSize: 26,
            color: "#9ca3af",
            marginTop: 28,
            maxWidth: 900,
          }}
        >
          Building production-grade LLM, Agentic AI &amp; deep-learning systems.
        </div>
        <div
          style={{
            display: "flex",
            gap: 28,
            marginTop: 48,
            fontSize: 24,
            color: "#c4b5fd",
          }}
        >
          <span>github.com/amitmohanty022</span>
          <span style={{ color: "#475569" }}>|</span>
          <span>linkedin.com/in/amitkrmohanty</span>
        </div>
      </div>
    ),
    { ...size }
  );
}
