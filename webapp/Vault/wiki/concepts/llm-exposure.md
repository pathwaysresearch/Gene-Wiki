---
type: concept
aliases: [LLM Exposure]
summary: A measure of the degree to which tasks within an occupation can be performed more efficiently with the assistance of Large Language Models like GPTs.
relationships:
  - target: llm-exposure-rubric
    type: is_measured_by
  - target: job-zones
    type: is_analyzed_by
  - target: gpt-4
    type: is_subject_of
  - target: webbs-ai-exposure-measures
    type: is_compared_with
  - target: suitability-for-machine-learning-sml
    type: is_compared_with
tags: [labor-economics, ai-impact, occupational-analysis]
sourced_from: 2303.10130V5
---

# LLM Exposure

## Definition
LLM exposure is a metric designed to gauge the potential impact of Generative Pre-trained Transformers (GPTs) on occupations in the labor market. It assesses the extent to which tasks can have their completion time reduced with equivalent quality through the use of LLMs, either directly or via LLM-powered software.

## Measurement Methodology
The study measures exposure using a rubric applied by both human annotators and GPT-4. The primary metric, denoted as beta (β), includes exposure to both direct LLM use and partial LLM-powered software. These ratings are calculated at the task level and then aggregated for each occupation, with all tasks typically weighted equally.

## Key Findings
The analysis reveals a positive correlation between LLM exposure and wages, indicating that higher-wage occupations tend to be more exposed to LLMs. The study also finds that its exposure measures are positively and significantly correlated with previous measures of exposure to software and AI, such as Webb's patent-based measures and the Suitability for Machine Learning (SML) score, suggesting cohesion with prior research.

## Relationships

- **is_measured_by**: [[llm-exposure-rubric|Llm Exposure Rubric]]
- **is_analyzed_by**: [[job-zones|Job Zones]]
- **is_subject_of**: [[gpt-4|Gpt 4]]
- **is_compared_with**: [[webbs-ai-exposure-measures|Webbs Ai Exposure Measures]]
- **is_compared_with**: [[suitability-for-machine-learning-sml|Suitability For Machine Learning Sml]]

---
*Extracted from: 2303.10130V5*