---
type: concept
aliases: [Keras Callbacks]
summary: Objects in Keras that can be passed to the `fit()` method to perform specific actions at different stages of the training process, such as model checkpointing.
relationships:
  - target: model-checkpointing
    type: enables
  - target: keras
    type: is_a_feature_of
tags: [keras, model-training, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Keras Callbacks

## Definition
Callbacks are objects in the Keras library that allow a user to inject custom behavior at various points during the model training process. They are passed to the model's `fit()` method in a list.

## Functionality
Callbacks provide a mechanism to automate tasks that need to be performed during training without altering the core logic of the `fit()` method. A key application is model checkpointing, where a callback is used to save the model at regular intervals or when a monitored metric improves. This is essential for long training sessions.

## Usage
To use a callback, one typically instantiates a callback class and passes it to the `fit()` method's `callbacks` argument. This allows the training loop to be customized to include actions like saving checkpoints, adjusting learning rates, or stopping training early.

## Relationships

- **enables**: [[model-checkpointing|Model Checkpointing]]
- **is_a_feature_of**: [[keras|Keras]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*