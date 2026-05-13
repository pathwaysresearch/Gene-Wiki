---
type: concept
aliases: [Planning Graph]
summary: A data structure used in planning to provide an admissible heuristic by creating a polynomial-size approximation of the search space. A data structure used in planning that consists of alternating layers of literals and actions, encoding reachability information and mutual exclusion (mutex) relations.
relationships:
  - target: domain-independent-heuristic
    type: is-a
  - target: extract-solution
    type: used-by
  - target: graphplan
    type: used-by
  - target: partial-order-planning
    type: provides-heuristics-for
  - target: state-space-search-for-planning
    type: provides-heuristics-for
tags: [planning, data-structure, heuristics, ai-algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Planning Graph

## Definition
A planning graph is a directed, leveled graph that approximates the tree of all possible action sequences from an initial state. It is constructed in polynomial time and provides an estimate of the number of steps required to reach a goal. This estimate is an admissible heuristic because it never overestimates the true cost.

## Structure and Construction
The graph is organized into alternating levels: a state level Sᵢ followed by an action level Aᵢ. The first level, S₀, contains all fluents that are true in the initial state. Each action level Aᵢ contains all ground actions whose preconditions are present and non-mutex in the preceding state level Sᵢ. Each state level Sᵢ₊₁ contains all literals that could result from actions in Aᵢ. The graph construction continues until two consecutive levels are identical, at which point the graph has "leveled off".

## Mutex Links
A key component of the planning graph is the use of **mutex links** to record impossibilities. A mutex relation holds between two actions at a level if they have inconsistent effects, if one interferes with the other's preconditions, or if they have competing needs. A mutex relation holds between two literals at a state level if every possible action that could achieve one is mutex with every possible action that could achieve the other.

## Application as a Heuristic
The planning graph provides a heuristic by estimating the cost to achieve a set of goals. The cost is the index of the first level Sᵢ at which all goal literals appear and are not mutually exclusive (mutex). If a goal literal never appears in the graph, the problem is proven to be unsolvable. While the appearance of a goal at level *i* does not guarantee a plan of length *i* exists, it provides a powerful and admissible estimate.

## Relationships

- **is-a**: [[domain-independent-heuristic|Domain Independent Heuristic]]
- **used-by**: [[extract-solution|Extract Solution]]
- **used-by**: [[graphplan|Graphplan]]
- **provides-heuristics-for**: [[partial-order-planning|Partial Order Planning]]
- **provides-heuristics-for**: [[state-space-search-for-planning|State Space Search For Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*