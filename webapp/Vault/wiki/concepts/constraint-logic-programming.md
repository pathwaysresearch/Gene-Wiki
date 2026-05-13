---
type: concept
aliases: [Constraint Logic Programming]
summary: A form of logic programming that allows variables to be constrained rather than immediately bound, enabling it to solve problems over infinite domains.
tags: [logic-programming, constraint-satisfaction, prolog]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Constraint Logic Programming

## Definition
Constraint Logic Programming (CLP) is an extension of logic programming where variables are handled by imposing constraints on them rather than binding them to specific values. The solution to a CLP query is the most specific set of constraints on the variables in the query that can be derived from the program.

## How It Works
Unlike standard Prolog, which uses a backtracking algorithm to enumerate the domains of variables, CLP employs algorithms such as bounds propagation or linear programming. This allows it to handle infinite-domain constraint satisfaction problems (CSPs), such as those involving integer or real-valued variables, which are intractable for standard backtracking.

## Advantages over Standard Prolog
Standard Prolog is limited to finite-domain CSPs because it must enumerate a finite number of solutions for goals with unbound variables. For example, a Prolog query like `triangle(3,4,Z)` will fail because it cannot handle a subgoal like `Z>=0` where `Z` is unbound. CLP is designed to overcome this limitation by working with the constraints themselves, making it possible to solve problems that are impossible to express or solve in standard Prolog.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*