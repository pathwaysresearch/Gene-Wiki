---
type: concept
aliases: [Closed-World Assumption]
summary: The formal assumption that any statement that cannot be proven to be true from the knowledge base is considered false.
relationships:
  - target: unique-names-assumption
    type: related-to
  - target: domain-closure-assumption
    type: related-to
  - target: first-order-logic
    type: is-an-assumption-for
tags: [knowledge-representation, logic, database-theory, non-monotonic-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Closed-World Assumption

## Definition
The Closed-World Assumption (CWA) is a principle used in some knowledge representation systems to handle incomplete information. It presumes that the knowledge base contains all relevant true facts, and therefore any fact not explicitly stated or derivable is false.

## Motivation
Standard first-order logic requires explicit statements to rule out possibilities. For example, to state that John and Geoffrey are Richard's *only* brothers, one must add a complex axiom: `∀x Brother(x, Richard) ⇒ (x=John ∨ x=Geoffrey)`. The Closed-World Assumption provides a semantic shortcut, allowing a system to infer that no other brothers exist because they are not mentioned. This makes knowledge representation more concise and aligns with the typical behavior of database systems.

## Context
The text introduces CWA as a key component of an "alternative semantics" popular in database systems. It is presented alongside the Unique-Names Assumption and Domain Closure as a set of conventions that allow for more straightforward logical expressions than are possible in standard, open-world first-order logic.

## Relationships

- **related-to**: [[unique-names-assumption|Unique Names Assumption]]
- **related-to**: [[domain-closure-assumption|Domain Closure Assumption]]
- **is-an-assumption-for**: [[first-order-logic|First Order Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*