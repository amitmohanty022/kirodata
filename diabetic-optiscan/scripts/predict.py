"""CLI: grade a single retinal image.

Usage:
    python scripts/predict.py path/to/fundus.png
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Make src/ importable when run from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from PIL import Image  # noqa: E402

from optiscan.inference import load_predictor  # noqa: E402


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/predict.py <image_path>")
        return 1
    image_path = sys.argv[1]
    predictor = load_predictor()
    result = predictor.predict(Image.open(image_path))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
