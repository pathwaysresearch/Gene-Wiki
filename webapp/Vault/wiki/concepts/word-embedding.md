---
type: concept
aliases: [Word Embedding]
summary: A learned, low-dimensional, real-valued vector representation of a word, where semantically similar words are located close to each other in the vector space. A learned distributed representation for a word, mapping it to a vector of real numbers, which became a foundational technique in modern Natural Language Processing.
relationships:
  - target: neural-language-model
    type: is_produced_by
tags: [representation-learning, nlp, feature-engineering, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Word Embedding

## Definition
Word embeddings, also known as word representations, are a technique for representing words in a low-dimensional feature space. This approach embeds raw symbols, which can be viewed as points in a space with a dimension equal to the vocabulary size (e.g., via one-hot vectors), into a continuous vector space of a much lower dimension. The embedding is learned by a model, typically a neural network.

## Key Properties
A crucial property of word embeddings is their ability to capture semantic relationships. In the original high-dimensional one-hot space, every pair of words is equidistant (e.g., Euclidean distance of √2), conveying no information about similarity. In the embedding space, however, words that frequently appear in similar contexts are mapped to nearby points. This results in words with similar meanings becoming neighbors in the vector space, which is a qualitatively dramatic change in how the data is represented.

## Generalization Beyond NLP
The concept of learning embeddings is not exclusive to natural language processing. For instance, a hidden layer of a convolutional network can be seen as providing an "image embedding." However, the idea is of particular interest to NLP practitioners because natural language does not inherently exist in a real-valued vector space, making the transformation into one especially powerful for applying machine learning models.

## Relationships

- **is_produced_by**: [[neural-language-model|Neural Language Model]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*