---
type: concept
aliases: [Principal Components Analysis]
summary: A machine learning algorithm for lossy data compression that reduces the dimensionality of data by projecting it onto a lower-dimensional space.
tags: [machine-learning, dimensionality-reduction, linear-algebra]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Principal Components Analysis

## Overview
Principal components analysis (PCA) is a simple machine learning algorithm, derivable from basic linear algebra, used for applying lossy compression to a collection of data points. The goal is to store the points using less memory while minimizing the loss of precision.

## How It Works
PCA encodes high-dimensional points (x in R^n) into lower-dimensional code vectors (c in R^l, where l < n). This is achieved through an encoder function, f(x) = D^T x, where D is an encoding matrix. A reconstruction operation, r(x) = DD^T x, attempts to recover the original point from its code.

## The Optimization Problem
The core of PCA is choosing the optimal encoding matrix D. This is done by minimizing the reconstruction error over all data points, typically measured by the Frobenius norm of the difference between the original and reconstructed data matrices. The optimization is performed subject to the constraint that the columns of D are orthonormal (D^T D = I_l).

---
*Extracted from: Deep+Learning+Ian+Goodfellow*