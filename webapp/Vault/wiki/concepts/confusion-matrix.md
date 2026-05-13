---
type: concept
aliases: [Confusion Matrix]
summary: A performance measurement tool for classification that summarizes the number of correct and incorrect predictions, broken down by each class (e.g., true positives, false positives).
tags: [classification, model-evaluation, error-analysis]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Confusion Matrix

## Definition
A confusion matrix is a table used to evaluate the performance of a classification algorithm. It provides a detailed breakdown of predictions, showing the number of true positives (TP), false positives (FP), true negatives (TN), and false negatives (FN). This gives more information than a simple accuracy score.

## How It Works
The matrix's rows typically represent the actual classes, while the columns represent the predicted classes. For a perfect classifier, all instances would lie on the main diagonal, meaning the number of false positives and false negatives would be zero. The off-diagonal cells show the errors, indicating where the classifier is 'confused'.

## Application in Error Analysis
The confusion matrix is a primary tool for error analysis, especially in multiclass classification. By analyzing the matrix, one can identify the specific types of errors a model makes. For example, it can reveal that a digit classifier frequently misclassifies the number '3' as '5', guiding efforts to improve the model by focusing on those specific, difficult cases.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*