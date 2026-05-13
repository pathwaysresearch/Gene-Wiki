---
type: concept
aliases: [Model Checkpointing]
summary: The practice of saving a machine learning model at regular intervals during a long training process to prevent loss of progress and to save the best-performing version.
relationships:
  - target: keras-callbacks
    type: implemented_using
tags: [model-training, deep-learning, keras]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Model Checkpointing

## Definition
Model checkpointing is a technique used during the training of machine learning models, especially for tasks that take several hours to complete. It involves saving the state of the model at regular intervals, or whenever performance on a validation set improves.

## Purpose
The primary purpose of checkpointing is to avoid losing progress if the training process is interrupted. For training runs that last several hours, this is a crucial feature. It also allows you to keep the version of the model that achieved the best performance during the entire training run, rather than just the one from the final epoch, which may have started to overfit.

## Implementation in Keras
In the Keras framework, checkpointing is implemented using callbacks. A callback is an object that can perform actions at various stages of training, such as at the end of an epoch. The `fit()` method can be configured with a checkpointing callback to save the model periodically to a file, ensuring that progress is not lost.

## Relationships

- **implemented_using**: [[keras-callbacks|Keras Callbacks]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*