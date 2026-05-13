---
type: concept
aliases: [Depth-wise Max Pooling]
summary: A pooling operation in CNNs that is performed along the depth dimension of feature maps, rather than the spatial dimensions, to help the network learn invariances to features like rotation.
relationships:
  - target: convolutional-neural-network
    type: is_a_component_of
tags: [cnn-layer, pooling, invariance]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Depth-wise Max Pooling

## Definition
Depth-wise max pooling is a pooling operation that can be used in a Convolutional Neural Network (CNN). Unlike standard max pooling which operates on the spatial dimensions (height and width) of feature maps, depth-wise max pooling is performed along the depth dimension. This technique allows a CNN to learn to be invariant to various features detected by different filters.

## How It Works
After a convolutional layer applies multiple filters to an input, it produces a stack of feature maps, with each map corresponding to a specific learned feature. For example, different filters could learn to detect the same pattern at different rotations. The depth-wise max pooling layer then takes the maximum value across the depth of these feature maps for each spatial location. This ensures that the output is strong if any of the filters fired, regardless of which specific one it was, effectively making the output invariant to the variations (e.g., rotation) captured by the different filters.

## Applications and Benefits
This technique can be used to make a CNN invariant to a wide range of transformations or characteristics. For instance, a network could learn filters to detect a handwritten digit at various rotations, and the depth-wise max pooling layer would ensure the output is the same regardless of the input digit's orientation. This principle of learning invariance can be extended to other attributes such as thickness, brightness, skew, and color.

## Implementation
While some deep learning frameworks like Keras do not include a dedicated depth-wise max pooling layer, the functionality can be implemented using lower-level APIs. For example, it can be achieved using TensorFlow’s `tf.nn.max_pool()` function.

## Relationships

- **is_a_component_of**: [[convolutional-neural-network|Convolutional Neural Network]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*