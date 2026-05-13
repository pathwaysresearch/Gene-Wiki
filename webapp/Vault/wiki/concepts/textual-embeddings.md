---
type: concept
aliases: [Textual Embeddings]
summary: A technique in natural language processing that transforms a body of text into a high-dimensional vector, representing its meaning and style in a linguistic space.
relationships:
  - target: all-minilm-l6-v2
    type: created_by
  - target: cosine-similarity
    type: is_a_prerequisite_for
tags: [nlp, machine-learning, text-analysis]
sourced_from: 2304.11771V2
---

# Textual Embeddings

## Definition
Textual embeddings are a method of representing text as high-dimensional numerical vectors. This transformation places the text into a 'linguistic space' where two pieces of text with similar meaning or style will have vectors (or 'coordinates') that are close to each other.

## Implementation in the Study
The study creates textual embeddings for each agent-customer conversation using the all-MiniLM-L6-v2 model, a large language model specifically intended to capture and cluster semantic information for assessing text similarity. This process is applied to the entire conversation text.

## Application
Once conversations are converted into embeddings, their similarity can be quantitatively measured using metrics like cosine similarity. The study uses this technique to compare the similarity of conversations across different workers and over time, for instance, by comparing an agent's post-AI conversations to their pre-AI conversations or comparing conversations between high- and low-skill agents.

## Relationships

- **created_by**: [[all-minilm-l6-v2|All Minilm L6 V2]]
- **is_a_prerequisite_for**: [[cosine-similarity|Cosine Similarity]]

---
*Extracted from: 2304.11771V2*