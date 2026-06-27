"""Screen capture service (for local desktop use).

Uses ``mss`` to grab a monitor. This only works in a desktop session; in a
headless/server environment it raises a clear, actionable error. The hosted
demo uses image uploads instead of live capture.
"""
from __future__ import annotations

import logging

from PIL import Image

logger = logging.getLogger(__name__)


class ScreenCaptureError(RuntimeError):
    """Raised when the screen cannot be captured (e.g. headless host)."""


def capture(monitor: int = 1) -> "Image.Image":
    """Capture a monitor and return a PIL image.

    Args:
        monitor: 1-based monitor index (1 = primary display).
    """
    try:
        import mss  # local import keeps it optional for server deployments
    except ImportError as exc:  # pragma: no cover
        raise ScreenCaptureError(
            "The 'mss' package is required for live screen capture. "
            "Install it with `pip install mss`."
        ) from exc

    try:
        with mss.mss() as sct:
            monitors = sct.monitors
            if monitor >= len(monitors):
                monitor = 1
            raw = sct.grab(monitors[monitor])
            return Image.frombytes("RGB", raw.size, raw.rgb)
    except Exception as exc:  # pragma: no cover - environment dependent
        raise ScreenCaptureError(
            "Could not capture the screen. Live capture needs a desktop "
            f"session with display access. Original error: {exc}"
        ) from exc
