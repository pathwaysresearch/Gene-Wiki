---
type: entity
aliases: [TT-ENTAILS?]
summary: A specific model-checking algorithm for propositional logic that determines entailment by recursively enumerating all possible models.
relationships:
  - target: model-checking
    type: is-an-implementation-of
  - target: soundness-of-inference
    type: exhibits
  - target: completeness-of-inference
    type: exhibits
tags: [algorithm, inference, model-checking]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# TT-ENTAILS?

## Overview
`TT-ENTAILS?` is a specific algorithm presented for deciding entailment in propositional logic. It is a direct implementation of the model-checking approach, which verifies if a knowledge base (KB) entails a sentence (α) by checking all possible models.

## Algorithm and Properties
The algorithm functions as a recursive enumeration of the finite space of assignments to proposition symbols, similar to a backtracking search. It is proven to be sound because it directly implements the formal definition of entailment. It is also complete because it works for any KB and α and is guaranteed to terminate, as there are only a finite number of models to examine.

## Complexity
The primary limitation of `TT-ENTAILS?` is its time complexity. If the total number of unique proposition symbols in the KB and α is *n*, the algorithm must check 2^n models in the worst case. This results in a time complexity of O(2^n), making it impractical for problems with many variables, despite its space complexity being only O(n).

## Relationships

- **is-an-implementation-of**: [[model-checking|Model Checking]]
- **exhibits**: [[soundness-of-inference|Soundness Of Inference]]
- **exhibits**: [[completeness-of-inference|Completeness Of Inference]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*