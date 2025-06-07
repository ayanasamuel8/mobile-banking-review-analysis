def summarize_sentiment_by_bank_rating(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby(['bank', 'rating'])['sentiment'].value_counts(normalize=True)
    return summary.unstack(fill_value=0)
