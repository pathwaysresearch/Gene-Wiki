---
type: concept
aliases: [ResNet (Residual Network)]
summary: A deep neural network architecture that introduces 'residual units' with skip connections, allowing for the training of networks that are hundreds or even thousands of layers deep by mitigating the vanishing gradient problem.
relationships:
  - target: convolutional-neural-network
    type: is_an_example_of
  - target: global-average-pooling
    type: uses
tags: [cnn-architecture, deep-learning, skip-connection, vanishing-gradient]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# ResNet (Residual Network)

## Overview
ResNet, or Residual Network, is a groundbreaking CNN architecture developed by K. He et al. that won the 2015 ILSVRC. Its main contribution is enabling the training of extremely deep neural networks by introducing a novel architectural element called a residual unit, which features a 'skip connection'.

## Residual Units and Skip Connections
The core component of a ResNet is the residual unit. In very deep networks, training can be hampered by the vanishing gradient problem, where gradients become too small to effectively update the weights of early layers. A residual unit addresses this by adding a 'skip connection' (or shortcut) that bypasses two or more layers and adds the input of the unit to its output. This allows gradients to flow more directly through the network during backpropagation, making it easier for the network to learn and preventing performance degradation as more layers are added.

## Architecture
A typical ResNet architecture, such as ResNet-34, is surprisingly simple in its overall structure. It starts and ends in a similar fashion to GoogLeNet, with an initial convolutional and pooling block and a final global average pooling layer followed by a fully connected layer. The main body of the network consists of a very deep stack of simple residual units. Each residual unit is typically composed of two 3x3 convolutional layers, along with Batch Normalization and ReLU activation, and is designed to preserve the spatial dimensions of the feature maps (using stride 1 and SAME padding).

## Relationships

- **is_an_example_of**: [[convolutional-neural-network|Convolutional Neural Network]]
- **uses**: [[global-average-pooling|Global Average Pooling]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*