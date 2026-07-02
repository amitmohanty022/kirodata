/* ------------------------------------------------------------------ *
 *  OWNER PROFILE — JARVIS uses this to "know you".
 *  Mirrors the data from the portfolio (src/lib/data.ts) so the
 *  assistant can answer questions about you fully offline.
 * ------------------------------------------------------------------ */
window.OWNER = {
  name: "Amit Kumar Mohanty",
  firstName: "Amit",
  honorific: "sir", // how JARVIS addresses you ("Yes, sir.")
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
  github: "https://github.com/amitmohanty022",
  linkedin: "https://www.linkedin.com/in/amitkrmohanty/",
  summary:
    "Machine Learning Engineer with about a year of experience building, training, and deploying production-grade AI and ML systems — specialised in large language models, agentic AI, deep learning, and end-to-end ML pipelines. Recognised as Rookie of the Year 2025 at Keywords Studios for exceeding all KPIs.",
  about: [
    "You are a Machine Learning Engineer who takes models all the way from research to scalable production. Over the past year you have built and deployed enterprise-grade AI and ML systems spanning LLMs, agentic AI, deep learning, and end-to-end ML pipelines.",
    "You specialise in fine-tuning with LoRA and QLoRA, retrieval-augmented generation, and cloud ML on AWS and Google Cloud Vertex AI. As the first member of a global AI team at Keywords Studios, you delivered the majority of self-generated training data straight to production and were named Rookie of the Year 2025.",
    "Beyond ML you work across the full stack — designing FastAPI inference backends, building multi-modal assistants, and shipping accessible applications. You also co-authored a peer-reviewed computer-vision research paper.",
  ],
  stats: [
    "Over one year of professional experience",
    "Five plus production projects shipped",
    "One published research paper",
    "Rookie of the Year 2025 award",
  ],
  skills: {
    "Languages & Frameworks": ["Python", "C++", "SQL", "R", "FastAPI", "TensorFlow", "PyTorch", "OpenCV", "Scikit-learn", "LangChain", "LangGraph"],
    "AI & Machine Learning": ["LLMs", "Generative AI", "Agentic AI", "RAG", "Fine-tuning (LoRA, QLoRA)", "Deep Learning", "Transformers", "Hugging Face", "BERT", "NLP", "Prompt Engineering"],
    "MLOps & Deployment": ["Docker", "Kubernetes", "CI/CD", "MLflow", "Model Serving", "Model Monitoring", "Vector DBs (FAISS / Chroma)", "Git"],
    "Data & Cloud": ["AWS", "GCP Vertex AI", "Power BI", "MySQL", "MongoDB", "Pandas", "NumPy", "Statistical Analysis"],
  },
  experience: [
    {
      role: "Research Associate — AI",
      company: "Keywords Studios India",
      period: "May 2025 to present",
      note: "Training enterprise-grade agentic AI models for complex multi-step workflows; delivered 85% of self-generated training data to production; awarded Rookie of the Year 2025.",
    },
    {
      role: "Artificial Intelligence Intern",
      company: "Infosys",
      period: "November 2024 to February 2025",
      note: "Engineered an AI call-center system with LangChain and LangSmith, boosting response accuracy by 35% and cutting latency by 25%.",
    },
    {
      role: "Data Analytics & ML Intern",
      company: "QL2 Software",
      period: "June 2024 to August 2024",
      note: "Built predictive ML models for competitive pricing intelligence.",
    },
  ],
  projects: [
    { title: "Dynamic Screen Companion", note: "A real-time multi-modal screen assistant using the Gemini API with continuous voice feedback, served on a FastAPI backend that reduced manual task time by 40%." },
    { title: "Diabetic Optiscan", note: "A Vision Transformer for diabetic retinopathy detection with a custom wavelet technique that improved precision by 50%, published in a peer-reviewed paper." },
    { title: "Currency Detection App for the Visually Impaired", note: "An image-classification model trained on over 200,000 banknote images at 96% accuracy, deployed with voice feedback for accessibility." },
  ],
  education: {
    institution: "K.R. Mangalam University",
    degree: "B.Tech in Computer Science & Engineering with an AI/ML specialisation",
    period: "2021 to 2025",
    detail: "Cumulative GPA 8.5 out of 10.",
  },
  achievements: [
    "Rookie of the Year 2025 at Keywords Studios for surpassing every performance KPI.",
    "Co-authored a peer-reviewed computer-vision research paper on diabetic retinopathy detection.",
    "Selected to present at Infosys' Best Project by Indian Interns initiative.",
  ],
};
