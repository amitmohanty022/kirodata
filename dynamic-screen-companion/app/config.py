"""Application configuration.

Settings are read from environment variables (and an optional .env file).
The app is designed to degrade gracefully: if no GEMINI_API_KEY is set, the
Gemini client runs in MOCK mode so the project is fully runnable out of the box.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache


def _load_dotenv() -> None:
    """Minimal .env loader (avoids a hard dependency on python-dotenv)."""
    env_path = os.path.join(os.getcwd(), ".env")
    if not os.path.exists(env_path):
        return
    try:
        with open(env_path, "r", encoding="utf-8") as fh:
            for raw in fh:
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key, value = key.strip(), value.strip().strip('"').strip("'")
                os.environ.setdefault(key, value)
    except OSError:
        pass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the service."""

    app_name: str = "Dynamic Screen Companion"
    app_version: str = "1.0.0"

    # Gemini / LLM
    gemini_api_key: str = ""
    gemini_model: str = "gemini-1.5-flash"

    # OCR
    tesseract_cmd: str = ""  # optional explicit path to the tesseract binary
    ocr_language: str = "eng"

    # Text-to-speech
    tts_enabled: bool = True
    tts_language: str = "en"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    @property
    def gemini_enabled(self) -> bool:
        return bool(self.gemini_api_key)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    _load_dotenv()
    return Settings(
        gemini_api_key=os.getenv("GEMINI_API_KEY", ""),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
        tesseract_cmd=os.getenv("TESSERACT_CMD", ""),
        ocr_language=os.getenv("OCR_LANGUAGE", "eng"),
        tts_enabled=os.getenv("TTS_ENABLED", "true").lower() == "true",
        tts_language=os.getenv("TTS_LANGUAGE", "en"),
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
    )
