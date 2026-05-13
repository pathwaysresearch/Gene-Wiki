---
type: entity
aliases: [Nonlinear Independent Components Estimation (NICE)]
summary: A nonlinear extension of Independent Component Analysis (ICA) that uses a series of specially designed invertible transformations to build a deep generative model with an exact and tractable likelihood.
relationships:
  - target: independent-component-analysis
    type: is_a_nonlinear_extension_of
tags: [generative-model, deep-learning, ica]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Nonlinear Independent Components Estimation (NICE)

## Overview
Nonlinear Independent Components Estimation, or NICE, is a nonlinear extension of the ICA approach proposed by Dinh et al. (2014). It functions as a nonlinear generative model, providing a way to generalize linear factor models like ICA to more complex, nonlinear data manifolds.

## Architectural Design
The NICE model is constructed by stacking a series of invertible transformations, which act as encoder stages. The crucial property of these transformations is that the determinant of the Jacobian matrix for each transformation can be computed very efficiently.

## Key Advantage
The ability to efficiently compute the Jacobian determinant for each transformation in the stack makes it possible to compute the exact likelihood of the data under the model using the change of variables formula. This allows the model to be trained directly via maximum likelihood, a significant advantage over many other deep generative models that must rely on variational approximations or adversarial training.

## Relationships

- **is_a_nonlinear_extension_of**: [[independent-component-analysis|Independent Component Analysis]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*