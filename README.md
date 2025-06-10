# Mobile Banking Review Analysis

## Overview
This project analyzes user reviews of mobile banking apps from the Google Play Store. It provides tools and scripts for scraping, cleaning, sentiment analysis, keyword extraction, theme clustering, and comparative analysis. The workflow is organized for reproducibility, modularity, and ease of collaboration, with Jupyter notebooks for interactive exploration and unit tests for code reliability.

## Project Structure
```
data-analysis-project/
├── data/                # Datasets: raw, cleaned, and processed (see data/README.md)
│   ├── raw/
│   ├── Cleaned/
│   ├── processed/
│   └── README.md
├── notebooks/           # Jupyter notebooks for each analysis step
│   ├── 00_scrapping.ipynb
│   ├── 01_sentiment_analysis.ipynb
│   ├── 02_keyword_theme_extraction.ipynb
│   ├── 03_drivers_and_pain_point.ipynb
│   ├── 04_distribution_analysis.ipynb
│   └── 05_comparision.ipynb
│   └── recommendation.md
├── src/                 # Source code modules
│   ├── task_1/          # Scraping and preprocessing
│   ├── task_2/          # Sentiment, keywords, clustering
│   └── task_4/          # Drivers, pain points, distribution, comparison
├── tests/               # Unit tests for all modules
│   └── test_main.py
├── .gitignore           # Files and directories to ignore in Git
├── requirements.txt     # Python dependencies for the project
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd data-analysis-project
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download spaCy model (if using lemmatization):**
   ```
   python -m spacy download en_core_web_sm
   ```

4. **Launch Jupyter Notebook to run the analysis:**
   ```
   jupyter notebook
   ```
   Open and run the notebooks in the `notebooks/` directory in order.

## Usage

- **Data Collection & Preprocessing:**  
  Use `notebooks/00_scrapping.ipynb` to scrape reviews and preprocess the data.
- **Sentiment Analysis:**  
  Use `notebooks/01_sentiment_analysis.ipynb` to add sentiment labels and scores.
- **Keyword Extraction & Clustering:**  
  Use `notebooks/02_keyword_theme_extraction.ipynb` to extract keywords and cluster reviews into themes.
- **Drivers & Pain Points:**  
  Use `notebooks/03_drivers_and_pain_point.ipynb` to identify key drivers and pain points for each bank.
- **Distribution Analysis:**  
  Use `notebooks/04_distribution_analysis.ipynb` for sentiment, rating, and theme distribution visualizations.
- **Comparative Analysis:**  
  Use `notebooks/05_comparision.ipynb` to compare banks by sentiment, rating, and themes.
- **Recommendations:**  
  See `notebooks/recommendation.md` for actionable insights based on the analysis.
- **Testing:**  
  Run the tests in the `tests/` directory to ensure code correctness.

## Folder Documentation

- See `data/README.md` for details on dataset organization.
- See `src/task_1/README.md`, `src/task_2/README.md`, and `src/task_4/README.md` for module-specific documentation.
- See `notebooks/README.md` for notebook descriptions.
- See `tests/README.md` for testing information.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or improvements.

---