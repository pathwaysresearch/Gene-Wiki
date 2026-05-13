---
type: concept
aliases: [Distributed Representation]
summary: A type of data representation where features are not mutually exclusive, allowing an exponential number of configurations to represent different regions in the input space. A method of representing concepts where each concept is a pattern of activity over multiple features, enabling generalization through shared attributes and creating a rich similarity space.
relationships:
  - target: symbolic-representation
    type: is_contrasted_with
  - target: representation-learning
    type: is_a_type_of
  - target: disentangled-representation
    type: is_related_to
tags: [representation-learning, feature-engineering, neural-networks, deep-learning, natural-language-processing]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Distributed Representation

## Definition and Expressive Power
A distributed representation is one where concepts are encoded by patterns of activity across multiple features. A key example is a vector of $n$ binary features, which can take on $2^n$ different configurations. Each of these configurations can correspond to a different region in the input space, giving the representation an exponentially large capacity compared to the number of features.

## Contrast with Symbolic Representation
Distributed representations are fundamentally different from symbolic representations, which are a form of non-distributed representation. A symbolic representation, such as a one-hot vector, has $n$ features that are mutually exclusive, meaning only one can be active at a time. This limits the representation to only $n$ possible configurations, carving the input space into just $n$ regions. In contrast, a distributed representation with $n$ features can carve the space into $2^n$ regions.

## Meaningful Feature Control
In a distributed representation, there is meaningful separate control over each entry or feature. This allows for the composition of features to represent a vast array of concepts. Non-distributed representations, on the other hand, may contain many entries but lack this fine-grained, independent control, limiting their combinatorial expressiveness.

## Relationships

- **is_contrasted_with**: [[symbolic-representation|Symbolic Representation]]
- **is_a_type_of**: [[representation-learning|Representation Learning]]
- **is_related_to**: [[disentangled-representation|Disentangled Representation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*