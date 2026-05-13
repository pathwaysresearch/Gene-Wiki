---
type: concept
aliases: [Truth Table]
summary: A tabular method used in logic to define the semantics of logical connectives by showing the truth value of a complex sentence for all possible truth value assignments to its components.
relationships:
  - target: propositional-logic
    type: defines-semantics-for
  - target: model-checking
    type: is-the-basis-for
tags: [logic, semantics, method]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Truth Table

## Definition
A truth table is a mathematical table that specifies the truth value of a logical expression for each possible assignment of truth values to its propositional variables. It provides a systematic way to define the meaning of logical connectives.

## How It Works
Each row of a truth table corresponds to one possible model (one combination of truth values for the atomic propositions). The columns show the atomic propositions and the complex sentence being evaluated. The entry in the final column of a given row shows the truth value of the complex sentence in that specific model.

## Application
Truth tables are used to define the five standard logical connectives (negation, conjunction, disjunction, implication, biconditional). They also form the basis for the model-checking approach to inference, where the truth of a knowledge base and a query sentence can be evaluated across all possible models to determine entailment.

## Relationships

- **defines-semantics-for**: [[propositional-logic|Propositional Logic]]
- **is-the-basis-for**: [[model-checking|Model Checking]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*