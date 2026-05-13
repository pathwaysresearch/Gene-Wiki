---
type: concept
aliases: [Arc Consistency]
summary: A property in a CSP where every value in a variable's domain is consistent with some value in the domain of another variable for a given binary constraint.
relationships:
  - target: constraint-satisfaction-problem
    type: is-property-of
tags: [csp, constraint-propagation, inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Arc Consistency

## Definition
A variable Xi is defined as arc-consistent with respect to another variable Xj if for every value in the current domain of Xi, there exists at least one value in the domain of Xj that satisfies the binary constraint on the arc connecting them. A network is considered arc-consistent if every variable is arc-consistent with every other variable.

## Role in Problem Solving
Enforcing arc consistency is a key inference technique that can significantly reduce the domains of variables in a CSP. This reduction can sometimes be sufficient to find a unique solution (by reducing every domain to a single value) or to prove that no solution exists (by reducing a domain to an empty set). It is a fundamental step in many CSP solvers.

## Limitations and Extensions
Arc consistency alone may not be powerful enough to solve all problems. The text provides an example of coloring a map with only two colors where arc consistency fails to make any inferences, even though the problem is unsolvable. The concept is extended to handle n-ary constraints through a technique called generalized arc consistency (or hyperarc consistency), which ensures that for any value of a variable, a valid tuple of values exists for the other variables in the n-ary constraint.

## Relationships

- **is-property-of**: [[constraint-satisfaction-problem|Constraint Satisfaction Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*