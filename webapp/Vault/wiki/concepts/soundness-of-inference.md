---
type: concept
aliases: [Soundness (of inference)]
summary: A property of an inference algorithm ensuring that it only derives sentences that are logically entailed by the knowledge base, making it "truth-preserving."
relationships:
  - target: inference-in-logic
    type: is-a-property-of
  - target: entailment
    type: preserves
  - target: tt-entails
    type: is-an-example-of
tags: [logic, inference, property]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Soundness (of inference)

## Definition
An inference algorithm is called sound or truth-preserving if it exclusively derives sentences that are entailed by the knowledge base. In other words, if an algorithm derives α from KB (KB ⊢ α), then it must be the case that KB entails α (KB ⊨ α).

## Importance
Soundness is a highly desirable property for any reasoning system. An unsound inference procedure is unreliable because it can "make things up" or announce conclusions that are not logically supported by the available knowledge. This is likened to announcing the discovery of nonexistent needles in a haystack.

## Examples
The model-checking algorithm `TT-ENTAILS?` is given as an example of a sound procedure. It is sound because it directly implements the definition of entailment by checking all relevant models, ensuring no conclusion is drawn unless it holds in every model where the knowledge base is true.

## Relationships

- **is-a-property-of**: [[inference-in-logic|Inference In Logic]]
- **preserves**: [[entailment|Entailment]]
- **is-an-example-of**: [[tt-entails|Tt Entails]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*