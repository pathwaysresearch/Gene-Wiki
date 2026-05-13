---
type: concept
aliases: [Reconstruction Loss]
summary: A regularization technique where a model is trained not only on its primary task but also on its ability to reconstruct its own inputs, encouraging hidden layers to preserve information.
relationships:
  - target: custom-keras-model
    type: is_implemented_in
tags: [regularization, loss-function, keras]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Reconstruction Loss

## Definition
Reconstruction loss is a form of regularization loss used in neural networks. It is designed to force the model to preserve as much information as possible through its hidden layers, even information that may not be directly useful for the primary task, such as regression or classification. This often helps improve the model's ability to generalize to new data.

## How It Works
To implement reconstruction loss, an auxiliary output layer is added to the model, typically connected to one of the last hidden layers. The role of this layer is to try to reconstruct the original inputs of the model. A loss function, such as mean squared error, is then computed between the reconstructed output and the original inputs. This reconstruction error, often scaled by a small factor to ensure the main task's loss dominates, is added to the model's list of losses via the `add_loss()` method. Keras automatically includes this additional loss in the total loss function during training.

## Implementation in a Custom Model
The text provides an example within a custom model class called `ReconstructingRegressor`. An extra `Dense` layer is created in the `build()` method to ensure its output shape matches the input shape. In the `call()` method, the model computes both the primary regression output and the reconstruction. The mean squared difference between the inputs and the reconstruction is calculated and added to the model's losses, thereby regularizing the model by penalizing information loss in the hidden layers.

## Relationships

- **is_implemented_in**: [[custom-keras-model|Custom Keras Model]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*