---
type: concept
aliases: [Custom Training Loop]
summary: A manually written training loop in TensorFlow that provides fine-grained control over the training process, as an alternative to the high-level `model.fit()` method.
relationships:
  - target: tf-gradient-tape
    type: uses
tags: [tensorflow, keras, model-training]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Custom Training Loop

## Definition
A custom training loop is a from-scratch implementation of the model training process in TensorFlow. Instead of relying on the high-level `model.fit()` method, the developer writes explicit Python code to iterate over epochs and batches, perform the forward pass, calculate loss, compute gradients, and update the model's weights. This approach offers maximum control and flexibility for research and complex model development.

## Core Steps
The process involves several key steps within nested loops for epochs and batches. For each batch: 1. The forward pass is executed within a `tf.GradientTape` context to record operations. 2. The main loss is calculated using a loss function (e.g., `keras.losses.mean_squared_error`). 3. Any additional losses stored in `model.losses` (such as regularization or reconstruction losses) are added to the main loss. 4. The tape's `gradient()` method is called to compute the gradients of the total loss with respect to the model's trainable variables. 5. The optimizer's `apply_gradients()` method is used to update the model weights based on the computed gradients.

## Metrics and State Management
Throughout the loop, metrics such as `keras.metrics.Mean` and `keras.metrics.MeanAbsoluteError` are used to track the loss and other performance indicators. These metric objects are updated at each step. It is crucial to reset the states of these metrics at the end of each epoch (using `metric.reset_states()`) to ensure that the metrics for the next epoch are calculated fresh.

## Relationships

- **uses**: [[tf-gradient-tape|Tf Gradient Tape]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*