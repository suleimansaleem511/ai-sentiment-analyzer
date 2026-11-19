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

## 🛠️ Architecture & How It Works

This application uses a **Lexicon and Rule-Based Natural Language Processing (NLP)** architecture powered by **NLTK VADER** and **TextBlob**, rather than a trained neural network.

### Why VADER Lexicon?
* **Lexical Knowledge Base:** VADER relies on an extensively validated sentiment lexicon of over 7,500 human-annotated sentiment ratings (tokens, emojis, slang, acronyms).
* **Heuristic Rules:** It applies grammatical heuristics including:
  * **Negation handling:** Flips polarity (e.g., *"not good"*).
  * **Punctuation & Capitalization:** Boosts sentiment intensity (e.g., *"GREAT!"* vs *"great"*).
  * **Degree modifiers / intensifiers:** Increases or dampens valence (e.g., *"extremely bad"* vs *"barely bad"*).
* **TextBlob Subjectivity:** Computes a subjectivity score from `0.0` (purely objective fact) to `1.0` (purely subjective opinion).

---

## 👨‍💻 Author
**Suleiman Saleem**  
*Computer Science (AI Specialization) — Taylor's University*  
* GitHub: [@suleimansaleem511](https://github.com/suleimansaleem511)
