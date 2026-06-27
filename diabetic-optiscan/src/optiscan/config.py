"""Typed configuration for training and inference."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DataConfig:
    data_dir: str = "data/aptos2019"
    train_csv: str = "train.csv"
    images_subdir: str = "train_images"
    image_ext: str = ".png"
    image_size: int = 224
    val_split: float = 0.15
    num_workers: int = 4


@dataclass
class ModelConfig:
    backbone: str = "vit_base_patch16_224"  # timm model name
    num_classes: int = 5
    pretrained: bool = True
    dropout: float = 0.1
    weights_path: Optional[str] = "weights/optiscan_vit.pt"


@dataclass
class PreprocessConfig:
    # Ben Graham style fundus normalisation
    use_circle_crop: bool = True
    use_clahe: bool = True
    # Custom wavelet enhancement
    use_wavelet: bool = True
    wavelet: str = "db2"
    wavelet_level: int = 2
    wavelet_gain: float = 1.4  # detail-coefficient amplification


@dataclass
class TrainConfig:
    epochs: int = 15
    batch_size: int = 16
    lr: float = 3e-5
    weight_decay: float = 1e-4
    label_smoothing: float = 0.1
    seed: int = 42
    output_dir: str = "weights"
    mixed_precision: bool = True


@dataclass
class Config:
    data: DataConfig = field(default_factory=DataConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    preprocess: PreprocessConfig = field(default_factory=PreprocessConfig)
    train: TrainConfig = field(default_factory=TrainConfig)
