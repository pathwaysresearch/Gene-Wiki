---
type: concept
aliases: [Auxiliary Output]
summary: A secondary output in a neural network, typically connected to a lower-level layer, that acts as a regularization mechanism during training.
relationships:
  - target: keras-functional-api
    type: implemented_using
  - target: regularization
    type: is_a_type_of
tags: [neural-network-architecture, regularization, keras]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Auxiliary Output

## Definition
An auxiliary output is an additional output added to a neural network model, which branches off from an intermediate or hidden layer rather than the final layer. Its primary purpose is to act as a regularization technique. By providing a loss signal deeper in the network, it encourages the lower layers to learn useful features independently, which can help mitigate issues like vanishing gradients and improve overall model performance.

## Implementation in Keras
Adding an auxiliary output is easily accomplished using the Keras Functional API. A new output layer, such as a `Dense` layer, is created and connected to the output of a chosen hidden layer. This new output is then included in the list of outputs when the `keras.models.Model` is instantiated.

## Training with Multiple Outputs
When a model has multiple outputs, each requires its own loss function. During model compilation, a list of losses must be provided. Keras sums these individual losses to compute the final loss used for training. To prioritize the main output over the auxiliary one, `loss_weights` can be specified during compilation (e.g., giving the main output's loss a weight of 0.9 and the auxiliary's a weight of 0.1). When training the model, labels must be provided for each output.

## Relationships

- **implemented_using**: [[keras-functional-api|Keras Functional Api]]
- **is_a_type_of**: [[regularization|Regularization]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*