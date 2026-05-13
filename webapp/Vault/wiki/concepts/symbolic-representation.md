---
type: concept
aliases: [Symbolic Representation]
summary: A type of non-distributed data representation where an input is associated with a single symbol or category from a fixed set, often implemented as a one-hot vector.
relationships:
  - target: distributed-representation
    type: is_contrasted_with
tags: [representation-learning, one-hot-encoding, clustering]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Symbolic Representation

## Definition
A symbolic representation associates an input with a single symbol or category from a predefined dictionary. It is a specific example of the broader class of non-distributed representations, which lack significant meaningful separate control over each entry. This type of representation is also commonly called a one-hot representation.

## Implementation and Properties
A symbolic representation with $n$ symbols can be implemented as a binary vector with $n$ mutually exclusive bits, where only one bit can be active at a time. This structure limits the representation space to only $n$ possible configurations, which in turn carves the input space into $n$ distinct regions. This is in stark contrast to distributed representations, which can represent an exponential number of configurations with the same number of features.

## Associated Learning Algorithms
Several learning algorithms are based on non-distributed representations like the symbolic one. Examples provided in the text include clustering methods, such as the k-means algorithm, where each input point is assigned to exactly one cluster (symbol). Another example is the k-nearest neighbors algorithm, where an input is associated with one or a few prototype examples from the training set.

## Relationships

- **is_contrasted_with**: [[distributed-representation|Distributed Representation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*