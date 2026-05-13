---
type: concept
aliases: [Slow Feature Analysis]
summary: A linear factor model that learns features from a time-varying signal that change as slowly as possible, subject to constraints of zero mean, unit variance, and decorrelation.
relationships:
  - target: linear-factor-model
    type: is_a
  - target: principal-component-analysis
    type: related_to
tags: [linear-factor-model, feature-learning, unsupervised-learning, time-series-analysis]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Slow Feature Analysis

## Definition
Slow Feature Analysis (SFA) is an unsupervised learning algorithm that extracts slowly varying features from a rapidly varying input signal. It is a type of linear factor model that identifies the underlying causes of variation in the data that change on a slower timescale.

## Key Constraints
To ensure a well-posed and useful solution, SFA operates under several key constraints. The learned features must have a zero mean to make the solution unique. They must also have unit variance to prevent the pathological solution where all features collapse to zero. When learning multiple features, they are constrained to be linearly decorrelated from each other, which forces the model to discover different slow signals rather than repeatedly capturing the single slowest one.

## How It Works
The SFA problem can be solved in a closed form using linear algebra. While the core method is linear, SFA is typically used to learn nonlinear features. This is achieved by first applying a nonlinear basis expansion to the input vector, such as a quadratic expansion containing all products of input elements. After this expansion, the standard linear SFA algorithm is applied. This approach allows linear SFA modules to be composed to learn deep, nonlinear slow features.

## Relationships

- **is_a**: [[linear-factor-model|Linear Factor Model]]
- **related_to**: [[principal-component-analysis|Principal Component Analysis]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*