---
type: concept
aliases: [Attention Mechanism]
summary: A technique used in sequence-to-sequence models that allows the decoder to dynamically focus on different parts of the input sequence when generating each element of the output sequence. A technique used in neural networks, particularly for sequence-to-sequence tasks, that computes a context vector as a weighted average of feature vectors, allowing the model to focus on relevant parts of the input.
relationships:
  - target: encoder-decoder-architecture
    type: enhances
  - target: neural-machine-translation
    type: component_of
tags: [sequence-to-sequence, neural-networks, architecture, nlp, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Attention Mechanism

## Definition
An attention mechanism is a component added to neural network architectures, particularly encoder-decoder models, to overcome the bottleneck of a fixed-size context vector. Instead of forcing the encoder to compress an entire input sequence into one static vector, the attention mechanism allows the decoder to 'look back' at the encoder's hidden states from every time step of the input sequence.

## Purpose and Function
The primary purpose of attention is to address the limitation of the standard encoder-decoder architecture where a fixed-size context vector struggles to summarize long sequences. As proposed by Bahdanau et al. (2015), the context `C` is made into a variable-length sequence (e.g., the sequence of all encoder hidden states). The attention mechanism then learns to compute a weighted sum of these encoder states at each step of the decoding process. This allows the model to selectively focus on the most relevant parts of the input sequence when generating a specific part of the output sequence.

## Impact on Sequence Modeling
By making the context a variable-length sequence and learning to associate elements of the input and output sequences, the attention mechanism significantly improves the performance of models on tasks involving long sequences, such as machine translation. It frees the model from the constraint of compressing all information into a single fixed-size representation, allowing for more direct and flexible modeling of alignments between input and output.

## Relationships

- **enhances**: [[encoder-decoder-architecture|Encoder Decoder Architecture]]
- **component_of**: [[neural-machine-translation|Neural Machine Translation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*