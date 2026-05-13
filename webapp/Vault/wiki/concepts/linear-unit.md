---
type: concept
aliases: [Linear Unit]
summary: An output unit in a neural network that produces an unconstrained real-valued output, suitable for regression tasks where the target is modeled by a Gaussian distribution.
relationships:
  - target: mean-squared-error
    type: is_used_with
tags: [output-unit, regression, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Linear Unit

## Definition and Use
A linear unit is a type of output unit in a neural network that does not apply a non-linearity to its input. It is typically used to produce the parameters of a conditional distribution. For example, when modeling a conditional Gaussian distribution p(y | x), a linear unit can be used to produce the mean of the Gaussian.

## Key Properties
The primary characteristic of linear units is that they do not saturate. Unlike sigmoid or softmax units that are constrained to a specific range, linear units can produce any real value. This makes them suitable for tasks where the target variable is unbounded.

## Optimization Characteristics
Because they do not saturate, linear units pose little difficulty for gradient-based optimization algorithms. Their gradients are constant and do not vanish, which facilitates effective training. As a result, they can be used with a wide variety of optimization algorithms for tasks like regression where the goal is to minimize mean squared error.

## Relationships

- **is_used_with**: [[mean-squared-error|Mean Squared Error]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*