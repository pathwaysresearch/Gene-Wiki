---
type: concept
aliases: [Ideal Price Index Condition]
summary: An equation within a task-based economic model that defines a sector's aggregate price level as a function of input costs (capital and labor) and the extent of automation.
relationships:
  - target: automation-threshold
    type: depends_on
tags: [economic-model, price-theory, automation]
sourced_from: Acss Newfrontiers 20220814
---

# Ideal Price Index Condition

## Definition
The ideal price index condition is a formula that links the aggregate price index of a sector, $P_j$, to the prices of the inputs used to produce a continuum of tasks within that sector. It essentially aggregates the costs of all automated and non-automated tasks into a single price level for the sector's output, based on the competitive supply of tasks.

## Mathematical Formulation
The condition is given by the equation $P_j^{1-\sigma} = [I_j - N_j + 1]R_j^{1-\delta} + W_j^{1-\delta} \int_{I_j}^{N_j} \gamma_j(i)^{\delta-1} di$. This equation shows how the sectoral price index is constructed from its underlying components, including factor prices and technology parameters.

## Economic Interpretation
The formula has two main parts. The first term, $[I_j - N_j + 1]R_j^{1-\delta}$, represents the cost contribution of the tasks that are automated, which depends on the rental rate of capital ($R_j$) and the range of automated tasks (determined by the automation threshold $I_j$). The second term, $W_j^{1-\delta} \int_{I_j}^{N_j} \gamma_j(i)^{\delta-1} di$, represents the cost contribution of tasks performed by labor, which depends on the wage rate ($W_j$) and labor's productivity ($\gamma_j(i)$) across those tasks.

## Relationships

- **depends_on**: [[automation-threshold|Automation Threshold]]

---
*Extracted from: Acss Newfrontiers 20220814*