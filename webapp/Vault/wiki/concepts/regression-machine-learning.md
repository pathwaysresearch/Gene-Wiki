---
type: concept
aliases: [Regression (Machine Learning)]
summary: A supervised learning task where the goal is to predict a continuous numerical value, such as a price or temperature.
relationships:
  - target: supervised-learning
    type: is-a-type-of
  - target: root-mean-square-error
    type: is-evaluated-by
tags: [machine-learning, supervised-learning, prediction]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Regression (Machine Learning)

## Definition
Regression is a type of supervised learning task where the system is asked to predict a continuous value. This is in contrast to classification tasks, where the goal is to predict a discrete category.

## Example from Text
The California housing price problem is classified as a regression task because the goal is to predict the median housing price, which is a numerical value, for any given district.

## Subtypes
The text further breaks down the housing problem into more specific categories. It is a *multiple regression* problem because it uses multiple features (population, median income, etc.) to make a prediction. It is also a *univariate regression* problem because it predicts only a single value (the median housing price) for each district. This is contrasted with *multivariate regression*, which would involve predicting multiple values per district.

## Relationships

- **is-a-type-of**: [[supervised-learning|Supervised Learning]]
- **is-evaluated-by**: [[root-mean-square-error|Root Mean Square Error]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*