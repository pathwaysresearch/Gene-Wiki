---
type: concept
aliases: [Cumulative Distribution]
summary: A function that gives the probability that a random variable X will take a value from a set of outcomes up to a certain point.
tags: [probability, statistics, sampling]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Cumulative Distribution

## Definition
For a discrete random variable X with a set of possible outcomes {x₁, ..., xₖ}, the cumulative distribution gives the probability that X will take a value within the subset {x₁, ..., xⱼ} for each possible j. It represents the accumulated probability as one moves through the ordered set of outcomes.

## Computation
The cumulative distribution for a discrete variable with k possible outcomes can be calculated efficiently. The process takes O(k) time, typically by iterating through the probabilities of each outcome and maintaining a running sum.

## Application in Sampling
A key application of the cumulative distribution is generating random samples from a specified probability distribution. By using a random number generator that produces a uniform value between 0 and 1, one can map this value to an outcome xᵢ based on where it falls within the intervals defined by the cumulative distribution. This allows for the creation of samples that adhere to the desired non-uniform distribution.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*