"""Fundus image normalisation (Ben Graham style) + the full preprocessing pipeline.

Steps:
1. Circle-crop the retina and remove the uninformative black border.
2. Resize to a square.
3. Optional CLAHE-like local contrast normalisation.
4. Optional custom wavelet lesion enhancement (see ``wavelet.py``).

Uses numpy + PIL only (no OpenCV dependency) so it runs anywhere.
"""
from __future__ import annotations

import numpy as np
from PIL import Image

from optiscan.preprocessing import wavelet as wavelet_mod


def _to_array(image: "Image.Image | np.ndarray") -> np.ndarray:
    if isinstance(image, Image.Image):
        return np.asarray(image.convert("RGB"))
    if image.ndim == 2:
        image = np.stack([image] * 3, axis=-1)
    return image


def circle_crop(arr: np.ndarray, tol: int = 7) -> np.ndarray:
    """Crop away the black border around a circular fundus photo."""
    gray = arr.mean(axis=2)
    mask = gray > tol
    if not mask.any():
        return arr
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    return arr[rows[0] : rows[-1] + 1, cols[0] : cols[-1] + 1]


def local_contrast(arr: np.ndarray, sigma: float = 10.0, weight: float = 4.0) -> np.ndarray:
    """Ben Graham normalisation: subtract a blurred copy to boost local detail."""
    blurred = _box_blur(arr.astype(np.float32), radius=int(sigma))
    out = weight * (arr.astype(np.float32) - blurred) + 128.0
    return np.clip(out, 0, 255).astype(np.uint8)


def _box_blur(arr: np.ndarray, radius: int) -> np.ndarray:
    """Cheap separable box blur (approximates a Gaussian) without scipy/cv2."""
    if radius < 1:
        return arr
    img = Image.fromarray(arr.astype(np.uint8))
    # PIL's resize down/up gives a fast, dependency-free smoothing approximation.
    small = img.resize(
        (max(1, img.width // (radius + 1)), max(1, img.height // (radius + 1))),
        Image.BILINEAR,
    )
    return np.asarray(small.resize(img.size, Image.BILINEAR)).astype(np.float32)


def preprocess(
    image: "Image.Image | np.ndarray",
    size: int = 224,
    use_circle_crop: bool = True,
    use_clahe: bool = True,
    use_wavelet: bool = True,
    wavelet: str = "db2",
    wavelet_level: int = 2,
    wavelet_gain: float = 1.4,
) -> "Image.Image":
    """Run the full fundus preprocessing pipeline and return a PIL image."""
    arr = _to_array(image)

    if use_circle_crop:
        arr = circle_crop(arr)

    pil = Image.fromarray(arr).resize((size, size), Image.BILINEAR)
    arr = np.asarray(pil)

    if use_clahe:
        arr = local_contrast(arr)

    if use_wavelet:
        arr = wavelet_mod.enhance(arr, wavelet=wavelet, level=wavelet_level, gain=wavelet_gain)

    return Image.fromarray(arr)
