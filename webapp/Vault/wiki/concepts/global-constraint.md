---
type: concept
aliases: [Global Constraint]
summary: A type of constraint in a Constraint Satisfaction Problem that involves an arbitrary number of variables and is often handled by special-purpose algorithms.
relationships:
  - target: alldiff-constraint
    type: has-example
tags: [constraint-satisfaction-problem, constraint-propagation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Global Constraint

## Definition
A global constraint is a constraint that involves an arbitrary number of variables, as opposed to binary constraints that involve only pairs. They are common in real-world problems because they can represent complex relationships more efficiently than a large collection of smaller constraints.

## How It Works
Instead of being decomposed into a set of smaller constraints, global constraints are handled by dedicated, special-purpose algorithms. These algorithms are typically more efficient for the specific structure they represent than general-purpose methods. They can perform more powerful forms of inconsistency detection by considering the interaction of all variables in the constraint simultaneously.

## Example: Alldiff
A prominent example is the Alldiff constraint, which requires that all variables in the constraint's scope must have distinct values. For instance, in a Sudoku puzzle, all the variables in a single row form an Alldiff constraint. An inconsistency can be detected if the number of variables involved in an Alldiff constraint is greater than the total number of unique values available in their combined domains.

## Relationships

- **has-example**: [[alldiff-constraint|Alldiff Constraint]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*