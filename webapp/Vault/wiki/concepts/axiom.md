---
type: concept
aliases: [Axiom (in Logic)]
summary: A statement in a formal language that is stipulated to be true and serves as a premise or starting point for further reasoning and arguments.
relationships:
  - target: first-order-logic
    type: is-a-component-of
  - target: knowledge-engineering
    type: is-produced-by
tags: [logic, knowledge-representation, formal-methods]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Axiom (in Logic)

## Role in Knowledge Representation
Axioms are the foundational sentences in a knowledge base that encode the general knowledge of a domain. They serve as the starting points from which a reasoning system can derive new conclusions, or theorems. The collection of axioms defines the meaning and interrelationships of the terms in the domain's ontology.

## Types of Axioms
The text explains that axioms can serve different purposes. Some axioms are definitions that provide a complete characterization of a predicate (e.g., defining a grandmother as the mother of a parent). Other axioms provide partial specifications without being a complete definition, which is useful for concepts that are not fully understood (e.g., `∀x Person(x) ⇒ ...`). Axioms can also be simple, ground facts that describe a specific problem instance, such as `Male(Jim)` or `Spouse(Jim, Laura)`.

## Example: Axiomatizing Set Theory
The text demonstrates how a complex domain like set theory can be formalized using a collection of axioms in first-order logic. It provides axioms to define fundamental concepts such as the empty set, set membership (`∈`), the subset relation (`⊆`), set equality, intersection (`∩`), and union (`∪`). These axioms collectively provide a formal, logical foundation for reasoning about sets.

## Relationships

- **is-a-component-of**: [[first-order-logic|First Order Logic]]
- **is-produced-by**: [[knowledge-engineering|Knowledge Engineering]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*