# app.py

import requests
from flask import Flask, render_template, request, jsonify
from bias_pipeline import run_pipeline
import datetime

app = Flask(__name__)

NEWSAPI_KEY = 'd2947d00f66247f8babd56f2da75f174'  # Replace with your actual key

def log_event(message):
    with open("backend_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    query = request.form.get('query')
    print("Query received:", query)
    if not query:
        return render_template('result.html', query="No query provided", articles=[])
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'pageSize': 5,
        'apiKey': NEWSAPI_KEY
    }
    response = requests.get(url, params=params)
    print("NewsAPI raw response:", response.text)
    articles = response.json().get('articles', [])
    articles = run_pipeline(articles)  # Now returns list of dicts
    return render_template('result.html', query=query, articles=articles)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    query = data.get('query')
    log_event(f"Received query: {query}")
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'pageSize': 5,
        'apiKey': NEWSAPI_KEY
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    log_event(f"Fetched {len(articles)} articles from NewsAPI")
    df = run_pipeline(articles)
    # Convert DataFrame to list of dicts for JSON response
    return jsonify({'results': df.to_dict(orient='records')})

if __name__ == '__main__':
    app.run(debug=True)


