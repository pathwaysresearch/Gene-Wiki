---
type: concept
aliases: [Probability Mass Function]
summary: A function that gives the probability that a discrete random variable is exactly equal to some value, and which must satisfy specific properties like normalization.
relationships:
  - target: probability-theory
    type: is_a_concept_in
tags: [probability, discrete-variables]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Probability Mass Function

## Definition
A probability mass function (PMF), denoted by P, is a function that describes the probability distribution over a discrete random variable.

## Required Properties
To be a valid PMF, a function P must satisfy three conditions. First, its domain must be the set of all possible states of the random variable. Second, for any state x, the probability P(x) must be between 0 and 1, inclusive. Third, the sum of the probabilities over all possible states must equal 1, a property known as being normalized.

## Example: Uniform Distribution
A simple example of a PMF is the uniform distribution over a discrete variable with k different states. This PMF assigns an equal probability of 1/k to each state, satisfying all the necessary properties.

## Relationships

- **is_a_concept_in**: [[probability-theory|Probability Theory]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*