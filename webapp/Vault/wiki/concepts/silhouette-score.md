---
type: concept
aliases: [Silhouette Score]
summary: A metric used to calculate the quality of a clustering result, representing how similar an object is to its own cluster compared to other clusters.
relationships:
  - target: k-means-clustering
    type: used-to-evaluate
  - target: clustering
    type: used-to-evaluate
tags: [model-evaluation, clustering, metric]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Silhouette Score

## Definition
The Silhouette Score is a metric used to evaluate the performance of a clustering algorithm and can help in selecting the optimal number of clusters, k. It is calculated as the mean of the Silhouette Coefficient over all instances in the dataset. While more computationally expensive than some other methods, it provides a more precise measure of cluster validity.

## The Silhouette Coefficient
For a single instance, the Silhouette Coefficient is calculated as (b - a) / max(a, b). In this formula, 'a' represents the mean intra-cluster distance (the average distance to other instances within the same cluster), and 'b' represents the mean nearest-cluster distance (the average distance to the instances of the next closest cluster).

## Interpretation and Usage
The Silhouette Coefficient ranges from -1 to +1. A coefficient close to +1 indicates that the instance is well-placed within its cluster and far from other clusters. A coefficient near 0 suggests the instance is close to a boundary between two clusters. A coefficient near -1 implies that the instance might have been assigned to the wrong cluster. In Scikit-Learn, the `silhouette_score()` function can be used to compute this metric for a given set of instances and their cluster labels.

## Relationships

- **used-to-evaluate**: [[k-means-clustering|K Means Clustering]]
- **used-to-evaluate**: [[clustering|Clustering]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*