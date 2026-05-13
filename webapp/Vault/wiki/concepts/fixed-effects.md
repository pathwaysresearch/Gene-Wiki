---
type: concept
aliases: [Fixed Effects]
summary: A statistical modeling technique that controls for unobserved, time-invariant characteristics of individuals or groups to isolate the effect of a variable of interest.
relationships:
  - target: difference-in-differences
    type: is_used_by
tags: [econometrics, statistical-method, panel-data]
sourced_from: 2304.11771V2
---

# Fixed Effects

## Definition
Fixed effects is a statistical method used in panel data regression to control for omitted variables that are constant over time within each individual unit (e.g., an agent). By including a separate intercept for each unit, the model effectively removes any time-invariant heterogeneity, allowing for a cleaner estimate of the effects of variables that do change over time.

## Application in the Study
The study extensively uses fixed effects in its regression models to improve the accuracy of its estimates. Specifically, it employs agent fixed effects, year-month fixed effects, and agent tenure fixed effects.

## Types of Fixed Effects Used
Agent fixed effects control for any stable, unobserved characteristics of an agent, such as innate skill or motivation. Year-month fixed effects account for common shocks or seasonality that affect all agents in a given month. Agent tenure fixed effects control for experience-related learning curves, ensuring that productivity gains are not mistakenly attributed to the AI when they are actually due to an agent becoming more experienced.

## Relationships

- **is_used_by**: [[difference-in-differences|Difference In Differences]]

---
*Extracted from: 2304.11771V2*