---
type: concept
aliases: [Dropout]
summary: A regularization technique for neural networks that randomly sets a fraction of neuron activations to zero during training to prevent co-adaptation and overfitting.
relationships:
  - target: bagging
    type: is-an-approximation-of
  - target: regularization
    type: is_a_type_of
  - target: bagging
    type: is_a_form_of
  - target: l2-weight-decay
    type: is_equivalent_to_for_linear_models
  - target: geoffrey-hinton
    type: developed_by
  - target: regularization
    type: is_a_form_of
  - target: dropconnect
    type: related_to
  - target: monte-carlo-dropout
    type: is_a_foundation_for
tags: [regularization, deep-learning, overfitting]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Dropout

## How It Works
Dropout is a regularization method that is only active during the training phase of a neural network. At each training step, it randomly drops a certain percentage of inputs to a layer (i.e., sets them to zero). The remaining inputs are then scaled up by dividing them by the "keep probability" (1 minus the dropout rate) to compensate for the dropped units. This process forces the network to learn more robust features that are not overly reliant on any single neuron.

## Behavior During Inference
After training is complete, the dropout layer becomes inactive and does nothing; it simply passes the inputs to the next layer without modification. This ensures that the full capacity of the trained network is used for making predictions.

## Implementation and Usage
In Keras, dropout is implemented using the `keras.layers.Dropout` layer, which is typically placed before a `Dense` or other hidden layer. The `rate` parameter specifies the fraction of inputs to drop. If a model is observed to be overfitting, the dropout rate can be increased. Conversely, if the model is underfitting, the rate should be decreased. A key consideration is that because dropout penalizes the training loss, a direct comparison between training and validation loss can be misleading.

## Relationships

- **is_a_foundation_for**: [[monte-carlo-dropout|Monte Carlo Dropout]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*