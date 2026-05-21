# Deep Learning Final Project
## Fake News Detection using Deep Learning

Author: Nurai Mauyaeva

---

# Project Overview

The goal of this project is to classify news articles as:

- Fake News
- Real News

Several machine learning and deep learning models were implemented and compared, including:

- Logistic Regression
- MLP (Multi-Layer Perceptron)
- Bidirectional LSTM
- Bidirectional GRU
- BERT

The project evaluates how sequential neural networks and transformer-based models perform on text classification tasks.

---

# Dataset

Dataset used:

Fake and Real News Dataset

Files:

- Fake.csv
- True.csv

Dataset contains:

- News title
- News text
- Labels:
  - 0 = Fake
  - 1 = Real

---

# Project Structure

```text
deep-learning-final-project/
│
├── notebooks/
│   ├── week2_baseline.ipynb
│   ├── week3_lstm.ipynb
│   └── week4_final.ipynb
│
├── reports/
│   ├── week-01.md
│   ├── week-02.md
│   ├── week-03.md
│   └── week-04.md
│
├── results/
│   ├── baseline_results.csv
│   ├── lstm_results.csv
│   ├── bert_results.csv
│   ├── all_model_results.csv
│   ├── error_analysis.csv
│   │
│   └── figures/
│       ├── model_comparison.png
│       ├── results_heatmap.png
│       ├── bilstm_loss_curve.png
│       ├── bigru_loss_curve.png
│       └── bert_confusion.png
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   ├── evaluate.py
│   └── bert_model.py
│
├── README.md
└── requirements.txt
