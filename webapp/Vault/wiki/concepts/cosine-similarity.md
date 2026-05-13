---
type: concept
aliases: [Cosine Similarity]
summary: A metric used to measure the similarity between two non-zero vectors in an inner product space, applied in this study to compare textual embeddings of conversations.
relationships:
  - target: textual-embeddings
    type: operates_on
tags: [nlp, metric, text-analysis]
sourced_from: 2304.11771V2
---

# Cosine Similarity

## Definition
Cosine similarity is a measure of similarity between two vectors, calculated as the cosine of the angle between them. In the context of textual analysis, it is used to compare the semantic similarity of two pieces of text that have been converted into vector embeddings.

## How It Works
The metric yields a score between 0 and 1. A score of 0 indicates that the two pieces of text are semantically orthogonal (completely unrelated), while a score of 1 means they have the same meaning. The study provides an example: the sentences “Can you help me with logging in?” and “Why is my login not working?” have a cosine similarity of 0.68 in the model used.

## Application in the Study
The study uses cosine similarity as its primary method for comparing the embeddings of different conversations. This allows the researchers to quantify changes in an agent's conversational style before and after AI deployment and to compare the conversational styles between top and bottom quintile agents.

## Relationships

- **operates_on**: [[textual-embeddings|Textual Embeddings]]

---
*Extracted from: 2304.11771V2*