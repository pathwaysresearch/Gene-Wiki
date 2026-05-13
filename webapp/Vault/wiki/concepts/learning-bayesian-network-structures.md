---
type: concept
aliases: [Learning Bayesian Network Structures]
summary: The task of learning the graphical structure of a Bayesian network from data, often approached as a search problem in the space of possible directed acyclic graphs.
relationships:
  - target: maximum-likelihood-parameter-learning
    type: uses
tags: [bayesian-networks, structure-learning, causal-inference, machine-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Learning Bayesian Network Structures

## The Problem
While parameter learning assumes a fixed Bayesian network structure, in many domains the underlying causal model is unknown or disputed. The goal of structure learning is to infer this network topology—the nodes and the directed links between them—directly from a dataset. This is a more complex task than simply learning the conditional probability parameters for a given structure.

## Search-Based Approach
A common method for structure learning is to treat it as a search problem. The algorithm searches through the space of possible network structures to find one that best explains the data. The search can start from a simple model (e.g., one with no links) and iteratively add parents for each node. Alternatively, it can start with an initial guess and use local search algorithms like hill-climbing or simulated annealing to perform modifications, such as adding, deleting, or reversing links.

## Process and Constraints
During the search, the algorithm must ensure that no cycles are introduced, as Bayesian networks must be directed acyclic graphs. A common way to enforce this is to impose an ordering on the variables and only allow a node to have parents that precede it in the ordering. After each structural change, the model's parameters are refit to the data (using methods like maximum-likelihood learning), and a scoring metric is used to measure the quality of the new structure, guiding the search towards better models.

## Relationships

- **uses**: [[maximum-likelihood-parameter-learning|Maximum Likelihood Parameter Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*