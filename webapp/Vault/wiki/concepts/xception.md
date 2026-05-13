---
type: concept
aliases: [Xception]
summary: A convolutional neural network architecture that is a variant of GoogLeNet, which replaces Inception modules entirely with depthwise separable convolutions.
relationships:
  - target: convolutional-neural-network
    type: is_an_example_of
  - target: googlenet
    type: is_a_variant_of
  - target: depthwise-separable-convolution
    type: uses
tags: [cnn-architecture, deep-learning, parameter-efficiency]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Xception

## Overview
The Xception architecture is a deep convolutional neural network that is considered a variant of GoogLeNet. Its name stands for 'Extreme Inception', as it takes the core idea of Inception modules—separating the learning of spatial and cross-channel patterns—to its logical extreme by using depthwise separable convolutions as its main building block.

## Core Component: Depthwise Separable Convolutions
Instead of using Inception modules, the Xception architecture is constructed almost entirely from depthwise separable convolutions. This type of layer first applies a spatial convolution to each input channel independently, and then uses a 1x1 pointwise convolution to combine the outputs across channels. This fully separates the process of learning spatial patterns from learning cross-channel patterns.

## Architecture Details
A typical Xception network starts with two regular convolutional layers, because depthwise separable convolutions are less effective when the number of input channels is very low. The remainder of the network is a deep stack of depthwise separable convolution layers (34 in total), interspersed with a few max pooling layers for downsampling. Similar to other modern architectures, it concludes with a global average pooling layer followed by a dense output layer for classification.

## Relationships

- **is_an_example_of**: [[convolutional-neural-network|Convolutional Neural Network]]
- **is_a_variant_of**: [[googlenet|Googlenet]]
- **uses**: [[depthwise-separable-convolution|Depthwise Separable Convolution]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*