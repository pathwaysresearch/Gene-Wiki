---
type: concept
aliases: [Bayesian Inference]
summary: A statistical perspective where probability is used to represent degrees of certainty. It involves updating a prior belief about a parameter with observed data to obtain a posterior belief.
relationships:
  - target: maximum-likelihood-estimation
    type: is_an_alternative_to_frequentist_methods_like
tags: [statistics, bayesian-methods, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bayesian Inference

## Core Perspective
The Bayesian perspective on statistics differs fundamentally from the frequentist view. In Bayesian inference, probability is used to reflect degrees of certainty or states of knowledge. The true parameter θ is considered unknown and uncertain, and is therefore represented as a random variable. In contrast, the dataset, once it has been observed, is considered fixed and not random.

## The Role of the Prior Distribution
Before observing any data, the practitioner's knowledge or belief about the parameter θ is captured in a prior probability distribution, p(θ). This prior can be chosen to be broad (high entropy) to reflect a high degree of initial uncertainty. Alternatively, many priors are chosen to reflect a preference for 'simpler' solutions, such as models with smaller magnitude coefficients or functions that are closer to being constant, acting as a form of regularization.

## Updating Beliefs with Data
After a set of data samples {x^(1), ..., x^(m)} is observed, the initial belief about θ is updated. This is done by combining the data likelihood, p(x^(1), ..., x^(m) | θ), with the prior distribution p(θ). This combination yields a posterior distribution, which represents the updated belief about the parameter after taking the evidence from the data into account.

## Relationships

- **is_an_alternative_to_frequentist_methods_like**: [[maximum-likelihood-estimation|Maximum Likelihood Estimation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*