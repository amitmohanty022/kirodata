import type { LucideIcon } from "lucide-react";
import {
  Brain,
  Cloud,
  Code2,
  Database,
  GitBranch,
  Sparkles,
} from "lucide-react";

/* -------------------------------------------------------------------------- */
/*                                   Profile                                  */
/* -------------------------------------------------------------------------- */

export const profile = {
  name: "Amit Kumar Mohanty",
  firstName: "Amit",
  roles: [
    "AI/ML Engineer",
    "Data Scientist",
    "Full-Stack Developer",
    "LLM & Agentic AI Specialist",
  ],
  tagline:
    "AI/ML Engineer building and shipping production-grade intelligent systems.",
  location: "Gurgaon, Haryana, India",
  email: "mohantyamit2003@gmail.com",
  phone: "+91 93549 37256",
  resumeFile: "/resume/Amit_Kumar_Mohanty_ML_Engineer_Resume.pdf",
  avatar: "https://avatars.githubusercontent.com/amitmohanty022",
  githubUsername: "amitmohanty022",
  summary:
    "Machine Learning Engineer with ~1 year of experience building, training, and deploying production-grade AI/ML systems — specialized in LLMs, Agentic AI, deep learning, and end-to-end ML pipelines. Recognized as “Rookie of the Year 2025” at Keywords Studios for exceeding all KPIs.",
  about: [
    "I'm a Machine Learning Engineer who takes models all the way from research to scalable production. Over the past year I've built and deployed enterprise-grade AI/ML systems spanning LLMs, Agentic AI, deep learning, and end-to-end ML pipelines.",
    "I specialize in fine-tuning (LoRA/QLoRA), Retrieval-Augmented Generation (RAG), and cloud ML on AWS and GCP Vertex AI. As the first member of a global AI team at Keywords Studios, I delivered the majority of self-generated training data straight to production and was named “Rookie of the Year 2025” for surpassing every performance KPI.",
    "Beyond ML, I work comfortably across the full stack — designing FastAPI inference backends, building multi-modal assistants, and shipping accessible applications. I also co-authored a peer-reviewed computer-vision research paper, blending rigorous research with real-world engineering.",
  ],
  stats: [
    { label: "Years of Experience", value: "1+" },
    { label: "Production Projects", value: "5+" },
    { label: "Published Paper", value: "1" },
    { label: "Award", value: "Rookie of the Year '25" },
  ],
} as const;

/* -------------------------------------------------------------------------- */
/*                                Social links                                */
/* -------------------------------------------------------------------------- */

export type SocialLink = {
  label: string;
  href: string;
  icon: "github" | "linkedin" | "mail" | "phone";
};

export const socials: SocialLink[] = [
  {
    label: "GitHub",
    href: "https://github.com/amitmohanty022",
    icon: "github",
  },
  {
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/amitkrmohanty/",
    icon: "linkedin",
  },
  {
    label: "Email",
    href: "mailto:mohantyamit2003@gmail.com",
    icon: "mail",
  },
  {
    label: "Phone",
    href: "tel:+919354937256",
    icon: "phone",
  },
];

/* -------------------------------------------------------------------------- */
/*                                   Skills                                    */
/* -------------------------------------------------------------------------- */

export type SkillGroup = {
  title: string;
  icon: LucideIcon;
  skills: string[];
};

export const skillGroups: SkillGroup[] = [
  {
    title: "Languages & Frameworks",
    icon: Code2,
    skills: [
      "Python",
      "C++",
      "SQL",
      "R",
      "FastAPI",
      "TensorFlow",
      "PyTorch",
      "OpenCV",
      "Scikit-learn",
      "LangChain",
      "LangGraph",
    ],
  },
  {
    title: "AI & Machine Learning",
    icon: Brain,
    skills: [
      "LLMs",
      "Generative AI",
      "Agentic AI",
      "RAG",
      "Fine-tuning (LoRA, QLoRA)",
      "Deep Learning",
      "Transformers",
      "Hugging Face",
      "BERT",
      "NLP",
      "Prompt Engineering",
      "Model Evaluation & Optimization",
    ],
  },
  {
    title: "MLOps & Deployment",
    icon: GitBranch,
    skills: [
      "Docker",
      "Kubernetes",
      "CI/CD",
      "MLflow",
      "Model Serving",
      "Model Monitoring",
      "Data Pipelines",
      "Git",
      "Vector DBs (FAISS / Chroma)",
    ],
  },
  {
    title: "Data & Cloud",
    icon: Cloud,
    skills: [
      "AWS",
      "GCP (Vertex AI)",
      "Power BI",
      "MySQL",
      "MongoDB",
      "Pandas",
      "NumPy",
      "Statistical Analysis",
    ],
  },
];

