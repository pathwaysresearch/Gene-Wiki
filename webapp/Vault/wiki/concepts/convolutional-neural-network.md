---
type: concept
aliases: [Convolutional Neural Network]
summary: A class of deep neural networks, commonly applied to analyzing visual imagery, that uses convolutional layers, pooling layers, and fully connected layers to process data.
relationships:
  - target: deep-feedforward-network
    type: is_a_type_of
  - target: backpropagation
    type: is_trained_using
  - target: parameter-sharing
    type: leverages
  - target: yann-lecun
    type: pioneered_by
  - target: alexnet
    type: is_a_type_of
  - target: googlenet
    type: is_a_type_of
  - target: resnet
    type: is_a_type_of
tags: [deep-learning, neural-network-architecture, computer-vision]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Convolutional Neural Network

## Overview
A Convolutional Neural Network (CNN or ConvNet) is a type of deep learning model particularly well-suited for processing data that has a grid-like topology, such as an image. A simple CNN can be constructed to tackle image classification tasks, such as identifying items in the Fashion MNIST dataset.

## Typical Architecture
A common CNN architecture is built as a sequence of layers. It typically starts with one or more convolutional layers that apply filters to the input image to create feature maps. These are often followed by a max pooling layer, which downsamples the feature maps to reduce their spatial dimensions and computational complexity. This pattern of alternating convolutional and pooling layers can be repeated multiple times to build a hierarchy of features. The network usually concludes with a `Flatten` layer to convert the 2D feature maps into a 1D vector, followed by one or more `Dense` (fully connected) layers for classification. `Dropout` layers are often inserted between the dense layers to mitigate overfitting.

## Example Implementation
An implementation in Keras can be built using the `Sequential` model API. For an input image of 28x28 pixels with a single color channel, the first `Conv2D` layer would be configured with `input_shape=[28, 28, 1]`. Subsequent layers like `MaxPooling2D`, more `Conv2D` layers, `Flatten`, `Dense`, and `Dropout` are stacked to form the complete network. A common practice to avoid repeating hyperparameters is to use Python's `functools.partial` to create a pre-configured version of a layer, such as `Conv2D`, with default settings for kernel size, activation, and padding.

## Relationships

- **is_a_type_of**: [[alexnet|Alexnet]]
- **is_a_type_of**: [[googlenet|Googlenet]]
- **is_a_type_of**: [[resnet|Resnet]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*