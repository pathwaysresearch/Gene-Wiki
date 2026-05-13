---
type: concept
aliases: [Backward Search (Regression)]
summary: A planning algorithm that searches backward from the goal state towards the initial state by determining the predecessor states from which a goal can be reached.
relationships:
  - target: state-space-search
    type: is-a
  - target: extract-solution
    type: used-by
tags: [planning, search-algorithm, regression]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Backward Search (Regression)

## Definition
Backward search, also known as regression search, is a state-space search strategy for planning problems. Instead of searching forward from the initial state (progression), it starts with the goal description and works backward, looking for a path to the initial state.

## How It Works
Backward search operates by regressing a state description over an action to find the predecessor state description. For a given ground goal description *g* and a ground action *a* that achieves part of *g*, the regression process calculates a new goal description *g'* that must have been true before action *a* was executed. The Planning Domain Definition Language (PDDL) is specifically designed to make this regression process straightforward.

## Regression Formula
The predecessor state description *g'* is derived from the goal *g* and action *a* using the formula: *g'* = (*g* − ADD(*a*)) ∪ Precond(*a*). This means the effects added by the action (ADD(*a*)) are removed from the goal, and the action's preconditions (Precond(*a*)) are added as the new subgoals that must have been true in the preceding state. The deleted effects (DEL(*a*)) are not used because their status before the action is unknown.

## Relationships

- **is-a**: [[state-space-search|State Space Search]]
- **used-by**: [[extract-solution|Extract Solution]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*