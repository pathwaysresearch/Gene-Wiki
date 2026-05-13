---
type: concept
aliases: [SVM Regression]
summary: An application of Support Vector Machines for regression tasks, which aims to fit as many instances as possible within a specified margin while limiting margin violations.
relationships:
  - target: support-vector-machine
    type: is_an_application_of
  - target: scikit-learn
    type: is_implemented_in
tags: [regression, supervised-learning, svm]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# SVM Regression

## Core Principle: ε-Insensitivity
The model's predictions are not affected by adding more training instances that fall within the margin defined by the hyperparameter ε. This property is known as ε-insensitivity. The width of this margin or "street" is controlled by ε.

## Linear and Nonlinear Tasks
For linear regression tasks, Scikit-Learn’s `LinearSVR` class can be used. To tackle nonlinear regression tasks, a kernelized SVM model can be employed. For example, a 2nd-degree polynomial kernel can be used to fit a quadratic training set.

## Regularization
The hyperparameter `C` controls the trade-off between the model's complexity and the number of margin violations. A large `C` value corresponds to little regularization, allowing the model to fit the training data more closely. A small `C` value results in much more regularization, leading to a smoother model that may tolerate more errors.

## Relationships

- **is_an_application_of**: [[support-vector-machine|Support Vector Machine]]
- **is_implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*