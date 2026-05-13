---
type: concept
aliases: [Problem-Solving Agent]
summary: A type of goal-based agent that finds a sequence of actions to achieve a goal by formulating a problem and using search algorithms to find a solution.
relationships:
  - target: problem-formulation
    type: uses
  - target: search-tree
    type: uses
tags: [agent-architecture, goal-based-agent, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Problem-Solving Agent

## Overview
A problem-solving agent is a kind of goal-based agent designed to achieve its goals by finding a sequence of actions, which is necessary when no single action will suffice. Unlike simpler reflex agents that rely on a direct mapping from states to actions, problem-solving agents consider future actions and the desirability of their outcomes to decide what to do.

## How It Works
The agent operates in a cycle. It first formulates a goal and a problem based on its current state and perception of the environment. It then uses a search algorithm to find a sequence of actions that constitutes a solution to this problem. Once a solution sequence is found, the agent executes the actions one at a time. After completing the sequence, it formulates a new goal and begins the process again.

## Key Components
The core of a problem-solving agent's operation is its ability to formulate a well-defined problem. This formulation includes defining the initial state, the set of possible actions, a transition model describing the outcome of each action, a goal test to recognize a solution state, and a path cost function. This formal problem description is then passed to a search algorithm to find a path from the initial state to a goal state.

## Relationships

- **uses**: [[problem-formulation|Problem Formulation]]
- **uses**: [[search-tree|Search Tree]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*