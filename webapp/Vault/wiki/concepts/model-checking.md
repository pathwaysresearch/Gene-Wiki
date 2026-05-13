---
type: concept
aliases: [Model Checking]
summary: An inference algorithm that determines logical entailment by systematically enumerating all possible models and checking if the conclusion is true in every model where the knowledge base is true.
relationships:
  - target: entailment
    type: is-an-algorithm-for
  - target: tt-entails
    type: is-implemented-as
  - target: model-in-logic
    type: enumerates
tags: [logic, inference, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Model Checking

## Definition
Model checking is an inference procedure that directly implements the definition of entailment (KB ⊨ α). It works by enumerating all possible models for the proposition symbols involved. For each model, it checks if the knowledge base (KB) is true. If it is, it then checks if the query sentence (α) is also true in that model. Entailment holds if α is true in all such models.

## Properties
This approach is both sound and complete for propositional logic. It is sound because it is a direct implementation of the definition of entailment. It is complete because it examines every possible model, guaranteeing that if an entailment holds, it will be found. The algorithm always terminates because there is a finite number of models.

## Complexity and Limitations
The primary drawback of model checking is its computational complexity. If a knowledge base and query contain *n* distinct proposition symbols, there are 2^n possible models to check. This makes the algorithm's time complexity O(2^n), which is infeasible for large *n*. The `TT-ENTAILS?` algorithm is a specific implementation of this approach.

## Relationships

- **is-an-algorithm-for**: [[entailment|Entailment]]
- **is-implemented-as**: [[tt-entails|Tt Entails]]
- **enumerates**: [[model-in-logic|Model In Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*