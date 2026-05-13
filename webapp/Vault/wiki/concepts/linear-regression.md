---
type: concept
aliases: [Linear Regression]
summary: One of the simplest and most commonly used Machine Learning techniques, often serving as an introductory example in the field. A simple statistical model that assumes a linear relationship between input features and a single, continuous output variable. A machine learning model that predicts a target value based on a linear combination of input features, plus a constant bias term.
relationships:
  - target: supervised-learning
    type: is_type_of
  - target: bias-parameter
    type: uses
  - target: model-capacity
    type: is_example_of
  - target: machine-learning
    type: is_a_technique_of
  - target: gradient-descent
    type: can_be_trained_with
  - target: normal-equation
    type: can_be_trained_with
  - target: polynomial-regression
    type: is_extended_by
  - target: ridge-regression
    type: has_regularized_version
tags: [machine-learning, regression, statistics, machine-learning-model, supervised-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Linear Regression

## Overview
Linear Regression is a fundamental Machine Learning technique. It is cited in the text as an example of one of the "simplest and most commonly used" methods that the book covers.

## Role in Learning
Due to its simplicity, Linear Regression serves as a foundational topic for those new to Machine Learning. The book's table of contents shows it as the first modeling technique discussed in the "Training Models" chapter.

## Associated Concepts
The discussion of Linear Regression in the table of contents is followed by related concepts such as the Normal Equation for solving it directly, Gradient Descent methods for optimizing it, and extensions like Polynomial Regression and regularized models such as Ridge Regression, Lasso Regression, and Elastic Net.

## Relationships

- **is_a_technique_of**: [[machine-learning|Machine Learning]]
- **can_be_trained_with**: [[gradient-descent|Gradient Descent]]
- **can_be_trained_with**: [[normal-equation|Normal Equation]]
- **is_extended_by**: [[polynomial-regression|Polynomial Regression]]
- **has_regularized_version**: [[ridge-regression|Ridge Regression]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*