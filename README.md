# Amit Kumar Mohanty — Portfolio

A modern, premium, fully responsive personal portfolio for **Amit Kumar Mohanty** — AI/ML Engineer, Data Scientist & Full-Stack Developer. Built with Next.js, TypeScript, Tailwind CSS, and Framer Motion, and engineered to be fast, accessible, SEO-friendly, and deployment-ready for Vercel.

![Built with Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3-38bdf8?logo=tailwindcss)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-11-ff0080?logo=framer)

---

## ✨ Features

- **Premium, unique design** — glassmorphism, animated gradients, and an animated aurora background.
- **Dark / Light mode** — system-aware theme with a smooth toggle (`next-themes`).
- **Smooth animations** — section reveals, animated project cards, interactive skill badges, and a timeline (Framer Motion).
- **Polished UX touches** — preloader, scroll progress indicator, back-to-top button, sticky shrinking navbar with active-section tracking, and smooth scrolling.
- **Contact form** — powered by [EmailJS](https://www.emailjs.com/) with a graceful `mailto:` fallback when not configured.
- **GitHub activity** — live contribution stats widget.
- **SEO optimized** — rich metadata, Open Graph & Twitter cards, dynamic OG image, JSON-LD structured data, `sitemap.xml`, `robots.txt`, and a web manifest.
- **Accessible** — semantic HTML, skip-to-content link, ARIA labels, keyboard-friendly, and `prefers-reduced-motion` support.
- **Fast & production-ready** — fully static rendering, optimized fonts, and a custom 404 page.

## 🧱 Sections

Hero · About · Skills · Experience (timeline) · Projects (filterable) · Education · Certifications · Achievements · Tech Stack · Contact · Social Links · Résumé download.

## 🛠️ Tech Stack

| Layer        | Technology                          |
| ------------ | ----------------------------------- |
| Framework    | [Next.js 14](https://nextjs.org/) (App Router) |
| Language     | [TypeScript](https://www.typescriptlang.org/) |
| Styling      | [Tailwind CSS](https://tailwindcss.com/) |
| Animation    | [Framer Motion](https://www.framer.com/motion/) |
| Theming      | [next-themes](https://github.com/pacocoursey/next-themes) |
| Icons        | [Lucide React](https://lucide.dev/) |
| Email        | [EmailJS](https://www.emailjs.com/) |
| Deployment   | [Vercel](https://vercel.com/) |

## 📁 Project Structure

```
.
├── public/
│   ├── favicon.svg
│   └── resume/                 # Downloadable résumé PDFs
├── src/
│   ├── app/
│   │   ├── layout.tsx          # Root layout, metadata, SEO, JSON-LD
│   │   ├── page.tsx            # Home page (assembles all sections)
│   │   ├── globals.css         # Design tokens & utilities
│   │   ├── not-found.tsx       # Custom 404
│   │   ├── opengraph-image.tsx # Dynamic OG image
│   │   ├── icon.tsx            # Dynamic favicon
│   │   ├── apple-icon.tsx      # Apple touch icon
│   │   ├── manifest.ts         # PWA manifest
│   │   ├── robots.ts           # robots.txt
│   │   └── sitemap.ts          # sitemap.xml
│   ├── components/
│   │   ├── layout/             # Navbar, Footer
│   │   ├── providers/          # Theme provider
│   │   ├── sections/           # Hero, About, Skills, ... Contact
│   │   └── ui/                 # Reusable UI primitives
│   └── lib/
│       ├── data.ts             # Centralized content (single source of truth)
│       └── utils.ts            # Helpers
├── tailwind.config.ts
├── next.config.mjs
└── package.json
```

> **All content lives in [`src/lib/data.ts`](src/lib/data.ts).** Update that single file to change any text, skills, projects, experience, etc.

## 🚀 Getting Started

### Prerequisites

- Node.js 18.17+ (Node 20+ recommended)

### Installation

```bash
# 1. Install dependencies
npm install

# 2. Create your environment file
cp .env.example .env.local

# 3. Start the dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

### Scripts

| Command         | Description                       |
| --------------- | --------------------------------- |
| `npm run dev`   | Start the development server      |
| `npm run build` | Create a production build         |
| `npm run start` | Run the production build locally  |
| `npm run lint`  | Run ESLint                        |

## 🔧 Configuration

Set these in `.env.local` (see [`.env.example`](.env.example)):

| Variable | Required | Description |
| -------- | -------- | ----------- |
| `NEXT_PUBLIC_SITE_URL` | Recommended | Canonical site URL for SEO, sitemap, and OG tags. |
| `NEXT_PUBLIC_EMAILJS_SERVICE_ID` | Optional | EmailJS service ID for the contact form. |
| `NEXT_PUBLIC_EMAILJS_TEMPLATE_ID` | Optional | EmailJS template ID. |
| `NEXT_PUBLIC_EMAILJS_PUBLIC_KEY` | Optional | EmailJS public key. |
| `NEXT_PUBLIC_GITHUB_USERNAME` | Optional | GitHub username for the activity widget. |

### Setting up the contact form (EmailJS)

1. Create a free account at [emailjs.com](https://www.emailjs.com/).
2. Add an **Email Service** and an **Email Template**.
3. In your template, use the variables `from_name`, `reply_to`, and `message`.
4. Copy your Service ID, Template ID, and Public Key into `.env.local`.

> Without EmailJS configured, the contact form gracefully falls back to opening the visitor's email client via a `mailto:` link.

## ☁️ Deploying to Vercel

1. Push this repository to GitHub.
2. Import the repo into [Vercel](https://vercel.com/new).
3. Add the environment variables from the table above in **Project Settings → Environment Variables**.
4. Deploy. Vercel auto-detects Next.js — no extra configuration needed.

You can also deploy from the CLI:

```bash
npm i -g vercel
vercel
```

## ♿ Accessibility & Performance

- Semantic landmarks, labeled controls, and a skip-to-content link.
- Honors `prefers-reduced-motion`.
- Optimized fonts via `next/font`, static rendering, and lightweight JS.

## 📄 License

Released under the [MIT License](LICENSE). Content (résumé, project details, personal information) © Amit Kumar Mohanty.

---

Built with care using Next.js, TypeScript, Tailwind CSS & Framer Motion.
