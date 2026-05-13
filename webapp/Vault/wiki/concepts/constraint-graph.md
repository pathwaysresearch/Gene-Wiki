---
type: concept
aliases: [Constraint Graph]
summary: A graph that represents the structure of a constraint satisfaction problem, with nodes for variables and edges for binary constraints between them.
relationships:
  - target: constraint-satisfaction-problem
    type: represents
tags: [csp, graph-theory, data-structure]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Constraint Graph

## Definition
A constraint graph is a visual and structural representation of a Constraint Satisfaction Problem (CSP). In this graph, the nodes correspond to the variables of the problem, and an edge or link connects any two variables that participate in a shared constraint.

## Role in Formulation
Visualizing a problem as a constraint graph is presented as a helpful step in formulating it as a CSP. It makes the relationships between variables explicit. For example, in the Australia map-coloring problem, the states and territories are the nodes, and an edge connects South Australia (SA) and Western Australia (WA) because of the constraint that they cannot have the same color.

## Extensions for Complex Constraints
The standard constraint graph represents binary constraints. For n-ary constraints involving more than two variables, a more complex structure called a constraint hypergraph is used. Another related concept is the dual graph transformation, which can convert an n-ary CSP into a binary one by creating a new graph where variables represent the original constraints.

## Relationships

- **represents**: [[constraint-satisfaction-problem|Constraint Satisfaction Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*