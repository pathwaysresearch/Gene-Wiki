---
type: concept
aliases: [Conjunct Ordering Problem]
summary: The problem of finding an optimal ordering of conjuncts in a rule's premise to minimize the total cost of evaluation during inference.
tags: [optimization, query-planning, inference]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conjunct Ordering Problem

## Definition
The conjunct ordering problem is the task of finding an ordering for the conjuncts in a rule's premise that minimizes the total cost of solving them. The choice of order can have a significant impact on performance.

## Complexity and Heuristics
Finding the optimal ordering is an NP-hard problem. However, good heuristics are available to find a reasonably efficient order. For example, the minimum-remaining-values (MRV) heuristic, also used for Constraint Satisfaction Problems, can be applied. This heuristic would suggest ordering conjuncts to test the most constrained parts first, such as checking for 'missiles' if there are fewer missiles than other objects in the knowledge base.

## Example
The text illustrates the problem with an example: to find a missile owned by Nono, it is better to first find all missiles (if there are few) and then check for ownership, rather than finding all objects owned by Nono (if there are many) and then checking if they are missiles.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*