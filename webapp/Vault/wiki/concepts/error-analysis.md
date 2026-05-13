---
type: concept
aliases: [Error Analysis]
summary: A process in the machine learning workflow for improving a model by analyzing the types of errors it makes on the training or validation data.
relationships:
  - target: confusion-matrix
    type: uses
tags: [model-improvement, machine-learning-workflow, debugging]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Error Analysis

## Purpose
Error analysis is a method for improving a machine learning model after an initial promising version has been developed. Instead of blindly trying different models or hyperparameters, this process involves analyzing the types of errors the current model makes to gain insights that can guide further improvements.

## Key Techniques
A primary tool for error analysis is the confusion matrix. By inspecting the confusion matrix, especially in a multiclass setting, you can identify which classes are frequently confused with one another. For example, an analysis might show that a digit classifier often misclassifies '3's as '5's.

## Gaining Deeper Insights
Beyond the confusion matrix, error analysis often involves looking at the specific data instances that the classifier gets wrong. This can reveal underlying patterns. For example, it might show that a simple linear model like `SGDClassifier` fails on inputs that are badly written or require non-linear decision boundaries, suggesting that a more complex model or better data preprocessing is needed.

## Relationships

- **uses**: [[confusion-matrix|Confusion Matrix]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*