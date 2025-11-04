# ❓ Duplicate Question Detection Using Machine Learning

This project aims to build an intelligent system to detect whether two questions are duplicates — a common challenge in community Q&A platforms like **Quora**. By applying **Natural Language Processing (NLP)** techniques and **machine learning algorithms**, this model can identify semantically similar question pairs and prevent redundant content.

---

## 🚀 Project Overview

Millions of user-submitted questions often lead to duplicates. Identifying these automatically improves user experience and saves computational resources.

This notebook-based project walks through the end-to-end pipeline:
- Data loading and exploration
- Advanced text preprocessing
- Feature engineering on question pairs
- Model training and evaluation
- Model saving for deployment

---

## 📂 Dataset

### Dataset Link - https://www.kaggle.com/c/quora-question-pairs

The project uses a CSV file named `questions.csv`, containing the following columns:

| Column        | Description                          |
|---------------|--------------------------------------|
| `question1`   | First question in the pair           |
| `question2`   | Second question in the pair          |
| `is_duplicate`| Label: `1` if duplicate, `0` otherwise |

---

## 🧼 Text Preprocessing

Robust preprocessing is essential for meaningful text comparison. The pipeline includes:
- Lowercasing and trimming
- Replacing currency, symbols, and common phrases
- Removing HTML tags using `BeautifulSoup`
- Replacing large numeric values (e.g., "1000000" → "1m")
- Expanding contractions (e.g., "can't" → "cannot")
- (Optional) Removing stopwords, stemming/lemmatization *(can be added)*

---

## 🛠️ Feature Engineering

To compare two questions, the following features are extracted:

- Length-based features (word/char counts, common words)
- Fuzzy matching ratios
- Token-based similarity measures (Jaccard, cosine similarity)
- TF-IDF embeddings (if included)
- Distance metrics (e.g., Levenshtein, word mover’s distance)

---

## 🤖 Model Training

Machine learning models used may include:

- **XGBoost** – Gradient boosting framework for structured data
- **Random Forest** or other classifiers

The trained model is serialized using `joblib`

