---
type: concept
aliases: [Fast-MCD (Minimum Covariance Determinant)]
summary: An outlier detection algorithm that assumes inliers are generated from a single Gaussian distribution and robustly estimates its parameters by ignoring likely outliers.
tags: [anomaly-detection, outlier-detection, robust-statistics]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Fast-MCD (Minimum Covariance Determinant)

## Overview
Fast-MCD (Minimum Covariance Determinant) is an algorithm useful for outlier detection, particularly for the purpose of cleaning up a dataset. In the Scikit-Learn library, it is implemented by the `EllipticEnvelope` class.

## Core Assumptions
The algorithm operates on the assumption that the normal instances, or inliers, within a dataset are generated from a single Gaussian distribution. It simultaneously assumes that the dataset is contaminated with outliers that do not originate from this same distribution.

## Robust Estimation
When estimating the parameters of the Gaussian distribution that describe the inliers (i.e., the shape of the elliptic envelope around them), the Fast-MCD algorithm is designed to carefully ignore the instances that it identifies as most likely to be outliers. This robust estimation process results in a more accurate characterization of the inlier distribution, which in turn improves its ability to correctly identify the actual outliers.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*