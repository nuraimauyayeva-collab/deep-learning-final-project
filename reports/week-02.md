# Week 02 Progress Report

Project: Fake News Detection using LSTM  
Date: Week 2

---

## What Was Completed This Week

### Text preprocessing pipeline

Implemented preprocessing for news articles:

- Lowercasing
- Removing punctuation
- Removing special symbols
- Removing numbers
- Basic regex cleaning

### Train/Test Split

Dataset split using sklearn train_test_split:

- Train: 80%
- Test: 20%

Random state fixed to 42 for reproducibility.

### TF-IDF Feature Extraction

Implemented TF-IDF vectorization:

- max_features=5000
- unigram features
- fit on train set only to avoid data leakage

### Baseline Model — Logistic Regression

Implemented Logistic Regression baseline model:

- Solver: default lbfgs
- max_iter=100

Model trained on TF-IDF vectors.

Notebook:
- notebooks/week2_baseline.ipynb

---

## Important Commits This Week

| Commit Message | Files Changed |
|---|---|
| add preprocessing | src/preprocessing.py |
| add TF-IDF vectorization | notebooks/week2_baseline.ipynb |
| add logistic regression baseline | src/baseline.py |
| add evaluation metrics | results/ |
| add week-02 report | reports/week-02.md |

---

## Baseline Results

| Model | Accuracy |
|---|---|
| Logistic Regression | ~0.99 |

### Key Observations

- Logistic Regression performs very well on TF-IDF features.
- Fake and real news contain strongly separable vocabulary patterns.
- TF-IDF representation works effectively for sparse text data.

---

## Problems / Blockers

- Large dataset increases preprocessing time.
- Some articles contain noisy formatting and repeated text.

---

## Plan for Week 3

- Implement LSTM model using PyTorch
- Create vocabulary and sequence encoding
- Add padding for variable-length sequences
- Train deep learning model
- Compare LSTM against baseline
