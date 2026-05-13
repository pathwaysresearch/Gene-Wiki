---
type: concept
aliases: [Partially Observable Markov Decision Process (POMDP)]
summary: A generalization of a Markov Decision Process where the agent cannot directly observe the underlying state and must instead maintain a probability distribution over possible states, known as a belief state.
relationships:
  - target: belief-state
    type: uses
  - target: value-iteration
    type: solved_by
  - target: markov-decision-process
    type: generalization_of
tags: [reinforcement-learning, planning, stochastic-process, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Partially Observable Markov Decision Process (POMDP)

## Overview
A Partially Observable Markov Decision Process (POMDP) is a framework for modeling decision-making problems where an agent's state is not fully known. Unlike in a standard MDP, the agent's percepts or observations do not uniquely determine its current state. To handle this uncertainty, the agent must reason about a set of possible states it could be in, which fundamentally changes how policies and values are computed.

## The Role of Belief States
In a POMDP, the agent maintains a **belief state**, which is a probability distribution over the actual, underlying states. The text writes $b(s)$ for the probability assigned to the actual state $s$ by the belief state $b$. This belief state is updated after every action and subsequent observation using a filtering process. The update rule is given by $b'(s') = \alpha P(e|s') \sum_s P(s'|s,a)b(s)$, where $b$ is the previous belief state, $a$ is the action taken, $e$ is the new evidence perceived, and $\alpha$ is a normalizing constant. This update is analogous to the recursive filtering described in Chapter 15.

## Value Iteration for POMDPs
Solving a POMDP is challenging because there are infinitely many possible belief states. The text describes a value iteration algorithm adapted for POMDPs. Instead of computing a single utility value for each state, this algorithm computes a utility function over the continuous belief space. This function is represented by a collection of conditional plans. The expected utility of executing a fixed conditional plan $p$ is a linear function of the belief state $b$, written as $b \cdot \alpha_p$, where $\alpha_p$ is a utility vector for that plan. The optimal utility function at any belief state is the maximum of these linear functions, forming a piecewise-linear and convex surface. The POMDP value iteration algorithm works by iteratively building up this set of utility vectors to approximate the optimal utility function.

## Relationships

- **uses**: [[belief-state|Belief State]]
- **solved_by**: [[value-iteration|Value Iteration]]
- **generalization_of**: [[markov-decision-process|Markov Decision Process]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*