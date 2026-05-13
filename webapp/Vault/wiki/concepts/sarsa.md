---
type: concept
aliases: [SARSA]
summary: A model-free, on-policy temporal difference (TD) control algorithm in reinforcement learning, whose name stands for State-Action-Reward-State-Action.
relationships:
  - target: q-learning
    type: is-related-to
  - target: temporal-difference-learning
    type: uses
  - target: q-function
    type: learns
tags: [reinforcement-learning, model-free, algorithm, on-policy]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# SARSA

## Overview

SARSA is presented as a close relative of the Q-learning algorithm. Its name is an acronym for the sequence of events that constitute a single update: observing the current State, choosing an Action, receiving a Reward, observing the next State, and choosing the next Action. This quintuple (s, a, r, s', a') forms the basis of its learning rule.

## Update Rule

The update rule for SARSA is very similar to that of Q-learning and is based on temporal-difference learning. The formula is: Q(s,a) ← Q(s,a) + α(R(s) + γ Q(s',a') - Q(s,a)). This update is performed after the agent has transitioned from state 's' to 's'' via action 'a' and has already committed to its next action, 'a''.

## Comparison with Q-learning

The critical difference between SARSA and Q-learning lies in the update rule. SARSA uses the Q-value of the actual next action chosen in the next state, Q(s', a'), to update the current Q-value. In contrast, Q-learning uses the maximum possible Q-value in the next state, max_a' Q(s', a'), regardless of which action is actually taken next. This distinction makes SARSA an on-policy algorithm (it learns the value of the policy it is following), whereas Q-learning is an off-policy algorithm (it learns the value of the optimal policy, independent of the agent's exploratory actions).

## Relationships

- **is-related-to**: [[q-learning|Q Learning]]
- **uses**: [[temporal-difference-learning|Temporal Difference Learning]]
- **learns**: [[q-function|Q Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*