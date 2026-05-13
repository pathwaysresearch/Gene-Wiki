---
type: concept
aliases: [Language Model]
summary: A probabilistic model that assigns a probability to a sequence of words, indicating how likely that sequence is in a given language.
relationships:
  - target: statistical-machine-translation
    type: component_of
tags: [natural-language-processing, probabilistic-models, smt]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Language Model

## Definition
A language model is a probabilistic model that determines the likelihood of a given sequence of words occurring in a particular language. In the context of Statistical Machine Translation (SMT), it is represented as the factor P(f), where 'f' is a sentence in the target language.

## Role in Statistical Machine Translation
Within the SMT framework, the language model's primary function is to ensure the fluency and grammatical correctness of the translated output. When translating an English sentence 'e' to a French sentence 'f', the system generates many possible French sentences. The language model P(f) assigns a probability to each candidate sentence, favoring those that are more natural and idiomatic in French. For example, it would assign a higher probability to a sentence with correct adjective-noun ordering in French than one that follows English word order.

## Function
The language model works independently of the source text. Its sole purpose is to evaluate the quality of the target language sentence on its own terms. By multiplying the translation model's score with the language model's score, SMT systems balance the faithfulness of the translation with the fluency of the output.

## Relationships

- **component_of**: [[statistical-machine-translation|Statistical Machine Translation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*