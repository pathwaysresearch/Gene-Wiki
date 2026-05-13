---
type: concept
aliases: [Bandit Problem]
summary: A special case of reinforcement learning where an agent takes only a single action and receives a single reward, focusing on the exploration-exploitation tradeoff.
relationships:
  - target: reinforcement-learning
    type: is_a_special_case_of
tags: [reinforcement-learning, machine-learning, decision-theory]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bandit Problem

## Definition
The bandits scenario is a simplified but fundamental form of reinforcement learning. In this setting, a learner must make only a single decision (i.e., take one action) and then receives a single reward based on that action.

## Relationship to General Reinforcement Learning
Unlike the general reinforcement learning problem, which can involve a sequence of many actions and rewards over time, the bandit problem is constrained to one step. This simplifies the credit assignment problem, as the learner knows precisely which reward is associated with the action it took. The general RL setting is more complex because a reward might be the result of a long sequence of prior actions.

## Application Context
The problem of getting limited feedback in recommendation systems is analogous to the bandit problem. When a system recommends one item, it only gets feedback for that choice (e.g., a click or purchase), not for what would have happened if it had recommended other items. This creates the classic bandit dilemma of balancing exploiting known good choices with exploring potentially better, unknown ones.

## Relationships

- **is_a_special_case_of**: [[reinforcement-learning|Reinforcement Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*