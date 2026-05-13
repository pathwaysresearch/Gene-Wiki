---
type: concept
aliases: [Model-Based Learning]
summary: A machine learning approach that involves selecting a model, training it on data to find the best parameters, and then using that model for predictions.
relationships:
  - target: model-parameters
    type: uses
  - target: cost-function
    type: uses
  - target: inference-machine-learning
    type: includes_step
tags: [machine-learning, learning-paradigm]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Model-Based Learning

## The Generalization Process
Model-based learning is a way for machine learning systems to generalize from training examples to make predictions on new cases. The core idea is to select a specific type of model, such as a linear model, and then train it on the available data.

## Training the Model
Training involves finding the optimal values for the model's parameters. This is achieved by defining a performance measure, which can be a utility function (measuring how good the model is) or, more commonly, a cost function (measuring how bad it is). The learning algorithm searches for the parameter values that minimize the cost function or maximize the utility function.

## Making Predictions (Inference)
Once the model has been trained and its parameters are set, it can be used to make predictions on new, unseen data. This final step is called inference. The success of the project depends on how well the trained model generalizes to these new cases.

## Relationships

- **uses**: [[model-parameters|Model Parameters]]
- **uses**: [[cost-function|Cost Function]]
- **includes_step**: [[inference-machine-learning|Inference Machine Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*