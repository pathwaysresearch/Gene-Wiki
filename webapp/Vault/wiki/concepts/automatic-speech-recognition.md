---
type: concept
aliases: [Automatic Speech Recognition]
summary: The task of creating a system that maps an acoustic signal of a spoken utterance into its corresponding sequence of words.
relationships:
  - target: gmm-hmm-model
    type: historically-used
tags: [applications, speech-processing, natural-language-processing]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Automatic Speech Recognition

## Task Definition
The task of automatic speech recognition (ASR) is to map a sequence of acoustic input vectors, X, into the corresponding sequence of words, y, intended by the speaker. Formally, the goal is to create a function that finds the most probable linguistic sequence y given the acoustic sequence X. The input is typically produced by splitting the audio into short frames, such as 20ms.

## Historical Context
From the 1980s until the rise of deep learning around 2009-2012, the state-of-the-art ASR systems were predominantly based on a combination of hidden Markov models (HMMs) and Gaussian mixture models (GMMs).

## Input Representation
Most speech recognition systems preprocess the raw acoustic signal using specialized, hand-designed features. However, some deep learning systems have demonstrated the ability to learn features directly from the raw input, reducing the reliance on such domain-specific feature engineering.

## Relationships

- **historically-used**: [[gmm-hmm-model|Gmm Hmm Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*