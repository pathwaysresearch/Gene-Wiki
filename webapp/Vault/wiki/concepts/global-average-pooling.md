---
type: concept
aliases: [Global Average Pooling]
summary: A pooling operation that calculates the average of each feature map across its spatial dimensions, reducing each map to a single number. It is often used in modern CNNs to replace final fully connected layers, reducing parameters and overfitting.
relationships:
  - target: googlenet
    type: is_a_component_of
  - target: resnet
    type: is_a_component_of
tags: [cnn-layer, pooling, regularization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Global Average Pooling

## Definition
Global Average Pooling (GAP) is a pooling layer that reduces the spatial dimensions of a feature map to a single value. For each feature map in its input, it calculates the average of all values, effectively collapsing the height and width dimensions. This results in an output vector where each element represents the mean activation of a corresponding input feature map.

## Function and Benefits
The primary benefit of using a GAP layer is a significant reduction in the number of model parameters. In modern CNN architectures like GoogLeNet and ResNet, GAP layers are often used to replace the large, parameter-heavy fully connected layers that traditionally followed the convolutional base. By drastically reducing parameters, GAP layers help to mitigate overfitting and reduce the computational load of the network.

## Example Usage
In the GoogLeNet architecture, a global average pooling layer is placed after the final stack of inception modules. It takes the resulting feature maps and outputs their mean values, which are then fed directly into a final dense layer for classification. Similarly, the ResNet architecture uses a GAP layer after its deep stack of residual units and before the final fully connected output layer.

## Relationships

- **is_a_component_of**: [[googlenet|Googlenet]]
- **is_a_component_of**: [[resnet|Resnet]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*