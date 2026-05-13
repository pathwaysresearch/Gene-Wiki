---
type: entity
aliases: [Suitability for Machine Learning (SML)]
summary: An occupational exposure score used as a benchmark in the study to validate its new LLM exposure metrics.
relationships:
  - target: llm-exposure
    type: is_benchmark_for
tags: [economic-measurement, ai-impact, machine-learning]
sourced_from: 2303.10130V5
---

# Suitability for Machine Learning (SML)

## Overview
The Suitability for Machine Learning (SML) score is a metric developed in a previous study to assess the degree to which occupations are suitable for the application of machine learning. It provides a quantitative measure of AI exposure at the occupational level.

## Role as a Benchmark
In this paper, the SML score is used as a key benchmark to validate the newly created LLM exposure measures. The authors state that the "SML exposure scores by occupation show significant and positive associations with the exposure scores we develop in this paper," demonstrating a level of cohesion between the two approaches.

## Correlation Findings
The regression analysis presented in the study confirms this strong relationship. The SML variable shows a highly statistically significant and positive coefficient when predicting the study's GPT-4 and Human exposure ratings. This highlights its strong predictive power and alignment with the new measures of LLM exposure.

## Relationships

- **is_benchmark_for**: [[llm-exposure|Llm Exposure]]

---
*Extracted from: 2303.10130V5*