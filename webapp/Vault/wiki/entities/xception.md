---
type: entity
aliases: [Xception]
summary: A convolutional neural network architecture provided by Keras, often used as a pretrained base model for transfer learning tasks.
relationships:
  - target: transfer-learning
    type: is-example-of
tags: [deep-learning-model, cnn, keras]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Xception

## Overview
Xception is a specific deep convolutional neural network architecture. The text presents it as an example of a powerful pretrained model available in the `keras.applications` module, which can be readily used for transfer learning.

## Role in Transfer Learning
The text demonstrates how to use the Xception model, pretrained on the "imagenet" dataset, as a base for a new classification task. The process involves loading the model with `keras.applications.xception.Xception(weights="imagenet", include_top=False)`, which omits the final classification layer. This allows a new custom output layer, such as a `Dense` layer with a softmax activation, to be added for the specific number of classes in the new task.

## Training with Xception
When using Xception as a base model, a common strategy is to initially freeze the layers of the `base_model` to prevent the pretrained weights from being corrupted during the early stages of training the new top layers. This is done by setting `layer.trainable = False` for each layer in the base model before compiling and fitting the new composite model.

## Relationships

- **is-example-of**: [[transfer-learning|Transfer Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*