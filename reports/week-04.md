Week 04 Progress Report

Project: Fake News Detection using LSTM
Date: Week 4

What Was Completed This Week
Final Model Evaluation

All previously trained models were evaluated and compared.

Models evaluated:

Logistic Regression
MLP
LSTM

Evaluation metrics:

Accuracy
Precision
Recall
F1-score

Results from all models were combined into one final table.

Results Aggregation

Created a pipeline for loading saved CSV result files:

baseline_results.csv
lstm_results.csv

Combined all metrics into:

results/all_model_results.csv

This allows easier comparison between traditional ML and deep learning models.

Model Comparison Visualization

Implemented comparison charts for all models.

Generated:

Bar chart comparing Accuracy and F1-score
Heatmap for all evaluation metrics

Saved figures:

results/figures/model_comparison.png
results/figures/results_heatmap.png

These visualizations help identify the strongest model.

Error Analysis

Implemented error analysis for model predictions.

Analysis included:

False Positives
False Negatives
Misclassified news samples

The model sometimes struggled with:

Very short news articles
Ambiguous headlines
Articles containing mixed factual and emotional language

Error analysis outputs saved in:

results/error_analysis.csv
Final Observations

Key findings:

LSTM outperformed baseline machine learning models.
Sequential learning improved contextual understanding.
Logistic Regression trained faster but captured less semantic information.
LSTM required more computation but produced better generalization.
Important Commits This Week
Commit Message	Files Changed
add final evaluation pipeline	notebooks/week4_final.ipynb
add model comparison charts	results/figures/
add heatmap visualization	results/figures/
add error analysis	results/error_analysis.csv
add all model results csv	results/all_model_results.csv
add week-04 report	reports/week-04.md
Final Model Results
Model	Accuracy	Precision	Recall	F1-score
Logistic Regression	~0.95	~0.95	~0.95	~0.95
MLP	~0.96	~0.96	~0.96	~0.96
LSTM	~0.98	~0.98	~0.98	~0.98
Figures Generated

Generated outputs:

model_comparison.png
results_heatmap.png
error_analysis.csv

Saved in:

results/
results/figures/
Problems / Blockers

Main limitations encountered:

Training deep learning models on CPU was slow.
Sequence padding increased RAM usage.
Google Colab session disconnects interrupted long experiments.

Solutions used:

Reduced dataset size
Reduced epoch count
Used shorter sequence length
Final Conclusion

The project successfully implemented fake news detection using both machine learning and deep learning approaches.

The LSTM model achieved the best performance because it captures sequential dependencies in text better than traditional models.

The project demonstrates the effectiveness of deep learning for NLP classification tasks.
