---
type: concept
aliases: [Random Forest]
summary: An ensemble learning method consisting of a multitude of Decision Trees, typically trained with the bagging method on different random subsets of the data. It is known for its high accuracy and ability to measure feature importance.
relationships:
  - target: ensemble-learning
    type: is_a_type_of
  - target: decision-tree
    type: is_composed_of
  - target: bagging
    type: uses
  - target: scikit-learn
    type: implemented_in
tags: [machine-learning, ensemble-learning, classification, regression]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Random Forest

## Definition
A Random Forest is an ensemble of Decision Trees, generally trained via the bagging method (or sometimes pasting). It combines the predictions of many individual trees to produce a more robust and accurate final prediction. The method introduces extra randomness when growing trees beyond the instance sampling of bagging.

## Training and Prediction
The training process involves creating many Decision Trees, each trained on a different random sample of the training instances. The final prediction for a new instance is obtained by aggregating the predictions of all the individual trees. For classification, this is typically the majority vote (the most frequent prediction), as demonstrated by using SciPy's `mode()` function on the predictions of 1,000 trees.

## Feature Importance
Random Forests are very useful for getting a quick understanding of which features are most important for a prediction task. By measuring how much each feature contributes to reducing impurity on average across all the trees in the forest, the model can calculate a feature importance score. This is valuable for feature selection. For example, when trained on the MNIST dataset, a Random Forest can correctly identify the central pixels as being more important than the pixels at the edges.

## Relationships

- **is_a_type_of**: [[ensemble-learning|Ensemble Learning]]
- **is_composed_of**: [[decision-tree|Decision Tree]]
- **uses**: [[bagging|Bagging]]
- **implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*