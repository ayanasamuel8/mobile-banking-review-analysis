from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np


def extract_top_keywords(df: pd.DataFrame, column: str = 'review', top_n: int = 20) -> pd.DataFrame:
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(df[column])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    top_indices = np.argsort(tfidf_scores)[::-1][:top_n]

    keywords = [{'keyword': feature_names[i], 'score': tfidf_scores[i]} for i in top_indices]
    return pd.DataFrame(keywords)
