---
type: concept
aliases: [Sensorless Planning]
summary: A planning approach for agents that have no sensors, requiring them to reason about belief states representing all possible worlds consistent with their knowledge. A planning technique that generates a single sequence of actions guaranteed to achieve a goal from any possible initial state, without requiring any sensory input during execution.
relationships:
  - target: belief-state
    type: uses
  - target: open-world-assumption
    type: relies-on
  - target: contingent-planning
    type: is-an-alternative-to
tags: [planning, uncertainty, robotics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Sensorless Planning

## Definition
Sensorless planning is a type of planning where the agent has no sensors to perceive the world. The agent must generate a plan that works regardless of the initial state or the outcomes of its actions, as long as they are consistent with its initial knowledge. The agent reasons about the percepts it would obtain if it were executing the plan, even though it has no sensors to actually receive them.

## Core Component: Belief States
The central concept in sensorless planning is the belief state, which represents the set of all possible physical worlds the agent might be in. The initial belief state is derived from what the agent knows initially; for example, that objects have colors even if the specific colors are unknown (`∀x ∃c Color(x,c)`). Planning involves finding a sequence of actions that transitions the initial belief state to a final belief state where the goal is satisfied in every possible world.

## Planning Process
To solve a sensorless problem, an agent progresses its belief state through a sequence of actions. An action is applicable if its preconditions are satisfied by the current belief state. The process continues until a belief state is reached that satisfies the goal. Heuristic functions can be used to guide this search, estimating the cost to achieve the goal from a given belief state. The satisfiability of a plan can be checked using a SAT solver by determining if the initial belief state and the successor-state axioms for the plan entail the goal.

## Relationships

- **uses**: [[belief-state|Belief State]]
- **relies-on**: [[open-world-assumption|Open World Assumption]]
- **is-an-alternative-to**: [[contingent-planning|Contingent Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*