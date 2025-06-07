from transformers import pipeline
import pandas as pd

# Lazy load pipeline to avoid early import issues
def get_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_transformer_sentiment(text: str) -> str:
    if not isinstance(text, str) or text.strip() == "":
        return "neutral"

    sentiment_pipeline = get_sentiment_pipeline()
    result = sentiment_pipeline(text)[0]['label'].lower()

    if result == "positive":
        return "positive"
    elif result == "negative":
        return "negative"
    else:
        return "neutral"

def add_transformer_sentiment_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['transformer_sentiment'] = df['review'].apply(analyze_transformer_sentiment)
    return df
