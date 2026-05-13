---
type: concept
aliases: [Markov Network]
summary: An undirected graphical model representing a set of random variables and their conditional independence relationships, often used as an intermediate representation for inference in Bayesian networks.
relationships:
  - target: bayesian-networks
    type: is-related-to
  - target: hugin-system
    type: is-implemented-by
tags: [graphical-models, probabilistic-models, inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Markov Network

## Overview
A Markov network is an undirected form of graphical model. Unlike Bayesian networks, which use directed edges to represent conditional dependencies, Markov networks use undirected edges to represent probabilistic relationships between variables. (Chunk 311)

## Role in Bayesian Inference
One significant approach to performing exact inference in general Bayesian networks involves converting the directed network into an undirected Markov network. This transformation is a key step in certain clustering algorithms. Once converted, methods like message passing can be used on the new structure to achieve consistency and compute probabilities. (Chunk 311)

## Development and Implementation
This inference approach based on conversion to a Markov network was developed by statisticians David Spiegelhalter and Steffen Lauritzen. It is the method implemented in the HUGIN system, which is described as an efficient and widely used tool for uncertain reasoning. (Chunk 311)

## Relationships

- **is-related-to**: [[bayesian-networks|Bayesian Networks]]
- **is-implemented-by**: [[hugin-system|Hugin System]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*