---
type: concept
aliases: [Mean-Covariance Restricted Boltzmann Machine]
summary: An RBM variant that models both the mean and conditional covariance of data by combining the energy functions of a Gaussian-Bernoulli RBM and a covariance RBM.
relationships:
  - target: restricted-boltzmann-machine
    type: is_a
  - target: gaussian-bernoulli-rbm
    type: uses
tags: [generative-model, rbm-variant, energy-based-model]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Mean-Covariance Restricted Boltzmann Machine

## Definition
The Mean-Covariance Restricted Boltzmann Machine (mcRBM) is a generative model designed to capture both the mean and the conditional covariance information in data. It achieves this by combining two separate energy functions, one for the mean and one for the covariance, into a single model.

## Architecture
The mcRBM uses two distinct sets of binary hidden units: mean units, denoted as \(\boldsymbol{h}^{(\text{m})}\), and covariance units, denoted as \(\boldsymbol{h}^{(\text{c})}\). The mean units are responsible for modeling the conditional mean of the data, while the covariance units model the conditional covariance.

## Energy Function
The total energy function of the mcRBM is the sum of two components: \(E_{\text{mc}} = E_{\text{m}} + E_{\text{c}}\). The first component, \(E_{\text{m}}\), is the standard energy function of a Gaussian-Bernoulli RBM, which models the mean. The second component, \(E_{\text{c}}\), is the energy function of a covariance RBM (cRBM), which models the covariance information using covariance weight vectors \(\boldsymbol{r}^{(j)}\) and offsets \(\boldsymbol{b}^{(\text{c})}\). This combined energy function defines the joint probability distribution over the visible and both sets of hidden units.

## Relationships

- **is_a**: [[restricted-boltzmann-machine|Restricted Boltzmann Machine]]
- **uses**: [[gaussian-bernoulli-rbm|Gaussian Bernoulli Rbm]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*