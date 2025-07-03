# bias_pipeline.py

from bias_eval import evaluate_bias
from preprocess import clean_text

def run_pipeline(articles):
    results = []
    for article in articles:
        content = article.get('content') or article.get('description') or ''
        cleaned = clean_text(content)
        bias, fake = evaluate_bias(cleaned)
        results.append({
            'title': article.get('title', ''),
            'source': article.get('source', {}).get('name', ''),
            'bias': bias,
            'fake': fake,
            'url': article.get('url', '')
        })
    return results
