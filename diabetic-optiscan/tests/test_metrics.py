"""Tests for the Quadratic Weighted Kappa implementation."""
from __future__ import annotations

from optiscan.engine.metrics import accuracy, quadratic_weighted_kappa


def test_perfect_agreement_is_one():
    y = [0, 1, 2, 3, 4, 2, 1]
    assert abs(quadratic_weighted_kappa(y, y) - 1.0) < 1e-9


def test_qwk_penalises_large_errors_more():
    y_true = [0, 0, 4, 4]
    near = [0, 1, 4, 3]   # off by 1
    far = [4, 4, 0, 0]    # maximally wrong
    assert quadratic_weighted_kappa(y_true, near) > quadratic_weighted_kappa(y_true, far)


def test_qwk_in_valid_range():
    y_true = [0, 1, 2, 3, 4, 0, 1, 2]
    y_pred = [0, 2, 1, 3, 4, 1, 1, 2]
    score = quadratic_weighted_kappa(y_true, y_pred)
    assert -1.0 <= score <= 1.0


def test_accuracy():
    assert accuracy([0, 1, 2], [0, 1, 2]) == 1.0
    assert accuracy([0, 1, 2], [0, 1, 0]) == 2 / 3
