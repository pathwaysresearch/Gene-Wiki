---
type: concept
aliases: [Clustering as a Preprocessing Step]
summary: A technique where an unsupervised clustering algorithm, like K-Means, is used to transform input features before they are fed into a downstream supervised learning model, such as a classifier.
relationships:
  - target: k-means
    type: is_an_application_of
  - target: logistic-regression
    type: can_be_used_with
  - target: gridsearchcv
    type: uses
tags: [feature-engineering, preprocessing, machine-learning-pipeline, semi-supervised-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Clustering as a Preprocessing Step

## Concept Overview
Clustering can be used as a powerful preprocessing step in a larger machine learning pipeline. Instead of training a model on the original input features, the data is first grouped into clusters. This can significantly improve the performance of a subsequent supervised model, such as a classifier. The text notes that it is important to scale input features before running the clustering algorithm to prevent stretched clusters and poor performance.

## Implementation Example
The text demonstrates this technique by creating a scikit-learn `Pipeline` that first applies K-Means clustering and then feeds the result into a Logistic Regression classifier. This approach significantly improved classification accuracy, nearly halving the error rate in the provided example. The transformed features provided to the classifier are based on the cluster assignments of the original data.

## Hyperparameter Tuning
When clustering is used for preprocessing, the optimal number of clusters (k) is not determined by intrinsic metrics like inertia or silhouette score. Instead, the best value of k is the one that results in the best performance for the final downstream task (e.g., classification accuracy). This can be found efficiently using tools like `GridSearchCV` to search for the `n_clusters` value that maximizes the pipeline's cross-validation score. In the provided example, `GridSearchCV` found that 90 clusters was optimal, leading to a further boost in accuracy.

## Relationships

- **is_an_application_of**: [[k-means|K Means]]
- **can_be_used_with**: [[logistic-regression|Logistic Regression]]
- **uses**: [[gridsearchcv|Gridsearchcv]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*