---
type: concept
aliases: [Whitening]
summary: A data preprocessing technique, also known as sphering, that transforms a dataset so that its features have zero mean and equal variance.
relationships:
  - target: preprocessing
    type: is-a-type-of
  - target: global-contrast-normalization
    type: is-a-type-of
tags: [preprocessing, data-preparation, statistics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Whitening

## Definition
Whitening is a preprocessing transformation applied to data. The text states that this technique is more commonly known as sphering.

## Goal
The objective of whitening is to transform the input data so that each feature has zero mean and equal variance. This is a common step before applying algorithms like Principal Component Analysis (PCA), as it ensures the multivariate normal distribution used by PCA has spherical contours.

## Relation to Contrast Normalization
The text mentions whitening in the context of global contrast normalization (GCN). It is presented as a specific form of GCN, highlighting its role in standardizing the statistical properties of the input data.

## Relationships

- **is-a-type-of**: [[preprocessing|Preprocessing]]
- **is-a-type-of**: [[global-contrast-normalization|Global Contrast Normalization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*