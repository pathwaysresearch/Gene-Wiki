---
type: concept
aliases: [Feature Extraction]
summary: A specific method of dimensionality reduction where new, more informative features are created by combining or transforming existing ones.
relationships:
  - target: dimensionality-reduction
    type: is_a
tags: [machine-learning, data-preprocessing, feature-engineering]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Feature Extraction

## Definition
Feature extraction is a form of dimensionality reduction where several correlated features are merged into a single, more representative feature. This process aims to create a more compact and informative representation of the original data.

## Example
A practical example is in the context of predicting car values. A car's mileage may be highly correlated with its age. A feature extraction algorithm can merge these two features into a single new feature that represents the car's overall wear and tear.

## Role in Machine Learning
Feature extraction is presented as a valuable step to perform on training data before it is fed to another Machine Learning algorithm. By reducing the dimension of the data, it can help improve model speed and reduce memory usage.

## Relationships

- **is_a**: [[dimensionality-reduction|Dimensionality Reduction]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*