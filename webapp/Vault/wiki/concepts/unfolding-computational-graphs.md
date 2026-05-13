---
type: concept
aliases: [Unfolding Computational Graphs]
summary: A technique used to handle recurrent or recursive computations in models like RNNs by mapping a cyclical graph into a deep, acyclic graph with a repetitive structure and shared parameters.
relationships:
  - target: recurrent-neural-networks
    type: technique_for
tags: [deep-learning, neural-networks, rnn, computation-graph]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Unfolding Computational Graphs

## Definition
Unfolding is the operation that maps a computational graph with cycles, such as the circuit diagram of an RNN, into a deep computational graph that has a repetitive structure but no cycles. This process is a way to formalize the structure of a recurrent computation by creating a separate variable for each component at each point in time, effectively unrolling the recurrence into a chain of events.

## How It Works
A recurrent model can be drawn in two ways: as a circuit with a loop (indicating a delay of one time step) or as an unfolded computational graph. The unfolding process takes the circuit representation and expands it into a sequence of repeated components. Each component in the original circuit is replicated for each time step in the sequence, and the parameters of the model are shared across all these replicated pieces. The resulting unfolded graph has a size that is dependent on the length of the sequence being processed.

## Significance
By transforming a recurrent computation into a deep, feedforward-like structure, unfolding allows standard training algorithms like back-propagation to be applied. The unfolded recurrence after `t` steps can be represented by a single function `g(t)` that takes the entire input history up to that point (`x(1), ..., x(t)`) and computes the current state. This makes the flow of information and gradients explicit, which is essential for training recurrent models.

## Relationships

- **technique_for**: [[recurrent-neural-networks|Recurrent Neural Networks]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*