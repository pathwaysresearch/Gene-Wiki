---
type: concept
aliases: [Randomized PCA]
summary: A stochastic algorithm that provides a fast approximation of the principal components, particularly efficient for large datasets when the target dimensionality is much smaller than the original.
relationships:
  - target: principal-component-analysis
    type: variant_of
tags: [pca, dimensionality-reduction, stochastic-algorithm]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Randomized PCA

## Definition
Randomized PCA is a stochastic algorithm that quickly finds an approximation of the first *d* principal components. It is an alternative to the full Singular Value Decomposition (SVD) method used in standard PCA.

## Performance and Use Cases
This algorithm is significantly faster than the full SVD approach, especially when the number of dimensions to reduce to (*d*) is much smaller than the original number of features or instances.

## Implementation in Scikit-Learn
Scikit-Learn's `PCA` class can utilize this algorithm by setting the `svd_solver` hyperparameter to `"randomized"`. The default setting, `svd_solver="auto"`, will automatically use Randomized PCA when the dataset is large (m or n > 500) and the target dimensionality is less than 80% of the original, otherwise it defaults to the full SVD approach.

## Relationships

- **variant_of**: [[principal-component-analysis|Principal Component Analysis]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*