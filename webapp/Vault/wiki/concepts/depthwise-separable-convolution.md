---
type: concept
aliases: [Depthwise Separable Convolution]
summary: A computationally efficient alternative to standard convolution that splits the operation into two steps: a depthwise convolution that applies a single spatial filter to each input channel, followed by a pointwise (1x1) convolution that combines the outputs.
relationships:
  - target: xception
    type: is_a_component_of
tags: [cnn-layer, convolution, parameter-efficiency]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Depthwise Separable Convolution

## Definition
A Depthwise Separable Convolution is an efficient factorization of a standard convolutional layer into two distinct, simpler operations. It is the core building block of modern efficient architectures like Xception. This term should not be confused with spatially separable convolutions, which are a different concept.

## How It Works
The operation is performed in two stages. The first stage is a 'depthwise convolution', which applies a single spatial filter to each input channel independently. This step is responsible for learning spatial patterns within each channel. The second stage is a 'pointwise convolution', which is a regular 1x1 convolution. This step takes the output of the depthwise stage and combines the information across channels to create new features.

## Applications and Considerations
By splitting the convolution into two steps, this method dramatically reduces the number of parameters and the computational cost compared to a standard convolution. It is the foundational component of the Xception architecture, which is built almost entirely from these layers. However, since these layers apply only one spatial filter per input channel, they are less effective on layers with very few channels. For this reason, architectures like Xception often begin with a few regular convolutional layers before switching to depthwise separable convolutions.

## Relationships

- **is_a_component_of**: [[xception|Xception]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*