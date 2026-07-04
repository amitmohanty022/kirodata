#!/usr/bin/env python3
"""ATS-tailored one-page resume for Amit Kumar Mohanty targeting the
Keywords Studios 'AI Engineer' role (GenAI, LLMs, agentic workflows).

NOTE: Keywords Studios is the applicant's CURRENT employer (internal move).
Role asks for 3-6 years; applicant has ~1+ year but directly-relevant internal
experience. Real titles/experience kept; genuine work mapped to JD keywords.
"""

import os
from resume_lib import build_docx, build_pdf, autofit_opts

COMPANY = "Keywords Studios"

CONTENT = {
    "NAME": "Amit Kumar Mohanty",
    "CONTACT": "mohantyamit2003@gmail.com | +91 9354937256 | github.com/amitmohanty022 | linkedin.com/in/amitkrmohanty",
    "TARGET": "AI Engineer  |  Keywords Studios",

    "SUMMARY": (
        "AI Engineer with 1+ year of hands-on experience building, deploying, and optimizing Generative AI "
        "and Large Language Model (LLM) solutions in production. Specialized in context-aware, autonomous "
        "AI agents and multi-agent orchestration, RAG pipelines, and conversational AI served via scalable "
        "FastAPI REST APIs. Strong Python engineer across the modern LLM ecosystem (transformers, PEFT/"
        "LoRA), skilled in fine-tuning foundation models, prompt engineering (Few-Shot, Chain-of-Thought, "
        "ReAct), multimodal AI, and LLMOps (Docker, CI/CD) on AWS and GCP. Peer-reviewed research author "
        "focused on turning state-of-the-art AI into reliable products that impact millions of users."
    ),

    "EDUCATION": [
        ("K.R. Mangalam University, Gurgaon", "July 2021 - July 2025",
         "B.Tech in Computer Science and Engineering (Specialization in AI/ML)"),
        ("Birla Institute of Technology and Science, Pilani (BITS Pilani)", "July 2026 - July 2028",
         "M.Tech in Artificial Intelligence and Machine Learning (Pursuing)"),
    ],

    "EXPERIENCE": [
        ("Research Associate - AI, Keywords Studios India", "Gurgaon, Haryana", "May 2025 - Present", [
            "Built context-aware, autonomous AI agents and multi-agent workflows using modern frameworks to automate complex business logic and multi-step tasks.",
            "Designed, trained, and deployed production-ready GenAI pipelines; collaborated with data engineers to preprocess and curate large datasets, delivering 85% of training data to production.",
            "Experimented with state-of-the-art LLMs and fine-tuned foundation models, running structured evaluations to optimize model performance; awarded \"Rookie of the Year 2025.\"",
        ]),
        ("Artificial Intelligence Intern, Infosys", "Remote", "Nov 2024 - Feb 2025", [
            "Built conversational AI with LangChain and LLM orchestration, raising response accuracy by 35% through advanced prompt engineering (Few-Shot, Chain-of-Thought).",
            "Defined evaluation and guardrails that reduced hallucinations by 20%, and optimized model deployment for latency (-25%) within a 12-engineer Agile team.",
        ]),
    ],

    "PROJECTS": [
        ("Dynamic Screen Companion - Multimodal LLM + RAG", "June 2025 - Present", [
            "Built a real-time multimodal (vision + language) GenAI assistant integrating LLM APIs (Gemini/OpenAI) with a RAG retrieval layer for context-aware responses.",
            "Engineered a FastAPI REST backend serving concurrent inference streams; built the embeddings + vector-search pipeline and containerized with Docker + CI/CD.",
        ]),
        ("Diabetic Optiscan - Vision Transformer (Peer-reviewed research)", "Jan 2025 - June 2025", [
            "Built and fine-tuned a Vision Transformer (ViT-B/16) on the APTOS dataset; co-authored a peer-reviewed paper on the architecture and accuracy gains.",
            "Created a custom wavelet technique improving detection precision by 50% over legacy methods.",
        ]),
    ],

    "SKILLS": [
        ("Languages & LLM Ecosystem", "Python, Hugging Face Transformers, PEFT/LoRA, QLoRA, accelerate, PyTorch, TensorFlow, scikit-learn, NumPy, Pandas"),
        ("LLMs & Orchestration", "LLMs (Gemini, GPT-4, Claude), LangChain, LangGraph, LlamaIndex, OpenAI SDK, Google AI SDK, Prompt Engineering (Few-Shot, Chain-of-Thought, ReAct)"),
        ("Agentic AI", "Autonomous AI Agents, Context-Aware Agents, Multi-Agent Systems, Agent Orchestration, Tool Use, Workflow Automation"),
        ("RAG, Vectors & Data", "RAG Pipelines, Embeddings, Vector Databases (FAISS, Chroma, Pinecone), Data Preprocessing & Curation, SQL, MongoDB"),
        ("APIs & MLOps", "FastAPI, Flask, RESTful APIs, Model Serving, Docker, Kubernetes, CI/CD, MLflow, Deployment & Monitoring"),
        ("Deep Learning & Cloud", "Fine-tuning Foundation Models, Multimodal AI (Vision + Language), Transformers, NLP, Computer Vision, AWS, GCP (Vertex AI), Azure"),
    ],

    "CERTIFICATIONS": [
        "Peer-reviewed research publication in medical AI (Vision Transformers for diabetic retinopathy detection).",
        "Ducat India - Data Science Professional Training (Python, ML, statistics, predictive modeling), Apr 2024 - Apr 2025.",
        "ISRO - AI/ML for Geodata Analysis (applied ML/DL to remote-sensing imagery).",
    ],
}

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    base = f"Amit Kumar Mohanty - {COMPANY} AI Engineer"
    docx_path = os.path.join(out_dir, base + ".docx")
    pdf_path = os.path.join(out_dir, base + ".pdf")
    opts = autofit_opts(CONTENT)
    build_docx(CONTENT, docx_path, opts)
    pages, last_y = build_pdf(CONTENT, pdf_path, opts)
    print("DOCX ->", docx_path)
    print("PDF  ->", pdf_path, "| pages:", pages, "| last_y(mm):", round(last_y, 1))
