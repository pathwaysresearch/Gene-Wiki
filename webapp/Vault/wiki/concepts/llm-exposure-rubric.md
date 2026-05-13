---
type: concept
aliases: [LLM Exposure Rubric]
summary: A classification taxonomy used to label tasks based on their degree of exposure to Large Language Models, categorizing them as having no, direct, or LLM-powered application exposure.
relationships:
  - target: llm-exposure
    type: measures
  - target: gpt-4
    type: is_used_by
tags: [methodology, ai-measurement, taxonomy]
sourced_from: 2303.10130V5
---

# LLM Exposure Rubric

## Purpose
The LLM Exposure Rubric is a taxonomy presented in the study to systematically gauge a task's exposure to Generative Pre-trained Transformers (GPTs). It provides a standardized method for annotators, both human and AI, to classify the potential for LLMs to impact the performance of specific job-related tasks based on time savings.

## Exposure Levels
The rubric defines three distinct levels of exposure. **E0 (No exposure)** applies to tasks where an LLM cannot reduce completion time by at least half with equivalent quality, especially those requiring in-person interaction. **E1 (Direct exposure)** is for tasks where direct access to an LLM interface like ChatGPT can cut completion time by at least half, such as writing, coding, or summarizing text. **E2 (Exposure by LLM-powered applications)** covers tasks where an LLM alone is insufficient, but it is easy to imagine LLM-powered software that could be developed to achieve the 50% time reduction.

## Application in the Study
This rubric was used by both human annotators and GPT-4 to label tasks within the U.S. labor market. The resulting classifications were then aggregated to create occupational-level exposure scores, which formed the core data for the paper's analysis of LLM impact on employment and wages.

## Relationships

- **measures**: [[llm-exposure|Llm Exposure]]
- **is_used_by**: [[gpt-4|Gpt 4]]

---
*Extracted from: 2303.10130V5*