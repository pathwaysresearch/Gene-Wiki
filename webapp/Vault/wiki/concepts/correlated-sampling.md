---
type: concept
aliases: [Correlated Sampling]
summary: A technique used to reduce measurement error when comparing stochastic systems or policies by ensuring they are evaluated on the same set of random events.
relationships:
  - target: pegasus-algorithm
    type: is-used-by
tags: [statistics, simulation, reinforcement-learning, policy-evaluation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Correlated Sampling

## Definition
Correlated sampling is a method for reducing measurement error when comparing the performance of different programs or policies that are subject to random fluctuations. The core idea is to generate a set of random scenarios in advance and have each program or policy operate on the exact same set.

## Application Example
The text illustrates this concept with the task of determining which of two blackjack programs is better. The winnings of each program can fluctuate widely based on the cards they are dealt. By generating a number of hands in advance and having both programs play the same set of hands, the error due to differences in cards is eliminated, allowing for a more accurate comparison of the programs' strategies.

## Use in Reinforcement Learning
This idea underlies a policy-search algorithm called PEGASUS, introduced by Ng and Jordan (2000). In the context of reinforcement learning, it allows for a more stable comparison of different policies by removing the variance that comes from random transitions or rewards in the environment.

## Relationships

- **is-used-by**: [[pegasus-algorithm|Pegasus Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*