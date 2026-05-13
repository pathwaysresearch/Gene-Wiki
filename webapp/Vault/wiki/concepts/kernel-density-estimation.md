---
type: concept
aliases: [Kernel Density Estimation]
summary: A non-parametric method to estimate the probability density function of a random variable by placing a kernel function (e.g., a Gaussian) on each data point and summing them.
tags: [density-estimation, non-parametric-statistics, machine-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Kernel Density Estimation

## Definition
Kernel density estimation, also known as Parzen window density estimation, is a non-parametric technique for estimating the probability density of a dataset. It is related to other local methods like locally weighted regression.

## How It Works
The method assumes that each data point in the sample generates its own small, local density function, which is represented by a kernel function. A common choice for the kernel is a Gaussian. The estimated density at any given query point **x** is then calculated as the average of the densities contributed by the kernels centered at each data point in the sample.

## Parameter Selection
The shape of the resulting density estimate is highly dependent on the bandwidth or width (*w*) of the kernel. As shown in Figure 20.9, a small width (e.g., w=0.02) can lead to a very "spiky" estimate that overfits the data, while a large width (e.g., w=0.20) can result in an overly smooth estimate that underfits. An appropriate value for the width, such as w=0.07 in the provided example, provides a good balance and can be selected using techniques like cross-validation.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*