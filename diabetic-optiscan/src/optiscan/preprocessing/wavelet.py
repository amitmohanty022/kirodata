"""Custom wavelet enhancement for retinal fundus images.

Diabetic retinopathy lesions (microaneurysms, haemorrhages, exudates) are
small, high-frequency structures that are easily lost to a CNN/ViT after
down-sampling. This module performs a multi-level 2-D discrete wavelet
transform per colour channel, selectively amplifies the *detail* sub-bands
(horizontal/vertical/diagonal) that carry these fine lesions, and reconstructs
the image. The result sharpens diagnostically-relevant micro-structures while
leaving the low-frequency anatomy intact.

Only depends on numpy + PyWavelets, so it is fully unit-testable without a GPU.
"""
from __future__ import annotations

import numpy as np

try:  # PyWavelets is lightweight; import lazily so the module imports cleanly.
    import pywt

    _HAS_PYWT = True
except ImportError:  # pragma: no cover
    _HAS_PYWT = False


def _enhance_channel(channel: np.ndarray, wavelet: str, level: int, gain: float) -> np.ndarray:
    """Apply detail-band amplification to a single 2-D channel in [0, 1]."""
    coeffs = pywt.wavedec2(channel, wavelet=wavelet, level=level)
    # coeffs[0] = approximation; coeffs[1:] = (cH, cV, cD) per level.
    new_coeffs = [coeffs[0]]
    for (c_h, c_v, c_d) in coeffs[1:]:
        new_coeffs.append((c_h * gain, c_v * gain, c_d * gain))
    recon = pywt.waverec2(new_coeffs, wavelet=wavelet)
    # waverec2 can return an image 1px larger on odd dimensions; crop back.
    recon = recon[: channel.shape[0], : channel.shape[1]]
    return np.clip(recon, 0.0, 1.0)


def enhance(
    image: np.ndarray, wavelet: str = "db2", level: int = 2, gain: float = 1.4
) -> np.ndarray:
    """Wavelet-enhance an RGB (H, W, 3) or grayscale (H, W) uint8/float image.

    Args:
        image: input image, uint8 [0, 255] or float [0, 1].
        wavelet: PyWavelets wavelet name (e.g. 'db2', 'haar', 'sym4').
        level: decomposition levels.
        gain: multiplier applied to detail coefficients (>1 sharpens lesions).

    Returns:
        Enhanced image as uint8 with the same shape as the input.
    """
    if not _HAS_PYWT:  # pragma: no cover
        raise ImportError("PyWavelets is required: pip install PyWavelets")
    if gain <= 0:
        raise ValueError("gain must be positive")

    arr = image.astype(np.float32)
    if arr.max() > 1.0:
        arr = arr / 255.0

    if arr.ndim == 2:
        out = _enhance_channel(arr, wavelet, level, gain)
    elif arr.ndim == 3 and arr.shape[2] == 3:
        out = np.stack(
            [_enhance_channel(arr[:, :, c], wavelet, level, gain) for c in range(3)],
            axis=-1,
        )
    else:
        raise ValueError(f"Unsupported image shape: {image.shape}")

    return (out * 255.0).round().astype(np.uint8)
