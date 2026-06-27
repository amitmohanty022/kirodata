"""Tests for the custom wavelet enhancement."""
from __future__ import annotations

import numpy as np
import pytest

from optiscan.preprocessing import wavelet


def _sample_image(seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return (rng.random((64, 64, 3)) * 255).astype(np.uint8)


def test_output_shape_and_dtype_preserved():
    img = _sample_image()
    out = wavelet.enhance(img)
    assert out.shape == img.shape
    assert out.dtype == np.uint8
    assert out.min() >= 0 and out.max() <= 255


def test_grayscale_supported():
    img = (np.random.default_rng(1).random((48, 48)) * 255).astype(np.uint8)
    out = wavelet.enhance(img)
    assert out.shape == img.shape


def test_gain_one_is_near_identity():
    img = _sample_image(2)
    out = wavelet.enhance(img, gain=1.0)
    # Reconstruction with gain=1 should be close to the original (rounding aside).
    assert np.mean(np.abs(out.astype(int) - img.astype(int))) < 3.0


def test_higher_gain_increases_detail_energy():
    img = _sample_image(3)
    low = wavelet.enhance(img, gain=1.0).astype(float)
    high = wavelet.enhance(img, gain=2.0).astype(float)
    # Amplifying detail bands should increase local variance (sharper edges).
    assert high.var() >= low.var()


def test_invalid_gain_raises():
    with pytest.raises(ValueError):
        wavelet.enhance(_sample_image(), gain=0)
