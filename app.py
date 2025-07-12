from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
from bias_pipeline import run_pipeline
import datetime

app = Flask(__name__)
NEWSAPI_KEY = 'd2947d00f66247f8babd56f2da75f174'

def log_event(message):
    with open("backend_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

def get_bias_counts(articles):
    counts = {'left': 0, 'center': 0, 'right': 0, 'neutral': 0, 'fake': 0}
    for article in articles:
        bias = article.get('bias', '').lower()
        if bias in counts:
            counts[bias] += 1
    return counts

def mock_bias_detector(text):
    # TEMP bias detector, until model is plugged in
    if "modi" in text.lower():
        return "Right-Leaning"
    elif "opposition" in text.lower():
        return "Left-Leaning"
    else:
        return "Moderately Biased"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nuze')
def render_it():
    return render_template("nuze_website_original.html")

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    print("HIT /analyze route!")
    if request.method == 'GET':
        return redirect(url_for('home'))
    
    url = request.form.get('news_url')
    if not url:
        return render_template('result.html', result="No URL provided", articles=[], bias_counts={}, link="")

    # Step 1: Scrape article from the pasted URL
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        log_event(f"Scraped article from URL: {url}")
    except Exception as e:
        log_event(f"Failed to scrape article: {str(e)}")
        return render_template('result.html', result="Failed to fetch article", articles=[], bias_counts={}, link=url)

    # Step 2: Estimate bias of the scraped article
    original_bias = mock_bias_detector(content)

    # Step 3: Use article content as search query for NewsAPI
    search_query = ' '.join(content.split()[:10])  # Limit to 10 words to keep query tight
    params = {
        'q': search_query,
        'pageSize': 10,
        'apiKey': NEWSAPI_KEY
    }
    response = requests.get('https://newsapi.org/v2/everything', params=params)
    articles = response.json().get('articles', [])
    articles = run_pipeline(articles)  # Your AI-based bias detection pipeline
    bias_counts = get_bias_counts(articles)

    # 🧠 This is the "main result" used on top of result.html
    result = original_bias  

    # Step 4: Send all to result.html
    return render_template(
        'result.html',
        result=result,
        link=url,
        original_url=url,
        original_bias=original_bias,
        original_content=content[:1500],
        articles=articles,
        bias_counts=bias_counts
    )


if __name__ == '__main__':
    app.run(debug=True)
