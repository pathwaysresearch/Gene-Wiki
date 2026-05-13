---
type: concept
aliases: [Exposure (to LLMs)]
summary: A measure of whether access to an LLM or LLM-powered system would reduce the time required for a human to perform a specific work task at the same level of quality.
relationships:
  - target: large-language-models
    type: is_a_measure_for
  - target: task-based-framework
    type: uses_methodology
  - target: gpt-4
    type: uses_tool
  - target: o-net
    type: uses_data_from
tags: [labor-economics, measurement, methodology]
sourced_from: 2303.10130V5
---

# Exposure (to LLMs)

## Definition
Exposure is a metric developed to quantify the potential impact of Large Language Models on job tasks. It is specifically defined as a measure of whether access to an LLM or an LLM-powered system would reduce the time a human needs to complete a specific task while maintaining the same level of quality. This measure reflects the technical capacity for LLMs to make human labor more efficient, though it does not predict actual adoption or automation outcomes, which are influenced by social, economic, and regulatory factors.

## Measurement Methodology
Exposure is assessed using a detailed rubric applied to individual work tasks and Detailed Worker Activities (DWAs) from the O*NET database. In the study that introduced this concept, annotations were collected from both experienced human annotators and the GPT-4 model itself. The results were then aggregated to the occupation level. The analysis used different levels of exposure, denoted as α (direct LLM impact), β (LLM plus anticipated tools), and ζ, to capture varying degrees of technological integration.

## Key Findings
Analysis based on the exposure metric found that, on average, approximately 15% of tasks within an occupation are directly exposed to LLMs (α exposure). Using a broader measure that includes LLM-powered software (β exposure), the study estimated that 80% of the U.S. workforce is in an occupation with at least 10% of its tasks exposed, and 19% of workers are in occupations where over half of the tasks are exposed.

## Relationships

- **is_a_measure_for**: [[large-language-models|Large Language Models]]
- **uses_methodology**: [[task-based-framework|Task Based Framework]]
- **uses_tool**: [[gpt-4|Gpt 4]]
- **uses_data_from**: [[o-net|O Net]]

---
*Extracted from: 2303.10130V5*