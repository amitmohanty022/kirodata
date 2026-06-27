"""Unit tests for the service layer (mock mode, no external deps required)."""
from __future__ import annotations

from app.services import gemini_client


def test_mock_analysis_without_key():
    """Without an API key, analyze() returns mock mode and references the screen text."""
    text = "Traceback (most recent call last): ZeroDivisionError"
    analysis, mode = gemini_client.analyze(text, question="What does this error mean?")
    assert mode == "mock"
    assert "MOCK MODE" in analysis
    assert "What does this error mean?" in analysis


def test_mock_analysis_handles_empty_screen():
    analysis, mode = gemini_client.analyze("", question=None)
    assert mode == "mock"
    assert "couldn't detect" in analysis.lower()


def test_build_prompt_includes_question_and_text():
    prompt = gemini_client._build_prompt("hello world", "summarise this")
    assert "hello world" in prompt
    assert "summarise this" in prompt
    assert "SCREEN TEXT" in prompt
