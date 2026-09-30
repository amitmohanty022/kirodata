#!/usr/bin/env python3
"""Keyword match of the resume against real AI/ML job postings.

    python3 resume-src/jd_match.py        # score the built resume
    python3 resume-src/jd_match.py -v     # also list missing terms per posting

The hard skills of each posting were read by hand from the live listing (Sep
2026) and are listed in JDS below. A term matches if any "|"-separated
spelling appears in the PDF text layer. This mimics how ATS match reports
(e.g. Jobscan, which recommends 75%+) count keywords; it is not any ATS
vendor's own score. To tailor for a new job, add its skills as a new entry.

Sources:
  https://careers.unitedhealthgroup.com/job/gurgaon/ai-ml-engineer-nlp-python-machine-learning-rag-langchain-etc/34088/100966510064
  https://careers-inc.nttdata.com/job/Gurgaon-AI-Engineer-HR/1409002900/
  https://careers.unitedhealthgroup.com/job/bengaluru/ai-or-ml-engineer-llms-rag-langchain-langgraph/34088/99093468144
  https://www.accenture.com/in-en/careers/jobdetails?id=ATCI-4822077-S1849385_en
"""
import re
import sys
import unicodedata
from pathlib import Path

import pypdf

PDF = next((a for a in sys.argv[1:] if not a.startswith("-")), str(Path(__file__).resolve().parent.parent / "public/resume/Amit_Kumar_Mohanty_AI_ML_Engineer_Resume.pdf"))
text = unicodedata.normalize("NFKC", pypdf.PdfReader(PDF).pages[0].extract_text())
flat = re.sub(r"\s+", " ", text).lower()

def has(term):
    return any(re.search(r"(?<![a-z])" + re.escape(a.lower()) + r"(?![a-z])", flat) for a in term.split("|"))

JDS = {
 "UnitedHealth (Optum) AI/ML Engineer, Gurgaon": [
  "machine learning", "generative ai", "nlp", "llm|llms", "rag|retrieval-augmented", "ai agents|ai agent|agentic",
  "data pipelines|data pipeline", "exploratory data analysis|eda", "feature engineering|feature pipelines",
  "api|apis|rest api", "microservices", "production", "mlops", "ci/cd", "model versioning", "testing|tests",
  "monitoring", "model drift", "responsible ai", "supervised learning", "deep learning", "model evaluation|evaluation",
  "python", "tensorflow", "pytorch", "scikit-learn", "langchain", "hugging face", "agile|scrum",
  "version control|git", "cloud|aws|gcp|azure", "vertex ai", "vector databases|vector database",
  "prompt engineering", "semantic search", "conversational ai|call center", "mlflow", "kubeflow", "sagemaker",
  "databricks", "spark", "kafka"],
 "NTT DATA AI Engineer, Gurgaon": [
  "python", "c#", ".net", "sql", "ai agents|ai agent|agentic", "mcp|model context protocol", "llm|llms", "rag",
  "langchain", "llamaindex", "semantic kernel", "fastapi", "rest api|rest apis|api", "vector databases|vector database",
  "prompt engineering", "ci/cd", "embeddings", "semantic search", "multi-step|complex tasks", "tool calling",
  "gemini", "faiss", "aws", "evaluation", "hallucination|hallucinations", "observability|monitoring", "documentation"],
 "UnitedHealth (Optum) AI or ML Engineer, Bengaluru": [
  "agentic ai", "llm|llms", "rag", "vector databases|vector database", "embeddings", "prompt engineering",
  "langchain", "langgraph", "java", "python", "api|apis", "microservices", "aws", "azure", "docker", "kubernetes",
  "ci/cd", "git", "evaluation", "guardrails", "observability", "monitoring", "latency", "hallucination|hallucinations",
  "faiss", "chroma", "rest api|rest apis", "workflow automation|automated", "tool calling", "multi-step|complex tasks"],
 "Accenture AI/ML Engineer": [
  "machine learning", "generative ai", "deep learning", "neural networks", "chatbots|call center", "image processing|image classification|images",
  "nlp", "prompt engineering", "python", "tensorflow", "pytorch", "keras", "data structures", "algorithms", "aws",
  "gcp", "azure", "hugging face", "spacy", "nltk", "matplotlib", "seaborn", "plotly", "agile|scrum",
  "statistical|statistics", "gpt", "gans", "vae", "conversational ai|call center", "speech|voice"],
}
total_hit = total = 0
for jd, terms in JDS.items():
    hit = [t for t in terms if has(t)]; miss = [t.split("|")[0] for t in terms if not has(t)]
    total_hit += len(hit); total += len(terms)
    print(f"{jd:<50} {len(hit):>2}/{len(terms):<2} = {len(hit)*100/len(terms):5.1f}%")
    if "-v" in sys.argv: print("     missing:", ", ".join(miss))
print(f"{'ALL FOUR POSTINGS':<50} {total_hit:>2}/{total:<2} = {total_hit*100/total:5.1f}%")
