---
type: concept
aliases: [Ground Resolution Theorem]
summary: A fundamental theorem in propositional logic stating that if a set of clauses is unsatisfiable, its resolution closure will contain the empty clause.
tags: [propositional-logic, inference, theorem]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Ground Resolution Theorem

## Statement of the Theorem

The ground resolution theorem states that if a set of clauses is unsatisfiable, then the resolution closure of those clauses contains the empty clause.

## Proof by Contrapositive

The theorem is proven by demonstrating its contrapositive: if the resolution closure of a set of clauses S, denoted RC(S), does not contain the empty clause, then S must be satisfiable.

## Model Construction

In the case where the closure does not contain the empty clause, a satisfying model for the set of clauses S can be constructed. The procedure involves iterating through the proposition symbols P_1, ..., P_k and assigning a truth value to each based on the existing partial assignment, ensuring no clause in RC(S) is falsified.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*