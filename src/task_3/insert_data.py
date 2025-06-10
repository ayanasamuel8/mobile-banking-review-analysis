import cx_Oracle
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")

# Load cleaned reviews CSV
df = pd.read_csv('../../data/Cleaned/reviews_cleaned.csv')

# Connect to Oracle
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)
cursor = conn.cursor()

bank_id = cursor.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (
            bank_id,
            review_text,
            review_text_clean,
            sentiment_label,
            sentiment_score,
            identified_theme
        ) VALUES (
            :1, :2, :3, :4, :5, :6, :7
        )
    """, (
        bank_id,
        row['review'],
        row['review_text_clean'],
        row.get('sentiment_label'),
        row.get('sentiment_score'),
        row.get('identified_theme')
    ))

conn.commit()
cursor.close()
conn.close()