---
type: concept
aliases: [Unsupervised Learning]
summary: A paradigm in machine learning where algorithms learn from data without explicit supervision targets or labels, often focusing on discovering the underlying structure or distribution of the data. A category of machine learning algorithms that learn patterns from data that has not been labeled or classified, experiencing only features without a supervision signal. A class of machine learning techniques that learn patterns from unlabeled data, with its applicability being highly domain-specific.
relationships:
  - target: supervised-learning
    type: is_contrasted_with
  - target: semi-supervised-learning
    type: related_to
  - target: word-embeddings
    type: example_of
  - target: overfitting
    type: can_mitigate
tags: [machine-learning-paradigm, density-estimation, clustering, machine-learning, dimensionality-reduction, methodology]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Unsupervised Learning

## Overview
Unsupervised learning is a category of machine learning tasks that operate on data without provided labels or targets. Like supervised learning, it is not a completely formal or distinct concept, and the boundary between the two is often permeable. Many machine learning technologies can be applied to both supervised and unsupervised problems.

## Typical Tasks
The most common task associated with unsupervised learning is density estimation, where the goal is to model the probability distribution of the input data. This is often done in support of other tasks. The objective is to learn about the structure and patterns within the data itself.

## Relationship to Supervised Learning
An ostensibly unsupervised problem, such as modeling the joint distribution $p(\mathbf{x})$ for a vector $\mathbf{x}$, can be solved by decomposing it into a series of supervised learning problems. Using the chain rule of probability, the problem can be split into $n$ supervised learning problems of the form $p(x_i | x_1, \dots, x_{i-1})$. This illustrates how the two paradigms can be used to solve problems in the other's domain.

## Relationships

- **is_contrasted_with**: [[supervised-learning|Supervised Learning]]
- **related_to**: [[semi-supervised-learning|Semi Supervised Learning]]
- **example_of**: [[word-embeddings|Word Embeddings]]
- **can_mitigate**: [[overfitting|Overfitting]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*