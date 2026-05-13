---
type: concept
aliases: [Conflict-Directed Backjumping]
summary: An intelligent backtracking strategy that analyzes the cause of a failure (the conflict set) to jump back directly to the source of the conflict, rather than to the most recent variable. An advanced backtracking technique for CSPs that analyzes the conflict causing a dead end and jumps back directly to the source variable of the conflict, rather than just to the immediately preceding variable.
relationships:
  - target: chronological-backtracking
    type: is-an-improvement-on
  - target: constraint-learning
    type: is-related-to
  - target: backtracking-search
    type: is-an-enhancement-of
tags: [search-strategy, backtracking, csp-solver, search-algorithms, csp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conflict-Directed Backjumping

## Definition
Conflict-directed backjumping is an advanced form of backtracking that improves upon chronological backtracking. When the search reaches a dead end for a variable, it analyzes the set of previously assigned variables that are in conflict with it—the "conflict set"—and backjumps to the most recently assigned variable within that set.

## How It Works
During the search, the algorithm maintains a conflict set for the current variable Xi. If every possible value for Xi fails, the algorithm backjumps to the most recent variable Xj in the conflict set of Xi. The conflict set of Xi is then merged into the conflict set of Xj (minus Xj itself), effectively passing the information about the cause of the failure back up the search tree. This ensures the search addresses the actual source of the problem.

## Advantage Over Chronological Backtracking
This method avoids wasting time exploring irrelevant choices. By jumping directly to a variable responsible for the conflict, it can prune large parts of the search space that chronological backtracking would have explored needlessly. It prevents the algorithm from trying to fix the problem by changing variables that had nothing to do with the failure.

## Relationships

- **is-an-improvement-on**: [[chronological-backtracking|Chronological Backtracking]]
- **is-related-to**: [[constraint-learning|Constraint Learning]]
- **is-an-enhancement-of**: [[backtracking-search|Backtracking Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*