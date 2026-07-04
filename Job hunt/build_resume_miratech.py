#!/usr/bin/env python3
"""ATS-tailored one-page resume for Amit Kumar Mohanty targeting the
Miratech 'Junior GenAI Developer' (RAG / LLM backend) role."""

import os
from resume_lib import build_docx, build_pdf

CONTENT = {
    "NAME": "Amit Kumar Mohanty",
    "CONTACT": "mohantyamit2003@gmail.com | +91 9354937256 | github.com/amitmohanty022 | linkedin.com/in/amitkrmohanty",
    "TARGET": "Junior GenAI Developer  |  Miratech",

    "SUMMARY": (
        "GenAI Engineer with 1+ year of hands-on experience building production-grade Generative AI "
        "systems, Retrieval-Augmented Generation (RAG) pipelines, and Python backend services. Skilled "
        "in developing LLM-powered APIs with FastAPI, agent-based workflows with tool/function calling, "
        "and vector search using FAISS and Chroma. Experienced with LangChain, LangGraph, and OpenAI/"
        "Anthropic LLM APIs, and in debugging hallucinations and retrieval failures using faithfulness "
        "and relevance evaluation. Focused on writing clean, testable, maintainable code and moving GenAI "
        "POCs into reliable, scalable production on AWS."
    ),

    "EDUCATION": [
        ("K.R. Mangalam University, Gurgaon", "July 2021 - July 2025",
         "B.Tech in Computer Science and Engineering (Specialization in AI/ML)"),
        ("Birla Institute of Technology and Science, Pilani (BITS Pilani)", "July 2026 - July 2028",
         "M.Tech in Artificial Intelligence and Machine Learning (Pursuing)"),
    ],

    "EXPERIENCE": [
        ("Research Associate - AI, Keywords Studios India", "Gurgaon, Haryana", "May 2025 - Present", [
            "Built and optimized agent-based GenAI workflows with tool/function calling that autonomously execute complex multi-step tasks, improving task-completion reliability.",
            "Developed Python data-ingestion pipelines (ingestion, chunking, embedding) and delivered 85% of self-generated training datasets to production for LLM readiness.",
            "Debugged retrieval and quality issues across LLM outputs, collaborating with senior engineers to move POCs into production; awarded \"Rookie of the Year 2025\" for exceeding all KPIs.",
        ]),
        ("Artificial Intelligence Intern, Infosys", "Remote", "Nov 2024 - Feb 2025", [
            "Engineered a Python LLM service using LangChain and LangSmith, boosting response accuracy by 35% and integrating Large Language Models into backend workflows.",
            "Reduced hallucinations by 20% through prompt engineering and automated RAG-style evaluation of faithfulness and relevance.",
            "Deployed LLM features that cut system latency by 25%, collaborating with a 12-engineer team using Git and standard software development practices.",
        ]),
    ],

    "PROJECTS": [
        ("Dynamic Screen Companion (RAG + LLM Backend)", "June 2025 - Present", [
            "Built a real-time GenAI assistant integrating LLM APIs (Gemini/OpenAI) with a retrieval layer over screen context to generate grounded, low-hallucination responses.",
            "Engineered a Python FastAPI backend exposing REST APIs for concurrent LLM inference streams, containerized with Docker and CI/CD for scalable deployment.",
            "Implemented an embedding + vector-search pipeline (chunking, embeddings, retrieval) maintaining 95%+ extraction accuracy across varied inputs.",
        ]),
        ("Diabetic Optiscan (Peer-reviewed research)", "Jan 2025 - June 2025", [
            "Built a Vision Transformer (ViT-B/16) system on the APTOS dataset to detect diabetic retinopathy; co-authored a peer-reviewed paper on the design and accuracy gains.",
            "Designed a custom wavelet technique that boosted detection precision by 50% over legacy methods.",
        ]),
    ],

    "SKILLS": [
        ("Languages & Backend", "Python, REST API design, Backend Service Development, FastAPI, SQL, C++, Git"),
        ("GenAI & RAG", "LLMs, RAG (ingestion, chunking, embedding, retrieval, response generation), LangChain, LangGraph, OpenAI API, Anthropic (Claude) API, Agent Workflows, Tool/Function Calling, Prompt Engineering, Tokens & Context Windows, Hallucination Debugging, RAG Evaluation (Faithfulness, Relevance)"),
        ("Vector Search & Data", "Embeddings, Vector Databases (FAISS, Chroma, Pinecone), Hybrid Search, Data Pipelines, Pandas, NumPy, MongoDB, MySQL"),
        ("Cloud & MLOps", "AWS, GCP (Vertex AI), Docker, Kubernetes, CI/CD, MLflow, Model Serving & Monitoring"),
        ("ML Frameworks", "PyTorch, TensorFlow, Hugging Face, Transformers, Scikit-learn, OpenCV"),
    ],

    "CERTIFICATIONS": [
        "Ducat India - Data Science Professional Training (Python, ML, statistics, predictive modeling), Apr 2024 - Apr 2025.",
        "ISRO - AI/ML for Geodata Analysis (applied ML/DL to remote-sensing imagery).",
        "Actively pursuing AWS and GenAI/LLM engineering certifications.",
    ],
}

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    docx_path = os.path.join(out_dir, "Amit Kumar Mohanty - Miratech Junior GenAI Developer.docx")
    pdf_path = os.path.join(out_dir, "Amit Kumar Mohanty - Miratech Junior GenAI Developer.pdf")
    build_docx(CONTENT, docx_path)
    pages, last_y = build_pdf(CONTENT, pdf_path)
    print("DOCX ->", docx_path)
    print("PDF  ->", pdf_path, "| pages:", pages, "| last_y(mm):", round(last_y, 1))
