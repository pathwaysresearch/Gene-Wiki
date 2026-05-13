---
type: concept
aliases: [Passive Reinforcement Learning]
summary: A type of reinforcement learning where the agent's policy is fixed, and its objective is to learn the utility function U(s) for the states under that given policy.
relationships:
  - target: reinforcement-learning
    type: is-a-type-of
  - target: direct-utility-estimation
    type: uses
  - target: adaptive-dynamic-programming
    type: uses
  - target: temporal-difference-learning
    type: uses
tags: [reinforcement-learning, policy-evaluation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Passive Reinforcement Learning

## Definition

In passive reinforcement learning, an agent operates with a fixed policy, denoted as π. The agent's task is not to find an optimal policy, but rather to evaluate the given one. It does this by learning the utility, U^π(s), for each state 's', which represents the expected long-term reward from that state when following policy π.

## Objective Function

The utility of a state under a policy π is defined as the expected sum of discounted rewards obtained if the policy is followed starting from that state. This is formally written as U^π(s) = E[Σ γ^t R(S_t)], where R(s) is the reward for a state, S_t is the state at time t, and γ is a discount factor that determines the present value of future rewards.

## Learning Methods

The text describes several methods for passive learning. Direct utility estimation calculates the utility of a state as the average of the observed total rewards (reward-to-go) from all trials that passed through that state. Other, more sophisticated methods include Adaptive Dynamic Programming (ADP), which learns a model of the environment to compute utilities, and Temporal-Difference (TD) learning, which updates utility estimates based on observed transitions without needing a full model.

## Relationships

- **is-a-type-of**: [[reinforcement-learning|Reinforcement Learning]]
- **uses**: [[direct-utility-estimation|Direct Utility Estimation]]
- **uses**: [[adaptive-dynamic-programming|Adaptive Dynamic Programming]]
- **uses**: [[temporal-difference-learning|Temporal Difference Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*