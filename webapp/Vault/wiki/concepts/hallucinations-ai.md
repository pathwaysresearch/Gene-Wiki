---
type: concept
aliases: [Hallucinations (AI)]
summary: A phenomenon where Large Language Models generate factually inaccurate or nonsensical statements, often as a side effect of increasing creative parameters like "temperature".
relationships:
  - target: large-language-models
    type: is_limitation_of
tags: [llm-limitations, ai-safety, factual-accuracy]
sourced_from: Ai
---

# Hallucinations (AI)

## Definition
In the context of Large Language Models (LLMs), "hallucinations" are defined as the generation of factually inaccurate statements or nonsensical content. This phenomenon represents a key challenge in the reliability of AI-generated text.

## Causes and Tradeoffs
The text links hallucinations to efforts to increase model creativity. Specifically, dialing up an LLM's "temperature" parameter, a technique intended to produce more original ideas, also leads to a higher incidence of factual inaccuracies. This creates a tradeoff between originality and factual reliability.

## Impact on Ideation
While hallucinations are considered less of a critical concern in creative ideation, where the goal is to generate just one excellent idea even at the cost of much nonsense, they still introduce noise. This noise must be filtered out by humans during the evaluation phase, a process that is challenging as humans often struggle to predict which ideas will ultimately succeed.

## Relationships

- **is_limitation_of**: [[large-language-models|Large Language Models]]

---
*Extracted from: Ai*