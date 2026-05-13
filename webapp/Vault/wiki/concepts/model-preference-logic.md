---
type: concept
aliases: [Model Preference Logic]
summary: A class of non-monotonic logics where a sentence is considered entailed if it is true in all "preferred" models of a knowledge base, rather than in all possible models.
tags: [non-monotonic-reasoning, logic, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Model Preference Logic

## Definition

In a model preference logic, a sentence is entailed with a default status if it holds true across a specific subset of models known as preferred models. This contrasts with classical logic, which requires a sentence to be true in all possible models of the knowledge base to be entailed.

## Preference Criterion

The logic defines a method for preferring one model over another. The specific criterion for preference distinguishes different types of model preference logics. This allows for reasoning with default information where conclusions can be drawn in the absence of complete information.

## Example Formalism: Circumscription

Circumscription is a prominent example of a model preference logic. In circumscription, the preference criterion is based on minimizing abnormality; a model is preferred if it contains fewer abnormal objects than another.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*