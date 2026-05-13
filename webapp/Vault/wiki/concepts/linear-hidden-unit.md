---
type: concept
aliases: [Linear Hidden Unit]
summary: A hidden unit in a neural network that uses the identity function as its activation, performing a purely linear transformation, often to reduce parameters.
tags: [neural-networks, hidden-unit, network-architecture, parameter-reduction]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Linear Hidden Unit

## Definition
A linear hidden unit is a unit within a neural network that does not apply a nonlinear activation function, effectively using the identity function for its activation. While a network composed entirely of linear units is equivalent to a single linear transformation, incorporating linear units in some hidden layers can be a useful architectural choice.

## Factored Approach for Parameter Reduction
Linear hidden units enable an effective method for reducing the number of parameters in a network through factorization. A layer with a large weight matrix $W$ (containing $np$ parameters for $n$ inputs and $p$ outputs) can be replaced by two sequential layers. The first is a linear hidden layer with a smaller weight matrix $U$ producing $q$ outputs, followed by a second layer with weight matrix $V$. This factored approach uses only $(n + p)q$ parameters, which can be a significant saving for a small intermediate dimension $q$.

## Benefits and Constraints
The primary benefit of using linear hidden units in a factored architecture is the reduction in the network's parameter count. This comes at the cost of constraining the layer's linear transformation to be low-rank, as the rank of the effective weight matrix is at most $q$. However, these low-rank relationships are often sufficient for many tasks, making this an effective strategy.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*