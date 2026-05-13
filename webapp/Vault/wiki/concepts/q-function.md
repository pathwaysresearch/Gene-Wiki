---
type: concept
aliases: [Q-Function]
summary: A function in reinforcement learning, denoted Q(s, a), that represents the expected utility of taking a specific action 'a' in a specific state 's' and following the optimal policy thereafter.
relationships:
  - target: q-learning
    type: is-central-to
  - target: sarsa
    type: is-central-to
tags: [reinforcement-learning, utility-theory, core-concept]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Q-Function

## Definition

A Q-function is formally described as an action-utility function. Its purpose is to quantify the value, or expected utility, of performing a particular action within a given state. This provides a direct mapping from state-action pairs to their expected long-term reward, which an agent can use to make decisions.

## Role in Q-Learning

The Q-function is the central component learned by a Q-learning agent. The agent's entire goal is to learn the true Q-function for the environment. Once an accurate Q-function is learned, the optimal policy is simply to choose the action 'a' that maximizes Q(s, a) for any given state 's'. This makes the policy implicit in the Q-values, removing the need for a separate policy representation or an environment model.

## Update Method

The values of the Q-function are learned iteratively using a temporal-difference update rule. As shown in the Q-learning algorithm, the update for Q(s, a) incorporates the immediate reward received and the discounted maximum Q-value of the resulting state. This process allows the agent to propagate utility information backward from rewards through the state-action space over many trials.

## Relationships

- **is-central-to**: [[q-learning|Q Learning]]
- **is-central-to**: [[sarsa|Sarsa]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*