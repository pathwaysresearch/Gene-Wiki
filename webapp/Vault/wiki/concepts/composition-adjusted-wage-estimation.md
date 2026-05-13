---
type: concept
aliases: [Composition-Adjusted Wage Estimation]
summary: A statistical method to control for changes in worker composition, such as experience and education, when analyzing wage trends affected by occupational shifts.
relationships:
  - target: automation-threshold
    type: used_to_measure_impact_of
tags: [econometrics, labor-economics, statistical-method]
sourced_from: Acss Newfrontiers 20220814
---

# Composition-Adjusted Wage Estimation

## Purpose
The text explains that contracting occupations tend to retain more experienced, higher-earning workers, while expanding occupations do the opposite. This creates a negative correlation between employment and wage changes that is due to worker composition, not changes in the price of skill. Composition-adjusted wage estimation is a method designed to isolate the "price" component by controlling for these compositional shifts to better understand the effect of innovations like automation.

## Estimation Procedure
The method is implemented in multiple steps to construct composition-constant wages. The first step involves estimating cross-sectional log hourly wage regressions for each census year using data from the primary Census and ACS samples. This procedure produces a predicted wage for each worker, which accounts for their individual demographic and skill characteristics, thereby neutralizing the effect of compositional changes in the workforce over time.

## Regression Model
The core of the first step is a wage regression model specified as $w_{nt} = \alpha_{nt} + S_n' \beta_{1t} + (S_n \times A_n)' \beta_{2t} + (S_n \times A_n^2)' \beta_{3t} + e_{nt}$. In this equation, $w_{nt}$ is log hourly earnings, $S_n$ is a vector of dummies for schooling levels, and $A_n$ is age. The model includes a quadratic in age fully interacted with schooling levels to flexibly capture education-experience profiles, and it is fitted separately for eight distinct demographic groups (male/female × white/Black/Hispanic/other) in each time period.

## Relationships

- **used_to_measure_impact_of**: [[automation-threshold|Automation Threshold]]

---
*Extracted from: Acss Newfrontiers 20220814*