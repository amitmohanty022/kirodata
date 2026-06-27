"""Evaluation metrics.

The APTOS / diabetic-retinopathy challenges are scored with the
**Quadratic Weighted Kappa (QWK)**, which rewards predictions that are close to
the true severity grade and penalises large mistakes more heavily. Implemented
in pure numpy so it is dependency-light and fully unit-testable.
"""
from __future__ import annotations

import numpy as np


def quadratic_weighted_kappa(y_true, y_pred, num_classes: int = 5) -> float:
    """Compute the Quadratic Weighted Kappa between two integer rating arrays."""
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=int)
    if y_true.shape != y_pred.shape:
        raise ValueError("y_true and y_pred must have the same shape")

    # Confusion matrix O.
    obs = np.zeros((num_classes, num_classes), dtype=np.float64)
    for t, p in zip(y_true, y_pred):
        obs[t, p] += 1

    # Weight matrix (quadratic distance).
    idx = np.arange(num_classes)
    weights = (idx[:, None] - idx[None, :]) ** 2 / (num_classes - 1) ** 2

    # Expected matrix E from the outer product of the marginals.
    act_hist = obs.sum(axis=1)
    pred_hist = obs.sum(axis=0)
    expected = np.outer(act_hist, pred_hist)

    total = obs.sum()
    if total == 0:
        return 0.0
    expected = expected / expected.sum() * total

    denom = (weights * expected).sum()
    if denom == 0:
        return 1.0
    return float(1.0 - (weights * obs).sum() / denom)


def accuracy(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if y_true.size == 0:
        return 0.0
    return float((y_true == y_pred).mean())
