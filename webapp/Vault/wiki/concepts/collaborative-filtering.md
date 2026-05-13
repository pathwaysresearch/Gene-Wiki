---
type: concept
aliases: [Collaborative Filtering]
summary: A class of algorithms used in recommendation systems that makes predictions about a user's interests by collecting and analyzing preferences from many users.
relationships:
  - target: word-embedding
    type: uses_analogue_of
tags: [recommendation-systems, machine-learning, applications]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Collaborative Filtering

## Core Principle
Collaborative filtering is based on the principle that if two users have similar tastes, they are likely to agree on future preferences. For example, if user 1 and user 2 have historically liked similar items, and user 1 likes a new item D, this provides a strong cue that user 2 will also like item D.

## Methodologies
The approach can be implemented using both non-parametric methods, such as nearest-neighbor algorithms based on the similarity between user preference patterns, and parametric methods. Parametric methods are common and often rely on learning a distributed representation, or embedding, for each user and each item.

## Parametric Implementation with Embeddings
A highly successful and common parametric method involves a bilinear prediction of a target variable, such as a user's rating for an item. The prediction is calculated as the dot product of the user's embedding vector and the item's embedding vector, often adjusted by bias terms for the user's general rating tendency and the item's general popularity. The model is typically trained by minimizing the squared error between predicted and actual ratings.

## Relationships

- **uses_analogue_of**: [[word-embedding|Word Embedding]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*