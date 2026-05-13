---
type: concept
aliases: [Semantics (in logic)]
summary: The field of logic concerned with meaning, specifically defining the truth of sentences with respect to possible worlds or models.
relationships:
  - target: model-in-logic
    type: defines-truth-via
  - target: truth-table
    type: is-defined-by
  - target: propositional-logic
    type: is-a-component-of
tags: [logic, knowledge-representation, meaning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Semantics (in logic)

## Definition
Semantics defines the meaning of sentences in a logic. Its primary function is to determine the truth of each sentence in every possible world. In standard logics, every sentence is required to be either true or false in a given world, with no intermediate values.

## Role of Models
The concept of a "possible world" is formalized through mathematical abstractions called models. Each model fixes the truth or falsehood of every relevant sentence. For instance, in arithmetic, a model could be an assignment of numbers to variables like x=2 and y=2, which would make the sentence "x+y=4" true.

## Truth and Satisfaction
Semantics provides the rules for evaluating the truth of complex sentences based on the truth of their components. For example, the semantics of propositional logic defines how the truth value of a sentence like "P ∧ Q" is determined by the truth values of P and Q. If a sentence α is true in a model m, it is said that m satisfies α, or that m is a model of α.

## Relationships

- **defines-truth-via**: [[model-in-logic|Model In Logic]]
- **is-defined-by**: [[truth-table|Truth Table]]
- **is-a-component-of**: [[propositional-logic|Propositional Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*