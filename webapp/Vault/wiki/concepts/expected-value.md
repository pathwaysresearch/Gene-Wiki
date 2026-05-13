---
type: concept
aliases: [Expected Value]
summary: The weighted average value of a function of a random variable, where the weights are given by the variable's probability distribution.
relationships:
  - target: probability-theory
    type: is_a_concept_in
tags: [probability, statistics, descriptive-statistics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Expected Value

## Definition
The expectation, or expected value, of a function f(x) with respect to a probability distribution P(x) is the average or mean value that the function f takes on when its argument x is drawn from the distribution P.

## Calculation for Discrete Variables
For discrete random variables, the expected value is calculated by taking a sum over all possible states of x. The sum consists of the value of the function f(x) for each state, multiplied by the probability P(x) of that state occurring.

## Interpretation
The expected value can be thought of as the long-run average value of f(x) that would be observed if the process of drawing x from P were repeated many times.

## Relationships

- **is_a_concept_in**: [[probability-theory|Probability Theory]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*