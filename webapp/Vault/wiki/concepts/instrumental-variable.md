---
type: concept
aliases: [Instrumental Variable]
summary: A variable used in causal inference to estimate the causal effect of a variable X on an outcome Y when their relationship is confounded, by leveraging a third variable Z that influences X but not Y directly.
relationships:
  - target: john-snow
    type: used_by
  - target: philip-wright
    type: used_by
  - target: mendelian-randomization
    type: is_a_foundational_method_for
tags: [causal-inference, statistics, econometrics]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Instrumental Variable

## Definition
An instrumental variable is a variable used in observational studies to estimate a causal effect when controlled experiments are not feasible. It serves as a proxy for a randomized experiment. The text describes it as a variable that satisfies three key properties, allowing researchers to isolate a causal relationship from the influence of confounding factors.

## Key Properties
According to the text, for a variable Z to be a valid instrument for the effect of X on Y, it must satisfy three conditions. First, the instrument Z must be independent of any confounding variables that affect both X and Y. Second, there must be no direct causal path from Z to Y; any effect of Z on Y must be mediated entirely through X. Third, there must be a strong association between the instrument Z and the variable X whose effect is being studied.

## Historical and Modern Applications
The text provides several examples of its application. Dr. John Snow's use of 'Water Company' as an instrument to determine the effect of 'Water Purity' on 'Cholera' is presented as a pioneering case. Economist Philip Wright used 'Yield per Acre' as an instrument to disentangle the effects of supply and price for flaxseed oil. In modern contexts, the random assignment to a drug in a clinical trial (Z) can serve as an instrument for actually taking the drug (X) to measure its effect on a health outcome (Y). Mendelian randomization is another key application where a genetic variant serves as the instrument.

## Relationships

- **used_by**: [[john-snow|John Snow]]
- **used_by**: [[philip-wright|Philip Wright]]
- **is_a_foundational_method_for**: [[mendelian-randomization|Mendelian Randomization]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*