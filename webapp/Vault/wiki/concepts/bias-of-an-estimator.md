---
type: concept
aliases: [Bias (of an estimator)]
summary: A measure of the expected deviation of a statistical estimator from the true value of the parameter it is intended to estimate. An estimator is unbiased if its expected value equals the true parameter value.
relationships:
  - target: variance-of-an-estimator
    type: is_traded_off_with
  - target: bias-variance-tradeoff
    type: is_a_component_of
tags: [statistics, estimation-theory, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bias (of an estimator)

## Definition
Bias is one of the key sources of error in an estimator. It measures the expected deviation of a point estimate of a parameter, denoted \hat{\theta}, from the true, underlying value of the parameter, \theta. Formally, the bias is defined as bias(\hat{\theta}_m) = E[\hat{\theta}_m] - \theta. An estimator is considered unbiased if its bias is zero, meaning its expected value is equal to the true parameter value.

## Example: Bernoulli Mean Estimator
The text provides a detailed example using a Bernoulli distribution. For a set of m i.i.d. samples from a Bernoulli distribution with mean \theta, a common estimator is the sample mean, \hat{\theta}_m = \frac{1}{m} \sum_{i=1}^m x^{(i)}. The text shows through a step-by-step derivation that the expected value of this estimator, E[\hat{\theta}_m], is equal to \theta. Since E[\hat{\theta}_m] - \theta = 0, the sample mean is an unbiased estimator of the Bernoulli mean parameter.

## Role in Model Error
Bias represents a form of systematic error in an estimation. A model with high bias might be too simple for the data (underfitting) and consistently fail to capture the true underlying relationship, even with a large amount of training data. It is one of the two key components, along with variance, that are considered in the bias-variance tradeoff when selecting a model.

## Relationships

- **is_traded_off_with**: [[variance-of-an-estimator|Variance Of An Estimator]]
- **is_a_component_of**: [[bias-variance-tradeoff|Bias Variance Tradeoff]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*