---
type: concept
aliases: [Machine Translation]
summary: A sub-field of computational linguistics that uses software to translate text or speech from a source language to a target language.
relationships:
  - target: natural-language-processing
    type: is_a_subfield_of
  - target: language-model
    type: uses
tags: [nlp, computational-linguistics, translation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Machine Translation

## Overview
Machine translation (MT) is one of the oldest and most important tasks in artificial intelligence and natural language processing. The goal is to create systems that can automatically translate content between human languages. Early approaches were often rule-based, but the text focuses on modern statistical methods.

## Statistical Machine Translation
Statistical Machine Translation (SMT) became the dominant paradigm by treating translation as a machine learning problem. Instead of relying on hand-crafted linguistic rules, SMT systems learn to translate by analyzing vast amounts of parallel text corpora (texts available in both source and target languages). The core of SMT is to find the most probable translation of a source sentence by building probabilistic models from the data.

## Core Components
An SMT system typically combines two key models. The first is a translation model, which learns the probability of words or phrases in the target language being translations of words or phrases in the source language. The second is a `language model` for the target language, which calculates the probability of a given sequence of words, ensuring that the output is fluent and grammatically plausible. The system searches for a translation that maximizes the combination of these two models' scores.

## Relationships

- **is_a_subfield_of**: [[natural-language-processing|Natural Language Processing]]
- **uses**: [[language-model|Language Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*