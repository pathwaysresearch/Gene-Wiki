---
type: concept
aliases: [Backoff Model]
summary: A smoothing technique for n-gram language models that uses lower-order n-grams (e.g., bigrams) to estimate probabilities for higher-order n-grams (e.g., trigrams) that have zero or very low counts in the training data.
relationships:
  - target: smoothing-in-language-models
    type: is-a-type-of
tags: [natural-language-processing, language-modeling, smoothing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Backoff Model

## Definition
A backoff model is an advanced smoothing technique in language modeling that provides a more effective alternative to simpler methods like Laplace smoothing. The core idea is to use the full n-gram model when sufficient data exists but to fall back to a simpler, lower-order model when data is sparse.

## How It Works
When estimating the probability of a particular n-gram sequence that has a low or zero count in the training corpus, the model "backs off" to the corresponding (n-1)-gram to derive its probability. This strategy avoids assigning a zero probability to unseen but plausible sequences by leveraging the statistical strength of more frequent, shorter subsequences.

## Example: Linear Interpolation Smoothing
Linear interpolation smoothing is a specific implementation of a backoff model. It defines the probability of a sequence by creating a weighted average of the probabilities from multiple models, typically combining trigram, bigram, and unigram estimates through linear interpolation. This allows the final probability to be informed by evidence from different context lengths.

## Relationships

- **is-a-type-of**: [[smoothing-in-language-models|Smoothing In Language Models]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*