---
type: concept
aliases: [Inception Module]
summary: A sub-network block used in the GoogLeNet architecture that processes inputs in parallel through multiple convolutional and pooling paths with different filter sizes, and concatenates their outputs.
relationships:
  - target: googlenet
    type: is_a_component_of
tags: [cnn-architecture, network-block, googlenet]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Inception Module

## Definition
An inception module is the fundamental building block of the GoogLeNet CNN architecture, named in reference to the movie *Inception* due to the network's deep, layered structure. These modules are designed to be computationally efficient while allowing the network to learn features at multiple scales.

## How It Works
An inception module processes its input signal through four parallel branches simultaneously. These branches typically include a 1x1 convolutional layer, a 3x3 convolutional layer, a 5x5 convolutional layer, and a max pooling layer. The 1x1 convolutions are often used as 'bottleneck' layers to reduce the depth of the feature maps before the more computationally expensive 3x3 and 5x5 convolutions. The outputs of all four branches are then concatenated along the depth dimension, creating a single, rich feature map that combines patterns captured at different scales.

## Role in CNNs
The design of the inception module represents an intermediate step between a regular convolutional layer, which learns both spatial and cross-channel patterns together, and a depthwise separable convolution, which separates these two tasks completely. The 1x1 filters in an inception module focus on cross-channel patterns, while the larger filters on top of them handle both spatial and cross-channel patterns. This structure allows for deep and efficient networks by balancing feature richness with computational cost.

## Relationships

- **is_a_component_of**: [[googlenet|Googlenet]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*