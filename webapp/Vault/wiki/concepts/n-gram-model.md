---
type: concept
aliases: [N-gram Model]
summary: A statistical language model that assigns probabilities to sequences of n items (such as characters or words) by assuming the probability of an item depends only on the n-1 preceding items.
relationships:
  - target: shortlist-method
    type: used_in
  - target: ensemble-language-models
    type: component_of
  - target: smoothing-in-language-models
    type: requires
tags: [natural-language-processing, language-modeling, statistical-model]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# N-gram Model

## Definition
An n-gram is a contiguous sequence of n items from a given sample of text or speech; the items can be characters, syllables, or words. An n-gram model is a probability distribution over such sequences, formally defined as a Markov chain of order n-1. Special cases include unigrams (n=1), bigrams (n=2), and trigrams (n=3).

## How It Works
As a Markov chain of order n-1, an n-gram model assumes the probability of a given item depends only on the n-1 items that immediately precede it. For example, in a trigram model of characters, the probability of character c_i depends only on the two preceding characters, c_{i-2} and c_{i-1}, not on any other characters further back in the sequence.

## Challenges
Word n-gram models must deal with out-of-vocabulary words, which are words that appear in a test set but not in the training corpus. A common technique is to add a special token, `<UNK>`, to the vocabulary. During training, the first appearance of any word is replaced with `<UNK>`, and its n-gram counts are computed normally. This allows the model to assign a probability to any unknown word encountered later.

## Relationships

- **requires**: [[smoothing-in-language-models|Smoothing In Language Models]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*