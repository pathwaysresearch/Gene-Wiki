---
type: concept
aliases: [Hierarchical Softmax]
summary: A technique to efficiently compute probabilities over a large vocabulary by organizing words into a tree structure, typically a binary tree, and decomposing the probability of a word into a product of probabilities of decisions at each node on the path to that word.
tags: [language-modeling, optimization, neural-networks, softmax]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Hierarchical Softmax

## Core Idea
Hierarchical Softmax is an efficient alternative to the standard softmax output layer for models with large vocabularies. It works by organizing all words in the vocabulary into a tree structure, often a balanced binary tree. In this hierarchy, the leaves of the tree represent the actual words, while the internal nodes represent abstract classes or groups of words.

## How It Works
Instead of computing a single probability for a word out of |V| choices, the model computes a sequence of probabilities for decisions made while traversing the tree from the root to the target word's leaf. For a binary tree, each step involves a binary decision (e.g., go left or right). The probability of a specific word is then calculated as the product of the probabilities of making the correct binary decision at each node along this path, following the chain rule of probability.

## Computational Advantage
The primary benefit of this method is a significant reduction in computational complexity. For a standard softmax, the cost is proportional to the vocabulary size, O(|V|). With a balanced hierarchical structure, the depth of the tree is logarithmic with respect to the vocabulary size. Therefore, the number of operations required to compute a word's probability is reduced to O(log |V|), making it much more scalable for very large vocabularies.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*