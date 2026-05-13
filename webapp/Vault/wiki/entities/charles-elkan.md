---
type: entity
aliases: [Charles Elkan]
summary: A computer scientist who proposed an accelerated version of the K-Means algorithm using the triangle inequality.
relationships:
  - target: k-means-clustering
    type: improved
tags: [researcher, computer-scientist]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Charles Elkan

## Overview
Charles Elkan is a computer scientist recognized for his contributions to machine learning, particularly in the area of clustering algorithms.

## Contribution to K-Means
In a 2003 paper titled "Using the Triangle Inequality to Accelerate k-Means," Elkan introduced a significant improvement to the K-Means algorithm. His method considerably speeds up the algorithm by avoiding many unnecessary distance calculations between instances and centroids.

## The Elkan Algorithm
The acceleration is achieved by exploiting the triangle inequality and by maintaining lower and upper bounds for the distances between instances and centroids. This optimization allows the algorithm to prune a large number of distance computations in each iteration. This improved algorithm is the default one used by the `KMeans` class in the Scikit-Learn library.

## Relationships

- **improved**: [[k-means-clustering|K Means Clustering]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*