"""FastAPI application exposing the Dynamic Screen Companion pipeline.

Pipeline:  image -> OCR (text) -> Gemini (analysis) -> TTS (spoken audio)

Endpoints
---------
GET  /              service metadata
GET  /health        health + capability check
POST /analyze       upload an image (+ optional question) -> analysis (+ audio)
POST /capture       capture the server's screen (local desktop use only)
"""
from __future__ import annotations

import base64
import logging
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import get_settings
from app.schemas import AnalyzeResponse, CaptureRequest, HealthResponse
from app.services import gemini_client, ocr, screen_capture, tts

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dynamic-screen-companion")

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "A real-time multi-modal screen assistant. Send a screenshot and an "
        "optional question; it reads the screen with OCR, reasons about it with "
        "Gemini, and can speak the answer back."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _run_pipeline(image_bytes: bytes, question: Optional[str], speak: bool) -> AnalyzeResponse:
    extracted = ocr.extract_text(image_bytes)
    analysis, mode = gemini_client.analyze(extracted, question)

    audio_b64: Optional[str] = None
    if speak:
        audio = tts.synthesize(analysis)
        if audio:
            audio_b64 = base64.b64encode(audio).decode("ascii")

    return AnalyzeResponse(
        extracted_text=extracted,
        analysis=analysis,
        question=question,
        ocr_available=bool(extracted) or ocr.is_available(),
        llm_mode=mode,
        audio_base64=audio_b64,
    )


@app.get("/", tags=["meta"])
def root() -> dict:
    return {
        "app": settings.app_name,
        "version": __version__,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", response_model=HealthResponse, tags=["meta"])
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        app=settings.app_name,
        version=__version__,
        gemini_enabled=settings.gemini_enabled,
        ocr_available=ocr.is_available(),
    )


@app.post("/analyze", response_model=AnalyzeResponse, tags=["core"])
async def analyze(
    file: UploadFile = File(..., description="Screenshot / image to analyse."),
    question: Optional[str] = Form(None),
    speak: bool = Form(True),
) -> AnalyzeResponse:
    if file.content_type and not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")
    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Empty file.")
    return _run_pipeline(image_bytes, question, speak)


@app.post("/capture", response_model=AnalyzeResponse, tags=["local"])
def capture(req: CaptureRequest) -> AnalyzeResponse:
    """Capture the server host's screen. Only useful when running locally."""
    try:
        image = screen_capture.capture(req.monitor)
    except screen_capture.ScreenCaptureError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    from io import BytesIO

    buf = BytesIO()
    image.save(buf, format="PNG")
    return _run_pipeline(buf.getvalue(), req.question, req.speak)
