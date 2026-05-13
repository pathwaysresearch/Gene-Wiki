---
type: concept
aliases: [Singly Connected Network (Polytree)]
summary: A type of Bayesian network in which there is at most one undirected path between any two nodes, allowing for more efficient exact inference algorithms.
relationships:
  - target: bayesian-network
    type: is-a-type-of
  - target: clustering-in-bayesian-networks
    type: is-goal-of
tags: [bayesian-networks, network-structure, probabilistic-models]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Singly Connected Network (Polytree)

## Definition
A singly connected network, also known as a polytree, is a Bayesian network that has at most one undirected path between any two nodes in the network graph. This structural property distinguishes it from multiply connected networks, which contain loops in their undirected graph structure.

## Properties for Inference
The primary significance of polytrees is that they permit highly efficient exact inference. The time and space complexity of inference algorithms on singly connected networks is significantly lower than for general, multiply connected networks, for which the problem is NP-hard.

## Role in Other Algorithms
The desirable computational properties of polytrees make them a target structure for other, more complex inference algorithms. For example, the clustering algorithm explicitly transforms a multiply connected network into a polytree by grouping variables into cluster nodes, thereby enabling the use of specialized, efficient inference methods on the transformed structure.

## Relationships

- **is-a-type-of**: [[bayesian-network|Bayesian Network]]
- **is-goal-of**: [[clustering-in-bayesian-networks|Clustering In Bayesian Networks]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*