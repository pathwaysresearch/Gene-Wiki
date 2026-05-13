---
type: concept
aliases: [Inference (in Probabilistic Models)]
summary: The process of deducing properties of a probability distribution, such as computing marginal or conditional probabilities of certain variables given observations of others.
relationships:
  - target: undirected-probabilistic-model
    type: is_a_task_in
  - target: directed-probabilistic-model
    type: is_a_task_in
tags: [probabilistic-models, machine-learning, computational-complexity]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Inference (in Probabilistic Models)

## Definition
Inference is a central task in probabilistic modeling where one seeks to answer questions about how variables are related. This typically involves predicting the value of some variables given others, or more generally, predicting the probability distribution over a subset of variables given the values of another subset.

## Key Applications
A primary application of inference is in learning algorithms. For example, training models via maximum likelihood often requires computing conditional probabilities of latent variables given observed variables, such as p(h|v). Other applications include using a trained model for prediction, like diagnosing a disease from test results, or extracting meaningful features from data, such as computing the expectation E[h|v].

## Computational Challenge
For most interesting and complex deep learning models, exact inference is computationally intractable. Even with the efficiencies gained from structured graphical models, the graphs used in deep learning are typically not restrictive enough to allow for efficient inference. The problem of computing the marginal probability of a general graphical model is known to be #P-hard, which necessitates the use of approximate inference techniques.

## Relationships

- **is_a_task_in**: [[undirected-probabilistic-model|Undirected Probabilistic Model]]
- **is_a_task_in**: [[directed-probabilistic-model|Directed Probabilistic Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*