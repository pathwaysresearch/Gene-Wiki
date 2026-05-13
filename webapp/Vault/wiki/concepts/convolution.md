---
type: concept
aliases: [Convolution (in Machine Learning)]
summary: A mathematical operation used in neural networks to extract features by sliding a learned filter, or kernel, over an input tensor. It is a specialized form of linear operation that leverages the principles of sparse interactions and parameter sharing.
relationships:
  - target: convolutional-network
    type: is_core_component_of
  - target: sparse-interactions
    type: enables
  - target: parameter-sharing
    type: enables
  - target: zero-padding-in-convolutions
    type: is_modified_by
tags: [mathematical-operations, signal-processing, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Convolution (in Machine Learning)

## Definition
In the context of discrete data like images, convolution is a linear operation defined as s(t) = (x * w)(t) = Σ x(a)w(t - a), where x is the input and w is the kernel. The output is often referred to as the feature map. In machine learning applications, the input is typically a multidimensional array of data (a tensor) and the kernel is a multidimensional array of parameters that are adapted by the learning algorithm. The operation is implemented as a summation over a finite number of array elements.

## Implementation in Neural Networks
In neural networks, the term "convolution" usually refers to an operation consisting of many applications of convolution in parallel. A single kernel can only extract one kind of feature, so multiple kernels are used in each layer to extract many kinds of features at many spatial locations. Furthermore, the input is often a grid of vector-valued observations, such as a color image with red, green, and blue channels at each pixel. Consequently, the inputs and outputs of a convolutional layer are typically treated as 3-D tensors, with indices for channels and spatial coordinates.

## Probabilistic Interpretation
The use of convolution in a neural network can be interpreted as introducing an infinitely strong prior probability distribution over the parameters of a layer. This prior effectively states that the weights for one hidden unit must be identical to the weights of its neighbor but shifted in space (parameter sharing). It also specifies that the weights must be zero outside of a small, spatially contiguous receptive field (sparse interactions). This view frames a convolutional network as a fully connected network with very specific, structurally-enforced constraints on its weights.

## Relationships

- **is_core_component_of**: [[convolutional-network|Convolutional Network]]
- **enables**: [[sparse-interactions|Sparse Interactions]]
- **enables**: [[parameter-sharing|Parameter Sharing]]
- **is_modified_by**: [[zero-padding-in-convolutions|Zero Padding In Convolutions]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*