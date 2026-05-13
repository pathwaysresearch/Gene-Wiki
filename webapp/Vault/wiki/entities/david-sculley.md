---
type: entity
aliases: [David Sculley]
summary: A researcher who proposed the Mini-Batch K-Means algorithm for clustering large-scale datasets.
relationships:
  - target: mini-batch-k-means
    type: created
tags: [researcher, computer-scientist]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# David Sculley

## Overview
David Sculley is a machine learning researcher known for his work on scalable machine learning algorithms.

## Contribution to K-Means
In a 2010 paper, Sculley proposed an important variant of the K-Means algorithm called Mini-Batch K-Means. This variant was designed to address the challenge of clustering massive datasets that cannot fit into a computer's memory.

## Mini-Batch K-Means Algorithm
The algorithm works by using small, random batches of data at each iteration to update the cluster centroids, rather than using the full dataset. This approach significantly speeds up the algorithm, typically by a factor of three or four, and makes it possible to apply K-Means to very large datasets. Scikit-Learn implements this algorithm in its `MiniBatchKMeans` class.

## Relationships

- **created**: [[mini-batch-k-means|Mini Batch K Means]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*