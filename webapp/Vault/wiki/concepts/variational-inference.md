---
type: concept
aliases: [Variational Inference]
summary: A method in Bayesian statistics for approximating intractable posterior distributions by optimizing a simpler family of distributions to minimize KL divergence, which is equivalent to maximizing the Evidence Lower Bound (ELBO).
tags: [bayesian-statistics, inference, approximation-algorithms]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
relationships:
  - target: approximate-inference
    type: is_a_method_for
  - target: expectation-maximization-algorithm
    type: is_a_generalization_of
  - target: kullback-leibler-divergence
    type: minimizes
  - target: calculus-of-variations
    type: uses
  - target: mean-field-fixed-point-equations
    type: uses
---

# Variational Inference

## Definition
Variational inference is an approach used to solve a central problem in Bayesian statistics: the intractability of computing the evidence, or marginal likelihood, p(X). It works by approximating the true posterior distribution p(z|X) with a more manageable, parameterized family of distributions, denoted q(z; λ).

## How It Works
The method involves selecting a family of distributions q(z; λ) and then optimizing its variational parameters, λ, to make q(z) a good approximation of the true posterior p(z|X). This optimization is framed as finding the value of λ that minimizes the Kullback-Leibler (KL) divergence from the approximate distribution q(z) to the true posterior p(z|X).

## The Role of ELBO
The KL divergence can be mathematically rewritten as the log of the evidence (log p(X)) minus a term called the Evidence Lower Bound (ELBO). Since the log evidence is a constant with respect to the variational distribution q, minimizing the KL divergence is mathematically equivalent to maximizing the ELBO. In practice, various techniques, such as mean field variational inference, are employed to maximize this lower bound.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*