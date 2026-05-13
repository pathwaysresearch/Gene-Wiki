---
type: concept
aliases: [Clustering (in Bayesian Networks)]
summary: A technique for exact inference in Bayesian networks that transforms a multiply connected network into a singly connected one (a polytree) by grouping variables into cluster nodes.
relationships:
  - target: bayesian-network
    type: is-used-for
  - target: singly-connected-network
    type: produces
tags: [bayesian-networks, exact-inference, algorithm, join-tree]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Clustering (in Bayesian Networks)

## Definition
Clustering, also known as the join tree algorithm, is an inference technique that converts a multiply connected Bayesian network into a polytree structure. It achieves this by joining individual nodes to form larger cluster nodes, or "meganodes."

## How It Works
The process involves identifying nodes that form loops in the network's undirected graph and combining them into a single meganode. For example, two Boolean parent nodes like *Sprinkler* and *Rain* could be combined into a single *Sprinkler+Rain* node with four possible values. This restructuring eliminates the loop, resulting in a polytree. Once the network is in this form, a special-purpose inference algorithm, which works by ensuring neighboring meganodes agree on the posterior probabilities of shared variables, can be applied.

## Complexity and Trade-offs
After clustering, inference can be performed in time linear in the size of the new, clustered network. However, this does not eliminate the inherent NP-hardness of the problem. The complexity can manifest in the clustering step itself, as the meganodes can have an exponentially large number of states, leading to exponential time and space requirements for networks that were difficult to begin with.

## Relationships

- **is-used-for**: [[bayesian-network|Bayesian Network]]
- **produces**: [[singly-connected-network|Singly Connected Network]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*