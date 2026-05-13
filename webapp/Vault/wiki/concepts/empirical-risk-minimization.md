---
type: concept
aliases: [Empirical Risk Minimization]
summary: A principle in statistical learning where an algorithm seeks to find model parameters that minimize the average loss, or empirical risk, on the training data.
relationships:
  - target: overfitting
    type: is_prone_to
  - target: surrogate-loss-function
    type: requires_use_of
tags: [optimization, statistical-learning-theory, risk-minimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Empirical Risk Minimization

## Definition
Empirical Risk Minimization (ERM) is a foundational principle for training machine learning models. It involves finding the parameters of a model that minimize a cost function, where this cost function is the average performance measure evaluated on the entire training set. The quantity being minimized is the empirical risk, which is a proxy for the true risk (expected loss over the true data distribution).

## Proneness to Overfitting
In the context of deep learning, ERM is highly prone to overfitting. Models with high capacity, such as deep neural networks, have sufficient power to simply memorize the training set. When a model memorizes the training data, it minimizes the empirical risk perfectly but fails to generalize to new, unseen data, which is the ultimate goal of machine learning.

## Feasibility in Deep Learning
Beyond overfitting, true ERM is often not feasible for deep learning. The most effective modern optimization algorithms are based on gradient descent. However, many loss functions that one might truly care about, such as the 0-1 loss for classification, have no useful derivatives (the derivative is either zero or undefined everywhere). This incompatibility with gradient-based methods means that, in practice, deep learning rarely uses direct ERM. Instead, alternative approaches like using surrogate loss functions are necessary.

## Relationships

- **is_prone_to**: [[overfitting|Overfitting]]
- **requires_use_of**: [[surrogate-loss-function|Surrogate Loss Function]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*