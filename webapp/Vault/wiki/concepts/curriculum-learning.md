---
type: concept
aliases: [Curriculum Learning]
summary: A training strategy where a model is presented with training examples in a meaningful order, typically from easier to more difficult, to improve learning performance and convergence.
relationships:
  - target: continuation-methods
    type: is-a-type-of
tags: [training-strategy, optimization, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Curriculum Learning

## Definition
Curriculum learning is a training strategy in which a model is not exposed to the full, randomly ordered training set from the beginning. Instead, it is trained on examples in a structured order, typically progressing from easy examples to more difficult ones. This approach is inspired by how humans and animals learn more effectively when concepts are presented in a meaningful sequence.

## Stochastic Curriculum
A particularly effective variant is the stochastic curriculum. In this method, a random mix of easy and difficult examples is always presented to the learner, but the average proportion of more difficult examples is gradually increased over time. This contrasts with a deterministic curriculum where the model might get stuck if it only sees easy examples for too long.

## Efficacy in Practice
The text highlights research by Zaremba and Sutskever (2014) on training recurrent neural networks to capture long-term dependencies. They found that a stochastic curriculum, where the proportion of examples with longer dependencies was gradually increased, achieved much better results than both a deterministic curriculum and ordinary training on the full, randomly sampled dataset.

## Relationships

- **is-a-type-of**: [[continuation-methods|Continuation Methods]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*