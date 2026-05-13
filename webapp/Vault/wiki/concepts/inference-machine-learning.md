---
type: concept
aliases: [Inference (Machine Learning)]
summary: The process of using a trained machine learning model to make predictions on new, unseen data.
relationships:
  - target: model-based-learning
    type: is_step_in
tags: [machine-learning, model-deployment, prediction]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Inference (Machine Learning)

## Definition
Inference is the phase in a machine learning project where a trained model is applied to make predictions on new cases. It is the operational use of the model after the learning or training phase is complete.

## Role in the ML Workflow
Inference is the final step of a typical machine learning project. It follows the stages of studying the data, selecting a model, and training the model on the training data by minimizing a cost function.

## The Goal of Generalization
The ultimate objective during inference is for the model to generalize well. This means that the predictions it makes on new, previously unseen data should be accurate, demonstrating that the model has learned the underlying patterns from the training data rather than just memorizing it.

## Relationships

- **is_step_in**: [[model-based-learning|Model Based Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*