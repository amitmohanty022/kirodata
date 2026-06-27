"""Fine-tuning loop for the ViT-B/16 DR grader.

Kept deliberately small and readable. torch/timm are imported lazily; this
module is only exercised when you actually train (heavy deps required).
"""
from __future__ import annotations

import logging
import os
import random
from typing import Optional

import numpy as np

from optiscan.config import Config
from optiscan.engine.metrics import accuracy, quadratic_weighted_kappa

logger = logging.getLogger(__name__)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
    except ImportError:  # pragma: no cover
        pass


def train(config: Optional[Config] = None):  # pragma: no cover - needs GPU/data
    """Run fine-tuning. Returns the path to the best saved checkpoint."""
    import torch
    from torch.utils.data import DataLoader, random_split

    from optiscan.data.dataset import AptosDataset, read_labels_csv
    from optiscan.models.vit import build_model

    config = config or Config()
    set_seed(config.train.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    records = read_labels_csv(os.path.join(config.data.data_dir, config.data.train_csv))
    images_dir = os.path.join(config.data.data_dir, config.data.images_subdir)
    pc = config.preprocess
    pre_kwargs = dict(
        use_circle_crop=pc.use_circle_crop, use_clahe=pc.use_clahe, use_wavelet=pc.use_wavelet,
        wavelet=pc.wavelet, wavelet_level=pc.wavelet_level, wavelet_gain=pc.wavelet_gain,
    )

    def to_tensor(pil):
        arr = np.asarray(pil, dtype=np.float32) / 255.0
        return torch.from_numpy(arr).permute(2, 0, 1)

    full = AptosDataset(records, images_dir, config.data.image_ext, config.data.image_size,
                        pre_kwargs, transform=to_tensor)
    n_val = int(len(full) * config.data.val_split)
    train_ds, val_ds = random_split(full, [len(full) - n_val, n_val])
    train_dl = DataLoader(train_ds, batch_size=config.train.batch_size, shuffle=True,
                          num_workers=config.data.num_workers)
    val_dl = DataLoader(val_ds, batch_size=config.train.batch_size,
                        num_workers=config.data.num_workers)

    model = build_model(config.model.backbone, config.model.num_classes,
                        config.model.pretrained, config.model.dropout).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.train.lr,
                                  weight_decay=config.train.weight_decay)
    criterion = torch.nn.CrossEntropyLoss(label_smoothing=config.train.label_smoothing)

    os.makedirs(config.train.output_dir, exist_ok=True)
    best_qwk, best_path = -1.0, os.path.join(config.train.output_dir, "optiscan_vit.pt")

    for epoch in range(config.train.epochs):
        model.train()
        for imgs, labels in train_dl:
            imgs, labels = imgs.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(imgs), labels)
            loss.backward()
            optimizer.step()

        preds, gts = _evaluate(model, val_dl, device)
        qwk = quadratic_weighted_kappa(gts, preds)
        logger.info("epoch %d | val QWK %.4f | acc %.4f", epoch, qwk, accuracy(gts, preds))
        if qwk > best_qwk:
            best_qwk = qwk
            torch.save({"model_state": model.state_dict(), "qwk": qwk}, best_path)

    logger.info("Best QWK %.4f -> %s", best_qwk, best_path)
    return best_path


def _evaluate(model, dl, device):  # pragma: no cover
    import torch

    model.eval()
    preds, gts = [], []
    with torch.no_grad():
        for imgs, labels in dl:
            out = model(imgs.to(device))
            preds.extend(out.argmax(1).cpu().tolist())
            gts.extend(labels.tolist())
    return preds, gts
