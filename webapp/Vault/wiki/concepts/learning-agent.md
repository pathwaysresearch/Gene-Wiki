---
type: concept
aliases: [Learning Agent]
summary: An agent capable of improving its performance over time by modifying its internal components based on experience, using a critic, learning element, and performance element.
tags: [agent-architecture, ai, machine-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Learning Agent

## Definition
A learning agent is an agent designed to improve its behavior and decision-making capabilities through experience. Unlike agents with fixed, hand-programmed behaviors, a learning agent can adapt its internal components to become more competent and effective in its environment over time.

## Core Components
A general learning agent is structured with four main conceptual components. The **performance element** is responsible for selecting external actions. The **critic** evaluates the agent's performance by comparing its actions to an external performance standard and provides feedback. The **learning element** uses this feedback to make improvements to the performance element. Finally, the **problem generator** is responsible for suggesting actions that will lead to new and informative experiences, facilitating exploration and more comprehensive learning.

## How It Works
The agent interacts with its environment via its sensors and actuators, which are controlled by the performance element. The critic observes these interactions and provides feedback to the learning element on how well the agent is performing. The learning element then modifies the performance element's rules or representations to produce better actions in the future. This cycle of action, feedback, and modification allows the agent to autonomously improve its performance.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*