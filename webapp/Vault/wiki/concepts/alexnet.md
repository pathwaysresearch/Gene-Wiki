---
type: concept
aliases: [AlexNet]
summary: A deep convolutional neural network architecture that won the 2012 ImageNet ILSVRC, notable for being much larger and deeper than its predecessors and for stacking convolutional layers directly.
relationships:
  - target: convolutional-neural-network
    type: is_an_example_of
tags: [cnn-architecture, imagenet, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# AlexNet

## Overview
AlexNet is a convolutional neural network architecture developed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton. It achieved a landmark victory in the 2012 ImageNet ILSVRC challenge, reaching a 17% top-5 error rate, which was significantly better than the 26% achieved by the runner-up. The architecture is structurally similar to LeNet-5 but is considerably larger and deeper.

## Key Architectural Innovation
A key innovation of AlexNet was that it was the first architecture to stack convolutional layers directly on top of one another. Prior models typically alternated every convolutional layer with a pooling layer. This direct stacking allowed the network to learn a deeper and more complex hierarchy of features from the input data.

## Architecture Details
The AlexNet architecture is composed of a series of convolutional and max pooling layers, followed by several fully connected layers. It begins with a convolutional layer using a large 11x11 kernel and a stride, followed by a max pooling layer. The core of the network features stacks of convolutional layers (e.g., C5, C6, and C7 are stacked consecutively) using 3x3 kernels and SAME padding. The network concludes with two large 4,096-neuron fully connected layers before a final 1,000-neuron softmax output layer for classification on the ImageNet dataset. The ReLU activation function is used throughout the convolutional and fully connected layers.

## Relationships

- **is_an_example_of**: [[convolutional-neural-network|Convolutional Neural Network]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*