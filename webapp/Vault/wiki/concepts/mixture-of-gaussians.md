---
type: concept
aliases: [Mixture of Gaussians]
summary: A probability distribution represented as a weighted sum of multiple Gaussian (normal) distributions. A probabilistic model representing a distribution as a weighted sum of several Gaussian (normal) distributions, often used for unsupervised clustering.
relationships:
  - target: switching-kalman-filter
    type: is-produced-by
  - target: unsupervised-clustering
    type: used-for
  - target: expectation-maximization-em-algorithm
    type: is-learned-with
tags: [probability-distribution, statistical-model, machine-learning, probabilistic-model, clustering, gaussian-model]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Mixture of Gaussians

## Definition
A mixture of Gaussians is a probability distribution formed by a weighted sum of individual Gaussian distributions. The weights in this sum must themselves sum to 1.

## Role in Switching Kalman Filters
This type of distribution arises naturally in the context of switching Kalman filters. When predicting the next state of a system that can switch between *k* modes, if the initial state is represented by a single Gaussian, the predicted state becomes a mixture of *k* Gaussians, with each component corresponding to a possible mode.

## Computational Implications
The use of Gaussian mixtures in models like the switching Kalman filter has significant computational consequences. The number of Gaussian components required to represent the state distribution can grow exponentially with each time step (from *m* to *km* components). This demonstrates how the complexity of representing the posterior can grow without limit in even simple hybrid dynamic models.

## Relationships

- **is-produced-by**: [[switching-kalman-filter|Switching Kalman Filter]]
- **used-for**: [[unsupervised-clustering|Unsupervised Clustering]]
- **is-learned-with**: [[expectation-maximization-em-algorithm|Expectation Maximization Em Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*