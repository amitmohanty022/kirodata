"""Pydantic request/response models for the API."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class AnalyzeResponse(BaseModel):
    """Result of analysing a screen image."""

    extracted_text: str = Field(..., description="Text extracted from the image via OCR.")
    analysis: str = Field(..., description="The assistant's analysis / answer.")
    question: Optional[str] = Field(None, description="The user question, if one was asked.")
    ocr_available: bool = Field(..., description="Whether real OCR ran (vs. unavailable).")
    llm_mode: str = Field(..., description="'gemini' when the live API is used, else 'mock'.")
    audio_base64: Optional[str] = Field(
        None, description="Base64-encoded MP3 of the spoken analysis, if TTS succeeded."
    )


class HealthResponse(BaseModel):
    status: str
    app: str
    version: str
    gemini_enabled: bool
    ocr_available: bool


class CaptureRequest(BaseModel):
    """Request body for server-side screen capture (local use only)."""

    question: Optional[str] = Field(
        None, description="Optional question about what is on screen."
    )
    monitor: int = Field(1, description="Monitor index to capture (1 = primary).")
    speak: bool = Field(True, description="Whether to synthesize spoken feedback.")
