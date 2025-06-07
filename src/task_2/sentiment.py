from textblob import TextBlob
import pandas as pd


def analyze_sentiment(text: str) -> str:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.5:
        return 'positive'
    elif polarity < -0.5:
        return 'negative'
    else:
        return 'neutral'


def add_sentiment_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['sentiment'] = df['review'].apply(analyze_sentiment)
    return df
