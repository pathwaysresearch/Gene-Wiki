---
type: concept
aliases: [LRTA* Algorithm]
summary: An online search algorithm for agents that must act in real-time, which learns a map of the environment and updates heuristic cost estimates as it explores.
relationships:
  - target: richard-korf
    type: developed-by
tags: [online-search, real-time-search, reinforcement-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# LRTA* Algorithm

## How It Works
The LRTA*-AGENT function takes the current state `s'` as a percept. It maintains a persistent table `H` of cost estimates for states and a `result` table mapping state-action pairs to outcomes. When in a new state, it updates the heuristic cost `H` for its previous state `s` by taking the minimum `LRTA*-COST` over all possible actions. The cost function `LRTA*-COST` is the cost of the action `c(s, a, s')` plus the stored heuristic `H[s']` of the resulting state. The agent then chooses the action that minimizes this cost estimate from its current state.

## Development and Context
The LRTA* algorithm was developed by Korf (1990) for real-time search environments where an agent must act after a fixed amount of search time, a common situation in two-player games. It is considered a special case of reinforcement learning algorithms designed for stochastic environments.

## Properties and Limitations
The algorithm's policy is described as "optimism under uncertainty," as it always heads for the closest unvisited state. This exploration pattern can be less efficient than simple depth-first search in uninformed cases where no heuristic information is available. Several informed variants on the LRTA* theme have been developed with different methods for searching and updating within the known portion of the graph.

## Relationships

- **developed-by**: [[richard-korf|Richard Korf]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*