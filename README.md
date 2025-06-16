# NUZE: News Bias & Fake News Detector

**NUZE** is a web application that analyzes live news articles for **political bias** (Left, Center, Right, Neutral) and flags potential **fake news**.  
Users can search for any topic, and the app fetches recent articles, analyzes them, and presents the results in a **clean, visual dashboard**.

> ⚠️ **Note**: This is a prototype using simulated logic for bias and fake news classification. ML/NLP integration is planned in future versions.

---

## Features

- **Live News Search**  
  Enter a keyword to fetch fresh articles from NewsAPI in real time.

- **Bias & Fake News Detection**  
  Classifies each article by political bias and flags fake news (simulated with placeholder logic).

- **Interactive Dashboard**  
  Displays visual summaries using bar and doughnut charts, along with detailed tables.

- **Modern UI**  
  Responsive, intuitive frontend built for easy exploration of results.

---

## 🛠️ Tech Stack

| Layer         | Tools / Libraries                      |
|---------------|-----------------------------------------|
| **Frontend**  | HTML, CSS, JavaScript, Chart.js         |
| **Backend**   | Python, Flask                           |
| **API**       | [NewsAPI](https://newsapi.org/)         |
| **Visualization** | Chart.js (bar and doughnut charts)   |
| **Detection Logic** | Placeholder/randomized (prototype only) |

---

##  How It Works

1.  User types a query (e.g., `"climate change"`).
2.  NUZE fetches relevant articles using NewsAPI.
3.  Each article is analyzed for:
   - **Bias** → Left, Center, Right, Neutral
   - **Fake News** → Flagged if applicable  
   *(Currently, detection is based on randomized logic.)*
4. 📈 Results are presented using:
   - Summary cards
   - Interactive charts
   - Full article breakdown in a table

---

##  Project Structure

```bash
NUZE/
├── static/
│   ├── styles.css
│   └── dashboard.png  # (Optional: add a screenshot)
├── templates/
│   └── index.html
├── app.py
├── README.md
└── requirements.txt


