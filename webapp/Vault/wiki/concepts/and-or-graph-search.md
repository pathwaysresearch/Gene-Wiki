---
type: concept
aliases: [AND-OR Graph Search]
summary: A search algorithm for finding a contingency plan in nondeterministic environments by navigating a graph with alternating OR nodes (actions) and AND nodes (outcomes).
relationships:
  - target: contingency-plan
    type: generates
tags: [search-algorithm, planning, nondeterminism, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# AND-OR Graph Search

## Definition
AND-OR graph search is an algorithm designed to find a conditional plan (or contingency plan) to solve problems in nondeterministic environments. It explores a search tree where states are represented as OR nodes and the possible outcomes of actions are represented as AND nodes. This structure reflects the nature of the problem: the agent must choose an action (an OR choice) and then be prepared to handle any of the possible outcomes of that action (an AND requirement).

## How It Works
The search alternates between two main functions, `OR-SEARCH` and `AND-SEARCH`. `OR-SEARCH` is called on a state (an OR node) and tries to find an action that leads to a solution. For each possible action, it calls `AND-SEARCH` on the set of possible resulting states. `AND-SEARCH` is called on a set of outcomes (an AND node) and must find a plan for *every* state in the set. If it can find a sub-plan for each outcome, it combines them into a conditional plan. A solution is found when a plan is constructed that successfully handles all contingencies back to the initial state.

## Application
The algorithm is suited for problems like the erratic vacuum world, where an action like `Suck` can have multiple outcomes (e.g., success or failure). The search tree would have an OR node for the choice of action (`Suck`, `Left`, `Right`) and an AND node for the possible outcomes of the chosen action. The final solution is a conditional plan that specifies what to do in each case, ensuring the agent can reach a goal state regardless of which outcome occurs.

## Relationships

- **generates**: [[contingency-plan|Contingency Plan]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*