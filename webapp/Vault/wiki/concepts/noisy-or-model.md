---
type: concept
aliases: [Noisy-OR Model]
summary: A model for efficiently representing conditional probability tables (CPTs) in Bayesian networks, typically used when a variable has multiple independent causes that can be inhibited.
relationships:
  - target: bayesian-network
    type: is-a-component-of
tags: [cpt-representation, probabilistic-models, bayesian-networks]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Noisy-OR Model

## Definition
The noisy-OR model is a method for efficiently representing conditional distributions, particularly for nodes with many parent variables that act as causes. It models a disjunctive interaction where any of the causes can produce the effect, but each cause has an independent probability of being inhibited and failing to do so.

## Assumptions and Mechanism
The model relies on two main assumptions: that all possible causes are listed (or a 'leak node' is used for miscellaneous causes) and that the inhibition of one cause is independent of the inhibition of any other. Under these assumptions, the effect is absent if and only if all of its present causes are inhibited. The probability of the effect is calculated as one minus the product of the inhibition probabilities for all parent causes that are true.

## CPT Representation
This model provides an exponential reduction in the number of parameters needed to specify a CPT. Instead of a value for every combination of parent states, one only needs to specify the individual inhibition probability, $q_j$, for each parent $X_j$. The CPT entry for the effect $X_i$ is then calculated using the formula $P(x_i | \text{parents}(X_i)) = 1 - \prod_{j:X_j=\text{true}} q_j$.

## Relationships

- **is-a-component-of**: [[bayesian-network|Bayesian Network]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*