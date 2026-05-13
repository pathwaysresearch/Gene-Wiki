---
type: concept
aliases: [Two-Stage Least Squares (2SLS)]
summary: An econometric method used to estimate causal relationships in the presence of endogenous explanatory variables by using instrumental variables (IVs).
relationships:
  - target: augmentation-vs-automation-innovation
    type: used_to_analyze
tags: [econometrics, causal-inference, instrumental-variables]
sourced_from: Acss Newfrontiers 20220814
---

# Two-Stage Least Squares (2SLS)

## Application in the Study
The paper utilizes a Two-Stage Least Squares (2SLS) instrumental variable strategy to identify the causal impact of augmentation and automation innovations on labor market outcomes like new title emergence. A schematic of the 2SLS procedure is provided in Figure 7, illustrating how the model is structured to establish causality.

## First Stage
The first stage of the 2SLS model regresses the endogenous variables (counts of augmentation and automation patents) on instrumental variables. As shown in Table 3, the study uses "Augmentation IV" and "Automation IV" as instruments. The schematic in Figure 7 indicates these instruments are derived from "Breakthrough Patents" from 20 years prior (T-20), which are then used to predict patent flows by class.

## Instrument Validity
The strength and validity of the instruments are crucial for a 2SLS analysis. Table 3 reports very high F-statistics and Sanderson-Windmeijer F-statistics for the first-stage regressions across different time periods (e.g., Sanderson-Windmeijer F-stat of 4060.15 for the Augmentation IV from 1940-2018). These high values indicate that the instruments are strong predictors and not subject to a weak instrument problem, lending credibility to the study's causal claims.

## Relationships

- **used_to_analyze**: [[augmentation-vs-automation-innovation|Augmentation Vs Automation Innovation]]

---
*Extracted from: Acss Newfrontiers 20220814*