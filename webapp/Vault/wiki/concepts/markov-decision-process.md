---
type: concept
aliases: [Markov Decision Process]
summary: A mathematical framework for modeling sequential decision problems in a fully observable, stochastic environment with a Markovian transition model and additive rewards.
relationships:
  - target: sequential-decision-problem
    type: is_a
  - target: value-iteration
    type: is_solved_by
  - target: bellman-equation
    type: is_defined_by
  - target: discounted-rewards
    type: uses
tags: [decision-theory, stochastic-processes, reinforcement-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Markov Decision Process

## Definition
A Markov Decision Process (MDP) is a formal model for a sequential decision problem designed for a fully observable, stochastic environment. It is characterized by a Markovian transition model and additive rewards. The careful balancing of risk and reward is a key characteristic of MDPs, which have been studied in fields including AI, operations research, economics, and control theory.

## Key Components
An MDP is defined by a set of states, including an initial state $s_0$; a set of actions available in each state, ACTIONS($s$); a Markovian transition model, $P(s'|s,a)$, which gives the probability of reaching state $s'$ from state $s$ after taking action $a$; and a bounded reward function, $R(s)$, which specifies the reward received in state $s$.

## Solving MDPs
The solution to an MDP is an optimal policy, which specifies the best action for an agent to take in each state to maximize its expected utility. This utility is typically a function of the sequence of rewards, such as a sum of discounted rewards. Algorithms like value iteration are used to calculate the utilities of states and thereby determine the optimal policy.

## Relationships

- **is_a**: [[sequential-decision-problem|Sequential Decision Problem]]
- **is_solved_by**: [[value-iteration|Value Iteration]]
- **is_defined_by**: [[bellman-equation|Bellman Equation]]
- **uses**: [[discounted-rewards|Discounted Rewards]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*