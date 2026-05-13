---
type: entity
aliases: [Eloundou et al. Study]
summary: A study that identifies tasks and occupations exposed to generative AI and computer vision technologies, used to estimate the GDP share of tasks impacted by AI.
relationships:
  - target: svanberg-et-al-2024-study
    type: is_refined_by
tags: [ai-research, labor-economics, economic-impact]
sourced_from: Ai
---

# Eloundou et al. Study

## Overview
The Eloundou et al. study is a key data source used in the text's quantitative evaluation of AI's economic effects. Its primary contribution is to identify which tasks can ultimately be performed by generative AI and computer vision technologies.

## Methodology and Application
The author converts the study's task-level data into an aggregate economic measure. This is done by grouping tasks into occupations and then aggregating across these occupations using their wage bills from U.S. Bureau of Labor Statistics data. This procedure yields a wage bill-weighted share of exposed occupations of 19.9%, which is then interpreted as the GDP share of tasks exposed to AI.

## Limitations and Refinements
The text notes two key pieces of information missing from the Eloundou et al. data: the likely timeframe for the impact (e.g., within 10 years) and whether it would be profitable to automate all the identified tasks. To create a more realistic forecast, the author adjusts these figures using estimates from the Svanberg et al. (2024) study on the feasibility and profitability of automation.

## Relationships

- **is_refined_by**: [[svanberg-et-al-2024-study|Svanberg Et Al 2024 Study]]

---
*Extracted from: Ai*