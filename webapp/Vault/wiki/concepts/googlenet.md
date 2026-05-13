---
type: concept
aliases: [GoogLeNet]
summary: A deep convolutional neural network from Google Research that won the 2014 ImageNet ILSVRC. It is known for its computational efficiency and its use of 'inception modules' to create a deeper network with fewer parameters than AlexNet.
relationships:
  - target: convolutional-neural-network
    type: is_an_example_of
  - target: inception-module
    type: uses
  - target: global-average-pooling
    type: uses
  - target: alexnet
    type: is_an_improvement_on
tags: [cnn-architecture, imagenet, deep-learning, parameter-efficiency]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# GoogLeNet

## Overview
The GoogLeNet architecture, developed by Christian Szegedy and his colleagues at Google Research, won the ILSVRC 2014 challenge with a top-5 error rate below 7%. A key achievement of GoogLeNet was its parameter efficiency; it was much deeper than previous CNNs like AlexNet but had approximately 10 times fewer parameters (around 6 million compared to AlexNet's 60 million). This efficiency was largely due to its novel use of sub-networks called inception modules.

## Inception Modules
The core building block of GoogLeNet is the inception module. This module allows the network to use parameters more efficiently and capture features at multiple scales. It works by feeding the input signal into four parallel branches consisting of convolutional layers with different kernel sizes (1x1, 3x3, and 5x5) as well as a max pooling path. The outputs from these branches are then concatenated along the depth dimension. This structure allows the network to learn spatial patterns at various scales simultaneously within the same module.

## Overall Architecture
The full GoogLeNet architecture starts with two layers that aggressively reduce the input image's height and width to lower the computational load. This is followed by a tall stack of nine inception modules, which are interleaved with a couple of max pooling layers to further reduce dimensionality. A significant feature of the architecture is the replacement of the final large fully connected layers with a global average pooling layer. This layer outputs the mean of each feature map, drastically reducing the number of parameters before the final linear and softmax layers, which helps to prevent overfitting.

## Relationships

- **is_an_example_of**: [[convolutional-neural-network|Convolutional Neural Network]]
- **uses**: [[inception-module|Inception Module]]
- **uses**: [[global-average-pooling|Global Average Pooling]]
- **is_an_improvement_on**: [[alexnet|Alexnet]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*