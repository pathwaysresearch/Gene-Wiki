---
type: concept
aliases: [Max Pooling]
summary: A down-sampling operation common in convolutional networks that reduces the spatial dimensions of a feature map by outputting the maximum value from a neighborhood of units in the input.
relationships:
  - target: convolutional-network
    type: is_common_component_of
tags: [neural-network-layers, downsampling, invariance]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Max Pooling

## Definition
Max pooling is a pooling operation that calculates the maximum, or largest, value in a patch of a feature map. The result is a down-sampled feature map that highlights the most present feature in the patch. It is a common component in convolutional neural networks, typically applied after a convolutional layer.

## How It Works
The operation works by sliding a window over the input feature map (the "detector stage") and, for each position of the window, outputting the maximum value found within that window. For example, with a pooling region width of three pixels and a stride of one, each output unit of the pooling stage would be the maximum value of three adjacent units in the detector stage. This process reduces the spatial resolution of the representation.

## Invariance Property
A key function of max pooling is to introduce a degree of invariance to small translations in the input. Because the pooling unit reports only the maximum value within its neighborhood and not the location of that value, the representation becomes somewhat insensitive to the exact position of features. If an input is shifted slightly, the values in the detector stage will all change, but as long as the maximum activation remains within the same pooling neighborhood, the output of the max pooling unit will not change. This helps the network recognize patterns regardless of their precise location in the input.

## Relationships

- **is_common_component_of**: [[convolutional-network|Convolutional Network]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*