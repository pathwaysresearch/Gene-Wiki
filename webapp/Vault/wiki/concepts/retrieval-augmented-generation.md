---
type: concept
aliases: [Retrieval-Augmented Generation]
summary: A technique that supplements Large Language Models with specialized, external knowledge retrieved via an interface like an API to improve the relevance and accuracy of their outputs.
relationships:
  - target: large-language-models
    type: enhances
tags: [llm-technique, information-retrieval, prompt-engineering]
sourced_from: Ai
---

# Retrieval-Augmented Generation

## Definition
Retrieval-augmented generation is a technique used to enhance the outputs of Large Language Models (LLMs) by supplementing them with specialized, external knowledge. This allows the model to produce more informed and contextually relevant responses.

## How It Works
The method typically utilizes an Application Programming Interface (API) to retrieve information from external sources, such as the academic database Semantic Scholar. This retrieved knowledge is then used to "augment" the user's original prompt before it is processed by the LLM.

## Application Example
The text illustrates this technique with an example prompt where an LLM is instructed to act like an API. The user asks the model to retrieve recent consumer research papers on a specific topic, summarize their findings, and then use this retrieved information to generate practical insights and future research directions, all within a structured response.

## Relationships

- **enhances**: [[large-language-models|Large Language Models]]

---
*Extracted from: Ai*