# Fake News Detection using Deep Learning
## Final Project for Applied Deep Learning

Student: Mauyayeva Nurai  


---

# About the Project

The goal of this project is to build and evaluate deep learning models for detecting fake news articles.

The task is formulated as a binary text classification problem:

- Fake News
- Real News

The project applies Natural Language Processing (NLP) techniques together with machine learning and deep learning models to classify news articles based on their textual content.

Several approaches were implemented and compared, including traditional machine learning baselines and recurrent neural networks.

The main deep learning architecture used in this project is Bidirectional LSTM.

---

# Repository Structure

This repository follows the structure below:

- data/ — Instructions for downloading the dataset.
- notebooks/ — Jupyter/Google Colab notebooks for EDA, preprocessing, training, and evaluation.
- src/ — Python source code for preprocessing, tokenization, model architectures, and evaluation utilities.
- reports/ — Weekly project reports and progress updates.
- results/ — Saved plots, model metrics, confusion matrices, and comparison charts.

---

# Dataset

The dataset used in this project is:

Fake and Real News Dataset

Dataset source:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Dataset files:

- Fake.csv
- True.csv

The dataset contains:

- News titles
- News article text
- Labels indicating whether the news is fake or real

Label mapping:

- 0 → Fake News
- 1 → Real News

---

# Project Workflow

The project was completed in several stages.

## Week 1 — Data Exploration & Preprocessing

Completed tasks:

- Dataset loading
- Exploratory Data Analysis (EDA)
- Label balancing
- Text cleaning
- Tokenization
- Basic visualization

Outputs generated:

- Dataset distribution charts
- Text preprocessing pipeline

---

## Week 2 — Baseline Models

Implemented baseline machine learning models:

- Logistic Regression
- MLP (Multi-Layer Perceptron)

Features used:

- TF-IDF vectors
- Unigrams and Bigrams

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-score

---

## Week 3 — Deep Learning Models

Implemented recurrent neural network architectures:

- Bidirectional LSTM
- Bidirectional GRU

Deep learning pipeline included:

- Vocabulary construction
- Integer encoding
- Sequence padding
- Embedding layers
- Training loop implementation
- Validation pipeline

Additional experiments:

- BERT evaluation
- Error analysis

---

## Week 4 — Final Evaluation

Final tasks completed:

- Aggregation of all model results
- Model comparison charts
- Heatmap visualization
- Error analysis
- Final evaluation report

Generated outputs:

- Comparison plots
- Confusion matrices
- Loss curves
- Final metrics table

---

# Models Used

## Baseline Models

- Logistic Regression
- MLP

## Deep Learning Models

- Bidirectional LSTM
- Bidirectional GRU
- BERT

---

# Technologies Used

- Python
- PyTorch
- Transformers (HuggingFace)
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Google Colab

---

# Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# Final Results

| Model | Accuracy | F1-score |
|---|---|---|
| Logistic Regression | ~0.86 | ~0.91 |
| MLP | ~0.87 | ~0.92 |
| BiLSTM | ~0.86 | ~0.92 |
| BiGRU | ~0.85 | ~0.92 |
| BERT | ~0.84 | ~0.91 |

Key observation:

Deep learning models demonstrated better contextual understanding of text compared to traditional TF-IDF baselines.

---

# Figures Generated

Saved outputs include:

- Model comparison charts
- Heatmaps
- Loss curves
- Confusion matrices

All generated outputs are stored in:

results/figures/

---

# How to Run the Project

## 1. Download Dataset

Download the dataset from Kaggle:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

---

## 2. Upload Dataset to Google Colab

Upload:

- Fake.csv
- True.csv

---

## 3. Run Notebooks

Run notebooks step by step:

- week2_baseline.ipynb
- week3_lstm.ipynb
- week4_final.ipynb

---

# Conclusion

This project demonstrates the effectiveness of deep learning methods for fake news detection tasks.

Recurrent neural networks such as BiLSTM and BiGRU improved contextual understanding of textual data, while transformer-based approaches provided additional semantic understanding at the cost of increased computational complexity.

The project highlights the importance of NLP preprocessing, sequence modeling, and evaluation techniques in text classification problems.

---
