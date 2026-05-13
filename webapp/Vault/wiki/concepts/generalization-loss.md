---
type: concept
aliases: [Generalization Loss]
summary: The true expected error of a hypothesis over the entire, often unknown, distribution of examples.
relationships:
  - target: empirical-loss
    type: is_estimated_by
tags: [machine-learning, learning-theory, loss-function]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Generalization Loss

## Definition
Generalization loss is the expected loss of a hypothesis `h` over the true distribution of all possible examples `(x, y)`. It is formally defined as the sum of the loss function `L(y, h(x))` for every example, weighted by the true probability of that example, `P(x, y)`. The ultimate goal of a learning algorithm is to find the hypothesis `h*` that minimizes this generalization loss.

## Estimation Challenge
A key challenge in machine learning is that the true probability distribution `P(x, y)` is not known. Consequently, the generalization loss cannot be calculated directly. Learning agents must instead rely on an estimate derived from a finite set of observed examples.

## Relationship to Empirical Loss
Generalization loss is approximated by empirical loss, which is calculated on a given set of training examples. While minimizing empirical loss is the practical approach taken by learning algorithms, the resulting hypothesis may not perfectly minimize the generalization loss due to factors like variance and noise in the training data.

## Relationships

- **is_estimated_by**: [[empirical-loss|Empirical Loss]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*