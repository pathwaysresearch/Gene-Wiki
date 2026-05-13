---
type: concept
aliases: [Independence of Random Variables]
summary: A property of two random variables where their joint probability distribution can be expressed as the product of their individual marginal distributions.
relationships:
  - target: conditional-independence
    type: is_distinct_from
tags: [probability, random-variables]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Independence of Random Variables

## Definition
Two random variables, x and y, are defined as independent if their probability distribution can be expressed as a product of two separate factors: one that involves only x and another that involves only y.

## Mathematical Formulation
The condition for independence is that for all values of x and y, the joint probability p(x, y) equals the product of the individual probabilities p(x)p(y). This relationship is denoted with the compact notation x ⊥ y.

## Distinction from Conditional Independence
Independence is a distinct concept from conditional independence. While independent variables have a factorizable joint distribution, conditionally independent variables have a conditional distribution that factorizes only when given the value of a third variable.

## Relationships

- **is_distinct_from**: [[conditional-independence|Conditional Independence]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*