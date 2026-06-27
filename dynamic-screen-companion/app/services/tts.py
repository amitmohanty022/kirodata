"""Text-to-speech service using gTTS (Google Text-to-Speech).

Returns MP3 bytes. Requires network access. Fails gracefully by returning
None so the API still responds with text when audio can't be produced.
"""
from __future__ import annotations

import logging
from io import BytesIO
from typing import Optional

from app.config import get_settings

logger = logging.getLogger(__name__)

# Spoken output should never include the mock-mode bracket note.
_NOISE_PREFIXES = ("[MOCK MODE", "[mock mode")


def synthesize(text: str) -> Optional[bytes]:
    """Convert text to MP3 audio bytes, or None on failure / when disabled."""
    settings = get_settings()
    if not settings.tts_enabled or not text.strip():
        return None

    spoken = text
    for prefix in _NOISE_PREFIXES:
        if prefix in spoken:
            # strip the bracketed note for cleaner audio
            spoken = spoken.split("]", 1)[-1].strip()
            break

    try:
        from gtts import gTTS

        buffer = BytesIO()
        gTTS(text=spoken, lang=settings.tts_language).write_to_fp(buffer)
        return buffer.getvalue()
    except Exception as exc:
        logger.warning("TTS synthesis failed: %s", exc)
        return None
