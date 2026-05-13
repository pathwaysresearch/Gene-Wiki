---
type: concept
aliases: [Inductive Logic Programming (ILP)]
summary: A subfield of artificial intelligence that uses logic programming as a uniform representation for examples, background knowledge, and hypotheses to facilitate knowledge-based inductive learning. A field of machine learning that uses logic programming as a uniform representation for examples, background knowledge, and hypotheses, enabling the learning of relational concepts that are difficult for attribute-based methods.
relationships:
  - target: knowledge-based-inductive-learning
    type: studies
  - target: foil
    type: has-method
  - target: inverse-resolution
    type: has-method
  - target: progol
    type: implemented-by
tags: [machine-learning, logic-programming, subfield, symbolic-ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Inductive Logic Programming (ILP)

## Overview
Inductive Logic Programming (ILP) is a field of study focused on learning algorithms that incorporate prior knowledge, specifically Knowledge-Based Inductive Learning (KBIL) algorithms. It provides a formal framework where background knowledge, examples, and hypotheses are all represented within the language of logic programming.

## The Role of Prior Knowledge
In ILP systems, prior knowledge serves two key functions that reduce the complexity of the learning task. First, any hypothesis generated must be consistent not only with new observations but also with the existing knowledge base, which effectively reduces the size of the search space for valid hypotheses. Second, the background knowledge provides a richer vocabulary and pre-existing predicates that can be used to construct simpler and more meaningful hypotheses.

## Relationship to KBIL
ILP is the primary domain for the development and study of KBIL algorithms. It provides the theoretical and practical tools for implementing systems that satisfy the KBIL entailment constraint, where the goal is to find hypotheses that, in conjunction with background knowledge, can explain observed data.

## Relationships

- **studies**: [[knowledge-based-inductive-learning|Knowledge Based Inductive Learning]]
- **has-method**: [[foil|Foil]]
- **has-method**: [[inverse-resolution|Inverse Resolution]]
- **implemented-by**: [[progol|Progol]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*