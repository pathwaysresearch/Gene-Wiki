---
type: entity
aliases: [all-MiniLM-L6-v2]
summary: A specific large language model used in the study to generate textual embeddings for agent-customer conversations.
relationships:
  - target: textual-embeddings
    type: creates
tags: [large-language-model, nlp-tool, embedding-model]
sourced_from: 2304.11771V2
---

# all-MiniLM-L6-v2

## Overview
all-MiniLM-L6-v2 is a large language model (LLM) specifically designed for tasks involving semantic information capture and text similarity assessment. It is part of the sentence-transformer family of models, optimized for creating meaningful sentence and text embeddings.

## Role in the Study
The researchers used this model to create textual embeddings for each agent-customer conversation in their dataset. This process transformed the raw text of each conversation into a high-dimensional vector that represents its semantic content and style.

## Significance for Analysis
By using all-MiniLM-L6-v2 to generate embeddings, the study was able to perform quantitative comparisons of conversations. This was a crucial step for the analysis of conversation similarity, which involved calculating the cosine similarity between these vectors to understand how an agent's communication style changed over time or differed from that of other agents.

## Relationships

- **creates**: [[textual-embeddings|Textual Embeddings]]

---
*Extracted from: 2304.11771V2*