---
type: concept
aliases: [Polynomial Regression]
summary: A regression model that models the relationship between variables as an nth degree polynomial, allowing it to fit non-linear datasets. A technique that allows a linear model to fit non-linear data by adding powers of each feature as new features to the dataset.
relationships:
  - target: linear-regression
    type: is_an_extension_of
  - target: linear-regression
    type: extends
tags: [regression, machine-learning-model, overfitting, feature-engineering, non-linear-modeling]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Polynomial Regression

## Overview
Polynomial Regression is a more complex model than Linear Regression that is capable of fitting non-linear datasets. It extends the linear model by adding powers of the original features as new features, creating a polynomial relationship between the inputs and the output.

## Overfitting Risk
Because Polynomial Regression has more parameters than a simple Linear Regression model, it is more flexible and can capture more complex patterns. However, this increased complexity also makes it more prone to overfitting the training data, meaning it may perform well on the data it was trained on but poorly on new, unseen data.

## Detecting and Mitigating Overfitting
To determine if a Polynomial Regression model is overfitting, one can use tools like learning curves. To reduce the risk of overfitting, several regularization techniques can be applied during the model training process.

## Relationships

- **is_an_extension_of**: [[linear-regression|Linear Regression]]
- **extends**: [[linear-regression|Linear Regression]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*