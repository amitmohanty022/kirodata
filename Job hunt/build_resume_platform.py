#!/usr/bin/env python3
"""ATS-tailored one-page resume for Amit Kumar Mohanty targeting the
'Platform Engineer I' fresher Generative AI Engineer role (NLP / LLM / portfolio focus).

NOTE: Company name not provided by the applicant. Update COMPANY below and the
output filenames once the company name is known.
"""

import os
from resume_lib import build_docx, build_pdf

COMPANY = "Platform Engineer I"  # <-- replace with actual company name when known

CONTENT = {
    "NAME": "Amit Kumar Mohanty",
    "CONTACT": "mohantyamit2003@gmail.com | +91 9354937256 | github.com/amitmohanty022 | linkedin.com/in/amitkrmohanty",
    "TARGET": "Platform Engineer I - Generative AI Engineer (Fresher)",

    "SUMMARY": (
        "Generative AI Engineer and Computer Science graduate (AI/ML specialization) with strong Python "
        "fundamentals (NumPy, Pandas) and a public GitHub portfolio of functioning GenAI projects, "
        "including an LLM-powered assistant and an AI chatbot. Solid theoretical foundation in NLP, "
        "tokenization, embeddings, and Transformer architecture. Hands-on with LLM-powered applications, "
        "smart chatbots, and data pipelines for AI training and retrieval using LangChain, LlamaIndex, and "
        "vector databases (FAISS, ChromaDB, Pinecone). Comfortable with Git/GitHub collaboration and eager "
        "to turn academic and project experience into real-world enterprise AI solutions."
    ),

    "EDUCATION": [
        ("K.R. Mangalam University, Gurgaon", "July 2021 - July 2025",
         "B.Tech in Computer Science and Engineering (Specialization in AI/ML)"),
        ("Birla Institute of Technology and Science, Pilani (BITS Pilani)", "July 2026 - July 2028",
         "M.Tech in Artificial Intelligence and Machine Learning (Pursuing)"),
    ],

    "EXPERIENCE": [
        ("Research Associate - AI, Keywords Studios India", "Gurgaon, Haryana", "May 2025 - Present", [
            "Trained and optimized LLM-powered GenAI agents that autonomously execute multi-step workflows, improving task-completion reliability.",
            "Optimized data pipelines for AI training and retrieval, delivering 85% of self-generated training datasets to production using Python (NumPy, Pandas).",
            "Awarded \"Rookie of the Year 2025\" for exceeding all KPIs; collaborated with a global team using Git and GitHub.",
        ]),
        ("Artificial Intelligence Intern, Infosys", "Remote", "Nov 2024 - Feb 2025", [
            "Built a smart AI chatbot / call-center assistant with LangChain, boosting response accuracy by 35% by integrating LLMs into Python services.",
            "Applied prompt engineering and Transformer-based NLP to reduce hallucinations by 20% and improve conversation quality.",
            "Deployed LLM features that reduced system latency by 25% within a 12-engineer collaborative team.",
        ]),
    ],

    "PROJECTS": [
        ("Dynamic Screen Companion - LLM Assistant  (github.com/amitmohanty022)", "June 2025 - Present", [
            "Built a real-time GenAI assistant integrating LLM APIs (Gemini/OpenAI) to analyze live screen activity and deliver conversational voice responses.",
            "Engineered a Python FastAPI backend and an embeddings + retrieval pipeline (tokenization, embeddings, vector search) with 95%+ extraction accuracy.",
        ]),
        ("Diabetic Optiscan - Vision Transformer  (Peer-reviewed research)", "Jan 2025 - June 2025", [
            "Built a Vision Transformer (ViT-B/16) on the APTOS dataset to detect diabetic retinopathy; co-authored a peer-reviewed paper.",
            "Designed a custom wavelet technique that boosted detection precision by 50% over legacy methods.",
        ]),
        ("Currency Detection App for the Visually Impaired", "July 2024 - Dec 2024", [
            "Trained an image-classification model on 200,000+ banknote images (96% accuracy) and deployed it in a mobile app with voice feedback.",
        ]),
    ],

    "SKILLS": [
        ("Programming", "Python (NumPy, Pandas), SQL, C++, R, Git, GitHub"),
        ("NLP & Transformers", "NLP, Tokenization, Embeddings, Transformer Architecture, LLMs, Hugging Face, BERT, Prompt Engineering, Fine-tuning (LoRA/QLoRA)"),
        ("GenAI Frameworks", "LangChain, LangGraph, LlamaIndex, RAG, Agent Workflows, OpenAI API, Gemini API"),
        ("Vector Databases & Data", "FAISS, ChromaDB, Pinecone, Vector Search, Data Pipelines, MySQL, MongoDB"),
        ("ML & Deployment", "PyTorch, TensorFlow, Scikit-learn, OpenCV, FastAPI, Docker, AWS, GCP (Vertex AI)"),
    ],

    "CERTIFICATIONS": [
        "Ducat India - Data Science Professional Training (Python, ML, statistics, predictive modeling), Apr 2024 - Apr 2025.",
        "ISRO - AI/ML for Geodata Analysis (applied ML/DL to remote-sensing imagery).",
        "Portfolio: functioning GenAI projects (LLM assistant, AI chatbot, document analysis) on github.com/amitmohanty022.",
    ],
}

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    base = f"Amit Kumar Mohanty - {COMPANY} Generative AI Engineer"
    docx_path = os.path.join(out_dir, base + ".docx")
    pdf_path = os.path.join(out_dir, base + ".pdf")
    build_docx(CONTENT, docx_path)
    pages, last_y = build_pdf(CONTENT, pdf_path)
    print("DOCX ->", docx_path)
    print("PDF  ->", pdf_path, "| pages:", pages, "| last_y(mm):", round(last_y, 1))
