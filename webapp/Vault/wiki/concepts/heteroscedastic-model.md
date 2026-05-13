---
type: concept
aliases: [Heteroscedastic Model]
summary: A statistical model where the variance of the output variable is not constant, but is instead predicted as a function of the input variables.
relationships:
  - target: maximum-likelihood-estimation
    type: uses
tags: [statistical-model, regression, uncertainty-quantification]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Heteroscedastic Model

## Definition
A heteroscedastic model is one that predicts a different amount of variance in the output variable y for different values of the input x. This contrasts with homoscedastic models, which assume a constant variance across all inputs. This allows the model to represent varying levels of uncertainty in its predictions.

## Implementation in Neural Networks
In the context of a neural network, a heteroscedastic model can be implemented by making the specification of the variance one of the values output by the network's function f(x; θ). For example, when modeling a conditional Gaussian distribution, the network would output both the mean and the variance (or a parameterization of the variance, like its logarithm or inverse) as a function of the input x.

## Learning the Variance
The model learns the input-dependent variance through a standard optimization procedure like gradient descent. By using the negative log-likelihood of the data as the cost function, the appropriate terms are automatically included to drive the optimization procedure to incrementally learn the correct variance for each input. This does not require special-case code and integrates seamlessly into the maximum likelihood framework.

## Relationships

- **uses**: [[maximum-likelihood-estimation|Maximum Likelihood Estimation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*