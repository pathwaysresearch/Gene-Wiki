---
type: concept
aliases: [Neural Machine Translation]
summary: An approach to machine translation that uses a neural network to read a sentence in a source language and generate an equivalent sentence in a target language.
relationships:
  - target: attention-mechanism
    type: uses
tags: [machine-translation, nlp, sequence-to-sequence, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Neural Machine Translation

## Task Definition
Machine translation is the task of automatically converting a sentence from a source natural language to a target language while preserving its meaning. Neural Machine Translation (NMT) accomplishes this using deep learning models, typically in a sequence-to-sequence framework.

## Core Challenge and Representation
A key challenge for NMT is to effectively represent the entire source sentence to condition the generation of the target sentence. This is a departure from earlier statistical machine translation systems that could only represent individual words or phrases. From a representation learning perspective, a goal of NMT is to learn a representation where sentences with the same meaning have similar representations, regardless of the language they are in.

## Model Architectures
NMT models have evolved over time. Early work explored using a combination of convolutions and Recurrent Neural Networks (RNNs). Later, more powerful approaches emerged that used an RNN to score proposed translations or to directly generate the translated sentence from the source representation. These models were subsequently scaled to handle larger vocabularies, making them practical for real-world applications. Modern NMT systems often incorporate attention mechanisms to further improve performance.

## Relationships

- **uses**: [[attention-mechanism|Attention Mechanism]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*