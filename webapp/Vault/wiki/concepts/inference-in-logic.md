---
type: concept
aliases: [Inference (in logic)]
summary: The process of deriving new sentences (conclusions) from a knowledge base using a set of inference rules or an algorithm.
relationships:
  - target: entailment
    type: aims-to-find
  - target: soundness-of-inference
    type: is-characterized-by
  - target: completeness-of-inference
    type: is-characterized-by
  - target: resolution-inference-rule
    type: is-a-method-for
  - target: model-checking
    type: is-a-method-for
tags: [logic, reasoning, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Inference (in logic)

## Definition
Inference is the practical procedure of deriving a sentence α from a knowledge base KB. If an inference algorithm *i* can derive α from KB, this is written as KB ⊢i α. This process is distinct from entailment, which is the underlying logical relationship that inference aims to capture.

## Key Properties
Two crucial properties of inference algorithms are soundness and completeness. A sound algorithm only derives sentences that are actually entailed by the knowledge base, meaning it is truth-preserving. A complete algorithm is capable of deriving every sentence that is entailed.

## Examples of Inference Procedures
The text discusses several inference procedures. One is model checking, which directly implements the definition of entailment by enumerating models. Another is proof by resolution, which uses a single, powerful inference rule to derive new sentences, often after converting the knowledge base to Conjunctive Normal Form (CNF).

## Relationships

- **aims-to-find**: [[entailment|Entailment]]
- **is-characterized-by**: [[soundness-of-inference|Soundness Of Inference]]
- **is-characterized-by**: [[completeness-of-inference|Completeness Of Inference]]
- **is-a-method-for**: [[resolution-inference-rule|Resolution Inference Rule]]
- **is-a-method-for**: [[model-checking|Model Checking]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*