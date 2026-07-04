#!/usr/bin/env python3
"""ATS-tailored one-page resume for Amit Kumar Mohanty targeting the
Siemens Energy 'AI/ML Engineer' role (GenAI, RAG, multi-agent, MLOps focus).

HONESTY NOTE: Role asks for 3-5 years (2-3 in GenAI). Applicant has ~1+ year.
Real titles/experience level kept; genuine work reframed to the JD keywords.
No experience is fabricated.
"""

import os
from resume_lib import build_docx, build_pdf, autofit_opts

COMPANY = "Siemens Energy"

CONTENT = {
    "NAME": "Amit Kumar Mohanty",
    "CONTACT": "mohantyamit2003@gmail.com | +91 9354937256 | github.com/amitmohanty022 | linkedin.com/in/amitkrmohanty",
    "TARGET": "AI/ML Engineer  |  Siemens Energy",

    "SUMMARY": (
        "AI/ML Engineer with 1+ year of experience designing, building, and productionizing Generative AI "
        "solutions - including RAG pipelines, multi-agent systems, and LLM integrations - as scalable "
        "FastAPI microservices. Strong Python engineer (NumPy, Pandas, scikit-learn) with hands-on MLOps "
        "on Docker, Kubernetes, and CI/CD across AWS and GCP. Experienced in prompt engineering, retrieval "
        "optimization, LLM evaluation (accuracy, latency, cost, safety), Document AI (OCR/extraction), and "
        "Responsible AI guardrails. Skilled at rapid prototyping to production in cross-functional Agile "
        "teams, translating problem statements into reliable, enterprise-grade systems."
    ),

    "EDUCATION": [
        ("K.R. Mangalam University, Gurgaon", "July 2021 - July 2025",
         "B.Tech in Computer Science and Engineering (Specialization in AI/ML)"),
        ("Birla Institute of Technology and Science, Pilani (BITS Pilani)", "July 2026 - July 2028",
         "M.Tech in Artificial Intelligence and Machine Learning (Pursuing)"),
    ],

    "EXPERIENCE": [
        ("Research Associate - AI, Keywords Studios India", "Gurgaon, Haryana", "May 2025 - Present", [
            "Built multi-agent GenAI applications with agent orchestration, tool use, and planning/execution workflows, improving task-completion reliability.",
            "Engineered production data pipelines (ingestion, transformation, quality validation, versioning) delivering 85% of self-generated training datasets; awarded \"Rookie of the Year 2025.\"",
            "Defined evaluation metrics and structured test reviews with a global team to harden agent policies and improve action accuracy.",
        ]),
        ("Artificial Intelligence Intern, Infosys", "Remote", "Nov 2024 - Feb 2025", [
            "Built LLM integrations for an AI knowledge/assistance system with LangChain, raising response accuracy by 35% and optimizing prompt strategies.",
            "Defined LLM evaluation and guardrails (automated scoring/tracing) that reduced hallucinations by 20% and improved safety of outputs.",
            "Optimized deployment for latency (-25%) in cloud services, collaborating across a 12-engineer team using Agile/Scrum.",
        ]),
    ],

    "PROJECTS": [
        ("Dynamic Screen Companion - RAG + Document AI", "June 2025 - Present", [
            "Designed an end-to-end GenAI system: LLM integration, RAG retrieval, and a FastAPI microservice backend handling concurrent inference streams with event-driven flows.",
            "Built the embeddings + vector-search layer (indexing, chunking, retrieval) and Document AI/OCR pipeline maintaining 95%+ extraction accuracy; containerized with Docker + CI/CD.",
        ]),
        ("Diabetic Optiscan - Vision Transformer (Peer-reviewed research)", "Jan 2025 - June 2025", [
            "Built a Vision Transformer (ViT-B/16) on the APTOS dataset for image classification/anomaly detection; co-authored a peer-reviewed paper.",
            "Created a custom wavelet technique improving detection precision by 50% over legacy methods.",
        ]),
    ],

    "SKILLS": [
        ("Programming & APIs", "Python (typing, packaging, testing), NumPy, Pandas, scikit-learn, FastAPI, Flask, SQL, Git, GitHub/GitLab"),
        ("GenAI, RAG & Agentic AI", "LLMs, RAG (indexing, chunking, reranking), Prompt Engineering, LLM Integration, Multi-Agent Systems, Agent Orchestration, Tool Use, Guardrails, Model Selection & Fine-tuning (LoRA/QLoRA), Document AI (OCR, classification, extraction)"),
        ("Frameworks", "LangChain, LangGraph, Semantic Kernel, LlamaIndex, Hugging Face, Transformers, PyTorch, TensorFlow"),
        ("Vector, Data & Cloud", "Embeddings, Vector Databases (FAISS, Pinecone, Chroma, Azure AI Search), Data Pipelines, MongoDB, Azure OpenAI, AWS, GCP (Vertex AI)"),
        ("MLOps & Architecture", "Docker, Kubernetes, CI/CD, MLflow, Deployment & Monitoring, Microservices, Event-Driven Design, API Security, Scalability, Concurrency, Latency/Cost Optimization"),
        ("Responsible AI & Collaboration", "Responsible AI Guardrails, Bias Mitigation, Data Privacy & PII Handling, Access Controls, Auditability, Agile/Scrum, Jira/Azure DevOps"),
    ],

    "CERTIFICATIONS": [
        "Ducat India - Data Science Professional Training (Python, ML, statistics, predictive modeling), Apr 2024 - Apr 2025.",
        "ISRO - AI/ML for Geodata Analysis (applied ML/DL to remote-sensing imagery; time-series & pattern analysis).",
        "Actively pursuing Azure AI and cloud MLOps certifications.",
    ],
}

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    base = f"Amit Kumar Mohanty - {COMPANY} AI-ML Engineer"
    docx_path = os.path.join(out_dir, base + ".docx")
    pdf_path = os.path.join(out_dir, base + ".pdf")
    opts = autofit_opts(CONTENT)
    build_docx(CONTENT, docx_path, opts)
    pages, last_y = build_pdf(CONTENT, pdf_path, opts)
    print("DOCX ->", docx_path)
    print("PDF  ->", pdf_path, "| pages:", pages, "| last_y(mm):", round(last_y, 1))
