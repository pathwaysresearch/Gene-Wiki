---
type: concept
aliases: [Zero-Padding (in Convolutions)]
summary: A technique used in convolutional layers where zeros are added around the border of the input tensor, primarily to control the spatial dimensions of the output feature map.
relationships:
  - target: convolution
    type: is_a_technique_for
tags: [neural-network-techniques, convolution]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Zero-Padding (in Convolutions)

## Overview
Zero-padding is the practice of adding a border of zeros around an input tensor before applying a convolution operation. This technique is used to control the spatial size of the output feature map and to manage the behavior of the convolution near the borders of the input, where the kernel might otherwise hang off the edge.

## "Valid" Convolution
One approach is to use no zero-padding whatsoever. This is sometimes referred to as "valid" convolution, where the convolution kernel is only applied to positions where the entire kernel is contained within the image. A direct consequence of this method is that the size of the output shrinks with each layer. If an input has width 'm' and the kernel has width 'k', the output width will be 'm - k + 1'. This shrinkage can be dramatic and limits the number of convolutional layers that can be stacked in a network before the spatial dimensions become too small.

## "Same" Convolution
An alternative approach is to add just enough zero-padding to ensure that the output feature map has the same spatial dimensions as the input. This is often called "same" convolution. This method is advantageous because it allows for the construction of much deeper networks, as the convolution operation does not reduce the spatial size available to subsequent layers. A drawback is that the input pixels near the border, which are influenced by the artificial zero-padding, influence fewer output pixels than those in the center of the image.

## Relationships

- **is_a_technique_for**: [[convolution|Convolution]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*