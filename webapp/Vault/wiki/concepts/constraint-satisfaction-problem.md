---
type: concept
aliases: [Constraint Satisfaction Problem]
summary: A problem formulation where a solution is found by satisfying a set of constraints on variables, each of which has a domain of possible values.
relationships:
  - target: constraint-graph
    type: is-represented-by
  - target: arc-consistency
    type: uses-technique
tags: [problem-formulation, search, artificial-intelligence]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Constraint Satisfaction Problem

## Definition
A Constraint Satisfaction Problem (CSP) is defined by a set of variables, a domain of possible values for each variable, and a set of constraints that specify allowable combinations of values. A solution to a CSP is a complete assignment of values to all variables that is consistent with all constraints, meaning it does not violate any of the constraints.

## Representation
CSPs are often visualized using a constraint graph, where nodes represent variables and edges connect any two variables that participate in a constraint. This graphical representation helps in understanding the structure of the problem. For problems with constraints involving more than two variables (n-ary constraints), a constraint hypergraph can be used, which includes special hypernodes to represent these complex relationships.

## Example Applications
The text illustrates CSPs with several examples. These include map-coloring problems, such as coloring the states of Australia so no adjacent regions share a color; scheduling problems, which can involve disjunctive constraints like two tasks not overlapping in time; and cryptarithmetic puzzles, where letters in an arithmetic problem must be replaced by distinct digits.

## Relationships

- **is-represented-by**: [[constraint-graph|Constraint Graph]]
- **uses-technique**: [[arc-consistency|Arc Consistency]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*