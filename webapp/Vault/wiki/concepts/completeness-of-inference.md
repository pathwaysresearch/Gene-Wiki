---
type: concept
aliases: [Completeness (of inference)]
summary: A property of an inference algorithm ensuring that it is capable of deriving any sentence that is logically entailed by the knowledge base.
relationships:
  - target: inference-in-logic
    type: is-a-property-of
  - target: resolution-inference-rule
    type: provides
  - target: tt-entails
    type: is-an-example-of
tags: [logic, inference, property]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Completeness (of inference)

## Definition
An inference algorithm is complete if it can derive every sentence that is logically entailed by the knowledge base. Formally, if KB entails α (KB ⊨ α), then a complete algorithm *i* can derive α from KB (KB ⊢i α).

## Importance
Completeness is a desirable property that guarantees an inference procedure will not miss any valid conclusions. While for finite problems it might seem trivial, it becomes a critical issue for knowledge bases where the set of consequences is infinite. A complete algorithm ensures that if an entailed sentence exists, it can be found.

## Examples
The model-checking algorithm `TT-ENTAILS?` is complete for propositional logic because it can always terminate after checking a finite number of models. The resolution inference rule, when combined with a complete search algorithm, also yields a complete inference procedure for propositional logic.

## Relationships

- **is-a-property-of**: [[inference-in-logic|Inference In Logic]]
- **provides**: [[resolution-inference-rule|Resolution Inference Rule]]
- **is-an-example-of**: [[tt-entails|Tt Entails]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*