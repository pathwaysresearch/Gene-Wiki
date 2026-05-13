---
type: concept
aliases: [Propositionalization]
summary: A technique for first-order inference that involves converting a first-order knowledge base and query into propositional logic to leverage propositional inference methods.
relationships:
  - target: first-order-logic
    type: inference-method-for
  - target: jacques-herbrand
    type: relies-on-theorem-by
  - target: universal-instantiation
    type: uses
tags: [inference, first-order-logic, propositional-logic]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Propositionalization

## Definition
Propositionalization is a general method for performing inference in first-order logic. The core idea is to convert the entire first-order knowledge base and query into a set of propositional sentences in such a way that entailment is preserved, after which standard propositional inference algorithms can be used.

## How It Works
The process involves instantiating universally quantified sentences with all possible ground terms. For example, the first-order sentence `∀ x King(x) ∧ Greedy(x) ⇒ Evil(x)` would be replaced by a set of propositional sentences like `King(John) ∧ Greedy(John) ⇒ Evil(John)` and `King(Richard) ∧ Greedy(Richard) ⇒ Evil(Richard)` for all known constants.

## Limitations and Solutions
A significant challenge arises when the knowledge base contains function symbols, such as `Father`. This allows for the construction of an infinite number of ground terms (e.g., `Father(John)`, `Father(Father(John))`, etc.), which would lead to an infinitely large propositional knowledge base. This problem is addressed by a theorem from Jacques Herbrand (1930), which proves that if a sentence is entailed, a proof exists using only a finite subset of the propositionalized knowledge base. This allows for an incremental generation of instantiations until a proof is found, making the approach complete.

## Relationships

- **inference-method-for**: [[first-order-logic|First Order Logic]]
- **relies-on-theorem-by**: [[jacques-herbrand|Jacques Herbrand]]
- **uses**: [[universal-instantiation|Universal Instantiation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*