/* Curated tech stack for the marquee / tech-stack section */
export const techStack: string[] = [
  "Python",
  "PyTorch",
  "TensorFlow",
  "LangChain",
  "LangGraph",
  "Hugging Face",
  "FastAPI",
  "Docker",
  "Kubernetes",
  "AWS",
  "GCP Vertex AI",
  "MLflow",
  "OpenCV",
  "Scikit-learn",
  "FAISS",
  "MongoDB",
  "MySQL",
  "Git",
  "C++",
  "Power BI",
];

/* -------------------------------------------------------------------------- */
/*                                 Experience                                 */
/* -------------------------------------------------------------------------- */

export type Experience = {
  role: string;
  company: string;
  location: string;
  period: string;
  current?: boolean;
  highlights: string[];
};

export const experiences: Experience[] = [
  {
    role: "Research Associate — AI",
    company: "Keywords Studios India",
    location: "Gurgaon, Haryana",
    period: "May 2025 — Present",
    current: true,
    highlights: [
      "Train and optimize enterprise-grade Agentic AI models that autonomously execute complex multi-step workflows (flight booking, e-commerce ordering, web data retrieval), improving task-completion reliability.",
      "Built custom data pipelines and delivered 85% of self-generated training datasets directly to production as the first member of a global team, accelerating model readiness.",
      "Awarded “Rookie of the Year 2025” for surpassing all performance KPIs through advanced model training, data-pipeline optimization, and cross-functional collaboration.",
    ],
  },
  {
    role: "Artificial Intelligence Intern",
    company: "Infosys",
    location: "Remote",
    period: "Nov 2024 — Feb 2025",
    highlights: [
      "Engineered an AI call-center system with LangChain and LangSmith, boosting model response accuracy by 35% and elevating customer-AI interaction quality.",
      "Developed and deployed LLM features that reduced system latency by 25%, streamlining the model deployment process.",
      "Collaborated with a team of 12 engineers to integrate end-to-end ML workflows and earned selection to present at the “Best Project by Indian Interns” initiative.",
    ],
  },
  {
    role: "Data Analytics & ML Intern",
    company: "QL2 Software",
    location: "Gurgaon, Haryana",
    period: "Jun 2024 — Aug 2024",
    highlights: [
      "Built predictive ML models for competitive pricing intelligence.",
      "Performed large-scale data extraction and analysis to deliver actionable business insights.",
    ],
  },
];

/* -------------------------------------------------------------------------- */
/*                                  Projects                                  */
/* -------------------------------------------------------------------------- */

export type Project = {
  title: string;
  period: string;
  tagline: string;
  description: string[];
  tech: string[];
  github?: string;
  demo?: string;
  featured?: boolean;
  category: string;
};

