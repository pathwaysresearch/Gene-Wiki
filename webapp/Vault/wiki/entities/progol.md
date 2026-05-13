---
type: entity
aliases: [PROGOL]
summary: An influential Inductive Logic Programming (ILP) system known for its successes in scientific discovery, particularly in the field of molecular biology.
relationships:
  - target: inductive-logic-programming
    type: is-an-implementation-of
tags: [ilp-system, prolog, scientific-discovery]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# PROGOL

## Overview
PROGOL is an Inductive Logic Programming (ILP) system developed by Stephen Muggleton. It is notable for its application of ILP techniques to complex, real-world scientific problems, moving beyond toy examples to generate new scientific knowledge.

## Technical Approach
Unlike some ILP systems that rely on full theorem proving, PROGOL uses a form of model checking to limit its search for hypotheses. This is part of a bottom-up approach related to inverse entailment, which can make the search for valid hypotheses more efficient than purely top-down or exhaustive methods.

## Scientific Contributions
PROGOL has been successfully used to make discoveries that were deemed publishable in the scientific literature. A key example cited is its automated discovery of rules for protein folding, published in the *Journal of Molecular Biology*. The system learned rules, such as one for the "four-helical up-and-down bundle" concept, from logical descriptions of protein structures. Many of these rules, while derivable from known principles, had not been previously published as part of a standard biological database.

## Relationships

- **is-an-implementation-of**: [[inductive-logic-programming|Inductive Logic Programming]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*