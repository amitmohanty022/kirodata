"""FastAPI service exposing the DR grading model."""
from __future__ import annotations

import logging
from io import BytesIO

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image
from pydantic import BaseModel

from optiscan import __version__
from optiscan.inference import load_predictor

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Diabetic Optiscan",
    version=__version__,
    description=(
        "Diabetic retinopathy grading from retinal fundus images using a "
        "ViT-B/16 model with custom wavelet lesion enhancement."
    ),
)

_predictor = load_predictor()


class Prediction(BaseModel):
    grade: int
    label: str
    referable: bool
    confidence: float
    probabilities: dict
    mode: str


@app.get("/")
def root() -> dict:
    return {"app": "Diabetic Optiscan", "version": __version__, "docs": "/docs"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model_mode": _predictor.mode, "version": __version__}


@app.post("/predict", response_model=Prediction)
async def predict(file: UploadFile = File(...)) -> Prediction:
    if file.content_type and not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="Empty file.")
    try:
        image = Image.open(BytesIO(data))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid image: {exc}") from exc
    return Prediction(**_predictor.predict(image))
