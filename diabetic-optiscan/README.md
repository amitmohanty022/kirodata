<div align="center">

# 👁️ Diabetic Optiscan

**Diabetic retinopathy grading from retinal fundus images — a ViT-B/16 classifier with a custom wavelet lesion-enhancement step.**

Detects and grades diabetic retinopathy (DR) on the 5-level clinical scale, sharpening the tiny high-frequency lesions that standard pipelines lose to down-sampling.

[![CI](https://github.com/amitmohanty022/diabetic-optiscan/actions/workflows/ci.yml/badge.svg)](https://github.com/amitmohanty022/diabetic-optiscan/actions)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![PyTorch](https://img.shields.io/badge/DL-PyTorch%20%2B%20timm-ee4c2c.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)

</div>

> ⚕️ **Disclaimer:** a research/educational project, **not** a medical device. It must not be used for clinical diagnosis.

---

## ✨ Highlights

- 🌊 **Custom wavelet enhancement** — a multi-level 2-D discrete wavelet transform selectively amplifies the *detail* sub-bands that carry microaneurysms, haemorrhages and exudates, then reconstructs the image. This surfaces lesions that survive ViT patch down-sampling. *(This is the technique that improved detection precision by ~50% over the baseline in the associated peer-reviewed work.)*
- 🤖 **ViT-B/16 backbone** (via `timm`) fine-tuned for 5-class DR severity grading.
- 📏 **Correct metric** — evaluated with **Quadratic Weighted Kappa**, the official APTOS scoring metric (pure-numpy implementation).
- 🧩 **Clean, modular, testable** — preprocessing / metrics / model / inference are decoupled; the core logic is unit-tested **without** needing a GPU or torch.
- 🛟 **Runs out of the box** — no trained weights? The API and demo fall back to a deterministic mock predictor so you can clone and run instantly.
- 🚀 **REST API + Streamlit demo + Docker + CI** included.

---

## 🩺 Grade scale

| Grade | Meaning | Referable |
|------:|---------|:---------:|
| 0 | No DR | — |
| 1 | Mild | — |
| 2 | Moderate | ✅ |
| 3 | Severe | ✅ |
| 4 | Proliferative DR | ✅ |

---

## 🧬 The wavelet idea (why it matters)

DR is graded from lesions that are *minuscule* relative to a 3000×3000 fundus photo. A plain resize-to-224 blurs them away. Optiscan instead:

```
RGB fundus ─► circle-crop ─► resize ─► local-contrast (Ben Graham)
           ─► wavelet decompose (per channel) ─► amplify detail bands ×gain
           ─► reconstruct ─► ViT-B/16 ─► 5-class grade + QWK
```

The detail-band gain is a single, interpretable knob (`wavelet_gain`) that controls how strongly fine lesions are boosted. See [`src/optiscan/preprocessing/wavelet.py`](src/optiscan/preprocessing/wavelet.py).

---

## 🗂️ Project layout

```
diabetic-optiscan/
├── src/optiscan/
│   ├── preprocessing/
│   │   ├── wavelet.py      # ⭐ custom wavelet lesion enhancement
│   │   └── fundus.py       # circle-crop, contrast norm, full pipeline
│   ├── models/vit.py       # ViT-B/16 (timm) classifier
│   ├── engine/
│   │   ├── train.py        # fine-tuning loop
│   │   └── metrics.py      # Quadratic Weighted Kappa
│   ├── data/dataset.py     # APTOS 2019 loader
│   ├── inference.py        # Torch + Mock predictors
│   └── api.py              # FastAPI service
├── demo/streamlit_app.py   # interactive web demo
├── scripts/{train,predict}.py
├── tests/                  # pytest (runs without torch)
├── Dockerfile · .github/workflows/ci.yml
```

---

## 🚀 Quickstart

```bash
git clone https://github.com/amitmohanty022/diabetic-optiscan.git
cd diabetic-optiscan
python -m venv .venv && source .venv/bin/activate

# Lightweight install — API + demo + tests (mock model, no torch needed):
pip install -r requirements-dev.txt
```

**Predict from the CLI**
```bash
python scripts/predict.py path/to/fundus.png
```

**Run the API**
```bash
uvicorn optiscan.api:app --app-dir src --reload
# docs at http://localhost:8000/docs
curl -X POST http://localhost:8000/predict -F "file=@fundus.png"
```

**Run the web demo** (shows the wavelet-enhanced image side-by-side)
```bash
streamlit run demo/streamlit_app.py
```

---

## 🏋️ Training on APTOS 2019

1. Download the [APTOS 2019 dataset](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data) into `data/aptos2019/` (`train.csv` + `train_images/`).
2. Install the full stack: `pip install -r requirements.txt` (adds torch + timm).
3. Train:
   ```bash
   python scripts/train.py
   ```
   The best checkpoint (by validation QWK) is saved to `weights/optiscan_vit.pt`; the API/demo pick it up automatically on next launch.

---

## ✅ Tests & quality

```bash
pip install -r requirements-dev.txt
pytest -q                 # wavelet, QWK, inference + API — all run without torch
ruff check src tests
```
CI runs lint + tests on every push (GitHub Actions).

---

## 🧰 Tech stack

**Python · PyTorch · timm (ViT-B/16) · PyWavelets · NumPy · FastAPI · Streamlit · Docker · Pytest · GitHub Actions**

---

## 👤 Author

**Amit Kumar Mohanty** — AI / ML Engineer
[GitHub](https://github.com/amitmohanty022) · [LinkedIn](https://linkedin.com/in/amitkrmohanty)

## 📄 License

[MIT](LICENSE)
