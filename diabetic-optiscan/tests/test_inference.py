"""Tests for the inference layer and API (mock model, no torch required)."""
from __future__ import annotations

from io import BytesIO

import numpy as np
from fastapi.testclient import TestClient
from PIL import Image

from optiscan import DR_GRADES
from optiscan.inference import MockPredictor, load_predictor


def _fundus_png() -> bytes:
    rng = np.random.default_rng(0)
    arr = (rng.random((128, 128, 3)) * 255).astype("uint8")
    buf = BytesIO()
    Image.fromarray(arr).save(buf, format="PNG")
    return buf.getvalue()


def test_mock_predictor_returns_valid_grade():
    pred = MockPredictor()
    result = pred.predict(Image.open(BytesIO(_fundus_png())))
    assert result["grade"] in DR_GRADES
    assert result["label"] == DR_GRADES[result["grade"]]
    assert 0.0 <= result["confidence"] <= 1.0
    assert abs(sum(result["probabilities"].values()) - 1.0) < 1e-3
    assert result["mode"] == "mock"


def test_load_predictor_falls_back_to_mock():
    # No weights present in the test environment -> mock.
    pred = load_predictor()
    assert pred.mode == "mock"


def test_api_health_and_predict():
    from optiscan.api import app

    client = TestClient(app)

    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "ok"

    resp = client.post(
        "/predict", files={"file": ("fundus.png", _fundus_png(), "image/png")}
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["grade"] in DR_GRADES
    assert "probabilities" in body


def test_api_rejects_empty_file():
    from optiscan.api import app

    client = TestClient(app)
    resp = client.post("/predict", files={"file": ("x.png", b"", "image/png")})
    assert resp.status_code == 400
