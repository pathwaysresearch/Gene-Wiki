---
type: concept
aliases: [Disentangled Representation]
summary: An ideal representation that separates the distinct, underlying causal factors of variation in the data into separate, manipulable dimensions of the representation space.
relationships:
  - target: distributed-representation
    type: is_a_type_of
tags: [representation-learning, generative-models, unsupervised-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Disentangled Representation

## Definition
An ideal representation is one that disentangles the underlying causal factors of variation that generated the data. Most strategies for representation learning are based on introducing clues that help a learning algorithm find and separate these factors. While supervised learning provides a strong clue in the form of a label, representation learning on unlabeled data uses other, less direct hints and implicit prior beliefs to achieve this goal.

## How It Works
In a disentangled representation, different directions in the representation space correspond to different, independent factors of variation. For example, a generative model trained on images of faces can learn a representation where one direction corresponds to gender and another corresponds to whether the person is wearing glasses. A key aspect is that these features are discovered automatically by the model, not fixed a priori by a human designer.

## Example: Vector Arithmetic
A powerful demonstration of a disentangled representation is the ability to perform meaningful vector arithmetic. For instance, by starting with the vector for a “man with glasses,” subtracting the vector for a “man without glasses,” and adding the vector for a “woman without glasses,” a generative model can correctly decode the resulting vector into an image of a “woman with glasses.” This shows that the concepts have been separated and can be manipulated independently.

## Relationships

- **is_a_type_of**: [[distributed-representation|Distributed Representation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*