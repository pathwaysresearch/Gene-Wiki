---
type: concept
aliases: [Resolutions per Hour]
summary: A key productivity metric used in the study to measure the number of technical support problems an agent resolves per hour of work. A key performance metric used to measure the productivity of customer service agents, defined as the number of customer issues successfully resolved per hour of work.
relationships:
  - target: heterogeneous-treatment-effects
    type: is_an_outcome_for
  - target: average-handle-time
    type: is_related_to
tags: [performance-metric, productivity, contact-center, kpi]
sourced_from: 2304.11771V2
---

# Resolutions per Hour

## Definition
Resolutions per hour is the main measure of productivity used in the study. It is defined as the number of technical support problems that a contact center agent successfully resolves within a single hour of work. The mean value for this metric in the sample was approximately 2.1-2.2.

## Measurement and Calculation
This metric is calculated at the agent-month level. The data firm uses an algorithm that incorporates elements of chat text and analyzes future interactions between the customer and the firm to determine a monthly average call resolution score for each agent. This score is then normalized by hours worked to get the final metric.

## Role in the Analysis
Resolutions per hour serves as the primary dependent variable in the difference-in-differences regressions (Table 2) to quantify the impact of AI model deployment on agent productivity. The analysis shows a statistically significant increase in resolutions per hour for agents after gaining access to the AI assistant, with the preferred specification showing an increase of 0.301 resolutions per hour.

## Relationships

- **is_an_outcome_for**: [[heterogeneous-treatment-effects|Heterogeneous Treatment Effects]]
- **is_related_to**: [[average-handle-time|Average Handle Time]]

---
*Extracted from: 2304.11771V2*