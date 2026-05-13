---
type: concept
aliases: [Softmax Unit]
summary: An output activation function that generalizes the sigmoid to produce a probability distribution over a discrete variable with n possible values, commonly used in multi-class classification.
relationships:
  - target: sigmoid-unit
    type: is_a_generalization_of
  - target: maximum-likelihood-estimation
    type: is_used_for
tags: [activation-function, output-unit, multi-class-classification]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Softmax Unit

## Definition and Purpose
The softmax function is used to represent a probability distribution over a discrete variable with n possible values. It can be seen as a generalization of the sigmoid function, which represents a probability distribution over a binary variable. Softmax functions are most often used as the output layer of a classifier to represent the probability distribution over n different classes.

## Saturation Properties
Like the sigmoid, the softmax activation can saturate. Saturation occurs when the differences between the input values become extreme. An output softmax(z)_i will saturate to 1 when its corresponding input z_i is much greater than all other inputs. Conversely, an output can saturate to 0 when z_i is not the maximal input. This saturation can cause problems for many cost functions unless they are designed to invert the saturating activation.

## Numerical Stability
The softmax function is invariant to adding the same scalar to all of its inputs: softmax(z) = softmax(z + c). This property is exploited to create a numerically stable variant of the function by subtracting the maximum value from all inputs: softmax(z) = softmax(z - max_i z_i). This reformulation allows the function to be evaluated with only small numerical errors, even when the input vector z contains extremely large or negative numbers.

## Relationships

- **is_a_generalization_of**: [[sigmoid-unit|Sigmoid Unit]]
- **is_used_for**: [[maximum-likelihood-estimation|Maximum Likelihood Estimation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*