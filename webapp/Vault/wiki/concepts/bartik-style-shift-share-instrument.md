---
type: concept
aliases: [Bartik-Style Shift-Share Instrument]
summary: An econometric instrument used to estimate the causal impact of local shocks, constructed by interacting national or industry-level changes (shifts) with initial local exposures (shares).
relationships:
  - target: augmentation-innovations
    type: used_to_measure
  - target: automation-innovations
    type: used_to_measure
tags: [econometrics, instrumental-variables, causal-inference]
sourced_from: Acss Newfrontiers 20220814
---

# Bartik-Style Shift-Share Instrument

## Definition
A Bartik-style shift-share instrument is an econometric tool used in two-stage least squares (2SLS) regressions to identify causal effects. It is constructed as the product of quasi-exogenous, aggregate-level changes (the “shifts”) and fixed, initial local-level exposures to those changes (the “shares”). This construction helps to isolate exogenous variation in the treatment variable.

## Application in the Study
In this analysis, Bartik-style measures, denoted as π_{j,t}^{aug} and π_{j,t}^{aut}, are used as instruments for augmentation and automation patent exposures (AugX_{j,t} and AutX_{j,t}). The instruments are created from the product of class-level patent flows (shifts) and initial class exposures (shares) for each occupation or occupation-industry cell. The inverse hyperbolic sine (IHS) transformation is applied to these instruments to match the units of the endogenous variables.

## Methodological Considerations
The study follows the recommendations of Borusyak et al. (2021) for implementing this instrumental variable strategy. This involves controlling for the “share” main effects directly in the 2SLS regressions while using the full shift-share product as the instrument. This approach provides a more rigorous framework for causal inference using this type of measure.

## Relationships

- **used_to_measure**: [[augmentation-innovations|Augmentation Innovations]]
- **used_to_measure**: [[automation-innovations|Automation Innovations]]

---
*Extracted from: Acss Newfrontiers 20220814*