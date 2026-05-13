---
type: entity
aliases: [De Morgan's Laws]
summary: A pair of transformation rules in formal logic that define the relationship between conjunction, disjunction, and negation.
relationships:
  - target: conjunctive-normal-form-cnf
    type: is-used-in-conversion-to
tags: [logic, rule, equivalence]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# De Morgan's Laws

## Overview
De Morgan's laws are a pair of rules governing logical equivalences. They provide a method for distributing a negation operator over conjunctions and disjunctions.

## The Rules
The laws are stated as:
1. The negation of a conjunction is the disjunction of the negations: ¬(α ∧ β) ≡ (¬α ∨ ¬β).
2. The negation of a disjunction is the conjunction of the negations: ¬(α ∨ β) ≡ (¬α ∧ ¬β).

## Application in CNF Conversion
These laws are a crucial step in the process of converting a propositional logic sentence into Conjunctive Normal Form (CNF). Specifically, they are used to "move negation inwards" so that the ¬ operator only applies to atomic proposition symbols (creating literals), which is a requirement for the CNF format.

## Relationships

- **is-used-in-conversion-to**: [[conjunctive-normal-form-cnf|Conjunctive Normal Form Cnf]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*