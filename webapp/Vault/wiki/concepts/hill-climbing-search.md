---
type: concept
aliases: [Hill-Climbing Search]
summary: A local search algorithm that iteratively moves in the direction of increasing value (uphill) to find a peak or maximum of the state-space landscape, but is susceptible to getting stuck in local optima.
relationships:
  - target: simulated-annealing
    type: is-related-to
  - target: gradient-descent
    type: is-a-discrete-version-of
tags: [local-search, optimization, search-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Hill-Climbing Search

## Definition
Hill-climbing search is a local search algorithm that continuously attempts to move to a better state in the problem's state-space landscape. It is also known as greedy local search because it selects the best-looking immediate neighbor without considering the longer-term path. The algorithm terminates when it reaches a peak where no neighboring state has a higher value.

## How It Works
The algorithm maintains only the current state. In the steepest-ascent variant, it examines all possible successors of the current state and chooses the one with the best value. For example, in the 8-queens problem, this involves evaluating the heuristic cost for all states reachable by moving a single queen within its column and selecting the move that results in the lowest cost (highest value).

## Limitations
Hill-climbing algorithms are incomplete and can fail to find a solution. They are prone to getting stuck at a **local maximum**, a state that is better than all its neighbors but is not the global maximum. Other common problems include navigating **ridges**, which are sequences of local maxima, and getting lost on **plateaux**, which are flat areas of the state space where no uphill progress is possible. For the 8-queens problem, steepest-ascent hill climbing gets stuck 86% of the time.

## Relationships

- **is-related-to**: [[simulated-annealing|Simulated Annealing]]
- **is-a-discrete-version-of**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*