export const projects: Project[] = [
  {
    title: "Dynamic Screen Companion",
    period: "Jun 2025 — Present",
    tagline: "Real-time multi-modal screen assistant",
    category: "Generative AI",
    featured: true,
    description: [
      "Built a real-time multi-modal assistant integrating the Gemini API to analyze live screen activity and deliver continuous voice feedback and interactive support.",
      "Engineered a high-performance FastAPI model-serving backend handling concurrent inference streams, reducing manual task time by 40%.",
      "Designed the end-to-end multi-modal architecture from scratch and optimized OCR pipelines to maintain 95%+ extraction accuracy across varied screen layouts.",
    ],
    tech: ["Gemini API", "FastAPI", "Python", "OCR", "Multi-modal AI", "Voice UI"],
  },
  {
    title: "Diabetic Optiscan",
    period: "Jan 2025 — Jun 2025",
    tagline: "Vision Transformer for diabetic retinopathy detection",
    category: "Computer Vision",
    featured: true,
    description: [
      "Led integration of a Vision Transformer (ViT-B/16) on the APTOS dataset, optimizing self-attention to capture complex spatial patterns in high-resolution retinal images.",
      "Designed a custom wavelet modification technique that boosted detection precision by 50% over legacy methods.",
      "Co-authored a peer-reviewed research paper detailing the system architecture and performance breakthroughs.",
    ],
    tech: ["PyTorch", "Vision Transformer", "APTOS", "Wavelets", "Medical Imaging"],
  },
  {
    title: "Currency Detection App for the Visually Impaired",
    period: "Jul 2024 — Dec 2024",
    tagline: "Accessible banknote recognition with voice feedback",
    category: "Deep Learning",
    featured: true,
    description: [
      "Trained an image-classification model on 200,000+ banknote images achieving 96% accuracy, deployed in a mobile app with voice feedback to help prevent fraud.",
      "Conducted user interviews with visually impaired individuals to refine real-world accessibility features.",
    ],
    tech: ["TensorFlow", "CNN", "Computer Vision", "Mobile", "Accessibility"],
  },
];

/* -------------------------------------------------------------------------- */
/*                                 Education                                  */
/* -------------------------------------------------------------------------- */

export type Education = {
  institution: string;
  degree: string;
  location: string;
  period: string;
  detail: string;
  coursework: string[];
};

export const education: Education[] = [
  {
    institution: "K.R. Mangalam University",
    degree: "B.Tech in Computer Science & Engineering (AI/ML Specialization)",
    location: "Gurgaon, India",
    period: "Jul 2021 — Jul 2025",
    detail: "Cumulative GPA: 8.5 / 10",
    coursework: [
      "Data Structures & Algorithms",
      "Natural Language Processing",
      "Computer Vision",
      "DBMS",
      "Machine Learning",
      "Deep Learning",
    ],
  },
];

/* -------------------------------------------------------------------------- */
/*                               Certifications                               */
/* -------------------------------------------------------------------------- */

export type Certification = {
  title: string;
  issuer: string;
  period?: string;
  description: string;
};

export const certifications: Certification[] = [
  {
    title: "Data Science Professional Training",
    issuer: "Ducat India",
    period: "Apr 2024 — Apr 2025",
    description:
      "Professional training in Data Science — Python, statistics, machine learning, data analysis, and predictive modeling.",
  },
  {
    title: "AI/ML for Geodata Analysis",
    issuer: "ISRO (Indian Space Research Organisation)",
    description:
      "Applying AI/ML techniques to geospatial data analysis, offered by ISRO.",
  },
];

/* -------------------------------------------------------------------------- */
/*                                Achievements                                */
/* -------------------------------------------------------------------------- */

export type Achievement = {
  title: string;
  detail: string;
  icon: "award" | "scroll" | "presentation";
};

export const achievements: Achievement[] = [
  {
    title: "Rookie of the Year 2025",
    detail:
      "Recognized at Keywords Studios for surpassing every performance KPI in the first year.",
    icon: "award",
  },
  {
    title: "Peer-Reviewed Publication",
    detail:
      "Co-authored a published computer-vision research paper on diabetic retinopathy detection.",
    icon: "scroll",
  },
  {
    title: "Best Project by Indian Interns",
    detail:
      "Selected to present at Infosys' Best Project initiative among a cohort of intern engineers.",
    icon: "presentation",
  },
];

/* -------------------------------------------------------------------------- */
/*                              Navigation links                              */
/* -------------------------------------------------------------------------- */

export const navLinks = [
  { label: "About", href: "#about" },
  { label: "Skills", href: "#skills" },
  { label: "Experience", href: "#experience" },
  { label: "Projects", href: "#projects" },
  { label: "Education", href: "#education" },
  { label: "Achievements", href: "#achievements" },
  { label: "Contact", href: "#contact" },
] as const;

export const highlightIcons = { Sparkles, Database };
