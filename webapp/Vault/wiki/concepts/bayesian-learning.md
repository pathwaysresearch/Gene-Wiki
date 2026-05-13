---
type: concept
aliases: [Bayesian Learning]
summary: A method for updating the probability of a hypothesis based on new data, making predictions by averaging over all hypotheses weighted by their posterior probabilities.
relationships:
  - target: statistical-learning
    type: is-a
  - target: maximum-a-posteriori-learning
    type: is-approximated-by
  - target: conjugate-prior
    type: uses
tags: [machine-learning, bayesian-statistics, probabilistic-inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Bayesian Learning

## How It Works
Bayesian learning calculates the probability of each hypothesis given the data and uses these probabilities to make predictions. As data points are observed, the posterior probability of each hypothesis is updated. Predictions about future data are not based on a single best hypothesis, but are instead a weighted average over all possible hypotheses, where each hypothesis is weighted by its posterior probability. For example, the probability of the next candy being lime is the sum of $P(\text{lime}|h_i)P(h_i|\text{data})$ over all hypotheses $h_i$.

## Key Properties
Bayesian learning is considered optimal in the sense that, given the hypothesis prior, any other prediction method is expected to be correct less often, regardless of whether the data set is large or small. A key characteristic is that for any fixed prior that does not completely rule out the true hypothesis, the posterior probability of any false hypothesis will eventually approach zero as more data is collected. This convergence occurs because the probability of a false hypothesis generating uncharacteristic data indefinitely is vanishingly small.

## Limitations
The optimality of Bayesian learning comes at a significant computational cost. For most real-world problems, the hypothesis space is very large or infinite. This makes the summation (or integration) over all hypotheses required for prediction intractable. Consequently, practical applications must often resort to approximate or simplified methods, such as making predictions based on only the single most probable hypothesis (Maximum a Posteriori).

## Relationships

- **is-a**: [[statistical-learning|Statistical Learning]]
- **is-approximated-by**: [[maximum-a-posteriori-learning|Maximum A Posteriori Learning]]
- **uses**: [[conjugate-prior|Conjugate Prior]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*