---
type: concept
aliases: [Computational Graph]
summary: A formal representation of a computation as a directed graph, where nodes represent variables and edges represent operations, used to precisely describe algorithms like back-propagation. A data structure representing a mathematical computation as a directed graph, where nodes are variables or operations and edges represent the flow of data. It is the foundation for automatic differentiation algorithms like back-propagation.
relationships:
  - target: back-propagation-algorithm
    type: enables
tags: [neural-networks, back-propagation, automatic-differentiation, data-structure, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Computational Graph

## Definition
A computational graph is a formal language used to describe a computation as a directed graph. In this formalism, each node in the graph represents a variable, which can be a scalar, vector, matrix, tensor, or another data type.

## Components and Structure
The graph consists of nodes (variables) and directed edges that represent operations. An operation is a simple function of one or more variables that returns a single output variable. If a variable $y$ is computed by applying an operation to a variable $x$, a directed edge is drawn from the node for $x$ to the node for $y$. More complex functions are described by composing many simple operations together in the graph structure.

## Purpose in Deep Learning
Computational graphs provide a precise and structured framework for describing complex computations, such as the forward pass of a neural network. They are particularly essential for formalizing and implementing the back-propagation algorithm, which calculates gradients by traversing the graph and applying the chain rule at each node.

## Relationships

- **enables**: [[back-propagation-algorithm|Back Propagation Algorithm]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*