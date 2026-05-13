---
type: concept
aliases: [Policy Search]
summary: A reinforcement learning method that directly searches for an optimal policy by adjusting the parameters of a policy representation to improve performance.
relationships:
  - target: reinforce-algorithm
    type: is-implemented-by
  - target: pegasus-algorithm
    type: is-implemented-by
  - target: function-approximation-in-reinforcement-learning
    type: uses
tags: [reinforcement-learning, optimization, control-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Policy Search

## Definition
Policy search is a reinforcement learning approach where the agent learns a parameterized representation of the policy, $\pi_\theta$, and adjusts the parameters $\theta$ to improve performance. This contrasts with value-based methods like Q-learning, which first learn a value function and then derive a policy from it.

## Comparison with Q-Learning
While policy search can involve learning Q-functions to represent a policy, the process is fundamentally different from Q-learning with function approximation. Q-learning aims to find parameters $\theta$ that make the approximate function $Q_\theta$ as close as possible to the optimal Q-function, $Q^*$. In contrast, policy search finds a $\theta$ that results in good performance, even if the resulting $Q_\theta$ is not close to $Q^*$ (e.g., $Q_\theta(s, a) = Q^*(s, a)/10$ would still yield an optimal policy).

## Challenges and Methods
A problem with policy search in discrete action spaces is that the policy can be a discontinuous function of its parameters, making gradient-based optimization difficult. Gradient-based algorithms like REINFORCE have been developed to address this. Another approach is to use correlated sampling to compare policies, as implemented in the PEGASUS algorithm.

## Relationships

- **is-implemented-by**: [[reinforce-algorithm|Reinforce Algorithm]]
- **is-implemented-by**: [[pegasus-algorithm|Pegasus Algorithm]]
- **uses**: [[function-approximation-in-reinforcement-learning|Function Approximation In Reinforcement Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*