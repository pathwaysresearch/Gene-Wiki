---
type: concept
aliases: [Constraint Learning]
summary: A technique in CSP solving where the causes of failures are identified and recorded as new constraints (no-goods) to avoid repeating the same mistakes.
relationships:
  - target: conflict-directed-backjumping
    type: is-used-with
tags: [csp-solver, search-strategy, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Constraint Learning

## Definition
Constraint learning is the idea of finding a minimum set of variables from a conflict set that causes a problem. This set of variables, along with their corresponding values, is called a no-good. The no-good is then recorded to prevent the search from running into the same problem again.

## How It Works
When the search arrives at a contradiction, it means that some subset of the current assignments is inconsistent. Constraint learning analyzes the conflict set to identify a minimal subset of variable-value pairs responsible for the failure. This minimal set, or no-good, is then recorded, often by adding a new constraint to the problem.

## Purpose
The primary goal of constraint learning is to avoid redundant work. By explicitly forbidding combinations of assignments that are known to lead to failure, the solver can prune the search space more effectively in other parts of the tree. It is a way for the search algorithm to "remember" what it has learned from its failures, leading to more efficient problem-solving.

## Relationships

- **is-used-with**: [[conflict-directed-backjumping|Conflict Directed Backjumping]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*