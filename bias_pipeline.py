# bias_pipeline.py

from news_scraper import get_articles
from bias_eval import evaluate_bias
from preprocess import clean_text
# Import other necessary modules as needed

def run_pipeline(query, page_size=10):
    articles = get_articles(query=query, page_size=page_size)
    # Preprocess articles if necessary
    # For example:
    # cleaned_articles = [clean_text(article) for article in articles]
    df = evaluate_bias(articles)
    return df
