---
type: concept
aliases: [Probability Theory]
summary: A fundamental mathematical framework used in science and engineering to represent and reason in the presence of uncertainty.
relationships:
  - target: information-theory
    type: is_related_to
  - target: frequentist-probability
    type: has_interpretation
  - target: bayesian-probability
    type: has_interpretation
tags: [probability, statistics, machine-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Probability Theory

## Role in Machine Learning
Probability theory is a fundamental tool for machine learning because many aspects of the field deal with uncertain quantities rather than the deterministic entities common in other areas of computer science. It provides a formal means of representing and reasoning about uncertainty.

## Interpretations of Probability
There are two primary ways to interpret probability. The frequentist view relates probability to the long-run frequency of repeatable events. The Bayesian view uses probability to represent a "degree of belief" in a proposition, which is useful for non-repeatable events like a medical diagnosis.

## Relationship to Information Theory
While probability theory allows for making uncertain statements, the related field of information theory provides the tools to quantify the amount of uncertainty present in a probability distribution.

## Relationships

- **is_related_to**: [[information-theory|Information Theory]]
- **has_interpretation**: [[frequentist-probability|Frequentist Probability]]
- **has_interpretation**: [[bayesian-probability|Bayesian Probability]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*