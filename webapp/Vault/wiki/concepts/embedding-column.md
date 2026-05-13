---
type: concept
aliases: [Embedding Column]
summary: A feature engineering technique used in TensorFlow to represent categorical features as dense, low-dimensional vectors, which are learned during model training.
tags: [feature-engineering, tensorflow, deep-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Embedding Column

## Definition
An embedding column is a method for representing discrete, categorical data in a continuous, multi-dimensional vector space. Instead of a sparse, high-dimensional format like one-hot encoding, it uses a dense, lower-dimensional vector, or 'embedding', whose values are learned by the model during training.

## How It Works
Each unique category in the vocabulary is mapped to a specific vector. This is implemented via a lookup in an 'embedding matrix,' which has one row for each category and one column for each embedding dimension. For example, a vocabulary of five categories represented by 2D embeddings would use a 5x2 matrix. When the model receives a category as input, it looks up the corresponding row in this matrix and retrieves the learned vector, which is then fed into the network.

## Key Properties and Trade-offs
The embedding vectors are typically initialized randomly and their values are adjusted during the training process to create meaningful representations. The size of the embedding matrix is determined by the vocabulary size and the chosen embedding dimension. A large vocabulary can result in a very large matrix, which may require substantial training data to learn effectively. To manage this, one can reduce the `dimension` hyperparameter or shrink the vocabulary size, for instance by grouping rare categories into a single 'unknown' token.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*