---
type: concept
aliases: [Do-operator]
summary: A mathematical notation, written as do(X), that represents an active intervention in a system, distinguishing it from passive observation (seeing).
relationships:
  - target: causal-inference
    type: is_a_tool_in
tags: [causality, mathematical-notation, intervention]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Do-operator

## Definition
The do-operator is a formal mathematical tool used in causal inference to represent an intervention. It is used to distinguish the probability of an outcome given an observation, P(L | D), from the probability of an outcome given an action, P(L | do(D)). The former represents "seeing," while the latter represents "doing."

## The "Seeing" vs. "Doing" Distinction
The fundamental purpose of the do-operator is to resolve the confusion between seeing and doing. For example, *seeing* a barometer fall increases the probability of an impending storm, which is expressed as a standard conditional probability. However, actively *intervening* to force the barometer to fall, an action represented by the do-operator, would not affect the storm's probability. Similarly, P(L | D) is the observed lifespan among patients who happened to take a drug, while P(L | do(D)) is the predicted lifespan if we were to administer the drug as a deliberate intervention.

## Significance
The introduction of the do-operator is presented as a major breakthrough, as science previously operated in a world that lacked a formal way to express interventions. Without this distinction, one could fall into paradoxes, such as believing that going to a doctor causes illness or that dismissing firefighters reduces the incidence of fires, because these events are correlated. The do-operator allows for the prediction of the effects of an intervention without actually having to perform it.

## Relationships

- **is_a_tool_in**: [[causal-inference|Causal Inference]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*