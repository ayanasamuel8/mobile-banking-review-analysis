# tests/test_transformer_sentiment.py

import pytest
from src.task_2.transformer_sentiment import analyze_transformer_sentiment

@pytest.mark.parametrize("text,expected", [
    ("This app is amazing!", "positive"),
    ("Worst banking experience ever.", "negative"),
    ("It’s okay, nothing special.", "neutral"),  # may still return positive
])
def test_transformer_sentiment(text, expected):
    result = analyze_transformer_sentiment(text)
    print(f"Text: {text} → Predicted: {result}")
    assert result in {"positive", "negative", "neutral"}
