---
type: concept
aliases: [Parameter Sharing]
summary: A technique in neural network architecture where the same parameters are used across different parts of a model, significantly reducing the total number of unique parameters to be learned. A key principle in convolutional networks where the same set of parameters (a single kernel) is used to compute the output at every location in the input, drastically reducing the total number of parameters in the model.
relationships:
  - target: convolutional-network
    type: is_property_of
  - target: convolution
    type: is_a_result_of
tags: [regularization, convolutional-neural-networks, model-architecture, neural-network-properties, computational-efficiency]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Parameter Sharing

## Application in Convolutional Neural Networks
The most popular and extensive use of parameter sharing is in Convolutional Neural Networks (CNNs) applied to computer vision. Natural images possess statistical properties that are invariant to translation; for instance, a cat is still a cat if it is shifted within the image. CNNs exploit this by sharing parameters across different image locations, meaning the same feature detector (a hidden unit with the same weights) is applied over various parts of the input. This allows the network to detect a feature regardless of its position.

## Benefits
Parameter sharing dramatically lowers the number of unique model parameters that need to be learned. This reduction allows for the construction of significantly larger and deeper networks without requiring a corresponding increase in the amount of training data. It is considered one of the most effective ways to incorporate domain knowledge, such as translation invariance, directly into a network's architecture.

## Impact on Model Design
By reducing the parameter count, parameter sharing helps to regularize the model and improve its generalization capabilities. It enables models like CNNs to scale to high-dimensional inputs like images while remaining computationally tractable and less prone to overfitting than a fully connected network of a similar size would be.

## Relationships

- **is_property_of**: [[convolutional-network|Convolutional Network]]
- **is_a_result_of**: [[convolution|Convolution]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*