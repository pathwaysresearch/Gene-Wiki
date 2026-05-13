---
type: concept
aliases: [Gradient Descent]
summary: An optimization algorithm for finding a local minimum of a differentiable function by iteratively taking steps in the direction of the negative gradient. An iterative optimization algorithm for finding a local minimum of a differentiable function by repeatedly taking steps in the opposite direction of the gradient.
relationships:
  - target: newtons-method
    type: is_contrasted_with
  - target: linear-regression
    type: is_used_to_train
  - target: machine-learning
    type: is_a_technique_in
  - target: linear-regression
    type: is_training_method_for
  - target: stochastic-gradient-descent
    type: has_variant
  - target: feature-scaling
    type: requires
  - target: learning-rate
    type: has_hyperparameter
  - target: hill-climbing-search
    type: is-a-continuous-version-of
  - target: multivariate-linear-regression
    type: used_in
tags: [optimization, calculus, machine-learning, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Gradient Descent

## Definition
Gradient descent is an optimization algorithm used to find the local minimum of a function by iteratively moving in the direction of the negative gradient. The text discusses its counterpart, steepest-ascent hill climbing, which finds a local maximum by moving in the direction of the positive gradient. For a differentiable objective function $f(x)$, the update rule for steepest ascent is given as $x \leftarrow x + \alpha \nabla f(x)$, where $\alpha$ is the step size and $\nabla f(x)$ is the gradient.

## Step Size and Line Search
A critical parameter in the algorithm is the **step size**, $\alpha$. If $\alpha$ is too small, the search requires too many steps to converge; if it is too large, the search can overshoot the maximum and fail to converge. The technique of **line search** addresses this by dynamically adjusting $\alpha$. It extends the search along the current gradient direction, often by repeatedly doubling $\alpha$, until the objective function value starts to decrease again, thereby finding a more optimal step size for that iteration.

## Empirical Gradient
When the objective function is not available in a differentiable form, an **empirical gradient** can be calculated instead. This is done by evaluating the function's response to small increments and decrements in each coordinate of the state space. A search using an empirical gradient is equivalent to performing steepest-ascent hill climbing in a discretized version of the state space.

## Relationships

- **is-a-continuous-version-of**: [[hill-climbing-search|Hill Climbing Search]]
- **used_in**: [[multivariate-linear-regression|Multivariate Linear Regression]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*