---
type: concept
aliases: [Zero Padding]
summary: A technique used in convolutional neural networks where zeros are added around the borders of an input tensor before applying a convolutional or pooling operation.
relationships:
  - target: convolutional-layer
    type: is_a_technique_used_in
tags: [cnn-architecture, image-processing, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Zero Padding

## Definition
Zero padding is the process of adding rows and columns of zeros around the border of an input tensor before it is processed by a convolutional or pooling layer. This technique is used to control the spatial dimensions of the output and to ensure that features at the edges of the input are not underrepresented.

## Padding Strategies
In frameworks like TensorFlow, padding is typically controlled by a single parameter with two main settings. The first is 'VALID' padding, which means no padding is applied. In this case, the filter is only applied to positions where it fully overlaps with the input, which can cause the output dimensions to shrink and may lead to some pixels at the bottom and right of the input being ignored, depending on the stride.

## The 'SAME' Padding Strategy
The second common strategy is 'SAME' padding. When this is selected, the framework automatically adds the necessary number of zeros around the input so that the output feature map has the same spatial dimensions (height and width) as the input tensor, assuming a stride of 1. The number of output neurons is calculated as the number of input neurons divided by the stride, rounded up, and zeros are added as evenly as possible to achieve this target output size.

## Relationships

- **is_a_technique_used_in**: [[convolutional-layer|Convolutional Layer]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*