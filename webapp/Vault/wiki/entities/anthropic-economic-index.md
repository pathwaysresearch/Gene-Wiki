---
type: entity
aliases: [Anthropic Economic Index]
summary: A data source that measures occupational AI exposure by analyzing the share of queries related to O*NET tasks from millions of user conversations with the AI model Claude.
relationships:
  - target: occupational-ai-exposure
    type: is_an_instance_of
  - target: ai-automation-vs-augmentation
    type: used_to_measure
tags: [ai-exposure, measurement, dataset, anthropic]
sourced_from: Canariesinthecoalmine Nov25
---

# Anthropic Economic Index

## Overview
The Anthropic Economic Index, based on work by Handa et al. (2025), provides a usage-based measure of generative AI's relevance to different occupations. It is the second approach used in "Canaries in the Coal Mine?" to measure occupational AI exposure, complementing the model-capability-based measure from Eloundou et al. (2024).

## Methodology
The index is constructed by analyzing a large dataset of "several million conversations" with Claude, a large language model from Anthropic. It estimates the share of user queries that pertain to each specific task listed in the O*NET database. This provides a direct, real-world measure of how generative AI is being used in relation to different job tasks.

## Role in Research
This index is used to empirically distinguish between AI applications that automate work versus those that augment it. By examining the nature of the queries to Claude, researchers can infer whether the AI is being used to substitute for or complement human labor in the tasks of a given occupation, which helps explain differential employment outcomes.

## Relationships

- **is_an_instance_of**: [[occupational-ai-exposure|Occupational Ai Exposure]]
- **used_to_measure**: [[ai-automation-vs-augmentation|Ai Automation Vs Augmentation]]

---
*Extracted from: Canariesinthecoalmine Nov25*