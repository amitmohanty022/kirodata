"""Diabetic Optiscan - interactive web demo.

Upload a retinal fundus image and see the predicted diabetic-retinopathy grade,
the per-class probabilities, and the wavelet-enhanced image the model "sees".

Deploy free on Hugging Face Spaces (SDK: Streamlit) or run locally:
    streamlit run demo/streamlit_app.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import streamlit as st  # noqa: E402
from PIL import Image  # noqa: E402

from optiscan.config import Config  # noqa: E402
from optiscan.inference import load_predictor  # noqa: E402
from optiscan.preprocessing.fundus import preprocess  # noqa: E402

st.set_page_config(page_title="Diabetic Optiscan", page_icon="👁️", layout="centered")

GRADE_COLORS = {0: "🟢", 1: "🟡", 2: "🟠", 3: "🔴", 4: "🔴"}


@st.cache_resource(show_spinner=False)
def get_predictor():
    return load_predictor()


def main() -> None:
    st.title("👁️ Diabetic Optiscan")
    st.caption(
        "Diabetic retinopathy grading from retinal fundus images — "
        "ViT-B/16 with custom wavelet lesion enhancement."
    )

    predictor = get_predictor()
    mode_label = "🟢 Trained ViT" if predictor.mode == "vit" else "🟡 Demo (mock) model"
    st.info(
        f"**Model status:** {mode_label}. "
        "This is a research/educational tool and is **not** a medical device."
    )

    uploaded = st.file_uploader(
        "Upload a retinal fundus image", type=["png", "jpg", "jpeg"]
    )

    if uploaded is None:
        st.stop()

    image = Image.open(uploaded).convert("RGB")
    col1, col2 = st.columns(2)
    col1.image(image, caption="Original", use_container_width=True)

    cfg = Config().preprocess
    enhanced = preprocess(
        image, size=224, use_circle_crop=cfg.use_circle_crop, use_clahe=cfg.use_clahe,
        use_wavelet=cfg.use_wavelet, wavelet=cfg.wavelet,
        wavelet_level=cfg.wavelet_level, wavelet_gain=cfg.wavelet_gain,
    )
    col2.image(enhanced, caption="Wavelet-enhanced (model input)", use_container_width=True)

    if st.button("🔬 Analyse", type="primary", use_container_width=True):
        with st.spinner("Analysing..."):
            result = predictor.predict(image)

        grade, label = result["grade"], result["label"]
        st.markdown(f"### {GRADE_COLORS[grade]} Grade {grade} — **{label}**")
        c1, c2 = st.columns(2)
        c1.metric("Confidence", f"{result['confidence'] * 100:.1f}%")
        c2.metric("Referable?", "Yes" if result["referable"] else "No")

        st.subheader("Per-class probability")
        st.bar_chart(result["probabilities"])
        st.caption(f"Model mode: {result['mode']}")

    st.markdown("---")
    st.caption(
        "Built by Amit Kumar Mohanty · "
        "[GitHub](https://github.com/amitmohanty022) · PyTorch + timm + Streamlit"
    )


if __name__ == "__main__":
    main()
