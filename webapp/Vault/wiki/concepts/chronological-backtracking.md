---
type: concept
aliases: [Chronological Backtracking]
summary: The standard backtracking method where, upon failure, the search backs up to the most recent decision point and tries a different value.
relationships:
  - target: backtracking-search
    type: is-a-type-of
  - target: conflict-directed-backjumping
    type: is-less-efficient-than
tags: [search-strategy, backtracking]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Chronological Backtracking

## Definition
Chronological backtracking is the simplest strategy for backtracking in a search algorithm. When a branch of the search fails because a variable has no legal values left, the algorithm backs up to the preceding variable in the assignment order and tries a different value for it.

## How It Works
This method follows a strict temporal order of decisions. If an assignment to variable Xk leads to a dead end at a later variable Xm, the algorithm will undo the assignment to Xm, then Xm-1, and so on, until it reaches Xk-1. It then tries a new value for Xk-1. It is called "chronological" because it revisits the most recent decision point, regardless of what actually caused the failure.

## Limitations
This simple policy can be very inefficient. The failure might be caused by an assignment made much earlier in the search, but chronological backtracking will still explore all other options for the intermediate variables before correcting the root cause. More intelligent methods like conflict-directed backjumping are designed to overcome this limitation by identifying the source of the conflict and jumping directly to it.

## Relationships

- **is-a-type-of**: [[backtracking-search|Backtracking Search]]
- **is-less-efficient-than**: [[conflict-directed-backjumping|Conflict Directed Backjumping]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*