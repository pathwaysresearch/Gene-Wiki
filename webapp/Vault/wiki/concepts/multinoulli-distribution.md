---
type: concept
aliases: [Multinoulli Distribution]
summary: A probability distribution over a single discrete variable with k different finite states, also known as the categorical distribution.
tags: [probability-distribution, discrete-variable]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Multinoulli Distribution

## Definition
The multinoulli distribution, also called the categorical distribution, is a probability distribution for a single discrete random variable that can take on one of k distinct states, where k is a finite number. It is often used to describe distributions over categories of objects.

## Parametrization
The distribution is parametrized by a vector $p \in [0, 1]^{k-1}$, where the element $p_i$ represents the probability of the i-th state. The probability of the final, k-th state is implicitly defined as $1 – \mathbf{1}^T p$. A constraint that $\mathbf{1}^T p \le 1$ must be maintained. Because the states are typically categorical, computing the expectation or variance of a multinoulli-distributed variable is not usually necessary.

## Relationship to Multinomial Distribution
The multinoulli distribution is a special case of the multinomial distribution, specifically for a single trial (n=1). A multinomial distribution describes the vector of counts for how many times each of the k categories is observed over n independent trials, where each trial follows a multinoulli distribution.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*