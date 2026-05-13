---
type: concept
aliases: [Statistical Learning]
summary: A machine learning paradigm where data are treated as evidence (instantiations of random variables) and hypotheses are probabilistic theories about how a domain works.
tags: [machine-learning, probabilistic-models, density-estimation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Statistical Learning

## Definition
Statistical learning frames the learning problem in probabilistic terms. The key components are data, which are considered evidence in the form of instantiations of some or all random variables in a domain, and hypotheses, which are probabilistic theories explaining the domain's mechanics. This approach encompasses logical theories as a special, deterministic case.

## Core Example
An illustrative example involves a bag of candy with an unknown proportion of cherry and lime flavors. The bag is known to be one of five types (e.g., 100% cherry, 75% cherry, etc.), which represent the discrete set of hypotheses ($h_1$ through $h_5$). The type of the bag is a non-observable random variable, $H$. As candies are unwrapped, their flavor is revealed, providing a sequence of data points ($D_1, D_2, ...$) that serve as evidence to infer which hypothesis is most likely correct.

## General Task
The general task within statistical learning is to learn a probability model from data that are assumed to be generated from that model. This overall objective is known as density estimation. It can involve learning the numerical parameters of a pre-defined model structure or learning the structure of the model itself.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*