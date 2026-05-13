---
type: concept
aliases: [Bayes's Rule]
summary: A mathematical formula that provides a solution to the inverse probability problem, allowing one to update beliefs about a hypothesis in light of new evidence. A mathematical rule for updating the probability of a hypothesis based on new evidence, often described as a formalization of the scientific method.
relationships:
  - target: thomas-bayes
    type: created_by
  - target: inverse-probability
    type: solves
  - target: bayesian-networks
    type: is_foundation_for
tags: [probability-theory, statistics, belief-updating, scientific-method, inference]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Bayes's Rule

## Definition and Derivation
Bayes's rule is an equation derived from the definition of conditional probability, stating that P(S|T)P(T) = P(T|S)P(S). This allows for the calculation of an "inverse probability," P(T|S), if the "forward probability," P(S|T), and the base probabilities P(S) and P(T) are known.

## Role in Inverse Probability
The rule's primary role in statistics is to solve the inverse-probability problem: inferring the probability of a cause (or hypothesis) given an effect (or evidence). It allows one to use reliable judgments about forward probabilities (e.g., the probability of a symptom given a disease) to mathematically derive the less intuitive inverse probabilities (e.g., the probability of a disease given a symptom).

## Epistemological Significance
Beyond its mathematical utility, Bayes's rule acts as a normative rule for updating beliefs in response to evidence. It formalizes the idea that the more surprising a piece of evidence is (i.e., the smaller its prior probability), the more it should increase our belief in a hypothesis that explains it. This was seen by Bayes and his contemporaries as a powerful counterargument to philosophical skepticism about inferring causes from effects, such as David Hume's critique of miracles.

## Relationships

- **created_by**: [[thomas-bayes|Thomas Bayes]]
- **solves**: [[inverse-probability|Inverse Probability]]
- **is_foundation_for**: [[bayesian-networks|Bayesian Networks]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*