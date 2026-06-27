"""CLI entry point for fine-tuning the ViT-B/16 grader.

Usage:
    python scripts/train.py            # uses default config
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from optiscan.config import Config  # noqa: E402
from optiscan.engine.train import train  # noqa: E402


def main() -> int:
    config = Config()
    best = train(config)
    print(f"Best checkpoint saved to: {best}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
