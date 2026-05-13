---
type: concept
aliases: [Embeddings for Categorical Features]
summary: A technique for representing categorical variables as trainable, dense, low-dimensional vectors, which is particularly effective for categories with a large vocabulary.
relationships:
  - target: one-hot-encoding
    type: alternative_to
  - target: tensorflow-feature-columns
    type: enabled_by
tags: [feature-engineering, deep-learning, representation-learning, tensorflow]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Embeddings for Categorical Features

## Definition

An embedding is a trainable, dense vector that represents a category. Instead of using a sparse, high-dimensional representation like one-hot encoding, an embedding maps each category to a point in a continuous, lower-dimensional vector space. By default, these vectors are initialized randomly and are then learned during the model training process.

## When to Use Embeddings

Embeddings are the preferred method for encoding categorical features when the number of categories (the vocabulary size) is large. As a rule of thumb, if the number of categories is greater than 50, embeddings are usually preferable to one-hot encoding. For vocabularies between 10 and 50, it may be worth experimenting with both approaches. One-hot encoding is typically better for very small vocabularies (fewer than 10 categories).

## Training Considerations

Since embeddings are learned from the data, they typically require a sufficient amount of training data to be effective. If training data is limited, the learned embeddings may not be meaningful. However, it is sometimes possible to use pretrained embeddings that have been learned on a larger, related dataset, which can be a powerful alternative.

## Relationships

- **alternative_to**: [[one-hot-encoding|One Hot Encoding]]
- **enabled_by**: [[tensorflow-feature-columns|Tensorflow Feature Columns]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*