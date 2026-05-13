---
type: concept
aliases: [Monte Carlo Methods]
summary: A broad class of computational algorithms that rely on repeated random sampling to obtain numerical results, particularly for approximating quantities that are difficult to compute deterministically.
tags: [sampling-methods, computational-statistics, randomized-algorithms]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Monte Carlo Methods

## Definition and Classification
Monte Carlo methods are a category of randomized algorithms used to find approximate solutions to problems where exact computation is infeasible. They are distinct from Las Vegas algorithms, which always return a precise, correct answer. Monte Carlo methods are particularly useful for numerical integration and for drawing samples from a probability distribution.

## Core Principle
The fundamental idea is to estimate a desired quantity, often an expectation, by drawing many random samples and averaging the results. This approach relies on the law of large numbers, where the average of the sampled results converges to the expected value as the number of samples increases.

## Key Challenges and Variants
A primary challenge is that it is not always feasible to draw samples directly from the target probability distribution, $p(\mathbf{x})$. When direct sampling is not possible, alternative strategies are required. These include importance sampling, which samples from a different, more convenient distribution and re-weights the samples, and Markov chain Monte Carlo (MCMC) methods, which form a sequence of estimators that converge to the distribution of interest.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*