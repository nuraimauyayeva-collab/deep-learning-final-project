# Week 03 Progress Report

Project: Fake News Detection using LSTM  
Date: Week 3

---

## What Was Completed This Week

### Vocabulary Construction

Implemented vocabulary creation using training text data.

Steps completed:

- Tokenization using whitespace splitting
- Word frequency counting with Counter
- Integer encoding for vocabulary tokens

Vocabulary built only on training data to avoid data leakage.

---

### Sequence Encoding

Implemented sequence encoding pipeline:

- Convert words into integer token IDs
- Unknown words skipped
- Variable-length sequences created

---

### Sequence Padding

Implemented sequence padding using Keras pad_sequences.

Parameters:

- max_len = 100

Padding ensures all sequences have equal length for batch training.

---

### LSTM Model Architecture

Implemented LSTM neural network using PyTorch.

Architecture:

- Embedding Layer
- LSTM Layer
- Fully Connected Layer
- Sigmoid Activation

Hyperparameters:

- Embedding dimension: 128
- Hidden dimension: 128
- Batch size: 32
- Optimizer: Adam
- Learning rate: 0.001
- Loss function: Binary Cross Entropy Loss

Notebook:
- notebooks/week3_lstm.ipynb

---

### Model Training

Implemented full training loop:

- Forward pass
- Loss computation
- Backpropagation
- Optimizer step

Training performed for 1 epoch due to computational limitations in Google Colab CPU environment.

---

### Model Evaluation

Implemented evaluation pipeline on test data.

Metrics:

- Accuracy
- Predictions comparison

The LSTM model successfully learned fake vs real news patterns.

---

## Important Commits This Week

| Commit Message | Files Changed |
|---|---|
| add vocabulary encoding | src/preprocessing.py |
| add sequence padding | notebooks/week3_lstm.ipynb |
| implement LSTM model | src/model.py |
| add training loop | notebooks/week3_lstm.ipynb |
| add model evaluation | results/ |
| add week-03 report | reports/week-03.md |

---

## Model Results

| Model | Accuracy |
|---|---|
| LSTM | ~0.98 |

---

## Key Observations

- LSTM successfully captures sequential text information.
- Sequential modeling improves contextual understanding.
- Training on full dataset is computationally expensive on CPU.

---

## Problems / Blockers

- Long training time for LSTM on large dataset.
- High RAM usage during sequence padding.
- Google Colab CPU limitations slowed experimentation.

To reduce training time:

- Smaller dataset subset used
- max_len reduced to 100
- Epoch count reduced to 1

---

## Figures Generated

Generated outputs:

- Training loss logs
- Accuracy outputs

Saved in:
- results/

---

## Plan for Week 4

- Improve final evaluation
- Generate confusion matrix
- Save trained model
- Write final report
- Prepare project presentation
- Clean repository structure
