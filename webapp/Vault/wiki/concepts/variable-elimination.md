---
type: concept
aliases: [Variable Elimination]
summary: An exact inference algorithm for Bayesian networks that efficiently computes posterior probabilities by eliminating hidden variables one by one through operations on factors. An algorithm for exact inference in Bayesian networks that works by systematically eliminating variables from the network that are irrelevant to a given query. An exact inference algorithm for Bayesian networks that computes posterior probabilities by summing out variables from the joint distribution one by one, avoiding repeated computations.
relationships:
  - target: bayesian-network
    type: is-an-algorithm-for
  - target: factor-in-variable-elimination
    type: uses
  - target: bayesian-network
    type: is-used-for
  - target: singly-connected-network
    type: is-efficient-on
  - target: bayesian-networks
    type: is-a-method-for
tags: [inference-algorithms, exact-inference, bayesian-networks, algorithm, probabilistic-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Variable Elimination

## Core Idea
The variable elimination algorithm improves upon inference by enumeration by avoiding the explicit computation of the full joint distribution. It works by rewriting the query expression to push summation operations as far to the right as possible. This allows for the elimination of one hidden variable at a time by summing it out of the product of all factors that depend on it, creating a new intermediate factor. This process is repeated until only the query and evidence variables remain.

## Factors and Operations
The algorithm's core data structure is the factor, a multi-dimensional array representing a CPT or an intermediate computational result, indexed by a set of variables. The two primary operations on factors are pointwise product and summing out. The pointwise product of two factors creates a new, larger factor whose variables are the union of the originals. Summing out a variable from a factor marginalizes that variable, reducing the factor's dimensionality.

## Complexity
The efficiency of variable elimination is determined by the size of the largest factor generated during the process. The size of a factor is exponential in the number of variables it contains. Therefore, the algorithm's space and time complexity depend on the network's structure and the chosen order for eliminating variables. While still potentially exponential in the worst case, it is often far more efficient than enumeration for many network structures.

## Relationships

- **is-an-algorithm-for**: [[bayesian-network|Bayesian Network]]
- **uses**: [[factor-in-variable-elimination|Factor In Variable Elimination]]
- **is-used-for**: [[bayesian-network|Bayesian Network]]
- **is-efficient-on**: [[singly-connected-network|Singly Connected Network]]
- **is-a-method-for**: [[bayesian-networks|Bayesian Networks]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*