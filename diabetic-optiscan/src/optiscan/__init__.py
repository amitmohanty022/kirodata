"""Diabetic Optiscan - Diabetic Retinopathy grading with Vision Transformers.

A clean, modular pipeline for detecting and grading diabetic retinopathy from
retinal fundus images, featuring a custom wavelet enhancement step and a
ViT-B/16 classifier trained on the APTOS 2019 dataset.
"""

__version__ = "1.0.0"

# 5-class APTOS diabetic retinopathy severity scale.
DR_GRADES = {
    0: "No DR",
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Proliferative DR",
}
