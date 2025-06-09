from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
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

def cluster_themes(df, n_clusters=4) -> pd.DataFrame:

    custom_stopwords = list(ENGLISH_STOP_WORDS.union({'app', 'bank', 'account', 'mobile', 'service'}))
    vectorizer = TfidfVectorizer(stop_words=custom_stopwords, max_features=1000)

    X = vectorizer.fit_transform(df['review_text_clean'])

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    df['cluster'] = kmeans.fit_predict(X)

    # Extract top keywords for each cluster
    terms = vectorizer.get_feature_names_out()
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]

    cluster_keywords = []
    for i in range(n_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :5]]  # top 5 words
        cluster_keywords.append(", ".join(top_terms))

    # Map cluster number to keyword description
    df['identified_theme'] = df['cluster'].map(lambda x: cluster_keywords[x])
    df.drop(columns='cluster', inplace=True)
    
    return df

