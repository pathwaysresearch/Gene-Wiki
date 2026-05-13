---
type: concept
aliases: [Factor (in Variable Elimination)]
summary: A data structure, typically a multi-dimensional array, used in the variable elimination algorithm to represent conditional probability distributions or intermediate results of computation.
relationships:
  - target: variable-elimination
    type: is-a-component-of
tags: [inference-algorithms, data-structures, bayesian-networks]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Factor (in Variable Elimination)

## Definition
In the context of the variable elimination algorithm, a factor is a matrix or multi-dimensional array indexed by the values of a set of random variables. Each entry in the factor corresponds to a specific combination of values for those variables. The initial factors in the algorithm are the conditional probability tables (CPTs) from the Bayesian network.

## Core Operations
The variable elimination algorithm is built upon two fundamental operations performed on factors. The first is the pointwise product, where two factors are multiplied to create a new factor. The variables of the new factor are the union of the variables from the original two factors. The second operation is summing out, which marginalizes a variable from a factor, thereby reducing the factor's dimensionality.

## Role in Computational Complexity
The size of the factors generated during the algorithm is the primary determinant of its computational complexity. The pointwise product operation can create new factors that are larger and have more variables than any of the input factors. Because the size of a factor is exponential in the number of variables it contains, this step is the source of both the space and time complexity of the variable elimination algorithm.

## Relationships

- **is-a-component-of**: [[variable-elimination|Variable Elimination]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*