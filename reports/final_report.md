# Final Report
## Fake News Detection using Deep Learning

Student: Mauyayeva Nurai

---

# 1. Project Goal

The goal of this project was to build a machine learning and deep learning system capable of detecting fake news articles automatically.

The project compares traditional machine learning methods with deep learning approaches for text classification.

---

# 2. Dataset

Dataset used:

Fake and Real News Dataset

Files:
- Fake.csv
- True.csv

The dataset contains news articles labeled as fake or real.

---

# 3. Data Preprocessing

The following preprocessing steps were applied:

- Lowercasing
- URL removal
- Punctuation removal
- Text cleaning
- Tokenization
- Sequence encoding
- Padding sequences

---

# 4. Exploratory Data Analysis

EDA included:

- Dataset size analysis
- Class distribution visualization
- Word frequency analysis
- Text length analysis

---

# 5. Baseline Model

A Logistic Regression model was trained using TF-IDF features.

Results:
- Accuracy: ~0.91
- F1-score: ~0.91

The baseline model performed well on sparse text features.

---

# 6. Deep Learning Model

An LSTM model was implemented using PyTorch.

Architecture:
- Embedding Layer
- LSTM Layer
- Fully Connected Layer

Hyperparameters:
- Embedding dimension: 128
- Hidden dimension: 128
- Batch size: 32
- Optimizer: Adam

---

# 7. Model Training

The model was trained using Binary Cross Entropy Loss.

Training included:
- Forward pass
- Backpropagation
- Optimizer updates

---

# 8. Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# 9. Results

| Model | Accuracy | F1-score |
|------|------|------|
| Logistic Regression | 0.91 | 0.91 |
| LSTM | 0.98 | 0.98 |

The LSTM model outperformed the baseline model.

---

# 10. Problems Encountered

Several challenges occurred during the project:

- Long training time on CPU
- High RAM usage
- File loading issues in Google Colab

To reduce training time:
- Smaller dataset subset was used
- Sequence length was reduced

---

# 11. Conclusion

The project demonstrated that deep learning models can successfully classify fake and real news articles.

Sequential models such as LSTM capture contextual information better than traditional machine learning approaches.

---

# 12. Future Improvements

Future work may include:

- Using BERT transformers
- Hyperparameter tuning
- Larger datasets
- Attention mechanisms
- Deploying the model as a web application
