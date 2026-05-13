---
type: concept
aliases: [Empirical Loss]
summary: The average loss of a hypothesis calculated over a finite set of training examples, serving as a practical proxy for generalization loss.
relationships:
  - target: generalization-loss
    type: estimates
tags: [machine-learning, learning-theory, loss-function]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Empirical Loss

## Definition
Empirical loss is the average loss a hypothesis `h` incurs on a specific set of `N` examples, `E`. It is calculated by summing the loss function `L(y, h(x))` over all examples in `E` and dividing by `N`. This provides a computable estimate of the true generalization loss.

## Role in Learning
Since the true distribution of data is unknown, learning agents work to find the hypothesis `ĥ*` that minimizes the empirical loss on the available training data. This is the core optimization problem in many supervised learning algorithms.

## Limitations
The hypothesis `ĥ*` that minimizes empirical loss may differ from the true optimal hypothesis `h*` for several reasons. These include unrealizability (the true function is not in the hypothesis space), variance (different training sets lead to different hypotheses), and noise (the data itself may be nondeterministic).

## Relationships

- **estimates**: [[generalization-loss|Generalization Loss]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*