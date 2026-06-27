"""Dynamic Screen Companion - interactive web demo.

A single-file Streamlit app that runs the full pipeline
(OCR -> Gemini -> Text-to-Speech) on an uploaded screenshot.

Deploy free on Hugging Face Spaces (SDK: Streamlit) or run locally:
    streamlit run demo/streamlit_app.py

Set GEMINI_API_KEY (env var or the sidebar field) for live AI responses;
without it the app runs in MOCK mode so the demo always works.
"""
from __future__ import annotations

import os
import sys
from io import BytesIO

# Make the `app` package importable when run from the repo root or /demo.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st  # noqa: E402
from PIL import Image  # noqa: E402

st.set_page_config(
    page_title="Dynamic Screen Companion",
    page_icon="🖥️",
    layout="centered",
)


@st.cache_resource(show_spinner=False)
def _warm_imports():
    from app.services import gemini_client, ocr, tts

    return ocr, gemini_client, tts


def main() -> None:
    st.title("🖥️ Dynamic Screen Companion")
    st.caption(
        "A real-time multi-modal assistant: it reads your screen with OCR, "
        "reasons about it with Gemini, and speaks the answer back."
    )

    with st.sidebar:
        st.header("⚙️ Settings")
        api_key = st.text_input(
            "Gemini API key (optional)",
            type="password",
            help="Leave blank to run in MOCK mode. Get a key at aistudio.google.com.",
        )
        if api_key:
            os.environ["GEMINI_API_KEY"] = api_key
            # Reset cached settings so the new key is picked up.
            from app.config import get_settings

            get_settings.cache_clear()
        speak = st.toggle("🔊 Speak the answer", value=True)
        st.markdown("---")
        st.markdown(
            "**How it works**\n\n"
            "1. Upload a screenshot\n"
            "2. (Optional) ask a question\n"
            "3. OCR extracts on-screen text\n"
            "4. Gemini analyses it\n"
            "5. Optional spoken reply"
        )

    ocr, gemini_client, tts = _warm_imports()

    uploaded = st.file_uploader(
        "Upload a screenshot", type=["png", "jpg", "jpeg", "webp", "bmp"]
    )
    question = st.text_input(
        "Ask a question about the screen (optional)",
        placeholder="e.g. What does this error mean? Summarise this page.",
    )

    col1, col2 = st.columns([1, 1])
    run = col1.button("✨ Analyse screen", type="primary", use_container_width=True)

    from app.config import get_settings

    mode_label = "🟢 Live (Gemini)" if get_settings().gemini_enabled else "🟡 Mock mode"
    col2.markdown(f"**Status:** {mode_label}")

    if uploaded is not None:
        image = Image.open(uploaded)
        st.image(image, caption="Input screenshot", use_container_width=True)

    if run:
        if uploaded is None:
            st.warning("Please upload a screenshot first.")
            return

        image = Image.open(uploaded).convert("RGB")
        buf = BytesIO()
        image.save(buf, format="PNG")
        image_bytes = buf.getvalue()

        with st.spinner("Reading the screen..."):
            extracted = ocr.extract_text(image_bytes)
        with st.spinner("Thinking..."):
            analysis, llm_mode = gemini_client.analyze(extracted, question or None)

        st.subheader("🧠 Assistant response")
        st.write(analysis)

        if speak:
            with st.spinner("Generating speech..."):
                audio = tts.synthesize(analysis)
            if audio:
                st.audio(audio, format="audio/mp3")
            else:
                st.info("Audio unavailable (TTS needs network access).")

        with st.expander("🔎 Extracted text (OCR)"):
            if extracted:
                st.code(extracted)
            else:
                st.write(
                    "No text detected — Tesseract may not be installed on this host. "
                    "The pipeline still works; OCR just returned empty."
                )

        st.caption(f"LLM mode: {llm_mode}")

    st.markdown("---")
    st.caption(
        "Built by Amit Kumar Mohanty · "
        "[GitHub](https://github.com/amitmohanty022) · FastAPI + Gemini + Streamlit"
    )


if __name__ == "__main__":
    main()
