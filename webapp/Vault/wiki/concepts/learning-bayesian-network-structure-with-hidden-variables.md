---
type: concept
aliases: [Learning Bayesian Network Structure with Hidden Variables]
summary: The task of determining the graphical structure of a Bayesian network from data when some variables are unobserved (latent).
relationships:
  - target: expectation-maximization-em-algorithm
    type: uses
tags: [bayesian-networks, structure-learning, machine-learning, latent-variables]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Learning Bayesian Network Structure with Hidden Variables

## Problem Definition
This task involves learning the dependency structure (the directed acyclic graph) of a Bayesian network when the dataset is incomplete, meaning some variables that influence the observed data are not present in the dataset. This is significantly more difficult than learning the structure from complete data, where all variables are observed.

## Algorithmic Approach
The learning process typically involves an outer loop that searches through the space of possible network structures and an inner loop that fits the network parameters for a given structure. When hidden variables are present, this inner loop often requires an algorithm like Expectation-Maximization (EM) to estimate the parameters.

## Handling Hidden Variables
There are two main strategies for dealing with hidden variables. If an expert specifies that certain hidden variables exist, the algorithm can search for the best way to integrate them into the network structure. If the existence of hidden variables is not known beforehand, the algorithm can be extended to invent new ones. This is done by adding new modification choices to the structure search, such as adding or deleting a hidden variable or changing its number of possible values (arity), in order to find a simpler, more explanatory model.

## Relationships

- **uses**: [[expectation-maximization-em-algorithm|Expectation Maximization Em Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*