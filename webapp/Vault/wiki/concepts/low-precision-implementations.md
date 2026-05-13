---
type: concept
aliases: [Low-Precision Implementations]
summary: The use of numerical representations with fewer bits, such as 8-bit or 16-bit fixed-point numbers, to train and run deep neural networks, offering computational and efficiency benefits.
tags: [hardware, performance-optimization, quantization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Low-Precision Implementations

## Overview
Recent work suggests that deep neural networks can be successfully trained and used with low-precision numerical representations. Instead of standard floating-point numbers, implementations using between 8 and 16 bits of precision have been shown to be sufficient for back-propagation-based training and inference.

## Training vs. Inference
The precision requirements for a neural network can differ between its training and inference phases. The text indicates that more precision is generally required during training than at inference time. This allows for deploying models that are more computationally efficient than the versions used to train them.

## Dynamic Fixed Point
One technique to reduce the number of bits required per number is the use of dynamic fixed-point representations. Unlike traditional fixed-point numbers, which are restricted to a fixed range, a dynamic fixed-point representation allows a set of numbers (such as all the weights in a single layer) to share a common range or exponent. This provides a more efficient way to represent the necessary values compared to standard floating-point representations.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*