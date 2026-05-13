---
type: concept
aliases: [Confounding]
summary: A bias in causal inference where a third variable is associated with both the exposure and the outcome, creating a spurious correlation. A bias in causal inference that occurs when a third variable influences both the supposed cause and the supposed effect, distorting the true relationship. A source of bias in observational studies where a third variable is a common cause of both the exposure and the outcome, creating a spurious association.
relationships:
  - target: noncollapsibility
    type: has_flawed_definition
  - target: exchangeability
    type: is_defined_by
  - target: back-door-path
    type: is_addressed_by
  - target: back-door-criterion
    type: addressed_by
  - target: backdoor-criterion
    type: is_a_solution_for
  - target: observational-studies
    type: is_a_problem_in
tags: [causal-inference, statistics, epidemiology, bias]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Confounding

## Overview
Confounding is a central problem in causal inference that has puzzled and confused generations of scientists. It refers to a situation where the observed association between a variable X (treatment/exposure) and an outcome Y is distorted by a third variable, a confounder, which is related to both X and Y. The failure to properly account for confounding can lead to wrong decisions and incorrect scientific conclusions, as it did for years in the smoking-cancer debate.

## Flawed Definitions
Historically, confounding has been defined using inadequate statistical criteria. One flawed declarative definition is that a confounder is any variable correlated with both X and Y. A common flawed procedural definition is "noncollapsibility," which suggests testing for confounding by comparing a crude risk estimate with an adjusted one. Such approaches have misguided epidemiologists, economists, and social scientists for a century because they rely solely on statistical associations in the data without considering the underlying causal structure.

## The Causal Revolution's Solution
The Causal Revolution provides a clear, model-based solution to confounding through the use of causal diagrams. The "back-door path" criterion offers a precise graphical method to identify a sufficient set of variables to control for, thereby deconfounding the relationship between X and Y. This approach replaces ambiguous statistical tests with a straightforward graphical algorithm, turning a complex problem into a solvable one that can be treated like a game.

## Relationships

- **has_flawed_definition**: [[noncollapsibility|Noncollapsibility]]
- **is_defined_by**: [[exchangeability|Exchangeability]]
- **is_addressed_by**: [[back-door-path|Back Door Path]]
- **addressed_by**: [[back-door-criterion|Back Door Criterion]]
- **is_a_solution_for**: [[backdoor-criterion|Backdoor Criterion]]
- **is_a_problem_in**: [[observational-studies|Observational Studies]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*