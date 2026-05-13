---
type: concept
aliases: [Unique-Names Assumption]
summary: The convention in some knowledge systems that distinct constant symbols refer to distinct objects in the world.
relationships:
  - target: closed-world-assumption
    type: related-to
  - target: domain-closure-assumption
    type: related-to
  - target: first-order-logic
    type: is-an-assumption-for
tags: [knowledge-representation, logic, database-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Unique-Names Assumption

## Definition
The Unique-Names Assumption (UNA) is a simplifying convention used in some logical systems, particularly databases. It mandates that every constant symbol in the knowledge base refers to a unique and distinct object. This avoids the need to explicitly state that different names refer to different things.

## Motivation
The text illustrates the motivation for UNA with an example. To state that Richard has two brothers, John and Geoffrey, in standard first-order logic, one must write `Brother(John, Richard) ∧ Brother(Geoffrey, Richard)` and also explicitly add the assertion `John ≠ Geoffrey`. Under the Unique-Names Assumption, the inequality is automatically assumed because the names "John" and "Geoffrey" are different, making the logical expression more concise.

## Context
UNA is presented as part of a proposal for an "alternative semantics" to standard first-order logic, which is very popular in database systems. It is typically used in conjunction with the Closed-World Assumption and Domain Closure to create a more constrained and intuitive reasoning environment.

## Relationships

- **related-to**: [[closed-world-assumption|Closed World Assumption]]
- **related-to**: [[domain-closure-assumption|Domain Closure Assumption]]
- **is-an-assumption-for**: [[first-order-logic|First Order Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*