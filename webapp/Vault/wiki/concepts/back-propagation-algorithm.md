---
type: concept
aliases: [Back-Propagation Algorithm]
summary: An algorithm for efficiently computing gradients in a computational graph by applying the chain rule backwards from the output, avoiding redundant calculations by storing and reusing intermediate values.
relationships:
  - target: computational-graph
    type: operates_on
  - target: chain-rule
    type: based_on
  - target: gradient-descent
    type: provides_input_to
tags: [gradient-computation, automatic-differentiation, deep-learning, optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Back-Propagation Algorithm

## Definition and Core Principle
Back-propagation is an algorithm for computing gradients through a computational graph, based on the chain rule of calculus. The core idea is to apply the chain rule recursively, starting from the output and moving backwards through the graph to compute gradients for all inputs and parameters. For a chain of operations like z = f(f(f(w))), the gradient is calculated as f'(f(f(w))) * f'(f(w)) * f'(w). Back-propagation efficiently computes this by storing intermediate values like x = f(w) and y = f(x) to avoid recomputing them, which is a key advantage over naive differentiation.

## Implementation via Computational Graphs
Back-propagation operates on a computational graph that represents the function to be differentiated. It can be implemented using a "symbol-to-symbol" approach, where the algorithm adds new nodes to the graph that describe how to compute the derivatives, without needing specific numeric values initially. Each operation (e.g., matrix multiplication) in the graph is associated with a `bprop` (back-propagation) method. This method is responsible for computing the Jacobian-vector product for its inputs given the gradient on its output. For example, for C = AB, the `bprop` for A computes GB^T, where G is the gradient on C. The main algorithm simply calls these local `bprop` methods without needing to know the specific differentiation rules for the entire graph.

## Computational Efficiency
For the roughly chain-structured graphs common in deep networks, back-propagation has a computational cost of O(n) or O(# edges), where n is the number of nodes. This is significantly more efficient than a naive approach of applying the chain rule, which could have an exponential cost due to recomputing shared subexpressions. The number of computations for the gradient is guaranteed to be of the same order as the number of computations for the forward pass. After the gradients have been computed, an optimization algorithm like gradient descent uses them to update the model parameters.

## Relationships

- **operates_on**: [[computational-graph|Computational Graph]]
- **based_on**: [[chain-rule|Chain Rule]]
- **provides_input_to**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*