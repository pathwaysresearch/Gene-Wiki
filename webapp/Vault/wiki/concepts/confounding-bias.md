---
type: concept
aliases: [Confounding Bias]
summary: A systematic error in causal inference that occurs when a third variable, a confounder, is associated with both the exposure and the outcome, creating a spurious or distorted association between them.
relationships:
  - target: randomization
    type: eliminated-by
  - target: causal-network
    type: identified-by
  - target: randomized-controlled-trial
    type: addressed-by
tags: [statistics, bias, observational-study, causal-inference]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Confounding Bias

## Definition
Confounding bias is a major challenge in observational studies where the experimenter does not control the assignment of treatment. It arises when a variable, known as a confounder, influences both the variable being studied (the cause) and the outcome. This shared cause creates an association between the two variables of interest that is not causal.

## Example and Identification
An example from the Honolulu Heart Program illustrates this concept. Researchers observed that men who walked more had lower mortality rates. However, age could be a confounder: younger men might walk more and also have a lower risk of dying. In a causal diagram, this is represented by a fork structure where Age is a common cause of both Walking and Mortality (Age → Walking, Age → Mortality). This structure creates a non-causal association between walking and mortality that must be accounted for.

## Addressing Confounding
The traditional statistical approach to confounding is to "adjust" or "control for" potential confounding variables. However, this practice has been fraught with confusion, leading to "overcontrolling"—adjusting for too many variables or for variables that should not be controlled for, which can introduce new biases. The most robust method for eliminating confounding bias is randomization, which severs the link between any potential confounder and the treatment variable.

## Relationships

- **eliminated-by**: [[randomization|Randomization]]
- **identified-by**: [[causal-network|Causal Network]]
- **addressed-by**: [[randomized-controlled-trial|Randomized Controlled Trial]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*