---
type: concept
aliases: [Model (First-Order Logic)]
summary: A formal structure in first-order logic that represents a possible world, consisting of a set of objects and an interpretation of symbols.
relationships:
  - target: first-order-logic
    type: component-of
tags: [first-order-logic, semantics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Model (First-Order Logic)

## Definition
A model in first-order logic is a formal structure that represents a possible state of the world. It is composed of a set of objects and an interpretation that connects the language's symbols to these objects and the relationships between them.

## Components
The interpretation within a model maps the syntactic elements of the language to the semantic elements of the world. Specifically, it maps constant symbols to objects, predicate symbols to relations on those objects, and function symbols to functions on those objects. Every model must contain the necessary information to determine the truth value of any sentence.

## Role in Entailment and Validity
Logical concepts such as entailment and validity are defined with respect to all possible models. A key difference from propositional logic is that the number of possible models in first-order logic is unbounded, as models can contain any number of objects from one to infinity. This makes checking entailment by enumerating all models an infeasible computational task.

## Relationships

- **component-of**: [[first-order-logic|First Order Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*