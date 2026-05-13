---
type: concept
aliases: [Cumulative Probability Density Function]
summary: A function, denoted F_X(x), that gives the probability that a random variable X will take a value less than or equal to a specific value x.
relationships:
  - target: probability-density-function
    type: is_integral_of
tags: [probability-theory, statistics, continuous-variables]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Cumulative Probability Density Function

## Definition
The cumulative probability density function, denoted F_X(x), is defined as the probability that a random variable X takes on a value that is less than or equal to a given value x. This is formally expressed as F_X(x) = P(X <= x).

## Calculation from PDF
This function is directly derived from the probability density function (PDF). It is calculated by integrating the PDF, P(u), from negative infinity up to the value x. The formula is given as F_X(x) = integral from -infinity to x of P(u) du.

## Role in Probability Theory
The cumulative function provides a way to determine the probability of a random variable falling within any arbitrary range by accumulating probability from the lower tail of the distribution up to a specified point.

## Relationships

- **is_integral_of**: [[probability-density-function|Probability Density Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*