---
type: concept
aliases: [Factor Graph]
summary: A bipartite graphical model that explicitly represents the factorization of a probability distribution, resolving ambiguities present in standard undirected graphs.
relationships:
  - target: undirected-probabilistic-model
    type: is_a_representation_of
tags: [probabilistic-models, graphical-models, representation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Factor Graph

## Definition
A factor graph is a graphical representation of an undirected model that explicitly clarifies how the unnormalized probability distribution is factorized. It consists of a bipartite graph with two types of nodes: variable nodes (typically drawn as circles) and factor nodes (typically drawn as squares).

## Structure
In a factor graph, edges only exist between variable nodes and factor nodes. A variable is connected to a factor if and only if that variable is an argument to the corresponding factor function (φ) in the unnormalized probability distribution. There are no direct connections between variables or between factors.

## Purpose and Ambiguity Resolution
The primary purpose of a factor graph is to resolve ambiguity. A standard undirected graph with a three-node clique, for example, does not specify whether the distribution factorizes over one function of all three variables or three pairwise functions. A factor graph makes this explicit by using either one factor node connected to all three variables or three separate factor nodes connected to each pair.

## Relationships

- **is_a_representation_of**: [[undirected-probabilistic-model|Undirected Probabilistic Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*