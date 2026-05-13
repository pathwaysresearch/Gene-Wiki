---
type: concept
aliases: [Sigmoid Unit]
summary: An output activation function that squashes its input into the (0, 1) range, used for predicting probabilities in binary classification tasks based on a Bernoulli distribution.
relationships:
  - target: softmax-unit
    type: is_a_special_case_of
  - target: maximum-likelihood-estimation
    type: is_used_for
tags: [activation-function, output-unit, binary-classification]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Sigmoid Unit

## Purpose and Application
Sigmoid units are designed for tasks that require predicting the value of a binary variable, such as classification problems with two classes. The maximum-likelihood approach for such problems is to define a Bernoulli distribution over the output y conditioned on the input x. A sigmoid unit's role is to predict the single number P(y = 1 | x), which must lie in the interval [0, 1] to be a valid probability.

## How It Works
A sigmoid unit takes the output of a linear layer, z, and applies the sigmoid function σ(z) to it. This function maps any real-valued input z into the open interval (0, 1), satisfying the constraint for a probability. The output can then be used within a maximum likelihood framework to train the model.

## Numerical Considerations
When training with a log-likelihood cost function, the sigmoid provides a well-behaved logarithm because its output is strictly greater than 0 and less than 1. However, in software implementations, the sigmoid function can underflow to zero for very negative inputs. If this happens, taking the logarithm of the output results in negative infinity. To avoid these numerical problems, it is recommended to write the negative log-likelihood cost function directly as a function of the pre-activation value z, rather than the sigmoid's output.

## Relationships

- **is_a_special_case_of**: [[softmax-unit|Softmax Unit]]
- **is_used_for**: [[maximum-likelihood-estimation|Maximum Likelihood Estimation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*