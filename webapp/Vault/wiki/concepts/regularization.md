---
type: concept
aliases: [Regularization]
summary: A technique used in machine learning to constrain a model, making it simpler to reduce the risk of overfitting and improve its ability to generalize to new data.
relationships:
  - target: overfitting
    type: prevents
  - target: hyperparameter-tuning
    type: is-configured-by
tags: [machine-learning, model-tuning, overfitting]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Regularization

## Definition
Regularization is defined as the process of constraining a model to make it simpler and reduce the risk of overfitting. The goal is to find the right balance between fitting the training data perfectly and keeping the model simple enough to ensure it will generalize well.

## How It Works
Regularization reduces a model's *degrees of freedom*. For example, in a linear model with two parameters, height ($	heta_0$) and slope ($	heta_1$), regularization might force the algorithm to keep the slope parameter ($	heta_1$) small. This results in a model that is simpler than one with two unconstrained parameters but more complex than one with only a single parameter, effectively finding a middle ground between complexity and simplicity.

## Application
The text illustrates regularization with a figure showing three models. A model trained with a regularization constraint is shown to provide a better fit to the underlying data pattern than an unregularized model trained on the same incomplete data, demonstrating its effectiveness in improving generalization.

## Relationships

- **prevents**: [[overfitting|Overfitting]]
- **is-configured-by**: [[hyperparameter-tuning|Hyperparameter Tuning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*