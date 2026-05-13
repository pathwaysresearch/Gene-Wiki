---
type: concept
aliases: [Adaptive Dynamic Programming (ADP)]
summary: A model-based reinforcement learning approach where the agent learns a transition model of the environment and uses it to solve the underlying Markov decision process, often via value or policy iteration. A method in reinforcement learning and control theory that applies dynamic programming principles in an adaptive or online manner.
relationships:
  - target: reinforcement-learning
    type: is-a-type-of
  - target: q-learning
    type: contrasts-with
  - target: prioritized-sweeping
    type: uses
  - target: bellman-equation
    type: uses
tags: [reinforcement-learning, model-based, algorithm, dynamic-programming, control-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Adaptive Dynamic Programming (ADP)

## How It Works

An Adaptive Dynamic Programming (ADP) agent is a model-based reinforcement learner. It operates by first learning the transition model of the environment, P(s'|s, a), from its experiences. This is a supervised learning task where the agent tracks the frequency of outcomes for each state-action pair. Once it has a model, it can use algorithms like value iteration or policy iteration to compute the optimal utilities or policy, just as if the true model were known.

## Approximate ADP and Scalability

For environments with very large state spaces, such as 10^100 states, full ADP is intractable. Approximate ADP algorithms address this by making the process more efficient. Instead of performing a full sweep of value iteration, these methods can bound the number of adjustments made after each transition. They may also use heuristics, like prioritized sweeping, which focuses computation by adjusting states whose successors have just had a large change in their utility estimates.

## Advantages and Trade-offs

Approximate ADP algorithms can be several orders of magnitude more computationally efficient than full ADP and can learn as quickly in terms of training sequences. This enables them to handle much larger state spaces. However, a key trade-off is that in the early stages of learning, the learned environment model may be inaccurate, making the extensive computation based on this flawed model potentially wasteful.

## Relationships

- **is-a-type-of**: [[reinforcement-learning|Reinforcement Learning]]
- **contrasts-with**: [[q-learning|Q Learning]]
- **uses**: [[prioritized-sweeping|Prioritized Sweeping]]
- **uses**: [[bellman-equation|Bellman Equation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*