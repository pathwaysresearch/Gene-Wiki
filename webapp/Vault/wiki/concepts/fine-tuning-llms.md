---
type: concept
aliases: [Fine-tuning (LLMs)]
summary: A process of adapting a general-purpose Large Language Model to a specific task or domain by training it further on specialized data.
relationships:
  - target: large-language-models
    type: is_a_technique_for
tags: [machine-learning, large-language-models, model-training]
sourced_from: 2304.11771V2
---

# Fine-tuning (LLMs)

## Definition
Fine-tuning is a technique used to adapt a general-purpose Large Language Model (LLM) to generate output that better aligns with the priorities of a specific setting or application. This refinement process makes the model better suited to its intended use case.

## How It Works
Fine-tuning can be accomplished through several methods. One approach is to provide the model with labeled data relevant to the specific task, such as social media content paired with its user engagement data. Another method involves using human evaluators to rank multiple potential outputs from the LLM. This ranking data is then used to train a reward function that teaches the model to prioritize desirable responses, such as those that are factually correct and non-toxic.

## Significance
This refinement process is crucial for enhancing model quality and performance. By making a general-purpose model better suited to its specific application, fine-tuning can generate meaningful improvements and increase the model's practical utility.

## Relationships

- **is_a_technique_for**: [[large-language-models|Large Language Models]]

---
*Extracted from: 2304.11771V2*