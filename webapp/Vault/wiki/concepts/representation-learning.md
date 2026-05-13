---
type: concept
aliases: [Representation Learning]
summary: A machine learning approach that discovers not only the mapping from a representation to an output but also the representation itself, avoiding manual feature engineering. A set of machine learning techniques that allow a system to automatically discover the representations needed for feature detection or classification from raw data. A set of techniques that allow a system to automatically discover the representations or features needed for a task from raw data, often to facilitate transfer learning or semi-supervised learning.
relationships:
  - target: autoencoder
    type: exemplified_by
  - target: deep-learning
    type: is_a_key_part_of
  - target: transfer-learning
    type: enables
  - target: distributed-representation
    type: is_a_goal_of
tags: [machine-learning, feature-learning, deep-learning, unsupervised-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Representation Learning

## Definition
Representation learning is an approach to machine learning where the system learns to discover not only the mapping from a representation to an output but also the representation itself. Instead of relying on hand-designed features, the algorithm automatically learns the most effective way to represent the input data for a given task.

## Advantages
Learned representations often result in much better performance than can be obtained with hand-designed representations. A significant advantage is that they allow AI systems to rapidly adapt to new tasks with minimal human intervention. An algorithm can discover a good set of features for a simple task in minutes, or for a complex task in hours to months.

## Comparison to Manual Design
This approach stands in contrast to traditional methods that require extensive manual feature engineering. Manually designing features for a complex task requires a great deal of human time and effort, and the text notes it can take decades for an entire community of researchers to develop effective features for certain problems.

## Relationships

- **exemplified_by**: [[autoencoder|Autoencoder]]
- **is_a_key_part_of**: [[deep-learning|Deep Learning]]
- **enables**: [[transfer-learning|Transfer Learning]]
- **is_a_goal_of**: [[distributed-representation|Distributed Representation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*