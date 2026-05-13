---
type: concept
aliases: [Custom Keras Model]
summary: A technique in Keras for creating flexible neural network architectures by subclassing the `keras.models.Model` class and defining the forward pass in the `call()` method.
relationships:
  - target: reconstruction-loss
    type: can_implement
tags: [keras, tensorflow, model-architecture]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Custom Keras Model

## Definition
A Custom Keras Model is a user-defined model architecture created by subclassing the `keras.models.Model` base class. This approach provides maximum flexibility, allowing for the construction of complex models with non-sequential data flows, shared layers, and multiple inputs or outputs that are not possible with the Sequential API.

## Implementation
To create a custom model, a developer defines a new class that inherits from `keras.models.Model`. In the constructor (`__init__` method), all the necessary layers and variables for the model are created and assigned as attributes of the class instance. The core logic of the model, defining the forward pass, is then implemented in the `call()` method, which specifies how input tensors are processed by the layers to produce an output.

## Example Use Case
The text illustrates this concept with a model that includes a `ResidualBlock`, which adds its inputs to its outputs. This type of architecture, where skip connections are present, requires the subclassing API. The `call()` method would define the flow of data through the dense layers and the residual blocks, including the addition operation that characterizes the residual connection.

## Relationships

- **can_implement**: [[reconstruction-loss|Reconstruction Loss]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*