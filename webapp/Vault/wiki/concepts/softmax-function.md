---
type: concept
aliases: [Softmax Function]
summary: A function that converts a vector of real numbers into a probability distribution, commonly used in the output layer of a classifier for a multinoulli distribution.
relationships:
  - target: multinoulli-distribution
    type: used_for
  - target: underflow
    type: is_susceptible_to
  - target: overflow
    type: is_susceptible_to
tags: [activation-function, deep-learning, classification]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Softmax Function

## Definition
The softmax function is a mathematical function that takes a vector $x$ of $n$ real numbers and normalizes it into a probability distribution consisting of $n$ probabilities. The formula for the i-th element of the output is:
$\text{softmax}(x)_i = \frac{\exp(x_i)}{\sum_{j=1}^n \exp(x_j)}$.

## Application
In machine learning and deep learning, the softmax function is frequently used in the final layer of a model to predict the probabilities associated with a multinoulli distribution. For example, in a multi-class classification problem, it can output the probability that an input belongs to each of the possible classes.

## Numerical Stability
The softmax function must be implemented carefully to avoid numerical stability issues. It is highly susceptible to both underflow (when input values are very negative) and overflow (when input values are very positive) due to the use of the exponential function. A common stabilization technique involves subtracting the maximum value of the input vector from all its elements before applying the exponential.

## Relationships

- **used_for**: [[multinoulli-distribution|Multinoulli Distribution]]
- **is_susceptible_to**: [[underflow|Underflow]]
- **is_susceptible_to**: [[overflow|Overflow]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*