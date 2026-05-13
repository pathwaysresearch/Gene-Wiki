---
type: concept
aliases: [Locally Linear Embedding]
summary: A manifold learning technique for dimensionality reduction that works by preserving the local linear relationships between neighboring data points.
tags: [dimensionality-reduction, manifold-learning, unsupervised-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Locally Linear Embedding

## How It Works
Locally Linear Embedding (LLE) is a dimensionality reduction algorithm that operates in two main steps. The first step identifies the local structure of the data, and the second step maps the data to a lower-dimensional space while preserving this structure.

## Step 1: Modeling Local Relationships
The first step involves modeling the local linear relationships between training instances. For each training instance x⁽ⁱ⁾, the algorithm identifies its k closest neighbors. It then finds a set of weights, wᵢ,ⱼ, that reconstruct x⁽ⁱ⁾ as a linear combination of these neighbors. This is formulated as a constrained optimization problem where the goal is to minimize the squared distance between the instance and its reconstruction, subject to the constraints that weights are zero for non-neighbors and the weights for each instance sum to one.

## The Weight Matrix
The result of the first step is a weight matrix W, which contains all the weights wᵢ,ⱼ. This matrix effectively encodes the local linear relationships inherent in the training data. The second step of the algorithm then uses this weight matrix to map the training instances to a lower-dimensional embedding that best preserves these local relationships.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*