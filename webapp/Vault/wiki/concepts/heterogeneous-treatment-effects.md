---
type: concept
aliases: [Heterogeneous Treatment Effects]
summary: The analysis of how the impact of an intervention, such as AI deployment, varies across different subgroups of a population based on characteristics like skill, tenure, or behavior.
relationships:
  - target: difference-in-differences
    type: analyzed_using
  - target: resolutions-per-hour
    type: is_an_outcome_for
tags: [causal-inference, treatment-effects, subgroup-analysis]
sourced_from: 2304.11771V2
---

# Heterogeneous Treatment Effects

## Definition
Heterogeneous treatment effects occur when the causal effect of an intervention is not uniform across all individuals or units in a study. The paper conducts a detailed investigation of this phenomenon by analyzing how the productivity impact of AI assistance differs based on pre-existing agent characteristics.

## Analysis by Worker Skill and Tenure
The study finds strong evidence of heterogeneity based on both worker skill and tenure at the time of AI deployment. Table A.6 shows that the AI's impact on resolutions per hour is greatest for the lowest-skilled workers (a 0.527 increase for the bottom quintile) and progressively smaller for higher-skilled workers, becoming statistically insignificant for the top quintile. Similarly, the largest gains are for agents with less than one month of tenure, with the effect diminishing as tenure increases.

## Analysis by AI Adherence
The paper also explores heterogeneity based on agent behavior, specifically their initial adherence to the AI's suggestions. The results in Table A.7 demonstrate a clear positive relationship between adherence and productivity gains. Agents in the lowest quintile of adherence saw a 0.213 increase in resolutions per hour, while those in the highest adherence quintile experienced a much larger increase of 0.432. This indicates that how agents engage with the tool is a critical determinant of its effectiveness.

## Relationships

- **analyzed_using**: [[difference-in-differences|Difference In Differences]]
- **is_an_outcome_for**: [[resolutions-per-hour|Resolutions Per Hour]]

---
*Extracted from: 2304.11771V2*