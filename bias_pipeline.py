# bias_pipeline.py

from bias_eval import evaluate_bias
from preprocess import clean_text

def run_pipeline(articles):
    # Preprocess and analyze each article
    results = []
    for article in articles:
        content = article.get('content') or article.get('description') or ''
        cleaned = clean_text(content)
        bias, fake = evaluate_bias(cleaned)  # Pass only the cleaned text
        results.append({
            'title': article.get('title', ''),
            'source': article.get('source', {}).get('name', ''),
            'bias': bias,
            'fake': fake,
            'url': article.get('url', '')
        })
    return results
