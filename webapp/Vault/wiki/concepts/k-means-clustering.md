---
type: concept
aliases: [K-Means Clustering]
summary: An iterative clustering algorithm that partitions a dataset into a pre-specified number of clusters (k) by assigning each data point to the cluster with the nearest mean, or centroid.
relationships:
  - target: clustering
    type: is-a
tags: [clustering, unsupervised-learning, algorithm]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# K-Means Clustering

## Overview
K-Means is a popular clustering algorithm that aims to find the center of each cluster (referred to as a centroid) and assign each instance to the closest one. It is an unsupervised learning task, and the user must specify the number of clusters, k, that the algorithm should find. The cluster index assigned to an instance is often called its "label," which should not be confused with class labels in supervised learning.

## Algorithm and Implementation
The K-Means algorithm iteratively updates cluster centroids and instance assignments until convergence. In Scikit-Learn, it is implemented in the `KMeans` class. After fitting the model on a dataset, the cluster assignments for each instance are available via the `labels_` attribute, and the coordinates of the final cluster centroids are stored in the `cluster_centers_` attribute. A significant challenge is that determining the optimal value for k is often not straightforward and requires separate evaluation methods.

## Computational Complexity
The computational complexity of K-Means is generally linear with respect to the number of instances (m), the number of clusters (k), and the number of dimensions (n). This makes it one of the fastest clustering algorithms in practice, especially when the data has a clear clustering structure. However, in a worst-case scenario where the data lacks such structure, the complexity can increase exponentially with the number of instances, though this rarely occurs in practice.

## Algorithmic Improvements
The standard K-Means algorithm has been improved over the years. One notable improvement, proposed by Charles Elkan, uses the triangle inequality to accelerate the algorithm by avoiding many redundant distance calculations. This faster version is the default implementation in Scikit-Learn's `KMeans` class.

## Relationships

- **is-a**: [[clustering|Clustering]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*