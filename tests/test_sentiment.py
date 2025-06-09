import pytest
from src.task_2.sentiment import analyze_sentiment

@pytest.mark.parametrize("text,expected", [
    ("This app is amazing!", "positive"),
    ("It’s okay, nothing special.", "neutral"),
    ("Worst banking experience ever.", "negative")
])
def test_sentiment_classification(text, expected):
    label, _ = analyze_sentiment(text)
    assert label == expected
