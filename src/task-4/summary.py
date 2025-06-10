import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def theme_sentiment_summary(df):
    """Group by theme and sentiment, calculate ratios."""
    theme_sentiment = df.groupby(['identified_theme', 'sentiment_label']).size().unstack(fill_value=0)
    theme_sentiment['total'] = theme_sentiment.sum(axis=1)
    theme_sentiment['positive_ratio'] = theme_sentiment.get('positive', 0) / theme_sentiment['total']
    theme_sentiment['negative_ratio'] = theme_sentiment.get('negative', 0) / theme_sentiment['total']
    return theme_sentiment.sort_values(by='total', ascending=False)

def identify_drivers(theme_sentiment, threshold=0.2):
    """Identify drivers (themes with high positive sentiment ratio)."""
    return theme_sentiment[theme_sentiment['positive_ratio'] > threshold].sort_values('positive_ratio', ascending=False)

def identify_pain_points(theme_sentiment, threshold=0.002):
    """Identify pain points (themes with high negative sentiment ratio)."""
    return theme_sentiment[theme_sentiment['negative_ratio'] > threshold].sort_values('negative_ratio', ascending=False)

def sentiment_distribution(df):
    """Plot overall sentiment distribution."""
    sns.countplot(data=df, x='sentiment_label')
    plt.title("Overall Sentiment Distribution")
    plt.show()

def rating_distribution(df):
    """Plot rating distribution."""
    sns.histplot(df['rating'], bins=5, kde=True)
    plt.title("Rating Distribution")
    plt.show()

def theme_distribution(df):
    """Plot most common themes."""
    df['identified_theme'].value_counts().plot(kind='bar')
    plt.title("Most Common Themes")
    plt.show()

def sentiment_by_bank(df):
    """Plot sentiment label distribution by bank."""
    df.groupby(['bank', 'sentiment_label']).size().unstack().plot(kind='bar', stacked=True)
    plt.title("Sentiment by Bank")
    plt.show()

def rating_by_bank(df):
    """Plot rating distribution by bank."""
    df.groupby(['bank', 'rating']).size().unstack().plot(kind='bar', stacked=True)
    plt.title("Rating by Bank")
    plt.show()

def average_rating_by_bank(df):
    """Plot average rating per bank."""
    df.groupby('bank')['rating'].mean().plot(kind='barh')
    plt.title("Average Rating by Bank")
    plt.show()

def grouped_theme_sentiment_by_bank(df):
    """Group by bank, theme, and sentiment label, and calculate ratios."""
    grouped = df.groupby(['bank', 'identified_theme', 'sentiment_label']).size().unstack(fill_value=0)
    grouped['total'] = grouped.sum(axis=1)
    if 'positive' in grouped.columns:
        grouped['positive_ratio'] = grouped['positive'] / grouped['total']
    if 'negative' in grouped.columns:
        grouped['negative_ratio'] = grouped['negative'] / grouped['total']
    return grouped.reset_index()