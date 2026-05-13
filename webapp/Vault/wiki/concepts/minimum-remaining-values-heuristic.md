---
type: concept
aliases: [Minimum-Remaining-Values (MRV) Heuristic]
summary: A domain-independent heuristic for variable selection in CSP search that chooses the variable with the fewest legal values remaining in its domain.
relationships:
  - target: backtracking-search
    type: enhances
  - target: constraint-satisfaction-problems
    type: applies-to
tags: [heuristic, search-algorithms, csp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Minimum-Remaining-Values (MRV) Heuristic

## Definition
The minimum-remaining-values (MRV) heuristic is a strategy used in backtracking search to decide which variable to assign a value to next. It selects the variable that has the fewest legal values left in its domain. This is also known as the most-constrained-variable heuristic.

## Rationale
The intuition behind this heuristic is to handle the most difficult parts of the problem first. By choosing the variable with the fewest options, the search is more likely to detect a failure early, which allows for pruning large sections of the search space. This 'fail-first' approach often leads to a more efficient search process overall.

## Historical Context
The text attributes the introduction of the MRV heuristic to Bitner and Reingold (1975), who originally called it the most-constrained-variable heuristic. It also notes that Brelaz (1979) used the degree heuristic as a tiebreaker after applying MRV, creating a powerful combination that remains one of the best methods for k-coloring arbitrary graphs.

## Relationships

- **enhances**: [[backtracking-search|Backtracking Search]]
- **applies-to**: [[constraint-satisfaction-problems|Constraint Satisfaction Problems]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*