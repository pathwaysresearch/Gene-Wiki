---
type: concept
aliases: [Independent Component Analysis (ICA)]
summary: A computational method for separating a multivariate signal into additive, non-Gaussian subcomponents that are assumed to be statistically independent.
relationships:
  - target: pca
    type: is_related_to
  - target: nice
    type: is_generalized_by
tags: [signal-processing, representation-learning, linear-factor-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Independent Component Analysis (ICA)

## Overview
Independent Component Analysis (ICA) is one of the oldest representation learning algorithms. It is most often used as an analysis tool for separating signals rather than for generating new data or estimating the density of existing data.

## Distinction from Generative Models
Many variants of ICA are not generative models in the sense that they can represent the data distribution `p(x)` or draw samples from it. These variants often only define a transformation to find the latent components `h` from the data `x` (e.g., by maximizing the kurtosis of `h = W^-1x`), but do not explicitly represent the distribution of the components `p(h)`.

## Nonlinear Extensions
Just as PCA can be generalized to nonlinear autoencoders, ICA can be extended to nonlinear generative models where a nonlinear function is used to generate the observed data. An example of such a nonlinear extension is the approach of Nonlinear Independent Components Estimation (NICE), which uses a series of invertible transformations to build a model where the likelihood can be computed exactly.

## Relationships

- **is_related_to**: [[pca|Pca]]
- **is_generalized_by**: [[nice|Nice]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*