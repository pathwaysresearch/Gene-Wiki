---
type: concept
aliases: [Gaussian RBF Kernel]
summary: A popular kernel function for Support Vector Machines that can handle complex, nonlinear relationships by measuring similarity based on a bell-shaped curve.
relationships:
  - target: kernel-trick
    type: is_an_application_of
  - target: support-vector-machine
    type: is_used_with
tags: [svm, kernel-methods, hyperparameter]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Gaussian RBF Kernel

## Definition
The Gaussian Radial Basis Function (RBF) kernel is a function defined as K(a, b) = exp(-γ||a - b||²). It can be used with SVMs to achieve a result similar to adding many similarity features, but without the computational cost, by applying the kernel trick.

## How It Works
The kernel function creates a bell-shaped curve around each instance. The `gamma` (γ) hyperparameter controls the width of this curve. A large gamma value makes the curve narrower, giving each instance a smaller range of influence and leading to a more irregular, complex decision boundary. Conversely, a small gamma value makes the curve wider, giving instances a larger range of influence and resulting in a smoother decision boundary.

## Role as a Regularizer
The `gamma` hyperparameter acts as a regularization hyperparameter, similar to the `C` hyperparameter. If a model is overfitting the training data, gamma should be reduced. If it is underfitting, gamma should be increased to make the model more flexible.

## Relationships

- **is_an_application_of**: [[kernel-trick|Kernel Trick]]
- **is_used_with**: [[support-vector-machine|Support Vector Machine]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*