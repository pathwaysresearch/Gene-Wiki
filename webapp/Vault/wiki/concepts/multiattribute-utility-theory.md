---
type: concept
aliases: [Multiattribute Utility Theory]
summary: A branch of decision theory that deals with making choices involving outcomes with multiple, often conflicting, attributes.
relationships:
  - target: utility-function
    type: is-a-type-of
  - target: strict-dominance
    type: uses-principle
tags: [decision-theory, multiple-criteria-decision-making, utility-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Multiattribute Utility Theory

## Purpose
When decision outcomes are characterized by multiple attributes (e.g., cost, noise, and safety for an airport site), a utility function must be defined over a vector of attribute values, U(x_1, ..., x_n). Multiattribute utility theory (MAUT) provides a formal framework for structuring and simplifying this complex, high-dimensional utility function.

## The Problem of Scale
Without assuming any structure, specifying a complete multiattribute utility function is often intractable. If there are n attributes, each with d possible values, the utility function would require d^n values to be specified. MAUT addresses this combinatorial explosion by identifying and exploiting regularities in an agent's preference structure.

## Representation Theorems
The core approach of MAUT is to use representation theorems. These theorems connect specific types of preference structures to simplified functional forms for the utility function. For example, if an agent's preferences satisfy certain independence conditions, their multiattribute utility function can be decomposed into a simpler form (e.g., an additive or multiplicative combination of single-attribute utility functions), making it much easier to elicit and use.

## Relationships

- **is-a-type-of**: [[utility-function|Utility Function]]
- **uses-principle**: [[strict-dominance|Strict Dominance]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*