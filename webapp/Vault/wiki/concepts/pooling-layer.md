---
type: concept
aliases: [Pooling Layer]
summary: A layer used in convolutional neural networks to subsample or downscale feature maps, reducing their spatial dimensions, computational cost, and the number of parameters.
relationships:
  - target: local-receptive-field
    type: is_based_on
  - target: stride-convolutional-networks
    type: uses
tags: [deep-learning, cnn-architecture, computer-vision]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Pooling Layer

## Definition and Purpose
A pooling layer's primary function is to subsample, or shrink, its input feature map. This downscaling process serves several important purposes: it reduces the computational load and memory usage for subsequent layers, and it decreases the number of parameters in the network, which helps to limit the risk of overfitting.

## How It Works
Similar to a convolutional layer, each neuron in a pooling layer is connected to a small rectangular receptive field in the previous layer. However, unlike convolutional neurons, pooling neurons have no learnable weights. Instead, they perform a fixed aggregation operation on the inputs within their receptive field. The most common type is a *max pooling layer*, which simply outputs the maximum value from its receptive field, effectively propagating the strongest activation. Other aggregation functions, such as taking the mean, can also be used.

## Key Parameters
A pooling layer's behavior is defined by its kernel size (the size of the receptive field), the stride (the step size it moves across the input), and the padding type. A common configuration is a 2x2 pooling kernel with a stride of 2 and no padding. This setup effectively halves the height and width of the input feature map by taking the maximum value from each 2x2 non-overlapping block of the input, discarding the other three values.

## Relationships

- **is_based_on**: [[local-receptive-field|Local Receptive Field]]
- **uses**: [[stride-convolutional-networks|Stride Convolutional Networks]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*