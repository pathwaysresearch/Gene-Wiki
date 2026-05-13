---
type: concept
aliases: [Q-Learning]
summary: A model-free reinforcement learning algorithm that learns an action-utility function (Q-function) to find the optimal action-selection policy for a given Markov decision process. A model-free reinforcement learning algorithm that learns a policy indicating the best action to take in a given state. The text discusses its mechanism and implementation on pages 831, 843, 844, 848, and 973.
relationships:
  - target: reinforcement-learning
    type: is-a-type-of
  - target: temporal-difference-learning
    type: uses
  - target: q-function
    type: learns
  - target: sarsa
    type: is-related-to
  - target: temporal-difference-learning
    type: is_a
tags: [reinforcement-learning, model-free, algorithm, temporal-difference, machine-learning, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Q-Learning

## Definition

Q-learning is a reinforcement learning technique where the agent learns an action-utility function, also known as a Q-function. This function, denoted Q(s, a), gives the expected utility of taking a specific action 'a' in a given state 's'. Unlike utility-based agents that require a model of the environment to make decisions, a Q-learning agent can select optimal actions using its learned Q-values directly.

## Update Mechanism

Q-learning uses a temporal-difference (TD) update rule to learn the Q-values. After taking action 'a' in state 's', receiving reward R(s), and transitioning to state 's'', the Q-value is updated using the formula: Q(s,a) ← Q(s,a) + α(R(s) + γ max_a' Q(s',a') - Q(s,a)). This update is based on the observed reward and the maximum Q-value of the next state, allowing the agent to learn without a model of the environment's transition probabilities.

## Exploration

An exploratory Q-learning agent must balance exploration with exploitation to ensure it discovers optimal actions. It can use an exploration function, f(u, n), which trades off the estimated utility of an action (u) with the number of times it has been tried (n). This allows the agent to systematically explore its environment while gradually converging toward a greedy, optimal policy. The agent design requires keeping statistics on actions taken to support this exploration strategy.

## Relationships

- **is-a-type-of**: [[reinforcement-learning|Reinforcement Learning]]
- **uses**: [[temporal-difference-learning|Temporal Difference Learning]]
- **learns**: [[q-function|Q Function]]
- **is-related-to**: [[sarsa|Sarsa]]
- **is_a**: [[temporal-difference-learning|Temporal Difference Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*