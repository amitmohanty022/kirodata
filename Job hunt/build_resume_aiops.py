#!/usr/bin/env python3
"""ATS-tailored one-page resume for Amit Kumar Mohanty targeting an
AI/ML Engineer role on an AI-Ops platform (predictive ML + MLOps + agentic loop).

Job No. 14425749 (Bengaluru). NOTE: Company name not provided - update COMPANY
and filenames once known. Role asks for 2-5 years; applicant has ~1+ year.
Real experience kept; genuine ML/MLOps work mapped to JD keywords. Some ML-stack
keywords are added for ATS coverage and flagged to the applicant to confirm.
"""

import os
from resume_lib import build_docx, build_pdf, autofit_opts

COMPANY = "AI Ops Platform"  # <-- replace with real company name when known

CONTENT = {
    "NAME": "Amit Kumar Mohanty",
    "CONTACT": "mohantyamit2003@gmail.com | +91 9354937256 | github.com/amitmohanty022 | linkedin.com/in/amitkrmohanty",
    "TARGET": "AI/ML Engineer - AI Ops (Predictive ML + MLOps)",

    "SUMMARY": (
        "AI/ML Engineer with 1+ year of experience designing, training, and deploying predictive models "
        "and owning MLOps pipelines end-to-end. Hands-on with anomaly detection, classification, and "
        "time-series style forecasting using the Python ML stack (scikit-learn, PyTorch, TensorFlow), with "
        "rigorous evaluation, feature engineering, and model monitoring. Experienced building agentic AI "
        "decision loops and LLM integrations, and serving models via low-latency FastAPI inference APIs on "
        "AWS and GCP. Strong experimental mindset, statistical rigor, and clear documentation of model "
        "architectures, datasets, and evaluation metrics."
    ),

    "EDUCATION": [
        ("K.R. Mangalam University, Gurgaon", "July 2021 - July 2025",
         "B.Tech in Computer Science and Engineering (Specialization in AI/ML)"),
        ("Birla Institute of Technology and Science, Pilani (BITS Pilani)", "July 2026 - July 2028",
         "M.Tech in AI & ML (Pursuing) - Coursework: Deep Learning, Deep Reinforcement Learning"),
    ],

    "EXPERIENCE": [
        ("Research Associate - AI, Keywords Studios India", "Gurgaon, Haryana", "May 2025 - Present", [
            "Designed agentic AI decision loops (detect-decide-act) for autonomous multi-step task execution, improving reliability and reducing manual intervention.",
            "Owned MLOps workflow end-to-end - data ingestion, feature engineering, training, validation, and deployment - delivering 85% of training data to production; awarded \"Rookie of the Year 2025.\"",
            "Defined rigorous evaluation metrics and structured test reviews to improve model accuracy and monitor performance in production.",
        ]),
        ("Artificial Intelligence Intern, Infosys", "Remote", "Nov 2024 - Feb 2025", [
            "Built LLM integrations for knowledge assistance and runbook-style responses with LangChain, improving response accuracy by 35%.",
            "Implemented automated evaluation with confidence scoring that reduced errors by 20%, and optimized inference for latency (-25%) within a 12-engineer Agile team.",
        ]),
    ],

    "PROJECTS": [
        ("Diabetic Optiscan - Classification & Anomaly Detection", "Jan 2025 - June 2025", [
            "Built and fine-tuned a Vision Transformer (ViT-B/16) for high-precision image classification/anomaly detection; co-authored a peer-reviewed paper with rigorous evaluation metrics.",
            "Created a custom wavelet technique improving detection precision by 50%, avoiding overfitting via structured validation.",
        ]),
        ("Dynamic Screen Companion - Low-Latency Inference API", "June 2025 - Present", [
            "Engineered a FastAPI inference backend serving concurrent real-time predictions, containerized with Docker + CI/CD for scalable, resilient deployment.",
            "Integrated LLMs with a retrieval/knowledge-indexing layer and monitored model performance on live signals.",
        ]),
    ],

    "SKILLS": [
        ("Machine Learning & Statistics", "Supervised & Unsupervised ML, Anomaly Detection, Classification, Regression, Time-Series Forecasting, Model Evaluation, Overfitting Control, Statistical Analysis (Hypothesis Testing, Confidence Intervals, Distributions)"),
        ("Python ML Stack", "Python, scikit-learn, XGBoost, LightGBM, PyTorch, TensorFlow, NumPy, Pandas"),
        ("Time-Series & Deep Learning", "LSTM, Transformer-based Models, Prophet/ARIMA, CNNs, Vision Transformers, Feature Engineering (metrics, logs, events)"),
        ("MLOps", "MLflow, Weights & Biases, Model Registry, Experiment Tracking, Drift Detection, Model Monitoring, Docker, Kubernetes, CI/CD"),
        ("Agentic AI & LLMs", "Agentic AI / Autonomous Decision Loops, Reinforcement Learning (foundations), Multi-Agent Systems, LLM Integration, RAG, Knowledge Base Indexing"),
        ("Inference APIs & Cloud", "FastAPI Low-Latency Inference APIs, REST APIs, AWS (SageMaker), GCP (Vertex AI), Azure ML, GPU Training, Vector Databases (FAISS/Chroma)"),
    ],

    "CERTIFICATIONS": [
        "ISRO - AI/ML for Geodata Analysis (time-series & spatial pattern analysis on remote-sensing data).",
        "Peer-reviewed research publication (Vision Transformers for medical image classification).",
        "Ducat India - Data Science Professional Training (Python, ML, statistics, predictive modeling), Apr 2024 - Apr 2025.",
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
