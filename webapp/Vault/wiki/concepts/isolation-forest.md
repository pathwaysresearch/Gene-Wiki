---
type: concept
aliases: [Isolation Forest]
summary: An efficient algorithm for outlier detection, particularly in high-dimensional datasets, that works by randomly partitioning data until anomalies are isolated.
tags: [anomaly-detection, outlier-detection, ensemble-methods]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Isolation Forest

## Overview
The Isolation Forest is an efficient algorithm specifically designed for outlier or anomaly detection. It is noted to be especially effective when applied to high-dimensional datasets.

## How It Works
The algorithm constructs a Random Forest where each Decision Tree is grown in a random manner. At every node within a tree, the algorithm randomly selects a feature and then picks a random threshold value between that feature's minimum and maximum values to split the dataset in two. This process of random partitioning is repeated, gradually chopping the dataset into smaller and smaller pieces until instances are isolated.

## Anomaly Detection Principle
The core idea behind the Isolation Forest is that an anomaly is usually far from other instances in the feature space. Because of this, anomalous data points are more susceptible to isolation and will, on average, be separated from other instances in fewer random splits than a normal data point. The algorithm leverages this property to identify outliers.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*