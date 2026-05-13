---
type: concept
aliases: [Decision Boundary]
summary: A threshold or surface in the feature space that separates instances of different classes as predicted by a classification model.
relationships:
  - target: logistic-regression
    type: is_a_concept_in
  - target: support-vector-machine
    type: is_a_concept_in
  - target: classification
    type: is_a_concept_in
tags: [classification, machine-learning-concepts, model-interpretation]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Decision Boundary

## Definition
A decision boundary is a threshold used by a classifier to separate classes. For a probabilistic model like Logistic Regression, it represents the points in the feature space where the estimated probabilities for two or more classes are equal. In a binary classification task, this is typically where the probability for each class is 50%.

## Role in Prediction
The decision boundary is central to how a classifier makes its final prediction. An instance is assigned to a class based on which side of the boundary it falls. For example, the text describes a classifier for Iris flowers where the decision boundary is at a petal width of 1.6 cm. If a flower's petal width is higher than 1.6 cm, it is predicted to be an Iris-Virginica; otherwise, it is not.

## Visualization
In a problem with two features, the decision boundary can be visualized as a line or curve separating the data points of different classes. The text refers to a plot with two features (petal width and length) where a dashed line represents the points where the model estimates a 50% probability, clearly marking the boundary between the two predicted classes.

## Relationships

- **is_a_concept_in**: [[logistic-regression|Logistic Regression]]
- **is_a_concept_in**: [[support-vector-machine|Support Vector Machine]]
- **is_a_concept_in**: [[classification|Classification]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*