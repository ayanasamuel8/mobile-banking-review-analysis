from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.5:
        label = 'positive'
    elif polarity < -0.5:
        label = 'negative'
    else:
        label = 'neutral'
    return label, polarity

def add_sentiment_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['review'] = df['review'].fillna('').astype(str)
    results = df['review'].apply(analyze_sentiment)
    df['sentiment_label'] = results.apply(lambda x: x[0])
    df['sentiment_score'] = results.apply(lambda x: x[1])
    return df