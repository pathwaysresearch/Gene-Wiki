---
type: concept
aliases: [Gaussian Mixture Model (GMM)]
summary: A probabilistic model that assumes all data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters.
relationships:
  - target: prior-probability
    type: uses
  - target: expectation-maximization-algorithm
    type: uses
  - target: bayesian-information-criterion
    type: can_be_evaluated_by
  - target: akaike-information-criterion
    type: can_be_evaluated_by
tags: [probabilistic-model, clustering, unsupervised-learning, density-estimation]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Gaussian Mixture Model (GMM)

## Definition
A Gaussian Mixture Model (GMM) is a probabilistic model which posits that instances are generated from a mixture of several Gaussian distributions with unknown parameters. In this model, all instances generated from a single Gaussian distribution form a cluster that typically appears ellipsoidal. Each cluster can possess a different ellipsoidal shape, size, density, and orientation.

## Probabilistic Generative Process
The dataset is assumed to be generated via a specific probabilistic process. For each instance, a cluster is randomly selected from a total of *k* clusters, with the probability of choosing the *j*-th cluster defined by a weight $\phi^{(j)}$. Once a cluster is chosen for an instance, the location of that instance is randomly sampled from the corresponding Gaussian distribution, which is defined by its mean and covariance matrix.

## Training and Configuration
GMMs are implemented in scikit-learn's `GaussianMixture` class, which uses the Expectation-Maximization (EM) algorithm for training. The model's complexity and cluster shapes can be controlled by the `covariance_type` hyperparameter. The default, `"full"`, allows each cluster to have its own unconstrained covariance matrix. Other options include `"spherical"` (clusters are spherical with different diameters), `"diag"` (ellipsoidal clusters with axes parallel to coordinate axes), and `"tied"` (all clusters share the same shape, size, and orientation).

## Relationships

- **uses**: [[expectation-maximization-algorithm|Expectation Maximization Algorithm]]
- **can_be_evaluated_by**: [[bayesian-information-criterion|Bayesian Information Criterion]]
- **can_be_evaluated_by**: [[akaike-information-criterion|Akaike Information Criterion]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*