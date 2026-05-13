---
type: concept
aliases: [Likelihood Weighting]
summary: An approximate inference algorithm for Bayesian networks that generates samples consistent with the evidence and weights them by the likelihood of that evidence.
relationships:
  - target: bayesian-network
    type: is-used-for
  - target: rejection-sampling
    type: is-an-improvement-on
  - target: consistent-estimator
    type: is-an-example-of
tags: [bayesian-networks, approximate-inference, sampling, monte-carlo]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Likelihood Weighting

## Definition
Likelihood weighting is an approximate inference algorithm that estimates posterior probabilities in a Bayesian network. It is a form of importance sampling that improves upon rejection sampling by ensuring every generated sample is consistent with the given evidence, thus using all generated samples.

## How It Works
The algorithm fixes the values for the evidence variables and samples only the non-evidence variables. It processes variables in a topological order. When an evidence variable is encountered, its value is fixed, and the current sample's weight is multiplied by the conditional probability of that evidence given its parents. When a non-evidence variable is encountered, its value is sampled from its conditional probability distribution. The final estimate for a query is a normalized, weighted count over all generated samples.

## Properties and Limitations
Likelihood weighting produces consistent estimates, meaning the estimated probability converges to the true probability as the number of samples grows. However, its performance can degrade significantly as the number of evidence variables increases. This is because most samples will have very low weights, causing the weighted estimate to be dominated by a tiny fraction of samples that accord a high likelihood to the evidence. The problem is exacerbated if evidence variables appear late in the variable ordering.

## Relationships

- **is-used-for**: [[bayesian-network|Bayesian Network]]
- **is-an-improvement-on**: [[rejection-sampling|Rejection Sampling]]
- **is-an-example-of**: [[consistent-estimator|Consistent Estimator]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*