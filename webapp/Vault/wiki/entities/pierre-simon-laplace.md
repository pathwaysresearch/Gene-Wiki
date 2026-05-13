---
type: entity
aliases: [Pierre-Simon Laplace]
summary: An 18th-century French scholar credited with suggesting the simplest form of smoothing for probability estimates, known as Laplace smoothing or add-one smoothing.
tags: [mathematician, statistician, historical-figure]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
relationships:
  - target: bayes-rule
    type: created
---

# Pierre-Simon Laplace

## Overview
Pierre-Simon Laplace was an 18th-century scholar who made foundational contributions to mathematics and probability theory. His work included developing a method to handle the estimation of probabilities for events that have not been observed in a sample of data.

## Contribution to Smoothing
Laplace is credited with suggesting the simplest type of smoothing for probability estimates, a technique now known as Laplace smoothing or add-one smoothing. He proposed that, in the absence of other information, if a random Boolean variable has been observed to be false in all `n` observations, the probability of it being true should be estimated as `1/(n+2)`.

## Legacy in Language Models
This idea provides a basic solution to the problem of zero-frequency events in statistical modeling, which is crucial for the generalization of language models. While his method is considered to perform relatively poorly compared to more modern techniques like backoff models, it remains a fundamental and widely taught concept in statistical smoothing.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*