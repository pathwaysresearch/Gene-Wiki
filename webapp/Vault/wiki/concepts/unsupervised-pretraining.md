---
type: concept
aliases: [Unsupervised Pretraining]
summary: A technique for training deep networks when labeled data is scarce but unlabeled data is abundant, by training layers sequentially in an unsupervised manner before fine-tuning.
relationships:
  - target: representation-learning
    type: is_a_method_for
  - target: transfer-learning
    type: related_to
tags: [deep-learning, unsupervised-learning, model-training, pretraining]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Unsupervised Pretraining

## Problem Context

Unsupervised pretraining is a valuable technique for complex tasks where there is not much labeled training data, and a suitable pre-trained model for transfer learning is unavailable. It leverages large amounts of cheap, unlabeled training data to initialize the network's weights in a meaningful way before supervised training begins.

## The Process

The method involves training the network's layers one by one, starting from the lowest layer and moving upwards. Each layer is trained using an unsupervised feature detector algorithm, such as an autoencoder or a Restricted Boltzmann Machine (RBM). During the training of a specific layer, all previously trained layers are frozen, and the current layer is trained on the output of the layer below it.

## Fine-Tuning Stage

Once all layers have been trained in this unsupervised manner, the output layer for the specific supervised task is added to the network. The final step is to fine-tune the entire network using the available labeled training examples. At this stage, one can choose to unfreeze all the pretrained layers or just some of the upper ones to allow their weights to be adjusted by backpropagation.

## Relationships

- **related_to**: [[transfer-learning|Transfer Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*