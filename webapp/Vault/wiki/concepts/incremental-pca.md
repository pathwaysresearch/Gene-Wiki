---
type: concept
aliases: [Incremental PCA (IPCA)]
summary: A variant of PCA that allows for out-of-core or online learning by processing the training set in mini-batches, making it suitable for very large datasets.
relationships:
  - target: principal-component-analysis
    type: variant_of
tags: [pca, dimensionality-reduction, online-learning, big-data]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Incremental PCA (IPCA)

## Definition
Incremental PCA (IPCA) is an algorithm developed to overcome a major limitation of standard PCA implementations, which require the entire training set to fit in memory. IPCA processes the dataset in smaller chunks or mini-batches.

## How It Works
Instead of fitting the model on the entire dataset at once, the training set is split into mini-batches. The IPCA algorithm is then fed one mini-batch at a time. In Scikit-Learn's `IncrementalPCA` class, this is achieved by repeatedly calling the `partial_fit()` method with each mini-batch, rather than using the `fit()` method on the whole set.

## Applications
IPCA is highly useful for training on large datasets that cannot be loaded into memory all at once. It also enables the application of PCA in an online learning setting, where the model can be updated as new data instances arrive over time.

## Relationships

- **variant_of**: [[principal-component-analysis|Principal Component Analysis]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*