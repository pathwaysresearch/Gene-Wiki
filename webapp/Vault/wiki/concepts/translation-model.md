---
type: concept
aliases: [Translation Model]
summary: A probabilistic model in SMT that estimates the probability of a source language sentence being a translation of a given target language sentence.
relationships:
  - target: statistical-machine-translation
    type: component_of
tags: [natural-language-processing, probabilistic-models, smt]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Translation Model

## Definition
A translation model is a core component of a Statistical Machine Translation (SMT) system that quantifies the relationship between sentences in two different languages. It is represented as P(e|f), which is the probability of an English sentence 'e' being the translation for a given French sentence 'f'. The model P(f|e) is also a translation model, but in the opposite direction.

## Role in Statistical Machine Translation
The translation model is responsible for ensuring the fidelity or adequacy of the translation. It learns correspondences between words and phrases from a large parallel corpus. For a given target language sentence 'f', the model assigns a higher probability to source language sentences 'e' that are likely translations. This component captures the lexical and structural mappings between the source and target languages.

## Modeling Direction
The text notes that while the ultimate goal is to compute P(f|e), it is common practice in SMT to apply Bayes' rule and instead model P(e|f) and P(f). This is analogous to diagnostic reasoning where it is often easier to model P(symptoms|disease) than the other way around. In translation, however, both directions are considered equally easy to model, and the choice is often based on the specific architecture of the SMT system.

## Relationships

- **component_of**: [[statistical-machine-translation|Statistical Machine Translation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*