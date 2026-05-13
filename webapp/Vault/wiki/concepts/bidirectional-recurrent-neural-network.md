---
type: concept
aliases: [Bidirectional Recurrent Neural Network]
summary: An extension of recurrent neural networks that processes sequence data in both forward and backward directions to capture context from both past and future elements.
relationships:
  - target: recurrent-neural-network
    type: is-a-specialization-of
tags: [sequence-modeling, neural-networks, architecture]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bidirectional Recurrent Neural Network

## Definition
A Bidirectional Recurrent Neural Network (Bidirectional RNN) is a sequence processing model, invented by Schuster and Paliwal (1997), that consists of two separate RNNs. One RNN processes the input sequence forward through time from the beginning to the end, while the second RNN processes the sequence backward from the end to the beginning. This architecture is designed for applications where the output at a given time step needs to be informed by the entire input sequence.

## How It Works
At any given time step `t`, the output of the Bidirectional RNN is computed using the hidden states from both the forward and backward RNNs. The forward RNN's hidden state, `h^(t)`, captures information from the past, while the backward RNN's hidden state, `g^(t)`, captures information from the future. By combining these two states, the output unit `o^(t)` can form a representation that depends on both past and future context surrounding the current input, making it sensitive to the local context without needing a fixed-size window.

## Applications
Bidirectional RNNs have been extremely successful in applications where context from both directions is crucial. The text cites several examples, including handwriting recognition, speech recognition, and bioinformatics. The concept can also be extended to two-dimensional inputs like images by using four RNNs, each processing the data in a different direction: up, down, left, and right.

## Relationships

- **is-a-specialization-of**: [[recurrent-neural-network|Recurrent Neural Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*