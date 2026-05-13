---
type: concept
aliases: [Procedural Attachment]
summary: A technique used in knowledge representation systems, particularly semantic networks, to link a relation to a specialized procedure that is executed upon query or assertion.
relationships:
  - target: semantic-networks
    type: extension-of
tags: [knowledge-representation, inference, semantic-networks]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Procedural Attachment

## Definition
Procedural attachment is a technique where a query about, or an assertion of, a particular relation results in a call to a special, custom-written procedure designed for that relation, rather than being handled by a general-purpose inference algorithm.

## Purpose in Semantic Networks
This technique is used to extend the capabilities of knowledge representation formalisms like semantic networks. When the declarative language of the network is not expressive enough to represent certain concepts or perform certain inferences (e.g., it lacks negation, disjunction, or complex numerical reasoning), procedural attachment provides a practical way to fill these gaps.

## Advantages and Transparency
A key advantage of this approach is that it can make inference processes more transparent and predictable for the system designer. By attaching specific code to specific relations, a designer can have a good idea of what queries will be efficient and can easily visualize the steps the system will take, in contrast to the sometimes opaque behavior of a general theorem prover.

## Relationships

- **extension-of**: [[semantic-networks|Semantic Networks]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*