"""LLM analysis service backed by Google Gemini.

Falls back to a deterministic MOCK analyser when no API key is configured,
so the project is fully runnable and testable without credentials.
"""
from __future__ import annotations

import logging
from typing import Optional

from app.config import get_settings

logger = logging.getLogger(__name__)

_SYSTEM_PROMPT = (
    "You are Dynamic Screen Companion, a helpful real-time assistant that looks "
    "at what is currently on a user's screen and gives concise, useful guidance. "
    "You receive text extracted from the screen via OCR. Summarise what the user "
    "is looking at, surface anything important, and answer their question if one "
    "is provided. Keep responses short, friendly and spoken-aloud friendly."
)


def _build_prompt(screen_text: str, question: Optional[str]) -> str:
    parts = [_SYSTEM_PROMPT, "\n\n--- SCREEN TEXT (via OCR) ---\n"]
    parts.append(screen_text.strip() or "(no readable text detected on screen)")
    if question:
        parts.append(f"\n\n--- USER QUESTION ---\n{question.strip()}")
    parts.append("\n\n--- YOUR RESPONSE ---\n")
    return "".join(parts)


def _mock_analysis(screen_text: str, question: Optional[str]) -> str:
    """A readable, deterministic stand-in used when no API key is set."""
    snippet = " ".join(screen_text.split())[:160]
    lines = ["[MOCK MODE - set GEMINI_API_KEY for live AI responses]"]
    if snippet:
        lines.append(f"I can see your screen mentions: \"{snippet}\".")
    else:
        lines.append("I couldn't detect readable text on the screen.")
    if question:
        lines.append(f"You asked: \"{question.strip()}\". ")
        lines.append(
            "With a live Gemini key I would answer this directly using the screen context."
        )
    else:
        lines.append("Ask me a question and I'll help based on what's on screen.")
    return " ".join(lines)


def analyze(screen_text: str, question: Optional[str] = None) -> tuple[str, str]:
    """Return (analysis_text, mode) where mode is 'gemini' or 'mock'."""
    settings = get_settings()
    if not settings.gemini_enabled:
        return _mock_analysis(screen_text, question), "mock"

    try:
        import google.generativeai as genai

        genai.configure(api_key=settings.gemini_api_key)
        model = genai.GenerativeModel(settings.gemini_model)
        response = model.generate_content(_build_prompt(screen_text, question))
        return (response.text or "").strip(), "gemini"
    except Exception as exc:
        logger.error("Gemini call failed, falling back to mock: %s", exc)
        return _mock_analysis(screen_text, question), "mock"
