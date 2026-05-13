---
type: concept
aliases: [Polynomial Features]
summary: A feature engineering technique used to model non-linear relationships with a linear model by adding powers of existing features as new features.
relationships:
  - target: linear-svc
    type: is_used_with
  - target: polynomial-regression
    type: is_a_concept_in
  - target: feature-engineering
    type: is_a_method_of
tags: [feature-engineering, non-linear-models, svm, scikit-learn]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Polynomial Features

## Purpose
The technique of adding polynomial features allows linear models, such as LinearSVC (a linear Support Vector Machine), to fit non-linear data. By creating new features that are powers or combinations of the original features, a dataset that is not linearly separable in its original feature space can become linearly separable in a higher-dimensional space.

## Implementation with Scikit-Learn
The text demonstrates how to implement this idea using a Scikit-Learn `Pipeline`. A typical pipeline for this purpose would consist of three steps: first, a `PolynomialFeatures` transformer to create the new features (e.g., of degree 3); second, a `StandardScaler` to scale all features; and third, a linear classifier like `LinearSVC` to fit the transformed data.

## Application Example
This technique is tested on the 'moons dataset', a toy dataset where data points are shaped as two interleaving half-circles, making them non-linearly separable. By applying a pipeline that includes `PolynomialFeatures`, a linear SVM classifier is able to learn a non-linear decision boundary that successfully separates the two classes.

## Relationships

- **is_used_with**: [[linear-svc|Linear Svc]]
- **is_a_concept_in**: [[polynomial-regression|Polynomial Regression]]
- **is_a_method_of**: [[feature-engineering|Feature Engineering]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*