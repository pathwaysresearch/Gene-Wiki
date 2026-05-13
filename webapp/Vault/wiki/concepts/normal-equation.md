---
type: concept
aliases: [Normal Equation]
summary: A closed-form mathematical equation that directly computes the optimal parameters to minimize the cost function in a Linear Regression model.
relationships:
  - target: linear-regression
    type: is_training_method_for
tags: [linear-regression, optimization, closed-form-solution]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Normal Equation

## Definition
The Normal Equation is a closed-form solution for finding the value of the parameter vector $\boldsymbol{\theta}$ that minimizes the cost function in a linear regression model. Unlike iterative methods, it is a mathematical equation that provides the result directly without requiring multiple steps of optimization.

## The Equation
The Normal Equation is expressed as $\hat{\boldsymbol{\theta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$. In this formula, $\hat{\boldsymbol{\theta}}$ represents the value of the parameter vector $\boldsymbol{\theta}$ that minimizes the cost function, $\mathbf{X}$ is the matrix of input features (with a bias term added), and $\mathbf{y}$ is the vector of target values for the training instances.

## Computational Complexity
The Normal Equation's primary computational bottleneck is the inversion of the $\mathbf{X}^T \mathbf{X}$ matrix. This operation makes it very slow when the number of features grows large (e.g., 100,000). However, the algorithm's complexity is linear with regard to the number of instances in the training set ($O(m)$), which means it can handle large training sets efficiently, provided they can fit into memory.

## Relationships

- **is_training_method_for**: [[linear-regression|Linear Regression]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*