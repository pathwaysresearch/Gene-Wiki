---
type: concept
aliases: [Collider Bias]
summary: A statistical bias that occurs when conditioning on a common effect (a collider) of two independent causes, which can create a spurious association between those causes. A type of bias introduced in a statistical analysis by conditioning on a variable that is a common effect of the cause being studied and another variable.
relationships:
  - target: barbara-burks
    type: discovered_by
tags: [statistical-bias, causality, epidemiology, causal-inference]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Collider Bias

## Definition
A collider is a variable that is causally influenced by two or more other variables. Collider bias occurs when a statistical analysis conditions on a collider, which can create a spurious, non-causal association between its causes. This bias can be particularly misleading because it can create an association where none exists or distort an existing one.

## How It Works
When two variables (parents) are independent but both cause a third variable (the collider), conditioning on the collider creates a probabilistic dependence between the parents. The text explains this as opening up a "back-door path" between the causes. This is a systematic error that can arise in data analysis, especially when selecting a sub-population for study based on a particular outcome.

## Key Examples
The provided text uses two main examples to illustrate collider bias. The first is the Birth-Weight Paradox, where "Birth Weight" is a collider for "Smoking" and "Birth Defect." The second is the Monty Hall Problem, where the "Door Opened" by the host is a collider for the contestant's initial choice ("Your Door") and the "Location of Car."

## Relationships

- **discovered_by**: [[barbara-burks|Barbara Burks]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*