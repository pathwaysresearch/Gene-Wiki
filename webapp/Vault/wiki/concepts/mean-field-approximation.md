---
type: concept
aliases: [Mean Field Approximation]
summary: A variational inference technique used to approximate a complex, intractable probability distribution by a simpler, factorized distribution where variables are treated as independent.
relationships:
  - target: deep-boltzmann-machine
    type: is_method_for
  - target: variational-inference
    type: is_a
  - target: kullback-leibler-divergence
    type: uses
tags: [approximate-inference, variational-methods, graphical-models]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Mean Field Approximation

## Core Idea
The mean field approach is a method for approximate inference that aims to find a tractable distribution Q that best approximates an intractable posterior distribution P. The quality of the fit is measured by minimizing the Kullback-Leibler (KL) divergence between Q and P, i.e., minimizing KL(Q||P). The core simplifying assumption is that the distribution Q factorizes over variables or groups of variables, enforcing independence.

## Application to DBMs
In the context of a Deep Boltzmann Machine (DBM) with binary hidden units, the mean field approximation Q(h|v) is parameterized as a product of independent Bernoulli distributions. This means that for the purpose of inference, each hidden unit's probability is treated as independent of the others, governed by its own parameter. For a DBM with two hidden layers, the approximation takes the form Q(h^(1), h^(2) | v) = ∏_j Q(h_j^(1) | v) ∏_k Q(h_k^(2) | v).

## Role in Training and Inference
Mean field is used to perform approximate inference in DBMs. The text also describes a modification to the stochastic maximum likelihood algorithm for DBMs where a small amount of mean field is used during the negative phase of the joint training step. Furthermore, the multi-prediction DBM (MP-DBM) framework trains the mean field inference process itself to produce more accurate estimates by using back-propagation.

## Relationships

- **is_method_for**: [[deep-boltzmann-machine|Deep Boltzmann Machine]]
- **is_a**: [[variational-inference|Variational Inference]]
- **uses**: [[kullback-leibler-divergence|Kullback Leibler Divergence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*