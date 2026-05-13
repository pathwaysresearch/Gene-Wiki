---
type: concept
aliases: [Rectified Linear Unit]
summary: An activation function defined as g(z) = max{0, z} that introduces non-linearity, allowing neural networks to learn more complex functions like XOR. A piecewise linear activation function defined as max(0, z) that has become a standard choice for hidden units in deep feedforward networks, often replacing sigmoid units.
relationships:
  - target: deep-feedforward-network
    type: component_of
  - target: sigmoid-function
    type: alternative_to
tags: [activation-function, neural-networks, hidden-unit, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Rectified Linear Unit

## Definition
A Rectified Linear Unit, or ReLU, is a type of hidden unit in a neural network that uses the activation function g(z) = max{0, z}. This function is also referred to as a rectified linear transformation. It is non-linear, outputting zero for any negative input and the input value itself for any non-negative input.

## Role in Non-Linear Transformations
The non-linearity introduced by ReLU is crucial for the expressive power of deep networks. For problems like XOR, where the examples are not linearly separable, a linear model cannot find a solution. By applying a rectified linear transformation to the outputs of a hidden layer, the relationship between the examples is changed, projecting them into a new space where a subsequent linear model can solve the problem.

## Properties for Gradient-Based Learning
While the rectified linear function is not differentiable at z = 0, it is suitable for use with gradient-based learning algorithms. The function has a defined left derivative (0) and right derivative (1) at z = 0. In practice, neural network training algorithms do not usually arrive at a precise local minimum where the gradient is exactly zero, but rather significantly reduce the cost function's value. Therefore, it is acceptable for the minima of the cost function to correspond to points with an undefined gradient, and gradient descent performs well enough for these models to be used effectively.

## Relationships

- **component_of**: [[deep-feedforward-network|Deep Feedforward Network]]
- **alternative_to**: [[sigmoid-function|Sigmoid Function]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*