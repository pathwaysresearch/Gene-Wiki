---
type: concept
aliases: [Mediation Fallacy]
summary: The error of conditioning on a mediating variable to estimate a direct effect, instead of the correct procedure of holding the mediator constant.
relationships:
  - target: mediation-analysis
    type: is_a_pitfall_in
  - target: william-kruskal
    type: was_identified_by
tags: [causality, statistics, fallacy, confounding]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Mediation Fallacy

## Definition of the Error
The Mediation Fallacy is a common blunder in statistical analysis that occurs when an investigator attempts to estimate a direct effect by conditioning on a mediator variable. This is conceptually incorrect because conditioning (or "seeing") is not the same as intervening (or "doing"). The correct procedure to disable the indirect path and isolate the direct effect is to hold the mediator constant.

## Why It Is a Fallacy
Conditioning on a mediator is only a valid proxy for holding it constant if there is no confounding between the mediator and the outcome. As William Kruskal pointed out in the Berkeley admissions debate, if a confounder exists (e.g., an applicant's state of residence affecting both department choice and admission chances), conditioning on the mediator can completely reverse the analysis. It can lead an investigator to conclude there is no direct effect when, in fact, one exists.

## Historical Recognition
The text notes that this fallacy was recognized by figures like Burks and William Kruskal long before the formal language of modern causal inference was developed to clearly articulate it. Their struggle to explain the problem highlights the historical difficulty statisticians faced in distinguishing between statistical association (found by conditioning) and causal effects (found by intervention).

## Relationships

- **is_a_pitfall_in**: [[mediation-analysis|Mediation Analysis]]
- **was_identified_by**: [[william-kruskal|William Kruskal]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*