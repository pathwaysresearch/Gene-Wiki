---
type: concept
aliases: [Horizon Effect]
summary: A problem in fixed-depth AI search where a negative event is pushed beyond the search limit, causing the algorithm to mistakenly favor a losing line of play.
relationships:
  - target: alpha-beta-pruning
    type: is-a-limitation-of
tags: [adversarial-search, search-algorithm, ai-in-games, limitation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Horizon Effect

## Definition
The horizon effect is a problem that can occur in AI search algorithms that use a fixed-depth search. It happens when the algorithm makes a move to delay an inevitable negative outcome, pushing that outcome just beyond the search depth limit, or "horizon." This can cause the algorithm to incorrectly evaluate the current position as favorable because the negative consequence is not visible within its search range.

## Example in Chess
The text provides a clear example from chess. A program controlling the black pieces might face the certain loss of its bishop. However, it can make a series of pawn sacrifices to check the white king. These checks force a response from white, delaying the capture of the bishop. The search algorithm, with its limited depth, sees the pawn sacrifices as good moves because the loss of the bishop is pushed over its search horizon.

## Impact on Decision Making
This effect leads the search algorithm to make poor strategic decisions. It mistakes delaying tactics for genuinely good moves, failing to recognize that it is simply postponing an unavoidable loss, potentially into an even worse position. It is a fundamental limitation of relying on a fixed-depth cutoff with an evaluation function.

## Relationships

- **is-a-limitation-of**: [[alpha-beta-pruning|Alpha Beta Pruning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*