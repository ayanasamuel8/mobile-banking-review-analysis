import pandas as pd
from src.task_2.keywords import extract_top_keywords


def test_extract_keywords_basic():
    df = pd.DataFrame({
        'review': [
            'The app is fast and reliable',
            'Terrible app with bugs',
            'Fast support and good features',
            'Unusable and buggy app'
        ]
    })
    keywords = extract_top_keywords(df, top_n=5)
    assert not keywords.empty
    assert 'keyword' in keywords.columns
    assert len(keywords) == 5
