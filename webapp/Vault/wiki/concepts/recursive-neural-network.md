---
type: concept
aliases: [Recursive Neural Network]
summary: A generalization of recurrent networks that operates on hierarchical, tree-structured data rather than linear sequences, applying the same set of weights recursively over the structure.
relationships:
  - target: recurrent-neural-network
    type: is-a-generalization-of
tags: [hierarchical-data, neural-networks, tree-structures]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Recursive Neural Network

## Definition and Structure
A Recursive Neural Network is a type of neural network designed to process data with a hierarchical or tree-like structure, representing a generalization of recurrent networks. Introduced by Pollack (1990), its computational graph is structured as a deep tree rather than the chain-like structure of an RNN. The same set of weights is applied recursively at each node of the tree to compute a representation of that node based on its children.

## Comparison with RNNs
The primary advantage of recursive networks over recurrent networks is their ability to handle long-term dependencies more effectively. For an input sequence of length `τ`, an RNN has a computational depth of `τ`. In contrast, a recursive network with a tree structure (such as a balanced binary tree) can drastically reduce this depth to `O(log τ)`. This reduction in the number of composed nonlinear operations can help mitigate issues like the vanishing gradient problem when modeling long-range dependencies.

## Applications and Open Questions
Recursive networks have been successfully applied in domains where data has an inherent tree structure, such as natural language processing (e.g., processing sentence parse trees) and computer vision. A key open question is how to best determine the tree structure for a given input. While in some domains external methods can suggest the structure, in others, a fixed structure like a balanced binary tree must be assumed.

## Relationships

- **is-a-generalization-of**: [[recurrent-neural-network|Recurrent Neural Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*