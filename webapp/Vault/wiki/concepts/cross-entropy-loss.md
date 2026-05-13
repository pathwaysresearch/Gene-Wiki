---
type: concept
aliases: [Cross-Entropy Loss]
summary: A loss function, also known as log loss, that is a good choice for classification models that predict probability distributions.
relationships:
  - target: classification-mlp
    type: used_in
tags: [loss-function, classification, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Cross-Entropy Loss

## Definition
Cross-entropy loss, also called log loss, is a loss function used to evaluate the performance of a classification model that outputs a probability distribution. It measures the dissimilarity between the predicted probability distribution and the actual distribution (the ground truth labels), penalizing the model more heavily for confident but incorrect predictions.

## Application in MLPs
The text identifies cross-entropy as the generally recommended and typical loss function for training classification Multi-Layer Perceptrons (MLPs).

## Usage Across Classification Tasks
Cross-entropy is the standard choice for a wide range of classification scenarios. A summary table in the text explicitly lists it as the appropriate loss function for binary classification, multilabel binary classification, and multiclass classification tasks when building an MLP.

## Relationships

- **used_in**: [[classification-mlp|Classification Mlp]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*