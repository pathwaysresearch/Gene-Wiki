---
type: concept
aliases: [Variance (of an estimator)]
summary: A measure of the variability of a statistical estimator across different samples of the data; it quantifies the deviation from the expected estimator value.
relationships:
  - target: bias-of-an-estimator
    type: is_traded_off_with
  - target: bias-variance-tradeoff
    type: is_a_component_of
tags: [statistics, estimation-theory, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Variance (of an estimator)

## Definition
Variance is the second key source of error in an estimator, complementing bias. It provides a measure of the deviation from the expected estimator value that any particular sampling of the data is likely to cause. In other words, it quantifies how much the estimate \hat{\theta} would change if we were to use a different training dataset drawn from the same underlying distribution.

## Example: Bernoulli Mean Estimator
The text demonstrates the calculation of variance for the sample mean estimator of a Bernoulli distribution. It shows that the variance of the estimator \hat{\theta}_m is Var(\hat{\theta}_m) = \frac{1}{m} \theta(1 - \theta). This result highlights a common and important property of many estimators.

## Key Properties
A key property illustrated by the Bernoulli example is that the variance of the estimator decreases as a function of m, the number of examples in the dataset. This property, where the estimator's variance shrinks as more data becomes available, is related to the concept of consistency and is a desirable feature for an estimator. High variance is often associated with overfitting, where a model is overly sensitive to the specific training data.

## Relationships

- **is_traded_off_with**: [[bias-of-an-estimator|Bias Of An Estimator]]
- **is_a_component_of**: [[bias-variance-tradeoff|Bias Variance Tradeoff]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*