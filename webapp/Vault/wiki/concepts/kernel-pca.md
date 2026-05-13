---
type: concept
aliases: [Kernel PCA]
summary: A non-linear dimensionality reduction technique that uses the kernel trick to project data, which is linearly inseparable in its original space, into a lower-dimensional space where it becomes separable.
tags: [dimensionality-reduction, kernel-methods, unsupervised-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Kernel PCA

## How It Works
Kernel PCA (kPCA) applies the kernel trick to perform non-linear dimensionality reduction. Mathematically, this process is equivalent to first mapping the training set to a high-dimensional, or even infinite-dimensional, feature space using a feature map (φ). After this transformation, standard linear PCA is applied to project the transformed training set down to a lower-dimensional space. This allows kPCA to unroll complex manifolds like the Swiss roll dataset.

## Reconstruction Challenge
Reconstruction of instances from the reduced space is not as straightforward as with linear PCA. If one were to invert the linear PCA step for an instance in the reduced space, the resulting reconstructed point would lie in the high-dimensional feature space, not the original space. Since the feature space can be infinite-dimensional, computing this point directly is impossible.

## The Reconstruction Pre-image
To overcome the reconstruction challenge and evaluate the model, it is possible to find a "reconstruction pre-image." This is a point in the original space that would map very close to the reconstructed point in the feature space. By finding this pre-image, one can measure its squared distance to the original instance. This distance can then be used as a reconstruction error metric to select the best kernel and hyperparameters for the kPCA model in an unsupervised manner.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*