"""OCR service.

Wraps pytesseract. If the Tesseract binary is not installed, OCR degrades
gracefully: ``extract_text`` returns an empty string and ``is_available``
reports False, so the rest of the pipeline keeps working.
"""
from __future__ import annotations

import logging
from io import BytesIO
from typing import Union

from PIL import Image

from app.config import get_settings

logger = logging.getLogger(__name__)

_ImageInput = Union[bytes, "Image.Image"]


def _to_image(data: _ImageInput) -> "Image.Image":
    if isinstance(data, Image.Image):
        return data
    return Image.open(BytesIO(data))


def is_available() -> bool:
    """Return True if the Tesseract engine is callable."""
    try:
        import pytesseract  # noqa: WPS433 (local import keeps dep optional)

        settings = get_settings()
        if settings.tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd
        pytesseract.get_tesseract_version()
        return True
    except Exception as exc:  # pragma: no cover - depends on host
        logger.debug("Tesseract unavailable: %s", exc)
        return False


def extract_text(image: _ImageInput) -> str:
    """Extract text from an image. Returns '' if OCR is unavailable."""
    try:
        import pytesseract

        settings = get_settings()
        if settings.tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd
        img = _to_image(image)
        text = pytesseract.image_to_string(img, lang=settings.ocr_language)
        return text.strip()
    except Exception as exc:
        logger.warning("OCR failed or unavailable: %s", exc)
        return ""
