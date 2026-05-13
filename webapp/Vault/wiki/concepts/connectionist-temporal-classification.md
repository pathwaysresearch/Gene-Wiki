---
type: concept
aliases: [Connectionist Temporal Classification]
summary: An output layer and loss function for training recurrent neural networks on sequence-to-sequence tasks without requiring prior alignment between the input and target sequences.
relationships:
  - target: alex-graves
    type: created_by
  - target: jurgen-schmidhuber
    type: created_by
  - target: recurrent-neural-network
    type: used_with
tags: [sequence-labeling, loss-function, speech-recognition, recurrent-neural-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Connectionist Temporal Classification

## Definition
Connectionist Temporal Classification (CTC) is a method for training sequence models, particularly recurrent neural networks, introduced by Alex Graves, Santiago Fernández, Faustino Gomez, and Jürgen Schmidhuber in a 2006 paper. Its key innovation is the ability to train models on unsegmented sequence data, where the alignment between the input steps and the output labels is not known in advance.

## How It Works
CTC works by defining a probability distribution over all possible alignments between the input and output sequences. The loss function then maximizes the sum of these probabilities for the correct output sequence. This allows the network to learn both the classification of elements and their alignment simultaneously, making it highly suitable for tasks with variable-rate inputs and outputs.

## Applications
The primary application of CTC is in areas where sequence alignment is a major challenge, such as speech and handwriting recognition. The original paper by Graves et al. (2006) specifically frames it as a method for "labelling unsegmented sequence data with recurrent neural networks," and it has become a standard approach for end-to-end systems in these domains.

## Relationships

- **created_by**: [[alex-graves|Alex Graves]]
- **created_by**: [[jurgen-schmidhuber|Jurgen Schmidhuber]]
- **used_with**: [[recurrent-neural-network|Recurrent Neural Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*