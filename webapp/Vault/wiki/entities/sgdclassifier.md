---
type: entity
aliases: [SGDClassifier]
summary: A Scikit-Learn classifier that implements regularized linear models with stochastic gradient descent (SGD) learning.
relationships:
  - target: scikit-learn
    type: is_part_of
  - target: gradient-descent
    type: uses
tags: [scikit-learn, classifier, linear-model]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# SGDClassifier

## Overview
The `SGDClassifier` is a specific classifier model from the Scikit-Learn library that is used as a running example in the text. It is a linear model that is trained using the Stochastic Gradient Descent optimization algorithm.

## Performance and Evaluation
The text demonstrates how to evaluate the `SGDClassifier` using cross-validation, showing an accuracy of over 84% on the digit classification task. It is also shown that its performance can be significantly improved by preprocessing the inputs, such as by using Scikit-Learn's `StandardScaler`, which increases accuracy to above 89%.

## Limitations
As a linear model, the `SGDClassifier` has inherent limitations. The text's error analysis reveals that it makes mistakes that seem obvious to a human, such as confusing certain handwritten '3's and '5's. This is because a simple linear model struggles to separate classes when the decision boundary is complex and non-linear.

## Relationships

- **is_part_of**: [[scikit-learn|Scikit Learn]]
- **uses**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*