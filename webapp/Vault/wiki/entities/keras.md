---
type: entity
aliases: [Keras]
summary: A high-level Deep Learning API that simplifies the process of training and running neural networks and can run on top of frameworks like TensorFlow. A high-level Deep Learning API used for building, training, and evaluating neural networks. A high-level neural networks API, written in Python and capable of running on top of TensorFlow, used for fast experimentation with deep neural networks. A high-level API within TensorFlow for building and training neural networks, designed for fast experimentation and user-friendliness.
relationships:
  - target: tensorflow
    type: runs_on
  - target: deep-learning
    type: is_an_api_for
  - target: neural-networks
    type: used_for
  - target: keras-functional-api
    type: has_component
  - target: fashion-mnist
    type: provides_access_to
  - target: keras-callbacks
    type: has_feature
  - target: hyperparameter-tuning
    type: can_be_used_for
  - target: tensorflow
    type: component_of
  - target: custom-components-keras
    type: supports
tags: [deep-learning, api, python-framework, deep-learning-framework, python, tensorflow]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Keras

## Overview
Keras is a high-level API specifically designed for Deep Learning. Its main goal is to make it very simple to train and run neural networks. The author of the Keras library is identified as François Chollet.

## Functionality and Backend Support
Keras acts as an abstraction layer that can run on top of different backend frameworks. The text mentions it can use TensorFlow, Theano, or Microsoft Cognitive Toolkit (formerly known as CNTK) as its backend.

## Integration with TensorFlow
TensorFlow includes its own implementation of the Keras API, called tf.keras. This version is tightly integrated and provides support for some of TensorFlow's advanced features.

## Relationships

- **runs_on**: [[tensorflow|Tensorflow]]
- **is_an_api_for**: [[deep-learning|Deep Learning]]
- **used_for**: [[neural-networks|Neural Networks]]
- **has_component**: [[keras-functional-api|Keras Functional Api]]
- **provides_access_to**: [[fashion-mnist|Fashion Mnist]]
- **has_feature**: [[keras-callbacks|Keras Callbacks]]
- **can_be_used_for**: [[hyperparameter-tuning|Hyperparameter Tuning]]
- **component_of**: [[tensorflow|Tensorflow]]
- **supports**: [[custom-components-keras|Custom Components Keras]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*