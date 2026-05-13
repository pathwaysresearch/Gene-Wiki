---
type: concept
aliases: [Maxout Unit]
summary: An activation unit that learns a piecewise linear, convex activation function by taking the maximum value from a group of linear filters.
tags: [neural-networks, activation-function, hidden-unit]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Maxout Unit

## Definition
A maxout unit is a type of hidden unit in a neural network that can learn a piecewise linear, convex function with up to a specified number of pieces, $k$. Unlike traditional units with fixed activation functions, maxout units can be seen as learning the activation function itself rather than just the relationship between units.

## How It Works
A maxout unit computes its output by taking the maximum value over a group of $k$ linear transformations of its input. Consequently, each maxout unit is parameterized by $k$ weight vectors instead of just one. With a sufficient number of pieces, a maxout unit can approximate any convex function with arbitrary fidelity. For example, a maxout layer with two pieces can learn to implement the same function as a rectified linear unit, an absolute value rectification unit, or a leaky ReLU, or it can learn a completely different function.

## Key Properties and Considerations
Because they are parameterized by multiple weight vectors per unit, maxout units typically require more regularization than simpler units like rectified linear units. However, they can perform well without regularization if the training set is large and the number of pieces per unit is kept low. The number of linear regions carved out by a maxout network grows exponentially with the depth of the network, contributing to its expressive power.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*