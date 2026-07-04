#!/usr/bin/env python3
"""ATS-tailored one-page resume for Amit Kumar Mohanty targeting the
HCLTech 'AI Solution Architect I' role (GenAI / Agentic AI architecture focus).

HONESTY NOTE: This role asks for 5+ years as a Solution/Enterprise Architect.
The applicant has ~1+ year of experience. This resume keeps his REAL titles and
experience level; it only reframes genuine work toward architecture/design and
surfaces JD keywords he can defend in an interview. No seniority is fabricated.
"""

import os
from resume_lib import build_docx, build_pdf, autofit_opts

COMPANY = "HCLTech"

CONTENT = {
    "NAME": "Amit Kumar Mohanty",
    "CONTACT": "mohantyamit2003@gmail.com | +91 9354937256 | github.com/amitmohanty022 | linkedin.com/in/amitkrmohanty",
    "TARGET": "AI Solution Architect I  |  HCLTech",

    "SUMMARY": (
        "Generative AI Engineer with 1+ year of hands-on experience designing end-to-end GenAI and "
        "Agentic AI solutions - including Retrieval-Augmented Generation (RAG) pipelines, multi-agent "
        "workflows, and LLM integration layers. Strong foundation in system design (microservices, REST "
        "APIs, event-driven and cloud-native / 12-factor patterns) applied to production-grade, scalable "
        "AI services. Skilled in LLM evaluation, prompt engineering, LLMOps (tracing, monitoring, feedback "
        "loops), and Responsible AI (fairness, bias mitigation, prompt-injection safety). Seeking to grow "
        "into an AI architecture role, translating business goals into secure, production-ready GenAI "
        "systems on Azure, AWS, and GCP."
    ),

    "EDUCATION": [
        ("K.R. Mangalam University, Gurgaon", "July 2021 - July 2025",
         "B.Tech in Computer Science and Engineering (Specialization in AI/ML)"),
        ("Birla Institute of Technology and Science, Pilani (BITS Pilani)", "July 2026 - July 2028",
         "M.Tech in Artificial Intelligence and Machine Learning (Pursuing)"),
    ],

    "EXPERIENCE": [
        ("Research Associate - AI, Keywords Studios India", "Gurgaon, Haryana", "May 2025 - Present", [
            "Designed and implemented Agentic AI workflows - agent orchestration, tool use, and multi-step long-horizon task execution - improving task-completion reliability.",
            "Contributed to reference patterns and quality guardrails for GenAI agents, running structured design/test reviews with a global team to deliver client-ready iterations.",
            "Architected data pipelines (ingestion, preprocessing, feature engineering, versioning) that fed 85% of self-generated training datasets to production; awarded \"Rookie of the Year 2025.\"",
        ]),
        ("Artificial Intelligence Intern, Infosys", "Remote", "Nov 2024 - Feb 2025", [
            "Designed an LLM integration layer and prompt-management approach for an AI call-center system with LangChain/LangSmith, raising response accuracy by 35%.",
            "Built an LLM evaluation and observability loop (automated tracing + scoring) that reduced hallucinations by 20% and mitigated biased/undesired outputs.",
            "Optimized LLM deployment for latency (-25%) within cloud-native services, collaborating across a 12-engineer team using Agile/Scrum.",
        ]),
    ],

    "PROJECTS": [
        ("Dynamic Screen Companion - GenAI Solution Architecture", "June 2025 - Present", [
            "Architected an end-to-end multi-modal GenAI system: LLM integration layer, RAG retrieval, and a FastAPI microservice backend handling concurrent inference streams.",
            "Designed the embedding + vector-search data layer (chunking, embeddings, retrieval) and containerized the solution (Docker, CI/CD) for scalable cloud deployment.",
        ]),
        ("Diabetic Optiscan - Vision Transformer (Peer-reviewed research)", "Jan 2025 - June 2025", [
            "Designed and led integration of a Vision Transformer (ViT-B/16) on the APTOS dataset; co-authored a peer-reviewed paper on the architecture and accuracy gains.",
            "Created a custom wavelet technique that improved detection precision by 50% over legacy methods.",
        ]),
    ],

    "SKILLS": [
        ("AI Architecture & System Design", "Solution Design, Microservices, Event-Driven Architecture, REST API Design, Cloud-Native / 12-Factor, Distributed Systems, Scalability, Reliability & Latency Optimization"),
        ("GenAI & Agentic AI", "LLMs, RAG, Multi-Agent Systems, Agent Orchestration, Tool Use, Memory Management, Human-in-the-Loop, Prompt Engineering, Chain-of-Thought, LLM Integration"),
        ("Frameworks", "LangChain, LangGraph, LlamaIndex, Hugging Face, Transformers, PyTorch, TensorFlow, FastAPI"),
        ("Fine-tuning & LLMOps", "LoRA, QLoRA, PEFT, Prompt Tuning, MLflow, Model Evaluation Frameworks, Tracing, Monitoring, Feedback Loops, Docker, Kubernetes, CI/CD"),
        ("Cloud, Data & Vector Stores", "Azure OpenAI, AWS, GCP (Vertex AI), Vector Databases (FAISS, Chroma, Pinecone), Embedding Stores, Data Pipelines, SQL, MongoDB"),
        ("Responsible AI & Security", "AI Fairness, Explainability, Bias Mitigation, Prompt-Injection Protection, Data Privacy (GDPR), Audit Logging"),
    ],

    "CERTIFICATIONS": [
        "Ducat India - Data Science Professional Training (Python, ML, statistics, predictive modeling), Apr 2024 - Apr 2025.",
        "ISRO - AI/ML for Geodata Analysis (applied ML/DL to remote-sensing imagery).",
        "Actively pursuing cloud & AI architecture certifications (Microsoft Azure AI, AWS, Google Cloud).",
    ],
}

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    base = f"Amit Kumar Mohanty - {COMPANY} AI Solution Architect I"
    docx_path = os.path.join(out_dir, base + ".docx")
    pdf_path = os.path.join(out_dir, base + ".pdf")
    opts = autofit_opts(CONTENT)
    build_docx(CONTENT, docx_path, opts)
    pages, last_y = build_pdf(CONTENT, pdf_path, opts)
    print("DOCX ->", docx_path)
    print("PDF  ->", pdf_path, "| pages:", pages, "| last_y(mm):", round(last_y, 1))
