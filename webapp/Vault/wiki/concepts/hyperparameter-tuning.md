---
type: concept
aliases: [Hyperparameter Tuning]
summary: The process of selecting the optimal values for a model's hyperparameters, such as the amount of regularization, to achieve the best performance on new data. The process of systematically searching for the optimal combination of hyperparameters for a machine learning model to achieve the best performance on a validation set.
relationships:
  - target: regularization
    type: is-used-for
  - target: keras
    type: can_be_applied_to
tags: [machine-learning, model-selection, optimization, machine-learning-workflow]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Hyperparameter Tuning

## Definition
Hyperparameter tuning is the process of selecting the best values for a model's hyperparameters, which are parameters not learned from the data itself but set prior to training. An example given is choosing the value of the regularization hyperparameter.

## Example Process
To find the best value for a hyperparameter, one option is to train many different models with different hyperparameter values (e.g., 100 models with 100 different values) and select the one that produces the lowest generalization error on a validation set.

## A Critical Warning
The text highlights a major pitfall: if you use the test set to find the best hyperparameter, you are effectively fitting the model to that test set. This means your final measurement of the generalization error on that same test set will be deceptively low, and the model will likely perform worse in production on truly new data.

## Relationships

- **is-used-for**: [[regularization|Regularization]]
- **can_be_applied_to**: [[keras|Keras]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*