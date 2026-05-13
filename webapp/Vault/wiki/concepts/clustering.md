---
type: concept
aliases: [Clustering]
summary: An unsupervised machine learning task that involves grouping a set of objects such that objects in the same group (cluster) are more similar to each other than to those in other groups.
tags: [unsupervised-learning, data-analysis]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
relationships:
  - target: unsupervised-learning
    type: is_a_type_of
---

# Clustering

## Definition
Clustering is an unsupervised learning task where the goal is to assign each instance in a dataset to a specific group, or cluster. Unlike supervised tasks like classification, clustering algorithms work with unlabeled datasets, meaning they must discover the inherent groupings in the data without any pre-existing labels.

## Contrast with Classification
Clustering is often contrasted with classification. A classification algorithm is trained on a labeled dataset (e.g., the Iris dataset with species labels) to learn how to categorize new instances. In contrast, a clustering algorithm would be given the same Iris dataset without the species labels and would be tasked with identifying the distinct groups of flowers based solely on their features, such as petal and sepal measurements.

## Application and Performance
Clustering algorithms can leverage all available features in a dataset to identify clusters. For example, when applied to the Iris dataset, which has four features, a clustering algorithm like a Gaussian mixture model can identify the three distinct species with high accuracy, demonstrating its ability to find meaningful structure in unlabeled data.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*