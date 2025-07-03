import pandas as pd
import random
from transformers import pipeline

# You can use a custom/fine-tuned model for bias if available
# For demo, we'll use sentiment-analysis as a placeholder
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def evaluate_bias(articles):
    data = []
    for article in articles:
        title = article.get('title', '')
        url = article.get('url', '')
        title_link = f'<a href="{url}" target="_blank">{title}</a>' if url else title
        
        # Dummy logic: randomly assign bias/fake
        biases = ['left', 'center', 'right', 'neutral', 'fake']
        bias = random.choice(biases)
        fake = 'Yes' if bias == 'fake' else 'No'
        
        data.append({
            'Title': title_link,
            'Source': article.get('source', {}).get('name', ''),
            'Bias': bias,
            'Fake': fake
        })
    return pd.DataFrame(data)

def evaluate_bias(text):
    result = classifier(text[:512])[0]  # Truncate to 512 tokens for BERT models
    label = result['label'].lower()
    score = result['score']

    # Map sentiment to bias for demo purposes
    if label == "positive":
        bias = "center"
    elif label == "negative":
        bias = "right"
    else:
        bias = "neutral"

    # Fake detection placeholder (you can add a real model or logic)
    fake = "No"
    return bias, fake