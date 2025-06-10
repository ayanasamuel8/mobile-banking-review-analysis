# notebooks

This folder contains Jupyter notebooks that orchestrate the data analysis workflow:

- **00_scrapping.ipynb**: Scrape and preprocess reviews.
- **01_sentiment_analysis.ipynb**: Perform sentiment analysis and save results.
- **02_keyword_theme_extraction.ipynb**: Extract keywords and cluster reviews into themes.
- **03_drivers_and_pain_point.ipynb**: Identify key drivers (positive themes) and pain points (negative themes) for each bank.
- **04_distribution_analysis.ipynb**: Visualize sentiment, rating, and theme distributions.
- **05_comparision.ipynb**: Compare banks based on sentiment, rating, and themes.
- **recommendation.md**: Contains actionable recommendations for each bank based on the analysis.

Each notebook is designed to be run sequentially, producing intermediate and final datasets in the `data/` folder and supporting the full analysis pipeline.