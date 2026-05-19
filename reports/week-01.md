# Week 01 Progress Report

Project: Fake News Detection using LSTM  
Date: Week 1

---

## What Was Completed This Week

### Project Topic Selection

Selected the project topic:

- Fake News Detection using Deep Learning

The task is a binary text classification problem where the model predicts whether a news article is fake or real.

---

### Dataset Selection

Selected the Fake and Real News Dataset from Kaggle.

Dataset source:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Dataset contains:

- Fake news articles
- Real news articles

Files:
- Fake.csv
- True.csv

Total dataset size:
- Approximately 44,000 news articles

---

### Repository Setup

Created GitHub repository and initialized project structure.

Repository structure:

- README.md
- data/
- notebooks/
- src/
- reports/
- results/

---

### Exploratory Data Analysis (EDA)

Performed initial dataset analysis in Google Colab.

Implemented:

- Loading CSV files with pandas
- Dataset merging
- Label assignment
- Random shuffling
- Missing value inspection
- Text length analysis
- Class distribution analysis

Notebook:
- notebooks/week1_eda.ipynb

---

### Dataset Observations

Key observations from EDA:

- Dataset is relatively balanced between fake and real news classes.
- No major missing values were found.
- News article lengths vary significantly.
- Some articles contain noisy punctuation and formatting.

---

## Important Commits This Week

| Commit Message | Files Changed |
|---|---|
| add README | README.md |
| create repository structure | folders |
| add dataset instructions | data/README.md |
| upload week1 notebook | notebooks/week1_eda.ipynb |
| add week-01 report | reports/week-01.md |

---

## Figures Generated

Generated plots:

- Distribution of Fake vs Real News
- Distribution of Article Lengths

Saved in:
- results/

---

## Problems / Blockers

- Large dataset requires longer processing time.
- Google Colab session resets remove downloaded dataset files.
- Some articles contain inconsistent formatting.

---

## Plan for Week 2

- Implement text preprocessing pipeline
- Clean news article text
- Create train/test split
- Implement TF-IDF vectorization
- Train Logistic Regression baseline model
- Evaluate baseline performance
