---
type: concept
aliases: [Utility-Based Agent]
summary: An agent that uses a utility function to evaluate the desirability of different world states, allowing it to make rational choices among conflicting goals or under uncertainty.
tags: [agent-architecture, ai, decision-theory, rationality]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Utility-Based Agent

## Definition
A utility-based agent is an agent that selects actions based on a utility function, which provides a measure of desirability or "happiness" for any given world state. This approach is more general than goal-based agents, which only make a crude binary distinction between "happy" (goal achieved) and "unhappy" (goal not achieved) states.

## The Role of the Utility Function
An agent's utility function is an internalization of the external performance measure. It allows the agent to compare different world states and action sequences, enabling it to choose actions that lead to better outcomes. For example, a taxi agent can use a utility function to decide between routes that are quicker, safer, or cheaper. An agent that chooses actions to maximize its utility is considered rational according to the external performance measure.

## Challenges and Complexity
While the concept of building agents that maximize expected utility is central to AI, it is not simple to implement. A utility-based agent must model and keep track of its environment, which requires extensive research in perception, representation, reasoning, and learning. Furthermore, the task of choosing the utility-maximizing course of action is computationally difficult, and perfect rationality is often unachievable in practice due to this complexity.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*