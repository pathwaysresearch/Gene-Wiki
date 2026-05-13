---
type: entity
aliases: [GPT-4]
summary: A specific Large Language Model from OpenAI whose observed capabilities motivated this study and which was used as a tool to classify the exposure of job tasks. A specific Generative Pre-trained Transformer model used in the study both as a subject of analysis and as a tool for rating occupational exposure.
relationships:
  - target: jagged-technological-frontier
    type: exhibits
  - target: jagged-capability-frontier
    type: is_an_example_of
  - target: inside-the-frontier-task
    type: was_used_for
  - target: outside-the-frontier-task
    type: was_used_for
  - target: large-language-models
    type: is_a
  - target: openai
    type: developed_by
  - target: exposure-to-llms
    type: is_tool_for
  - target: llm-exposure
    type: is_used_to_measure
  - target: llm-exposure-rubric
    type: applies
tags: [ai-model, openai, research-tool, large-language-model, ai-research]
sourced_from: 2303.10130V5
---

# GPT-4

## Overview
GPT-4 is a large language model developed by OpenAI. The text refers to it as a state-of-the-art model whose observed capabilities were a strong motivation for the research into the labor market impact of LLMs. The study specifically used an early version of the model.

## Role in the Study
GPT-4 played a dual role in the research. First, its advanced capabilities, and those of the suite of tools being developed with it, served as the primary inspiration for creating a new rubric to measure LLM exposure in the labor market. Second, the model was actively used as a tool in the data collection process. It was prompted with a rubric to generate annotations on the exposure of O*NET tasks, providing a machine-generated dataset of classifications.

## Performance and Comparison
To validate its use as a research tool, the study compared GPT-4's classifications with those made by experienced human annotators. The results, presented in a table, show significant levels of agreement. For instance, under one weighting scheme (ζ E1 + E2), the agreement between GPT-4 and human ratings was 82.1%, with a Pearson's correlation of 0.654. This suggests a notable similarity between the model's and humans' assessments of task exposure.

## Relationships

- **is_a**: [[large-language-models|Large Language Models]]
- **developed_by**: [[openai|Openai]]
- **is_tool_for**: [[exposure-to-llms|Exposure To Llms]]
- **is_used_to_measure**: [[llm-exposure|Llm Exposure]]
- **applies**: [[llm-exposure-rubric|Llm Exposure Rubric]]

---
*Extracted from: 2303.10130V5*

---
*Also referenced in: Ssrn 4573321*