---
type: concept
aliases: [Value Iteration]
summary: An iterative algorithm for solving Markov Decision Processes (MDPs) by calculating the optimal utility for each state and then using these utilities to derive an optimal policy.
relationships:
  - target: markov-decision-process
    type: solves
  - target: bellman-equation
    type: uses
  - target: contraction
    type: convergence_proven_by
tags: [algorithm, dynamic-programming, mdp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Value Iteration

## Overview
Value iteration is an algorithm for calculating an optimal policy for a Markov Decision Process (MDP). The basic idea is to first calculate the utility of each state and then use these state utilities to select an optimal action in each state. It is one of the most important algorithm families for solving MDPs.

## How It Works
The algorithm works by iteratively applying the Bellman equation as an update rule. Starting with arbitrary initial utility values for all states, each iteration updates the utility of every state based on the immediate reward and the expected discounted utility of its successor states, maximized over all possible actions. This process continues until the utility values converge.

## Convergence
The value iteration algorithm is guaranteed to converge to a unique set of solutions for the Bellman equations. This convergence is proven using the mathematical concept of a contraction. The Bellman update operator is a contraction mapping, which ensures that with each application, the utility estimates get closer to the true utility values, eventually converging to the single fixed point which represents the optimal utility function.

## Relationships

- **solves**: [[markov-decision-process|Markov Decision Process]]
- **uses**: [[bellman-equation|Bellman Equation]]
- **convergence_proven_by**: [[contraction|Contraction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*