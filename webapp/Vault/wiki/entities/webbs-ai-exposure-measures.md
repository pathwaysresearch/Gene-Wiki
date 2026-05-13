---
type: entity
aliases: [Webb's AI Exposure Measures]
summary: A set of occupational exposure scores based on the text of patents, used as a benchmark to validate the study's new LLM exposure metrics.
relationships:
  - target: llm-exposure
    type: is_benchmark_for
tags: [economic-measurement, ai-impact, patent-analysis]
sourced_from: 2303.10130V5
---

# Webb's AI Exposure Measures

## Overview
Webb's AI Exposure Measures are a previously developed set of metrics that quantify the exposure of different occupations to various technologies. These measures are derived from analyzing the text of patents related to specific technologies.

## Components
The measures used for comparison in this study include three distinct components: "Software (Webb)", "Robot (Webb)", and "AI (Webb)". Each component provides a score for different occupations, reflecting their relevance to patents in that technological category.

## Use as a Benchmark
The study uses Webb's measures as a benchmark to validate its own newly developed LLM exposure ratings. The results show a statistically significant positive correlation between the study's GPT-4 and Human exposure ratings and Webb's "Software" and "AI" measures. Conversely, a significant negative correlation was found with the "Robot" measure, indicating that tasks exposed to LLMs are distinct from those exposed to physical robotics.

## Relationships

- **is_benchmark_for**: [[llm-exposure|Llm Exposure]]

---
*Extracted from: 2303.10130V5*