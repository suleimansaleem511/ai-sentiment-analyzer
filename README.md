# 🧠 AI Sentiment Analysis Engine

An interactive, end-to-end Natural Language Processing (NLP) web application built to analyze sentiment, polarity, and subjectivity across unstructured text data (customer reviews, social media comments, product feedback).

Developed as part of my **Bachelor of Computer Science (Honours) in Artificial Intelligence** at **Taylor's University**.

---

## 🌟 Key Features

* **Real-time Sentiment Scoring:** Analyzes text inputs and computes compound polarity scores (-1.0 to +1.0) along with positive, neutral, and negative index percentages.
* **Subjectivity Detection:** Identifies whether text is objective factual content vs. subjective opinion using TextBlob.
* **Interactive Visualizations:** Dynamically generated sentiment breakdowns and polarity gauges powered by Plotly.
* **Batch CSV Processing:** Upload any CSV dataset to analyze hundreds of reviews in seconds, with automatic statistical summaries and distribution charts.
* **Exportable Reports:** Export analyzed data and classification results directly to CSV.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.12+
* **Frontend / UI:** [Streamlit](https://streamlit.io/)
* **NLP Frameworks:** 
  * [NLTK VADER](https://www.nltk.org/) (Valence Aware Dictionary and sEntiment Reasoner)
  * [TextBlob](https://textblob.readthedocs.io/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
* **Visual Analytics:** [Plotly Express & Graph Objects](https://plotly.com/python/)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/suleimansaleem511/ai-sentiment-analyzer.git
cd ai-sentiment-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run app.py
```
The app will open automatically in your browser at `http://localhost:8501`.

---

## 📸 Screenshots & Workflow
* **Single Text Mode:** Instant polarity gauge, emotional index, and breakdown.
* **Batch Mode:** Upload custom review spreadsheets, preview dataset, and download enriched sentiment labels.

---

## 👨‍💻 Author
**Suleiman Saleem**  
*Computer Science (AI Specialization) — Taylor's University*  
*Targeting Work-Based Learning (WBL) 2027*  
* GitHub: [@suleimansaleem511](https://github.com/suleimansaleem511)
