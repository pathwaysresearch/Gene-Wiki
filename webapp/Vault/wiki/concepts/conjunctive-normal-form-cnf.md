---
type: concept
aliases: [Conjunctive Normal Form (CNF)]
summary: A standard representation of a logical sentence as a conjunction of clauses, where each clause is a disjunction of literals.
relationships:
  - target: resolution-inference-rule
    type: is-a-prerequisite-for
  - target: de-morgans-laws
    type: uses
tags: [logic, knowledge-representation, normal-form]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conjunctive Normal Form (CNF)

## Definition
A sentence is in Conjunctive Normal Form (CNF) if it is expressed as a conjunction (AND) of one or more clauses, where each clause is a disjunction (OR) of literals. A literal is an atomic proposition or its negation. For example, (A ∨ ¬B) ∧ (B ∨ C ∨ ¬D) is in CNF.

## Conversion Process
Any sentence in propositional logic can be converted into an equivalent sentence in CNF. The text outlines a multi-step procedure: first, eliminate biconditionals (⇔) and implications (⇒); second, move negations (¬) inward using De Morgan's laws and double-negation elimination; third, apply the distributivity law (distributing ∨ over ∧) to create a conjunction of disjunctions.

## Application
The primary application of CNF discussed in the text is as a required input format for the resolution inference rule. While the CNF representation can be much harder for humans to read than the original sentence, its standardized structure is ideal for algorithmic manipulation by a resolution-based theorem prover.

## Relationships

- **is-a-prerequisite-for**: [[resolution-inference-rule|Resolution Inference Rule]]
- **uses**: [[de-morgans-laws|De Morgans Laws]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*