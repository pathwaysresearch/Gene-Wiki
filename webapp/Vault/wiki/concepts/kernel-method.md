---
type: concept
aliases: [Kernel Method]
summary: A class of algorithms for pattern analysis, whose best known member is the Support Vector Machine (SVM), which use a kernel function to operate in a high-dimensional feature space.
relationships:
  - target: support-vector-machine
    type: is-used-by
tags: [machine-learning, supervised-learning, classification]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Kernel Method

## Definition and Function
A kernel is a function used in machine learning to weight the influence of each data example. As described in the text, a kernel function typically looks like a "bump," with its highest value at the center (zero distance) and decreasing values as distance increases. It is used in methods like locally weighted regression to determine how much weight to give to a training example $x_j$ when making a prediction for a query point $x_q$, based on the distance between them.

## Key Properties
A function must meet certain criteria to be used as a kernel. It should be symmetric around 0 and have its maximum value at 0. Furthermore, the area under the kernel function must remain bounded as the distance approaches infinity. While various shapes like Gaussians can be used, research suggests the specific shape is less critical than the kernel's width. The width is a crucial hyperparameter that controls the model's bias-variance tradeoff; too wide a kernel leads to underfitting, while too narrow a kernel leads to overfitting. This parameter is best chosen using cross-validation.

## Kernelization
The kernel concept can be generalized into a powerful technique called kernelization. This "kernel trick" can be applied to any learning algorithm that can be reformulated to work exclusively with dot products of pairs of data points. Once the algorithm is in this form, the standard dot product is replaced by a more complex kernel function. This implicitly maps the data into a higher-dimensional space where a linear separation might be possible, without ever having to compute the coordinates in that space. The text notes this can be done for algorithms like k-nearest-neighbors and perceptron learning.

## Relationships

- **is-used-by**: [[support-vector-machine|Support Vector Machine]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*