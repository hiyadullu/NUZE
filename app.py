# app.py

from flask import Flask, render_template, request
from bias_pipeline import run_pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    query = request.form.get('query')
    df = run_pipeline(query=query)
    # Convert DataFrame to HTML table or process as needed
    return render_template('result.html', query=query, data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True)


