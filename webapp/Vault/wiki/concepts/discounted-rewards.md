---
type: concept
aliases: [Discounted Rewards]
summary: A method for calculating the utility of an infinite sequence of states by summing rewards that are geometrically discounted over time, ensuring a finite total utility.
relationships:
  - target: sequential-decision-problem
    type: solves_horizon_problem_for
tags: [utility-theory, mdp, decision-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Discounted Rewards

## Definition
Discounted rewards are a technique for calculating the utility of an infinite state sequence in a sequential decision problem. This method addresses the issue that a simple sum of rewards over an infinite horizon can be infinite. The utility is defined as the sum of rewards received over time, where the reward $R(s_t)$ at time step $t$ is multiplied by a discount factor $\gamma^t$, with $0 \le \gamma < 1$.

## The Formula
The utility of an infinite history $[s_0, s_1, s_2, \ldots]$ using discounted rewards is given by the formula $U_h([s_0, s_1, s_2, \ldots]) = \sum_{t=0}^{\infty} \gamma^t R(s_t)$. Because the discount factor $\gamma$ is less than 1, this geometric series is guaranteed to converge to a finite value as long as the rewards are bounded. If rewards are bounded by $\pm R_{max}$, the total utility is bounded by $R_{max}/(1-\gamma)$.

## Application in MDPs
Discounted rewards are one of three primary solutions for comparing infinite sequences in MDPs. The use of discounting provides a good reason for solving MDPs, as it helps ensure that standard algorithms converge, even in the presence of improper policies (policies that never reach a terminal state). It effectively makes the agent prefer rewards that are received sooner rather than later.

## Relationships

- **solves_horizon_problem_for**: [[sequential-decision-problem|Sequential Decision Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*