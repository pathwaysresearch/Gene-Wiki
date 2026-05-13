---
type: concept
aliases: [Stacked Long-Difference Regressions]
summary: An econometric method used to analyze panel data by calculating changes over long periods (e.g., decades) and stacking these periods for a single regression analysis.
relationships:
  - target: augmentation-exposure
    type: used_to_analyze
  - target: automation-exposure
    type: used_to_analyze
tags: [econometrics, panel-data, statistical-method]
sourced_from: Acss Newfrontiers 20220814
---

# Stacked Long-Difference Regressions

## Definition
Stacked long-difference regression is a statistical technique for analyzing panel data over extended time horizons. The method involves calculating the changes (differences) in variables over long, discrete time periods and then "stacking" these periods into a single dataset for regression analysis. This approach is particularly useful for studying slow-moving processes and long-term relationships, smoothing out short-term fluctuations.

## Application in the Study
This method is the primary analytical tool used in the paper to assess the relationship between technological exposure and labor market outcomes. Tables 6 and 8 are explicitly titled as using "OLS Stacked Long-Difference Regressions" and "OLS and 2SLS Stacked Long-Difference Regressions." The analysis specifically uses four-decade changes, comparing the 1940-1980 period with the 1980-2018 period. These two long-difference periods are then stacked to form the dataset for the main analysis.

## Model Specification
The regressions are performed on industry-occupation cells, with observations weighted by the start-of-period employment share for each cell. The dependent variables are the decadalized changes in the logarithm of employment and various wage bill measures. The key independent variables are the Augmentation Exposure and Automation Exposure measures. The models also include various fixed effects, such as industry by 40-year period fixed effects, to control for unobserved heterogeneity.

## Relationships

- **used_to_analyze**: [[augmentation-exposure|Augmentation Exposure]]
- **used_to_analyze**: [[automation-exposure|Automation Exposure]]

---
*Extracted from: Acss Newfrontiers 20220814*