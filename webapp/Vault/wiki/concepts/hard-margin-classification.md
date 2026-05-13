---
type: concept
aliases: [Hard Margin Classification]
summary: A type of Support Vector Machine (SVM) classification that strictly requires all training instances to be correctly classified and outside the margin, making it sensitive to outliers.
relationships:
  - target: soft-margin-classification
    type: is_contrasted_with
  - target: support-vector-machine
    type: is_a_type_of
tags: [svm, classification, linear-models]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Hard Margin Classification

## Definition
Hard margin classification is a method where the model, typically a Support Vector Machine, strictly imposes that all training instances must be located 'off the street' (outside the margin) and on the correct side of the decision boundary. No instances are permitted to fall within the margin or be misclassified.

## Limitation 1: Linear Separability
A primary issue with hard margin classification is that it only works if the data is perfectly linearly separable. If the classes cannot be separated by a single straight line without any errors, it is impossible to find a hard margin.

## Limitation 2: Sensitivity to Outliers
This approach is highly sensitive to outliers. The presence of just one outlier can dramatically change the resulting decision boundary. The text shows an example where a single outlier forces the margin to become extremely narrow and results in a model that will probably not generalize as well to new data.

## Relationships

- **is_contrasted_with**: [[soft-margin-classification|Soft Margin Classification]]
- **is_a_type_of**: [[support-vector-machine|Support Vector Machine]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*