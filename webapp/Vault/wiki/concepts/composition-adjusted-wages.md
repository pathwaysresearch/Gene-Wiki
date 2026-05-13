---
type: concept
aliases: [Composition-Adjusted Wages]
summary: A methodological construct used to measure wage changes while controlling for shifts in worker demographics such as schooling, race, gender, and age.
relationships:
  - target: task-augmentation
    type: is_used_to_analyze
  - target: task-automation
    type: is_used_to_analyze
tags: [econometrics, labor-economics, methodology]
sourced_from: Acss Newfrontiers 20220814
---

# Composition-Adjusted Wages

## Definition and Purpose
Composition-adjusted wages are a refined measure used to analyze the impact of innovations on worker earnings. The purpose is to isolate the effect of forces like augmentation and automation on wages from concurrent shifts in the demographic composition of the workforce within an occupation-industry cell. This adjustment is crucial because, as the study suggests, adverse compositional shifts in augmentation-exposed occupations could otherwise mask a positive underlying relationship between augmentation and wages.

## Calculation Method
The measure is constructed using a multi-step process. First, cross-sectional Mincerian wage regressions are estimated in each Census year to predict the log hourly wage of each worker based solely on their demographic characteristics (schooling, race, gender, and a quartic in age). The average of these predictions within an occupation-industry cell yields an "expected wage" that is purged of specific occupation-industry wage premia. The final composition-adjusted wagebill change is then calculated as the sum of the observed log change in employment and the log difference between the observed and the composition-adjusted wage change.

## Application and Findings
By applying this method, the study finds that the causal effect of augmentation innovations on composition-adjusted wagebills is modestly greater than their effect on employment. This key finding supports the idea that augmentation not only creates jobs but may also have a positive impact on the wages for those jobs, an effect that is clarified once confounding changes in worker characteristics are controlled for.

## Relationships

- **is_used_to_analyze**: [[task-augmentation|Task Augmentation]]
- **is_used_to_analyze**: [[task-automation|Task Automation]]

---
*Extracted from: Acss Newfrontiers 20220814*