---
type: concept
aliases: [Statistical Machine Translation]
summary: An approach to machine translation that learns a probabilistic model from a large corpus of bilingual text to find the most probable translation of a sentence. An approach to machine translation that uses statistical models, whose parameters are derived from the analysis of bilingual text corpora, to translate text from one language to another.
relationships:
  - target: language-model
    type: uses
  - target: translation-model
    type: uses
tags: [machine-translation, natural-language-processing, probabilistic-models, statistical-methods]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Statistical Machine Translation

## Core Principle
Statistical Machine Translation (SMT) is an approach that frames translation as a probabilistic task. Instead of relying on handcrafted grammars or complex ontologies, SMT systems learn a translation model from a large corpus of existing translations. To translate a source sentence in English (e) into a target sentence in French (f), the goal is to find the French sentence f* that is the most probable translation. This is expressed by the formula: f* = argmax_f P(f|e). Using Bayes' rule, this is typically decomposed into two components: f* = argmax_f P(e|f)P(f).

## Key Components
The SMT framework consists of two primary probabilistic models. The first is the Language Model, P(f), which calculates the probability of a sentence f occurring in the target language (e.g., French). This model ensures that the output is fluent and grammatically correct. The second is the Translation Model, P(e|f), which calculates the probability that the source sentence e is a translation of the target sentence f. This model ensures that the meaning is preserved in the translation.

## Phrase-Based Approach
A common implementation of SMT involves breaking sentences into phrases. The probability of a full translation is calculated by assuming that each phrase translation and its reordering (or 'distortion') is independent of the others. The joint probability of a French phrase sequence `f` with distortions `d` being a translation of an English phrase sequence `e` can be factored as P(f, d|e) = Π_i P(f_i|e_i)P(d_i). The distortion probability, P(d_i), models how likely a phrase is to be moved by a certain number of positions during translation, independent of the words in the phrase.

## Relationships

- **uses**: [[language-model|Language Model]]
- **uses**: [[translation-model|Translation Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*