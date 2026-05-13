---
type: concept
aliases: [Convolutional Network]
summary: A type of neural network architecture that uses convolution in place of general matrix multiplication in at least one of its layers, making it highly effective for processing data with a grid-like topology such as images.
relationships:
  - target: convolution
    type: uses
  - target: max-pooling
    type: uses
  - target: sparse-interactions
    type: exhibits_property
  - target: parameter-sharing
    type: exhibits_property
tags: [neural-networks, deep-learning, computer-vision]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Convolutional Network

## Overview
Convolutional networks are a specialized kind of neural network for processing data that has a known, grid-like topology. They are named for the convolution operation, a mathematical operation that replaces general matrix multiplication in at least one of their layers. These networks leverage key ideas like sparse interactions, parameter sharing, and equivariant representations to improve performance and efficiency, particularly on tasks involving images, audio, or other sensor data with spatial structure.

## Key Principles
Convolutional networks are built on three important ideas that improve a machine learning system. The first is sparse interactions (or sparse connectivity), where each output unit is connected to only a local subset of input units, reducing parameters and computational cost. The second is parameter sharing, where the same set of weights (a kernel) is used across different locations in the input, further reducing the number of parameters. The third is equivariant representations, a property resulting from parameter sharing, where a change in the input (like a translation) results in a corresponding change in the output.

## Typical Architecture
A common architecture for a convolutional network involves a series of stages. The first stage typically performs convolution to produce a set of linear activations, which are then passed through a nonlinear activation function like a rectified linear unit (ReLU). This is followed by a pooling stage, such as max pooling, to introduce some translation invariance and reduce dimensionality. These stages of convolution and pooling can be repeated multiple times to build a hierarchy of features. Finally, the high-level features from the last pooling layer are often flattened into a vector and processed by one or more fully connected layers to produce the final output, such as a classification via a softmax function.

## Relationships

- **uses**: [[convolution|Convolution]]
- **uses**: [[max-pooling|Max Pooling]]
- **exhibits_property**: [[sparse-interactions|Sparse Interactions]]
- **exhibits_property**: [[parameter-sharing|Parameter Sharing]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*