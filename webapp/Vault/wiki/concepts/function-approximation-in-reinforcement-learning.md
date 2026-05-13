---
type: concept
aliases: [Function Approximation in Reinforcement Learning]
summary: A method in reinforcement learning that represents utility or Q-functions using a set of parameters, allowing an agent to generalize from experienced states to unexperienced ones.
relationships:
  - target: policy-search
    type: used-in
  - target: boxes-algorithm
    type: is-a-form-of
tags: [reinforcement-learning, machine-learning, generalization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Function Approximation in Reinforcement Learning

## Definition
Function approximation is a technique used in reinforcement learning to represent a utility function, such as $U(s)$, or a Q-function, $Q(s, a)$, with a parameterized function $U_{\theta}(s)$ or $Q_{\theta}(s, a)$ instead of a large table. This allows for an enormous compression of the state space, for example, representing a function with potentially $10^{40}$ values using a much smaller number of parameters, such as 20.

## How It Works
The learning algorithm adjusts the parameters $\theta$ to make the evaluation function approximate the true utility function. For example, a linear function approximator can be defined as $U_{\theta}(s) = \theta_1 f_1(s) + \theta_2 f_2(s) + \dots + \theta_n f_n(s)$, where $f_i(s)$ are basis functions or features of the state $s$. When the parameters are updated in response to an observed transition between two states, the estimated values for all other states are also changed.

## Generalization and Performance
The key benefit of function approximation is that it allows a reinforcement learner to generalize from its experiences. This is expected to speed up learning, provided the chosen function class (hypothesis space) is not too large and contains functions that are a reasonably good fit to the true utility function. However, the convergence of reinforcement learning algorithms using function approximation is an extremely technical subject, with several examples of divergence presented for nonlinear functions.

## Relationships

- **used-in**: [[policy-search|Policy Search]]
- **is-a-form-of**: [[boxes-algorithm|Boxes Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*