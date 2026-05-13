---
type: concept
aliases: [Transfer Learning]
summary: A machine learning method where a model developed for a task is reused as the starting point for a model on a second, related task. A machine learning technique where a model developed for a task is reused as the starting point for a model on a second task, often by using its pretrained layers.
relationships:
  - target: representation-learning
    type: is_enabled_by
  - target: unsupervised-pretraining
    type: related_to
  - target: freezing-layers
    type: uses-technique
  - target: xception
    type: uses
tags: [deep-learning, model-training, fine-tuning, computer-vision, training-technique]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Transfer Learning

## Core Idea

Transfer learning is a technique where a model trained on one task is repurposed for a second, related task. The fundamental principle is to reuse the lower layers of the pre-trained network, as they tend to learn more general features. The more similar the new task is to the original one, the more layers can be reused. For very similar tasks, one might only need to replace the output layer.

## Fine-Tuning Strategy

A common strategy is to first freeze the weights of all the reused layers, making them non-trainable, and train the new model. After this initial training, one or two of the top hidden layers can be unfrozen to allow backpropagation to tweak their weights. When unfreezing layers, it is beneficial to use a lower learning rate to avoid damaging the fine-tuned weights. The amount of training data available for the new task dictates how many layers can be unfrozen and fine-tuned.

## Adapting the Architecture

If performance is not satisfactory, the architecture can be further adapted. With limited training data, one might try dropping the top hidden layer(s) and freezing the remaining ones. Conversely, with a large amount of training data, one could try replacing the top hidden layers or even adding more hidden layers to increase the model's capacity for the new task.

## Relationships

- **related_to**: [[unsupervised-pretraining|Unsupervised Pretraining]]
- **uses-technique**: [[freezing-layers|Freezing Layers]]
- **uses**: [[xception|Xception]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*