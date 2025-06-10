import pandas as pd
import spacy

def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    nlp = spacy.load("en_core_web_sm")

    # Ensure text is string and apply spaCy preprocessing
    def preprocess(text):
        doc = nlp(str(text).lower())
        tokens = [
            token.lemma_ for token in doc
            if not token.is_stop and token.is_alpha
        ]
        return " ".join(tokens)

    # Fill missing review values early
    df['review'] = df['review'].fillna('').astype(str)

    # Clean review text
    df['review_text_clean'] = df['review'].apply(preprocess)

    # Drop duplicate reviews
    df = df.drop_duplicates(subset='review').copy()

    # Convert and clean date column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Remove very short reviews
    df = df[df['review'].str.len() >= 3].copy()

    # Remove non-ASCII characters
    df['review'] = df['review'].apply(lambda x: x.encode('ascii', errors='ignore').decode())

    # Clean whitespace
    df['review'] = df['review'].str.strip().replace(r'\s+', ' ', regex=True)

    # Handle rating column
    if 'rating' in df.columns:
        if df['rating'].isnull().any():
            median_rating = df['rating'].median()
            df['rating'] = df['rating'].fillna(median_rating)
        df = df[df['rating'].between(1, 5)].copy()
        df['rating'] = df['rating'].astype(int)

    # Final deduplication
    df = df.drop_duplicates(subset='review').reset_index(drop=True)

    return df

def add_review_id(df: pd.DataFrame) -> pd.DataFrame:
    if 'review_id' not in df.columns:
        df['review_id'] = range(1, len(df) + 1)
    return df

def save_cleaned_reviews(df: pd.DataFrame, path: str ="../data/Cleaned/reviews_cleaned.csv") -> None:
    columns = ['review_id', 'review', 'rating', 'bank', 'review_text_clean', 'sentiment_label', 'sentiment_score', 'identified_theme']
    df.to_csv(path, columns=columns, index=False)

def save_raw_reviews(df: pd.DataFrame) -> None:
    df.to_csv('../data/Raw/reviews.csv', index=False)

def save_processed_reviews(df: pd.DataFrame) -> None:
    df.to_csv('../data/processed/processed_reviews.csv', index=False)