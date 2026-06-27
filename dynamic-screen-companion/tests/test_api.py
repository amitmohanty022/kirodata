"""API tests using FastAPI's TestClient. Runs fully in mock mode."""
from __future__ import annotations

from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image

from app.main import app

client = TestClient(app)


def _png_bytes(text_color=(0, 0, 0)) -> bytes:
    img = Image.new("RGB", (320, 80), color=(255, 255, 255))
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def test_health_endpoint():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert "gemini_enabled" in body
    assert "ocr_available" in body


def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["app"]


def test_analyze_rejects_empty_upload():
    resp = client.post(
        "/analyze",
        files={"file": ("empty.png", b"", "image/png")},
    )
    assert resp.status_code == 400


def test_analyze_returns_analysis():
    resp = client.post(
        "/analyze",
        files={"file": ("screen.png", _png_bytes(), "image/png")},
        data={"question": "What is on screen?", "speak": "false"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["llm_mode"] in {"mock", "gemini"}
    assert "analysis" in body
    assert body["question"] == "What is on screen?"
