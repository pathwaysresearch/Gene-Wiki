---
type: concept
aliases: [Version Space]
summary: A concept in machine learning representing the set of all hypotheses that are consistent with the observed training examples, typically represented by its most general and most specific boundaries.
relationships:
  - target: meta-dendral
    type: was-applied-in
tags: [machine-learning, concept-learning, supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Version Space

## Definition
The version space is the set of all hypotheses from a given hypothesis space that are consistent with all the training examples observed so far. It represents the subset of hypotheses that are still viable candidates for the true concept.

## Representation
Instead of enumerating all consistent hypotheses, which can be enormous, the version space is compactly represented by two boundary sets. The first is the most specific boundary, called the S-set, which contains every consistent hypothesis for which there is no more specific consistent hypothesis. The second is the most general boundary, called the G-set, which contains every consistent hypothesis for which there is no more general consistent hypothesis. Everything in between these two boundaries is guaranteed to be consistent with the examples.

## Drawbacks
The version-space approach has several principal drawbacks. If the training data contains noise or the available attributes are insufficient for exact classification, the version space will eventually collapse to an empty set, indicating no hypothesis is consistent. Additionally, if the hypothesis space allows for unlimited disjunction, the S-set and G-set can become trivial representations of the positive and negative examples, respectively. For some hypothesis spaces, the number of hypotheses in the boundary sets can also grow exponentially with the number of attributes.

## Relationships

- **was-applied-in**: [[meta-dendral|Meta Dendral]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*