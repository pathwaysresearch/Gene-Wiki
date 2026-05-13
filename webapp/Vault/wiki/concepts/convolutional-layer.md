---
type: concept
aliases: [Convolutional Layer]
summary: A core building block of Convolutional Neural Networks (CNNs) that applies a set of learnable filters to an input, detecting specific features like edges, textures, or patterns.
relationships:
  - target: local-receptive-field
    type: is_based_on
  - target: zero-padding
    type: uses
  - target: stride-convolutional-networks
    type: uses
tags: [deep-learning, cnn-architecture, computer-vision]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Convolutional Layer

## Definition
A convolutional layer is a type of neural network layer where each neuron processes information from only a restricted area of the previous layer, known as its receptive field. This architecture is inspired by the organization of the animal visual cortex and is highly effective for processing data with a grid-like topology, such as images.

## How It Works
The layer operates by sliding one or more filters (also called kernels), which are small matrices of learnable weights, across the input. At each position, the filter is applied to a corresponding patch of the input, and the result (a dot product followed by an activation function) becomes a single value in an output 'feature map.' Each filter learns to detect a specific feature, and the resulting feature map indicates where that feature is present in the input. For inputs with multiple channels, like an RGB image, the filters are 3D, spanning the full depth of the input channels to produce a 2D feature map.

## Key Parameters
The behavior of a convolutional layer is controlled by several key hyperparameters. The `stride` defines the step size the filter moves across the input. `Padding` determines how the borders of the input are handled. The two main padding strategies are 'VALID', which uses no padding and may shrink the output dimensions, and 'SAME', which adds zero padding to ensure the output feature map has the same spatial dimensions as the input (for a stride of 1).

## Relationships

- **is_based_on**: [[local-receptive-field|Local Receptive Field]]
- **uses**: [[zero-padding|Zero Padding]]
- **uses**: [[stride-convolutional-networks|Stride Convolutional Networks]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*