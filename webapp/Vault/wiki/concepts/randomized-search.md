---
type: concept
aliases: [Randomized Search]
summary: A hyperparameter tuning technique that samples a fixed number of random combinations from the specified hyperparameter distributions, often more efficient than an exhaustive grid search.
relationships:
  - target: grid-search
    type: is_an_alternative_to
tags: [hyperparameter-tuning, model-optimization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Randomized Search

## Definition
Randomized Search is a hyperparameter tuning technique used as an alternative to Grid Search, especially when the hyperparameter search space is large. Instead of trying all possible combinations, it evaluates a specified number of random combinations by selecting a random value for each hyperparameter at every iteration.

## Advantages Over Grid Search
This approach offers two main benefits. First, it allows for a broader exploration of the hyperparameter space; if run for 1,000 iterations, it will explore 1,000 different values for each hyperparameter, unlike Grid Search which is limited to a few predefined values. Second, it gives the user direct control over the computational budget by simply setting the number of iterations, making it more flexible and often more efficient than an exhaustive search.

## Implementation
The `RandomizedSearchCV` class in Scikit-Learn is used in a similar way to `GridSearchCV`. It takes an estimator, a description of the hyperparameter space, and the number of iterations to perform to find the best combination of hyperparameters.

## Relationships

- **is_an_alternative_to**: [[grid-search|Grid Search]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*