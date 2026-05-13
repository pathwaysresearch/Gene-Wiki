---
type: concept
aliases: [Mini-Batch K-Means]
summary: A variant of the K-Means algorithm that uses small, random batches of data at each iteration to update centroids, making it faster and scalable to datasets that don't fit in memory.
relationships:
  - target: k-means-clustering
    type: variant-of
  - target: david-sculley
    type: developed-by
tags: [clustering, unsupervised-learning, scalable-ml, algorithm]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Mini-Batch K-Means

## Overview
Mini-Batch K-Means is an important variant of the standard K-Means algorithm, proposed in a 2010 paper by David Sculley. Its primary advantage is its increased speed and its ability to cluster huge datasets that do not fit in system memory.

## How It Works
Instead of using the entire dataset at each iteration to update the cluster centroids, the Mini-Batch K-Means algorithm uses small, randomly sampled mini-batches of the data. At each iteration, the centroids are moved slightly based on the information from the current mini-batch. This approach significantly accelerates the convergence process, often making the algorithm three to four times faster than the standard batch K-Means.

## Implementation in Scikit-Learn
Scikit-Learn provides an implementation of this algorithm in the `MiniBatchKMeans` class. It can be used in a similar fashion to the standard `KMeans` class and is particularly well-suited for large-scale clustering tasks where memory or time constraints are a concern.

## Relationships

- **variant-of**: [[k-means-clustering|K Means Clustering]]
- **developed-by**: [[david-sculley|David Sculley]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*