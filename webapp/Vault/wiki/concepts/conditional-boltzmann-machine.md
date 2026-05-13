---
type: concept
aliases: [Conditional Boltzmann Machine]
summary: An extension of the Boltzmann machine framework designed to model conditional probability distributions, such as p(y|x), for tasks like structured prediction and sequence modeling.
relationships:
  - target: boltzmann-machine
    type: is_a
tags: [probabilistic-model, sequence-modeling, structured-prediction]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Conditional Boltzmann Machine

## Definition
A Conditional Boltzmann Machine is a probabilistic model that extends the standard Boltzmann machine to represent conditional probability distributions. Instead of modeling a joint distribution \(p(\boldsymbol{x})\), it models the probability of an output \(\boldsymbol{y}\) given an input \(\boldsymbol{x}\), denoted \(p(\boldsymbol{y} | \boldsymbol{x})\). This makes it suitable for supervised and semi-supervised learning tasks.

## Application in Sequence Modeling
This framework is highly applicable to sequence modeling, where the goal is to estimate the probability of a sequence of variables, \(p(\boldsymbol{x}^{(1)}, \dots, \boldsymbol{x}^{(\tau)})\). Conditional Boltzmann machines can be used to represent the factors of this joint distribution, such as modeling the probability of the current state given past states, \(p(\boldsymbol{x}^{(t)} | \boldsymbol{x}^{(1)}, \dots, \boldsymbol{x}^{(t-1)})\).

## Example Use Case
An important application is in modeling sequences of joint angles for 3-D character animation, often derived from motion capture data. Taylor et al. (2007) used a conditional Restricted Boltzmann Machine (RBM) to model \(p(\boldsymbol{x}^{(t)} | \boldsymbol{x}^{(t-1)}, \dots, \boldsymbol{x}^{(t-m)})\) for a small history window \(m\). In their model, the bias parameters of the RBM for the current time step \(\boldsymbol{x}^{(t)}\) are determined by a linear function of the previous time steps, effectively conditioning the model on its recent history.

## Relationships

- **is_a**: [[boltzmann-machine|Boltzmann Machine]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*