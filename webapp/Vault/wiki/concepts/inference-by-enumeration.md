---
type: concept
aliases: [Inference by Enumeration]
summary: An exact inference algorithm for Bayesian networks that computes posterior probabilities by summing terms from the full joint probability distribution.
relationships:
  - target: bayesian-network
    type: is-an-algorithm-for
tags: [inference-algorithms, exact-inference, bayesian-networks]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Inference by Enumeration

## Definition
Inference by enumeration is a fundamental algorithm for performing exact inference in Bayesian networks. It answers a conditional probability query, such as **P**(**X**|**e**), by explicitly summing the probabilities of all atomic events consistent with the query. The core formula it implements is **P**(**X**|**e**) = α $\sum_y$ **P**(**X**, **e**, **y**), where **X** is the set of query variables, **e** is the set of evidence variables, and **y** represents all the hidden (unobserved) variables.

## How It Works
The algorithm iterates through all possible combinations of values for the hidden variables. For each combination, it calculates the corresponding term in the joint distribution by multiplying the appropriate conditional probabilities from the network's CPTs. These terms are then summed up. Finally, the resulting distribution over the query variable **X** is normalized by the constant α to ensure it sums to 1.

## Complexity
While this method is conceptually simple and always yields the correct answer, its performance is a significant limitation. The algorithm's time complexity is exponential in the number of hidden variables. This makes it intractable for all but the smallest and simplest networks, motivating the development of more efficient exact inference algorithms like variable elimination.

## Relationships

- **is-an-algorithm-for**: [[bayesian-network|Bayesian Network]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*