---
type: concept
aliases: [Importance Sampling]
summary: A general statistical technique used to estimate properties of a distribution by sampling from a different, simpler distribution (the proposal distribution) and correcting for the bias using weights. A Monte Carlo technique for estimating properties of a target distribution by drawing samples from a different, more convenient proposal distribution and re-weighting them.
relationships:
  - target: monte-carlo-methods
    type: is_a
tags: [sampling, statistical-methods, optimization, neural-networks, sampling-methods, monte-carlo, variance-reduction, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Importance Sampling

## Core Principle
Importance sampling is a technique for estimating an expectation with respect to a complex probability distribution by drawing samples from a different, simpler distribution, known as the proposal distribution (q). To correct for the fact that samples are drawn from the 'wrong' distribution, each sample is weighted. The weight for a sample is the ratio of its probability under the target distribution to its probability under the proposal distribution.

## Application in Language Models
In the context of training neural language models, importance sampling is used to approximate the gradient of the log-likelihood, specifically the computationally expensive 'negative phase' term which involves a sum over the entire vocabulary. Instead of summing over all words, a small number of 'negative' words are sampled to estimate this term.

## Biased Importance Sampling
Exact importance sampling is often inefficient for this application because computing the weights requires evaluating the target probability, which is what the method aims to avoid. A practical solution is biased importance sampling. In this variant, a set of negative samples are drawn from the proposal distribution q, and their importance weights are normalized to sum to 1. These normalized weights are then used to scale the gradients associated with the negative samples, forming an estimate of the negative phase contribution to the overall gradient. A unigram or bigram distribution is often used as an effective and easy-to-estimate proposal distribution.

## Relationships

- **is_a**: [[monte-carlo-methods|Monte Carlo Methods]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*