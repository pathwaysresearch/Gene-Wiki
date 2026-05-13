---
type: concept
aliases: [Back-Propagation]
summary: An algorithm for training multi-layer neural networks by iteratively adjusting weights based on error gradients calculated by propagating errors backward from the output layer.
relationships:
  - target: feedforward-network
    type: used_to_train
  - target: computational-graph
    type: uses
  - target: artificial-neural-network
    type: is-a-training-method-for
tags: [neural-networks, training-algorithm, gradient-descent, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Back-Propagation

## Algorithm Overview
Back-propagation is a supervised learning algorithm used to train multi-layer neural networks. It works by minimizing the network's error on a set of training examples through gradient descent. The algorithm consists of a forward pass to compute outputs and a backward pass to compute error gradients, or deltas.

## Forward and Backward Passes
In the forward pass, an input example is fed into the network, and activations are propagated forward layer by layer to compute the final output. In the backward pass, the error at the output layer is calculated (`Δ[j] ← g'(in_j) × (y_j - a_j)`). This error is then propagated backward through the network, allowing the error contribution (delta) of each node in the preceding layers to be calculated recursively.

## Weight Updates
After the backward pass, every weight in the network is updated to reduce the error. The update for a weight `w_ij` is proportional to the input activation `a_i` from the sending node and the error delta `Δ[j]` of the receiving node, scaled by a learning rate `α`. This process is repeated for all examples, often over many epochs, until the network converges.

## Relationships

- **is-a-training-method-for**: [[artificial-neural-network|Artificial Neural Network]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*