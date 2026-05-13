---
type: concept
aliases: [Active Learning]
summary: A machine learning strategy where a learning algorithm interactively queries a human expert to label new data points, typically those for which the model is most uncertain.
relationships:
  - target: semi-supervised-learning
    type: is_a_type_of
tags: [machine-learning, semi-supervised-learning, human-in-the-loop]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Active Learning

## Definition
Active learning is a process where a human expert interacts with a learning algorithm, providing labels for data points as the algorithm requests them. The goal is to iteratively improve the model and the training set, especially in semi-supervised contexts where labeled data is scarce.

## The Process
The typical active learning cycle involves several steps. First, the model is trained on the labeled instances gathered so far. Second, this model is used to make predictions on all the unlabeled instances. Third, the algorithm identifies the instances it needs to have labeled by the expert based on a specific strategy. This process is repeated until the performance improvement no longer justifies the cost and effort of labeling.

## Common Strategies
A very common strategy for active learning is called uncertainty sampling. In this approach, the model requests labels for the instances for which it is most uncertain, identified as those where its estimated prediction probability is lowest. Other strategies mentioned include labeling instances that would result in the largest model change, cause the largest drop in the model's validation error, or are points of disagreement between different models (e.g., an SVM and a Random Forest).

## Relationships

- **is_a_type_of**: [[semi-supervised-learning|Semi Supervised Learning]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*