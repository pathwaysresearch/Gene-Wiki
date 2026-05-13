---
type: concept
aliases: [Skip Connections]
summary: An architectural feature in neural networks where the output of an earlier layer is added to the output of a later layer, helping to preserve information and combat issues like vanishing gradients or loss of resolution.
relationships:
  - target: semantic-segmentation
    type: is-a-technique-in
tags: [deep-learning, neural-network-architecture, computer-vision]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Skip Connections

## Definition
Skip connections are pathways in a neural network architecture that bypass one or more layers. They are used to feed the output of an earlier layer to a much later layer in the network, often by adding the two feature maps together.

## Application in Semantic Segmentation
In the context of semantic segmentation, skip connections are a crucial technique for recovering the spatial resolution that is lost during the downsampling (e.g., pooling) stages of a CNN. As the network upsamples the feature maps to produce a full-resolution segmentation map, the skip connections add the output from lower, higher-resolution layers.

## How It Works
For example, a low-resolution feature map from a deep layer might be upsampled by a factor of 2. This upsampled map is then combined with a feature map from an earlier, shallower layer in the network that has the same, higher resolution. This process can be repeated multiple times, adding details from progressively lower layers. This allows the final output to incorporate both high-level semantic information from deep layers and fine-grained spatial details from shallow layers, leading to more precise segmentation.

## Relationships

- **is-a-technique-in**: [[semantic-segmentation|Semantic Segmentation]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*