---
type: concept
aliases: [Laplace Distribution]
summary: A probability distribution that allows for a sharp peak of probability mass at an arbitrary point, closely related to the exponential distribution.
relationships:
  - target: exponential-distribution
    type: related_to
tags: [probability-distribution, continuous-variable, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Laplace Distribution

## Definition
The Laplace distribution is a continuous probability distribution that is characterized by its ability to place a sharp peak of probability mass at an arbitrary point $\mu$.

## Key Properties
Its key feature is the sharp peak, which provides a way to model data where values are highly concentrated around a central point, with tails that are heavier than those of a Gaussian distribution. This makes it robust to outliers.

## Relationship to Exponential Distribution
The text describes the Laplace distribution as being closely related to the exponential distribution. While the exponential distribution has its sharp peak fixed at x=0, the Laplace distribution generalizes this concept, allowing the peak to be centered at any location $\mu$.

## Relationships

- **related_to**: [[exponential-distribution|Exponential Distribution]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*