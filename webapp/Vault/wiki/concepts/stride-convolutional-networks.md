---
type: concept
aliases: [Stride (Convolutional Networks)]
summary: A parameter in convolutional and pooling layers that defines the step size a filter or pooling kernel moves across the input data.
relationships:
  - target: convolutional-layer
    type: is_a_parameter_of
  - target: pooling-layer
    type: is_a_parameter_of
tags: [cnn-architecture, image-processing, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Stride (Convolutional Networks)

## Definition
In the context of convolutional neural networks, the stride is the parameter that specifies the step size with which a filter (or kernel) moves across the input. It defines the shift from one receptive field to the next. The stride can be set independently for the horizontal and vertical dimensions.

## Effect on Output Size
The stride has a direct impact on the spatial dimensions of the output feature map. A stride of 1 means the filter moves one pixel at a time, whereas a stride of 2 means it skips every other pixel. Using a stride greater than 1 results in a smaller output layer, effectively performing a form of downsampling. For example, a 5x7 input layer can be connected to a 3x4 output layer by using 3x3 receptive fields with a stride of 2.

## Implementation
In TensorFlow's `tf.nn.conv2d` function, the `strides` parameter is a 1D array of four elements. The second and third elements specify the vertical ($s_h$) and horizontal ($s_w$) strides, respectively. The first and last elements, which correspond to batch and channel strides, must currently be equal to 1.

## Relationships

- **is_a_parameter_of**: [[convolutional-layer|Convolutional Layer]]
- **is_a_parameter_of**: [[pooling-layer|Pooling Layer]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*