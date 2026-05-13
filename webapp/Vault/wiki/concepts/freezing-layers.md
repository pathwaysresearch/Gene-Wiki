---
type: concept
aliases: [Freezing Layers]
summary: A technique in transfer learning where the weights of pretrained layers in a neural network are prevented from being updated during the initial phase of training.
relationships:
  - target: transfer-learning
    type: is-a-technique-in
tags: [transfer-learning, deep-learning, training-technique]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Freezing Layers

## Definition
Freezing layers is a crucial step in the transfer learning workflow, particularly at the beginning of training a new model built upon a pretrained base. It involves setting the `trainable` attribute of the layers in the base model to `False`, which stops their weights from being modified by the optimizer during backpropagation.

## Rationale
This technique is employed to protect the well-learned features within the pretrained layers. When a new model is created by adding randomly initialized layers on top of a pretrained base, the initial gradients during training can be very large. If the base layers were trainable from the start, these large gradients could drastically alter and potentially corrupt the valuable, pre-existing weights. Freezing them allows the new top layers to learn reasonable weights first without disrupting the base.

## Implementation
In Keras, freezing is typically accomplished by iterating through the layers of the base model and setting `layer.trainable = False`. The text notes that if a new model uses the base model's layers directly, rather than the `base_model` object itself, then setting `base_model.trainable=False` would have no effect, and individual layers must be frozen. After an initial training phase for the new layers, the base layers can be "unfrozen" for fine-tuning.

## Relationships

- **is-a-technique-in**: [[transfer-learning|Transfer Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*