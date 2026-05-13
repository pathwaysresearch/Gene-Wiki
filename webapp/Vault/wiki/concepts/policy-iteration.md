---
type: concept
aliases: [Policy Iteration]
summary: An algorithm for finding an optimal policy in a Markov Decision Process (MDP) by alternating between policy evaluation and policy improvement until the policy converges.
relationships:
  - target: value-iteration
    type: related_to
  - target: markov-decision-process
    type: solves
tags: [reinforcement-learning, algorithm, mdp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Policy Iteration

## Algorithm Overview
Policy iteration is an algorithm for calculating an optimal policy in a Markov Decision Process (MDP). The algorithm operates by starting with an initial, random policy and then repeating two main steps until the policy becomes stable. First, in the policy evaluation step, the algorithm calculates the utility of each state under the current policy. Second, in the policy improvement step, it updates the policy by selecting the action that maximizes expected utility in each state, based on the utilities just calculated. This process continues until the policy no longer changes, at which point it has converged to the optimal policy.

## Policy Evaluation
The first core step within the policy iteration loop is policy evaluation, represented in the provided pseudocode as `U ← POLICY-EVALUATION(π, U, mdp)`. This step determines the utility vector `U` for the current policy `π`. For MDPs with small state spaces, this evaluation can be performed using exact solution methods. However, the text notes that for large state spaces, where an exact solution might be computationally prohibitive (e.g., O(n^3) time), it is not necessary to perform an exact evaluation.

## Modified Policy Iteration
The text introduces an efficient variant called Modified Policy Iteration for large state spaces. Instead of performing a full, exact policy evaluation, this approach uses a limited number of simplified value iteration steps to compute a reasonably good approximation of the utilities. The simplified Bellman update for this process is given as $U_{i+1}(s) \leftarrow R(s) + \gamma \sum_{s'} P(s'|s, \pi_i(s))U_i(s')$. This modified algorithm, which alternates between approximate policy evaluation and policy improvement, is often much more efficient than standard policy iteration or value iteration.

## Relationships

- **related_to**: [[value-iteration|Value Iteration]]
- **solves**: [[markov-decision-process|Markov Decision Process]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*