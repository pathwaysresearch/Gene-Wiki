---
type: concept
aliases: [Logistic Regression]
summary: A classification algorithm that fits the weights of a model using a logistic function to minimize loss on a dataset, typically through gradient descent.
relationships:
  - target: log-loss
    type: uses
  - target: decision-boundary
    type: has
  - target: classification
    type: is_a_method_for
  - target: activation-function
    type: uses
tags: [classification, linear-models, gradient-descent]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Logistic Regression

## Definition
Logistic regression is the process of fitting the weights of a classification model to minimize a loss function on a given dataset. The model's hypothesis function, `h_w(x)`, uses a logistic function (also called a sigmoid function) to map the weighted sum of inputs to a probability-like output.

## Optimization Method
The text states that there is no easy closed-form solution to find the optimal weight vector `w` for this model. Therefore, iterative optimization methods like gradient descent are used to find the weights that minimize the loss. The learning rule is applied to update the weights based on the gradient of the loss function.

## Gradient Calculation
To perform gradient descent, the partial derivative of the loss function with respect to each weight is calculated. The text provides a derivation for a single example `(x, y)` using an L2 loss function and the chain rule, resulting in the update rule: `∂Loss(w)/∂w_i = -2(y - h_w(x)) * g'(w . x) * x_i`, where `g` is the logistic function and `g'` is its derivative.

## Relationships

- **uses**: [[activation-function|Activation Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*