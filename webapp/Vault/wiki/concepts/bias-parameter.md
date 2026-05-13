---
type: concept
aliases: [Bias Parameter]
summary: The intercept term in an affine transformation used in machine learning models, which allows the output to be non-zero even when the input is zero.
relationships:
  - target: linear-regression
    type: is_component_of
tags: [model-parameter, linear-algebra, affine-transformation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bias Parameter

## Definition
In the context of an affine transformation like that used in linear regression, the intercept term, often denoted by $b$, is called the bias parameter. It allows the model to produce a non-zero output even when the input vector is zero. A model using only weights can incorporate a bias by augmenting the input vector $\boldsymbol{x}$ with an extra entry that is always set to 1; the weight corresponding to this entry then functions as the bias.

## Etymology
The terminology for this parameter derives from the perspective that the output of the transformation is 'biased' toward being the value $b$ in the absence of any input. This provides a baseline or offset for the model's predictions.

## Distinction from Statistical Bias
It is important to distinguish the bias parameter of an affine transformation from the concept of a statistical bias. A statistical bias occurs when a statistical estimation algorithm's expected estimate of a quantity is not equal to the true value of that quantity. The bias parameter is a component of the model's structure, not a property of the estimation process.

## Relationships

- **is_component_of**: [[linear-regression|Linear Regression]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*