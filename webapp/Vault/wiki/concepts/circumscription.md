---
type: concept
aliases: [Circumscription]
summary: A non-monotonic reasoning formalism that formalizes the common-sense assumption that things are as expected unless specified otherwise, by minimizing the extent of "abnormal" predicates.
relationships:
  - target: model-preference-logic
    type: is-a-type-of
tags: [non-monotonic-reasoning, logic, default-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Circumscription

## As a Model Preference Logic

Circumscription is a form of model preference logic where preference between models is determined by the number of abnormal objects they contain. A model with fewer abnormal objects is preferred over one with more, formalizing the idea of assuming normality.

## Resolving Ambiguity

This logic can be used to handle ambiguous situations like the "Nixon diamond" problem, where an individual belongs to two groups with conflicting default properties. By circumscribing the abnormality predicates, the logic produces two preferred models—one where Nixon is a pacifist and one where he is not—and thus remains correctly agnostic without more information.

## Prioritized Circumscription

An extension called prioritized circumscription allows for a more nuanced approach by specifying that some abnormalities are "worse" than others. This allows the system to enforce precedence, such as asserting that religious beliefs take precedence over political ones, by giving preference to models that minimize the higher-priority abnormality.

## Relationships

- **is-a-type-of**: [[model-preference-logic|Model Preference Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*