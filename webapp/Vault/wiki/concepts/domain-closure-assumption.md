---
type: concept
aliases: [Domain Closure Assumption]
summary: The assumption that the only objects that exist in the domain are those that can be named by the constant symbols in the knowledge base.
relationships:
  - target: unique-names-assumption
    type: related-to
  - target: closed-world-assumption
    type: related-to
  - target: first-order-logic
    type: is-an-assumption-for
tags: [knowledge-representation, logic, database-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Domain Closure Assumption

## Definition
The Domain Closure Assumption is a principle that constrains the universe of discourse in a logical system. It asserts that the set of objects in the domain is limited to only those entities that are explicitly named by constant symbols within the knowledge base.

## Motivation
This assumption addresses a key aspect of standard first-order logic, where models can contain an infinite number of unnamed objects. By assuming domain closure, the system can reason as if the known objects are the only objects that exist. This is crucial for tasks like confirming that Richard has *only* two brothers, as it prevents a model where an unnamed, unknown third brother exists. It simplifies reasoning by restricting the domain to a finite, known set of individuals.

## Context
Domain Closure is presented as part of a trio of assumptions, along with the Unique-Names and Closed-World assumptions, that form an "alternative semantics" to first-order logic. This semantic framework is particularly popular in database systems, where the set of entities is typically assumed to be finite and completely known.

## Relationships

- **related-to**: [[unique-names-assumption|Unique Names Assumption]]
- **related-to**: [[closed-world-assumption|Closed World Assumption]]
- **is-an-assumption-for**: [[first-order-logic|First Order Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*