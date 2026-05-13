---
type: concept
aliases: [Encoder-Decoder Architecture]
summary: A neural network framework for sequence-to-sequence tasks, where an encoder network processes an input sequence into a fixed-size context vector, and a decoder network generates an output sequence from that vector.
relationships:
  - target: recurrent-neural-network
    type: often-uses
  - target: attention-mechanism
    type: is-enhanced-by
tags: [sequence-to-sequence, neural-networks, architecture]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Encoder-Decoder Architecture

## Overview
The encoder-decoder architecture is a model design used for tasks that map an input sequence to an output sequence, where the lengths of the input and output may differ. It consists of two main components: an encoder and a decoder, both of which are often RNNs. The encoder processes the entire input sequence and compresses it into a single fixed-size vector, often called the context vector `C`. The decoder then takes this context vector as input and generates the output sequence one element at a time.

## How It Works
The encoder reads the input sequence, and its final hidden state is typically used as the context vector `C`, which is intended to be a summary of the entire input. The decoder is then initialized with this context vector. The vector can be provided as the initial hidden state of the decoder RNN, or it can be connected as an input to the hidden units at each time step of the decoding process. The decoder then generates the output sequence step-by-step until a stopping condition is met.

## Limitations
A significant limitation of this basic architecture is that the fixed-size context vector `C` can become an information bottleneck. If the input sequence is very long, it is difficult for the network to summarize all the necessary information into a single vector of limited dimension. This can lead to a loss of information and poor performance on long sequences, a phenomenon observed by Bahdanau et al. (2015) in the context of machine translation. This limitation motivated the development of the attention mechanism.

## Relationships

- **often-uses**: [[recurrent-neural-network|Recurrent Neural Network]]
- **is-enhanced-by**: [[attention-mechanism|Attention Mechanism]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*