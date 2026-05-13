---
type: concept
aliases: [Front-Door Adjustment]
summary: A method for estimating a causal effect when direct confounders are unobserved, by leveraging an intermediate variable that lies on the causal pathway between the cause and effect.
relationships:
  - target: back-door-adjustment
    type: is_an_alternative_to
  - target: do-calculus
    type: is_derived_from
tags: [causal-inference, mediation-analysis, statistical-adjustment]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Front-Door Adjustment

## Definition
The front-door adjustment is a technique for calculating the causal effect of a variable X on an outcome Y, even when there is an unobserved confounder between them. It works by identifying a mediating variable M that lies on the causal path from X to Y, is not directly affected by the confounder, and is the sole pathway through which X affects Y.

## How It Works
The method breaks down the problem into two parts that can be estimated from observational data. First, it estimates the causal effect of X on the mediator M. Second, it estimates the causal effect of the mediator M on the outcome Y, controlling for X. By combining these two estimated effects, one can compute the total causal effect of X on Y. The text illustrates this with the example of smoking (X), tar deposits (M), and cancer (Y), where the effect of smoking on cancer is calculated by combining the effect of smoking on tar and the effect of tar on cancer.

## Applications
Though not widely used initially, the front-door adjustment has proven valuable in fields like political science. A notable application by Adam Glynn and Konstantin Kashin analyzed the Job Training Partnership Act (JTPA) Study. They used the method to estimate the causal effect of job-training services on earnings, navigating the complexities of both randomized and observational data within the study.

## Relationships

- **is_an_alternative_to**: [[back-door-adjustment|Back Door Adjustment]]
- **is_derived_from**: [[do-calculus|Do Calculus]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*