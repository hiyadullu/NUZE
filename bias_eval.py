import pandas as pd
import random

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
    # Dummy logic: randomly assign bias/fake
    biases = ['left', 'center', 'right', 'neutral', 'fake']
    bias = random.choice(biases)
    fake = 'Yes' if bias == 'fake' else 'No'
    return bias, fake