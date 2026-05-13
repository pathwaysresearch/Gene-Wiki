---
type: concept
aliases: [d-separation]
summary: A criterion for determining conditional independence relationships between variables in a directed graphical model (Bayesian Network) by analyzing paths in the graph.
relationships:
  - target: thomas-verma
    type: developed_by
  - target: do-calculus
    type: is_a_foundation_for
  - target: judea-pearl
    type: developed_by
  - target: bayesian-networks
    type: used_in
  - target: directed-probabilistic-model
    type: is_a_property_of
tags: [probabilistic-models, conditional-independence, bayesian-network]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# d-separation

## Definition
In the context of directed graphical models, d-separation (directional separation) is the rule used to determine if a set of variables A is conditionally independent of another set B, given a third set S. The independence holds if the graph structure implies it.

## Mechanism
Two variables are considered dependent if there is an "active path" between them; they are d-separated if no such active path exists. Determining whether a path is active in a directed graph is more complicated than in an undirected graph, as it depends on the direction of the arrows and whether intermediate nodes on the path are part of the conditioning set S.

## Scope and Limitations
d-separation is a powerful tool for reading conditional independences directly from the graph. However, it only identifies independences that are guaranteed by the graph structure. A specific probability distribution might contain additional independences that are not captured or implied by the graph's topology.

## Relationships

- **is_a_property_of**: [[directed-probabilistic-model|Directed Probabilistic Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*

---
*Also referenced in: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*