---
type: concept
aliases: [Probability of Necessity (PN)]
summary: A counterfactual measure of causation that evaluates the probability that an outcome would not have occurred in the absence of a specific cause, given that both the cause and outcome did occur.
relationships:
  - target: probability-of-sufficiency
    type: is_contrasted_with
tags: [causal-inference, counterfactuals, probability]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Probability of Necessity (PN)

## Definition

The Probability of Necessity, abbreviated as PN, is a measure of causation that quantifies the likelihood that a specific cause was necessary for a particular outcome. It is symbolically represented as $P(Y_{x=0} = 0 | X = 1, Y = 1)$, which asks for the probability that the outcome Y would have been 0 if the cause X had been 0, given that in the actual world, both X and Y were 1. It is also referred to as the "but-for" cause.

## Role in Counterfactual Reasoning

PN is a concept from the third rung of the Ladder of Causation, involving counterfactuals. It critically relies on hindsight—the knowledge that both the cause and the effect actually occurred (X=1, Y=1). This distinguishes it from rung-two interventions, such as $P(Y = 0 | do(X = 0))$, which do not incorporate this hindsight. The information gained from observing the outcome (e.g., that a fire was strong enough to be fatal) changes the probability estimate compared to knowing only about the intervention. It has been shown that PN cannot be captured using a simple do-expression.

## Application in Causal Explanation

PN helps differentiate between necessary causes by considering the normality or baseline probability of those causes. In the classic example of a house fire, both striking a match and the presence of oxygen are logically necessary. However, because striking a match is an abnormal event (low probability) while oxygen is normal (high probability), the match is considered the more reasonable explanation. PN provides a quantitative basis for this intuition. It has also been used in climate science to attribute specific weather events, like heat waves, to human influence.

## Relationships

- **is_contrasted_with**: [[probability-of-sufficiency|Probability Of Sufficiency]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*