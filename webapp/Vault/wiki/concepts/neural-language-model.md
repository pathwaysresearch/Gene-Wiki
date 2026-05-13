---
type: concept
aliases: [Neural Language Model]
summary: A type of language model that uses neural networks to learn distributed representations of words (word embeddings) and model the probability of word sequences.
relationships:
  - target: word-embedding
    type: produces
  - target: bengio-et-al-2001
    type: was_introduced_by
tags: [nlp, language-modeling, neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Neural Language Model

## Overview
Introduced by Bengio et al. (2001), neural language models represented a shift back to modeling words as the fundamental units of language. Their introduction led to improved performance in language modeling tasks and helped popularize the use of word embeddings.

## Key Contribution
A primary contribution of neural language models is their ability to produce interpretable word embeddings as a byproduct of training to predict the next word in a sequence. These models have scaled significantly, from representing small sets of symbols in early work to handling millions of words in modern systems. This scaling effort drove the invention of many important deep learning techniques.

## Impact and Applications
The ideas behind neural language models have been foundational and have been extended into a wide variety of natural language processing applications beyond just language modeling. They demonstrated a powerful new way to represent linguistic units that captures semantic relationships.

## Relationships

- **produces**: [[word-embedding|Word Embedding]]
- **was_introduced_by**: [[bengio-et-al-2001|Bengio Et Al 2001]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*