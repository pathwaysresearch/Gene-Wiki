---
type: concept
aliases: [Mean Squared Error]
summary: A cost function that measures the average squared difference between estimated values and actual values, derived from the maximum likelihood principle for a Gaussian output distribution.
relationships:
  - target: maximum-likelihood-estimation
    type: is_a_special_case_of
  - target: linear-unit
    type: is_used_with
tags: [cost-function, regression, optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Mean Squared Error

## Definition
The Mean Squared Error (MSE) cost function is given by J(θ) = (1/2) * E_{x, y ~ p_data} [||y - f(x; θ)||^2], plus a constant term that does not depend on the model parameters θ and is typically discarded. It quantifies the average squared difference between the model's predictions, f(x; θ), and the true target values, y.

## Probabilistic Interpretation
MSE is not an arbitrary choice of cost function; it arises directly from the principle of maximum likelihood estimation. Specifically, minimizing the MSE is equivalent to maximizing the log-likelihood of the data when the model's output distribution is assumed to be a Gaussian, p_model(y | x) = N(y; f(x; θ), I), where the model predicts the mean of the Gaussian.

## Application with Linear Units
The MSE cost function is often paired with linear output units in a neural network. Because linear units do not saturate, they are well-suited for gradient-based optimization algorithms used to minimize the MSE. This combination is a standard approach for regression problems where the target variable is assumed to follow a Gaussian distribution.

## Relationships

- **is_a_special_case_of**: [[maximum-likelihood-estimation|Maximum Likelihood Estimation]]
- **is_used_with**: [[linear-unit|Linear Unit]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*