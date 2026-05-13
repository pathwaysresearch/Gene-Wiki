---
type: concept
aliases: [Maximum a Posteriori (MAP) Estimation]
summary: A Bayesian inference method that estimates model parameters by finding the mode of the posterior distribution, incorporating prior beliefs to regularize the model.
relationships:
  - target: regularization
    type: is_an_interpretation_of
tags: [bayesian-inference, estimation-theory, regularization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Maximum a Posteriori (MAP) Estimation

## Definition and Formulation
MAP Bayesian inference is a method for producing a point estimate of a model's parameters. It determines the posterior distribution over parameters, `p(w | X, y)`, which is proportional to the product of the likelihood `p(y | X, w)` and the prior distribution `p(w)`. The prior reflects naive beliefs about the parameter values, often specified as a broad distribution like a Gaussian to express uncertainty.

## Relationship to Regularization
Many regularized estimation strategies can be interpreted as a MAP approximation to Bayesian inference. This connection is made when the regularization penalty corresponds to the logarithm of the prior probability distribution, `log p(θ)`. For example, maximum likelihood learning regularized with weight decay is a form of MAP estimation. However, not all regularization penalties, such as those that depend on the data, correspond to MAP Bayesian inference.

## Properties and Trade-offs
The primary advantage of MAP inference is its ability to leverage information from the prior distribution that is not present in the training data. This additional information helps reduce the variance of the MAP point estimate compared to the maximum likelihood estimate. This reduction in variance, however, comes at the cost of increased bias. MAP also provides a straightforward framework for designing complex yet interpretable regularization terms, such as using a mixture of Gaussians as a prior.

## Relationships

- **is_an_interpretation_of**: [[regularization|Regularization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*