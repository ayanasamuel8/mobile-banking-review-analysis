import pandas as pd
from google_play_scraper import reviews, Sort

def fetch_reviews(app_id, bank_name, count=400):
    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=count
    )
    data = [{
        'review': r['content'],
        'rating': r['score'],
        'date': r['at'].strftime('%Y-%m-%d'),
        'bank': bank_name,
        'source': 'Google Play'
    } for r in result]
    return pd.DataFrame(data)
