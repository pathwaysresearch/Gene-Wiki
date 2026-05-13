---
type: concept
aliases: [Probabilistic PCA]
summary: A probabilistic formulation of Principal Component Analysis (PCA) that models data as being generated from a lower-dimensional latent space with added Gaussian noise.
relationships:
  - target: pca
    type: is_a_probabilistic_version_of
tags: [dimensionality-reduction, probabilistic-models, linear-factor-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Probabilistic PCA

## Model Definition
Probabilistic PCA (PPCA), introduced by Tipping and Bishop (1999), is a probabilistic generative model framed as a modification of the factor analysis model. It assumes the observed data `x` is generated from a latent variable `h` via the process `x = Wh + b + σz`, where `z` is isotropic Gaussian noise. This yields a conditional distribution for `x` as `N(x; b, WW^T + σ^2 I)`, where `σ^2` is a scalar variance.

## Relationship to PCA
PPCA provides a probabilistic interpretation of PCA. As shown by Tipping and Bishop, standard PCA is recovered in the limit as the noise variance `σ` approaches zero. In this zero-noise limit, the conditional expected value of the latent variable `h` given an observation `x` becomes an orthogonal projection of `x` onto the principal subspace spanned by the columns of `W`.

## Properties and Limitations
The model captures the intuition that most of the variation in the data can be explained by the latent variables, with `σ^2` representing a small residual reconstruction error. A potential issue is that as `σ` becomes very small, the model's probability density becomes sharply concentrated around the d-dimensional subspace. This can cause the model to assign very low likelihood to data points that do not lie very close to this learned hyperplane.

## Relationships

- **is_a_probabilistic_version_of**: [[pca|Pca]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*