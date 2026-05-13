---
type: concept
aliases: [Structured Probabilistic Models]
summary: Models that use a graph to represent the factorization of a complex probability distribution over many random variables, showing direct interactions and conditional dependencies.
tags: [graphical-models, probabilistic-models, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Structured Probabilistic Models

## Definition
Structured probabilistic models, also known as graphical models, are a class of machine learning models that represent a complex probability distribution over many random variables by using a graph. In these models, each node in the graph corresponds to a random variable, and the edges represent direct probabilistic interactions between them.

## Purpose
The graph structure allows for the representation of a high-dimensional probability distribution in a factored form. This factorization makes it computationally feasible to perform inference and learning on models with a large number of variables by exploiting the conditional independence relationships encoded in the graph.

## Main Types
There are two primary categories of structured probabilistic models. The first is *directed* models, which use directed edges to represent factorizations into conditional probability distributions. The second is *undirected* models, which use undirected edges to represent factorizations into a set of functions.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*