"""Inference: grade a single retinal image.

The Predictor runs the real ViT model when torch/timm and fine-tuned weights are
available. Otherwise it falls back to a deterministic heuristic ``MockPredictor``
so the API, demo and tests all work out of the box without a 300 MB download.
"""
from __future__ import annotations

import logging
from typing import Optional

import numpy as np

from optiscan import DR_GRADES
from optiscan.config import Config
from optiscan.preprocessing.fundus import preprocess

logger = logging.getLogger(__name__)


def _softmax(x: np.ndarray) -> np.ndarray:
    e = np.exp(x - x.max())
    return e / e.sum()


class MockPredictor:
    """Deterministic stand-in used when the real model isn't available.

    Estimates a pseudo-severity from the density of dark lesion-like pixels in
    the wavelet-enhanced image. Not clinically meaningful - it exists purely so
    the project is fully runnable and demonstrable without trained weights.
    """

    mode = "mock"

    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()

    def predict(self, image) -> dict:
        pc = self.config.preprocess
        proc = preprocess(
            image,
            size=self.config.data.image_size,
            use_circle_crop=pc.use_circle_crop,
            use_clahe=pc.use_clahe,
            use_wavelet=pc.use_wavelet,
            wavelet=pc.wavelet,
            wavelet_level=pc.wavelet_level,
            wavelet_gain=pc.wavelet_gain,
        )
        arr = np.asarray(proc, dtype=np.float32) / 255.0
        gray = arr.mean(axis=2)
        # Lesion-like = locally dark spots; use their fraction as a severity proxy.
        dark_fraction = float((gray < 0.25).mean())
        score = np.clip(dark_fraction * 12.0, 0, 4)
        logits = -((np.arange(5) - score) ** 2)
        probs = _softmax(logits)
        grade = int(np.argmax(probs))
        return _format(grade, probs, self.mode)


class TorchPredictor:
    """Runs the fine-tuned ViT-B/16 model."""

    mode = "vit"

    def __init__(self, config: Optional[Config] = None, device: str = "cpu"):
        import torch  # noqa: F401

        from optiscan.models.vit import build_model, load_weights

        self.config = config or Config()
        self.device = device
        self.model = build_model(
            backbone=self.config.model.backbone,
            num_classes=self.config.model.num_classes,
            pretrained=False,
            dropout=self.config.model.dropout,
        )
        load_weights(self.model, self.config.model.weights_path, device=device)

    def predict(self, image) -> dict:
        import torch

        pc = self.config.preprocess
        proc = preprocess(image, size=self.config.data.image_size,
                          use_circle_crop=pc.use_circle_crop, use_clahe=pc.use_clahe,
                          use_wavelet=pc.use_wavelet, wavelet=pc.wavelet,
                          wavelet_level=pc.wavelet_level, wavelet_gain=pc.wavelet_gain)
        arr = np.asarray(proc, dtype=np.float32) / 255.0
        tensor = torch.from_numpy(arr).permute(2, 0, 1).unsqueeze(0).to(self.device)
        with torch.no_grad():
            logits = self.model(tensor)
            probs = torch.softmax(logits, dim=1).cpu().numpy()[0]
        grade = int(probs.argmax())
        return _format(grade, probs, self.mode)


def _format(grade: int, probs, mode: str) -> dict:
    probs = np.asarray(probs, dtype=float)
    return {
        "grade": grade,
        "label": DR_GRADES[grade],
        "referable": grade >= 2,  # grade >= 2 (moderate+) warrants referral
        "confidence": round(float(probs[grade]), 4),
        "probabilities": {DR_GRADES[i]: round(float(p), 4) for i, p in enumerate(probs)},
        "mode": mode,
    }


def load_predictor(config: Optional[Config] = None, device: str = "cpu"):
    """Return a TorchPredictor if possible, else a MockPredictor."""
    config = config or Config()
    weights = config.model.weights_path
    try:
        import os

        import torch  # noqa: F401

        if weights and os.path.exists(weights):
            return TorchPredictor(config, device=device)
        logger.info("No weights at %s - using MockPredictor.", weights)
    except ImportError:
        logger.info("torch/timm not installed - using MockPredictor.")
    return MockPredictor(config)
