---
type: concept
aliases: [k-Nearest-Neighbors Density Estimation]
summary: A non-parametric method for estimating the probability density function at a point based on the volume of the region containing its k nearest neighbors in the dataset.
tags: [density-estimation, non-parametric-statistics, machine-learning, k-nn]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# k-Nearest-Neighbors Density Estimation

## Definition
k-Nearest-Neighbors (k-NN) is a non-parametric method used for density estimation. It estimates the density at a query point by examining the properties of the neighborhood containing its *k* nearest data points.

## How It Works
For a given query point, the algorithm identifies the *k* data points from the sample that are closest to it, forming its k-nearest-neighborhood. The density at the query point is then estimated based on the size (volume) of this neighborhood. A smaller volume for the k-neighborhood implies a higher density, as the points are more tightly packed.

## Parameter Selection
The choice of the parameter *k* is crucial for the quality of the density estimate. As illustrated in Figure 20.8, a small value of *k* (e.g., k=3) can produce a very "spiky" and noisy estimate that overfits the data. Conversely, a large value of *k* (e.g., k=40) can lead to an overly smooth estimate that misses underlying structural details. An intermediate value (e.g., k=10) often provides a reasonable fit, and the best value for *k* can be determined empirically using cross-validation.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*