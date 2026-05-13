---
type: concept
aliases: [Domain-Independent Heuristic]
summary: A heuristic for search problems that can be automatically derived from the problem description itself, without requiring domain-specific knowledge.
relationships:
  - target: classical-planning
    type: enabled-by
  - target: planning-graph
    type: is-a
tags: [planning, heuristics, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Domain-Independent Heuristic

## Definition
A domain-independent heuristic is a function that estimates the cost to reach a goal from a given state in a planning problem, which can be generated automatically from the factored representation of states and actions. This contrasts with domain-specific heuristics, which require a human analyst to define. The classical planning formalism is particularly well-suited for creating these heuristics.

## Relaxation Techniques
A common method for creating domain-independent heuristics is to solve a relaxed version of the planning problem. The cost of the solution to the relaxed problem then serves as an admissible heuristic for the original problem. The text describes two main ways to relax a problem: adding more edges to the state-space graph (making it easier to find a path) or grouping nodes together (creating a state-space abstraction).

## Examples of Relaxation
One specific technique is the **ignore preconditions heuristic**, which relaxes the problem by dropping all preconditions from actions, making every action applicable in every state. Another technique is **state abstraction**, which simplifies the problem by ignoring certain fluents. For example, in a large air cargo problem, one might only consider a subset of packages and airports, creating a smaller, abstract state space whose solution provides an admissible heuristic for the original problem.

## Relationships

- **enabled-by**: [[classical-planning|Classical Planning]]
- **is-a**: [[planning-graph|Planning Graph]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*