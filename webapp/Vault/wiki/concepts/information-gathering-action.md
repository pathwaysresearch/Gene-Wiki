---
type: concept
aliases: [Information Gathering Action]
summary: A deliberate action taken by a robot in a partially observable environment to reduce its uncertainty about its state.
tags: [robotics, planning-under-uncertainty, pomdp, robot-control]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Information Gathering Action

## Definition
An information gathering action is a decision made by a robot to acquire information to reduce uncertainty about a critical state variable, rather than to directly advance toward a goal.

## Context of Partial Observability
These actions are a key component of solving Partially Observable MDPs (POMDPs), where a robot maintains a belief state (a probability distribution over possible states) instead of knowing its exact state. The policy in a POMDP is defined over this belief state, allowing the robot to reason about what it does and does not know.

## Rationale
A robot can rationally choose an information gathering action when its uncertainty is high, enabling it to make more informed decisions later. This capability is absent in fully observable MDP frameworks, which assume the state is always known and thus have no need to plan actions to reduce uncertainty.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*