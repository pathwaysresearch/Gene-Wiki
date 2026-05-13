---
type: concept
aliases: [Tiled Convolution]
summary: A convolutional layer variant that offers a compromise between standard convolution and locally connected layers by learning a set of kernels that are cyclically applied across spatial locations.
relationships:
  - target: convolutional-layer
    type: is_a_variant_of
  - target: locally-connected-layer
    type: is_a_compromise_with
tags: [convolutional-neural-networks, deep-learning, computer-vision]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Tiled Convolution

## Definition

Tiled convolution is a technique used in convolutional networks that serves as a compromise between a standard convolutional layer and a locally connected layer. Instead of learning a single set of weights to be applied at all spatial locations (standard convolution) or a separate set of weights for every location (locally connected layer), tiled convolution learns a set of `t` different kernel stacks. These kernels are then rotated through, or cyclically applied, as the model moves across the spatial dimensions of the input.

## How It Works

Algebraically, the output Z of a tiled convolutional layer can be defined by the equation: $Z_{i,j,k} = \sum_{l,m,n} V_{i,j+m-1,k+n-1} K_{i,l,m,n,j\%t+1,k\%t+1}$. In this formulation, the indices `j` and `k` represent spatial locations in the output map, and the modulo operator `%` causes the network to cycle through a set of `t` different kernel choices in each direction. If the tiling parameter `t` is set to be equal to the output width, the tiled convolutional layer becomes equivalent to a locally connected layer.

## Properties and Advantages

Tiled convolution allows a network to have fewer parameters compared to a locally connected layer, which reduces memory consumption and increases statistical efficiency without reducing the number of hidden units. This approach also reduces the amount of computation needed for both forward and back-propagation. Furthermore, tiled convolution has a beneficial interaction with max-pooling; because neighboring detector units are driven by different filters, the subsequent max-pooled units can learn to become invariant to various transformations of the underlying features, whereas standard convolutional layers are hard-coded only for translation invariance.

## Relationships

- **is_a_variant_of**: [[convolutional-layer|Convolutional Layer]]
- **is_a_compromise_with**: [[locally-connected-layer|Locally Connected Layer]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*