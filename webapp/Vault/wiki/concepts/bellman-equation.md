---
type: concept
aliases: [Bellman Equation]
summary: A fundamental equation in dynamic programming that relates the utility of a state to the immediate reward and the expected discounted utilities of its successor states under an optimal policy. A fundamental equation in dynamic programming and reinforcement learning that characterizes the value of a decision problem.
relationships:
  - target: richard-bellman
    type: named_after
  - target: value-iteration
    type: is_used_by
  - target: markov-decision-process
    type: defines_solution_for
  - target: adaptive-dynamic-programming
    type: used_in
tags: [dynamic-programming, optimization, equation, reinforcement-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Bellman Equation

## Definition
Named after Richard Bellman, the Bellman equation describes a direct relationship between the utility of a state and the utility of its neighbors in a Markov Decision Process. It states that the utility of a state is the immediate reward for that state plus the expected discounted utility of the next state, assuming that the agent chooses the optimal action.

## The Equation
The Bellman equation for the utility $U(s)$ of a state $s$ is formally expressed as: $U(s) = R(s) + \gamma \max_{a \in A(s)} \sum_{s'} P(s'|s,a)U(s')$. In this equation, $R(s)$ is the immediate reward, $\gamma$ is the discount factor, $A(s)$ is the set of available actions, and $P(s'|s,a)$ is the transition probability to state $s'$ given the current state $s$ and action $a$.

## Role in Solving MDPs
The utilities of the states in an MDP are the unique solutions to the system of Bellman equations (one for each state). The equation forms the basis of the value iteration algorithm, where it is used as an iterative update rule to converge on these unique utility values. Once the utilities are known, the optimal policy can be directly extracted.

## Relationships

- **named_after**: [[richard-bellman|Richard Bellman]]
- **is_used_by**: [[value-iteration|Value Iteration]]
- **defines_solution_for**: [[markov-decision-process|Markov Decision Process]]
- **used_in**: [[adaptive-dynamic-programming|Adaptive Dynamic Programming]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*