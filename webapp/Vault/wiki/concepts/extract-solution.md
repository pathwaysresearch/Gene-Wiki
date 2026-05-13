---
type: concept
aliases: [EXTRACT-SOLUTION]
summary: An algorithm that attempts to find a valid plan from a completed planning graph once the graph has been expanded to a level where all goals are present and non-mutex.
relationships:
  - target: planning-graph
    type: uses
  - target: backward-search
    type: can-be-implemented-as
tags: [planning, search-algorithm, plan-extraction]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# EXTRACT-SOLUTION

## Overview
Once a planning graph has been constructed to a level *Sₙ* where all goal literals are present and no two are mutex with each other, the EXTRACT-SOLUTION algorithm is invoked to search for an actual plan. The planning graph itself does not represent a valid plan, only a relaxed structure from which a plan might be extracted.

## Formulation as Backward Search
One way to implement EXTRACT-SOLUTION is as a backward search problem. The search begins at the final level of the graph, *Sₙ*, with the set of goals from the original problem. An "action" in this search involves selecting a conflict-free subset of actions from the preceding action level, *Aₙ₋₁*, whose effects cover the current set of goals. The new state for the search is then at level *Sₙ₋₁* with the preconditions of the selected actions as the new set of goals.

## Search Process and Goal
The goal of this backward search is to reach a state at level S₀ where all subgoals are satisfied by the initial state of the planning problem. A set of actions is considered "conflict-free" if no two actions in the set are mutex and no two of their preconditions are mutex. If the search succeeds, it has found a valid plan; if it fails, the planning graph must be expanded to the next level and the process is repeated.

## Relationships

- **uses**: [[planning-graph|Planning Graph]]
- **can-be-implemented-as**: [[backward-search|Backward Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*