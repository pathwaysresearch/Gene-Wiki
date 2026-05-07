---
type: concept
aliases: [Productivity (in LLM Ideation)]
summary: An ideation strategy focused on using Large Language Models (LLMs) to generate a high volume of ideas within a specific and narrowly defined domain.
relationships:
  - target: semantic-breadth-in-llm-ideation
    type: is_contrasted_with
  - target: ideation-roles-for-llms
    type: is_a_goal_of
tags: [llm-application, ideation, creativity, prompt-engineering]
sourced_from: Ai
---

# Productivity (in LLM Ideation)

## Definition
Productivity, in the context of LLM-assisted ideation, refers to the strategy of generating more ideas within a narrow domain. It prioritizes the volume of relevant ideas over their diversity.

## Recommended Techniques
The text suggests several techniques to increase productivity. These include few-shot prompting (including a sample of highly relevant ideas in the prompt), retrieval-augmented generation (using an API that fetches specialized data to augment the prompt), or fine-tuning an LLM on specialized data.

## Limitations
The text explicitly warns that while this approach is effective for generating many ideas, the number of original ideas generated through this method will eventually plateau. This indicates a trade-off between the quantity of ideas and their novelty when focusing solely on a productivity-oriented strategy.

## Relationships

- **is_contrasted_with**: [[semantic-breadth-in-llm-ideation|Semantic Breadth In Llm Ideation]]
- **is_a_goal_of**: [[ideation-roles-for-llms|Ideation Roles For Llms]]

---
*Extracted from: Ai*