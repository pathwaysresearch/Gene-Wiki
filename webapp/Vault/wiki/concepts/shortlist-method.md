---
type: concept
aliases: [Shortlist Method]
summary: A technique for reducing the computational cost of the output layer in neural language models by splitting the vocabulary into a small, frequent 'shortlist' handled by the neural network and a 'tail' of rare words handled by a simpler model like an n-gram model.
relationships:
  - target: n-gram-model
    type: uses
tags: [language-modeling, optimization, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Shortlist Method

## Problem Addressed
The shortlist method was developed to address the high computational cost of the softmax output layer in neural language models, especially those with large vocabularies. The complexity of this operation is proportional to the vocabulary size, O(|V|n_h), and can dominate the entire computation, making models with hundreds of thousands of words impractical for early systems.

## How It Works
The core idea is to partition the vocabulary V into two disjoint sets: a shortlist L containing the most frequent words, and a tail T containing all other rare words. The neural language model is then trained to predict probabilities only for the words within the shortlist L. A separate, computationally cheaper model, such as a back-off n-gram model, is used to handle the probability distribution for words in the tail T.

## Combining Predictions
To produce a valid probability distribution over the entire vocabulary, the predictions from the two models must be combined. This is achieved by adding an extra output unit to the neural network, typically a sigmoid, which estimates the probability that the next word belongs to the tail, P(i ∈ T | C). The final probability for a word is then a weighted combination: for a word in the shortlist, its probability is the neural net's output scaled by (1 - P(i ∈ T | C)); for a word in the tail, its probability is the n-gram model's output scaled by P(i ∈ T | C).

## Relationships

- **uses**: [[n-gram-model|N Gram Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*