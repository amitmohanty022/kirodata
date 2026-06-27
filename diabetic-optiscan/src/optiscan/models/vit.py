"""Vision Transformer classifier for diabetic-retinopathy grading.

Wraps a timm ViT-B/16 backbone with a small classification head. torch + timm
are imported lazily so the rest of the package (preprocessing, metrics) can be
used and tested without a heavyweight deep-learning install.
"""
from __future__ import annotations


def build_model(
    backbone: str = "vit_base_patch16_224",
    num_classes: int = 5,
    pretrained: bool = True,
    dropout: float = 0.1,
):
    """Create a ViT classifier. Requires torch + timm."""
    try:
        import timm
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "Training/inference needs torch and timm: pip install torch timm"
        ) from exc

    model = timm.create_model(
        backbone,
        pretrained=pretrained,
        num_classes=num_classes,
        drop_rate=dropout,
    )
    return model


def load_weights(model, weights_path: str, device: str = "cpu"):
    """Load fine-tuned weights into a model in-place and return it."""
    import torch

    state = torch.load(weights_path, map_location=device)
    state = state.get("model_state", state) if isinstance(state, dict) else state
    model.load_state_dict(state)
    model.to(device).eval()
    return model
