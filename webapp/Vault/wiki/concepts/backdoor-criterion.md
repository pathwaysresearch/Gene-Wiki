---
type: concept
aliases: [Backdoor Criterion]
summary: A graphical criterion used to identify a sufficient set of variables for adjustment to remove confounding bias when estimating a causal effect from observational data.
relationships:
  - target: confounding
    type: solves
  - target: do-operator
    type: enables_estimation_of
  - target: do-calculus
    type: is_a_special_case_of
tags: [causal-inference, confounding, graphical-models, methodology]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Backdoor Criterion

## Definition
The backdoor criterion is a rule that uses a causal diagram to identify a set of variables that, if controlled for, can deconfound the relationship between a treatment and an outcome. It provides a precise, graphical method for selecting covariates for adjustment, moving beyond simple statistical association.

## How It Works
The criterion identifies confounding by looking for "noncausal paths" or "backdoor paths" between the treatment and outcome variables in a causal diagram. A backdoor path is a path that contains an arrow pointing into the treatment variable. To block these paths and eliminate confounding, one must adjust for a set of variables that satisfies the backdoor criterion. This allows the estimation of the causal effect as if it were from a randomized experiment.

## Relationship to Intervention
The text explicitly links the backdoor criterion to the `do-operator`. Satisfying the criterion allows one to equate a statistical, conditional probability with an interventional probability (a `do-expression`). It is a fundamental tool for connecting the second rung of the Ladder of Causation (doing) to the first (seeing) using the assumptions encoded in a causal model.

## Relationships

- **solves**: [[confounding|Confounding]]
- **enables_estimation_of**: [[do-operator|Do Operator]]
- **is_a_special_case_of**: [[do-calculus|Do Calculus]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*