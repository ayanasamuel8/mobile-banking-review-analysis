import pandas as pd

def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicate reviews
    df = df.drop_duplicates(subset='review').copy()

    # Safely convert date
    df.loc[:, 'date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Fill missing review values
    df.loc[:, 'review'] = df['review'].fillna('')

    # Remove reviews shorter than 3 characters
    df = df[df['review'].str.len() >= 3].copy()

    # Remove non-ASCII characters
    df.loc[:, 'review'] = df['review'].apply(lambda x: x.encode('ascii', errors='ignore').decode())

    # Clean whitespace
    df.loc[:, 'review'] = df['review'].str.strip()
    df.loc[:, 'review'] = df['review'].replace(r'\s+', ' ', regex=True)

    # Fill missing ratings with median
    if df['rating'].isnull().any():
        median_rating = df['rating'].median()
        df.loc[:, 'rating'] = df['rating'].fillna(median_rating)

    # Ensure valid integer ratings
    df = df[df['rating'].between(1, 5)].copy()
    df.loc[:, 'rating'] = df['rating'].astype(int)

    # Final deduplication
    df = df.drop_duplicates(subset='review').reset_index(drop=True)

    return df



def save_cleaned_reviews(df: pd.DataFrame, filename='../data/reviews_cleaned.csv'):
    df.to_csv(filename, index=False)
