---
type: concept
aliases: [Ontology (in Knowledge Representation)]
summary: A formal specification of the vocabulary for a domain, defining the types of objects, properties, and interrelationships that are presumed to exist.
relationships:
  - target: knowledge-engineering
    type: is-a-component-of
  - target: first-order-logic
    type: is-expressed-in
  - target: axiom
    type: is-defined-by
tags: [knowledge-representation, knowledge-engineering, semantics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Ontology (in Knowledge Representation)

## Definition
In the context of knowledge engineering, an ontology is the vocabulary of predicates, functions, and constants used to represent a domain. The text defines it as "a particular theory of the nature of being or existence." The ontology establishes what kinds of things exist in the domain but does not specify their particular properties or relationships, which are instead defined by axioms.

## Role in Knowledge Engineering
Creating the ontology is a critical step in the knowledge engineering process. It involves translating important domain-level concepts into logic-level names. This choice of representation, described as a form of "knowledge-engineering style," can significantly impact the success of the project. The process is often iterative, as attempts to encode general knowledge (writing axioms) may reveal gaps or misconceptions in the ontology, requiring it to be revised.

## Purpose-Driven Design
The text emphasizes that an ontology is not a universal model of a domain but is designed for a specific purpose. Using the example of digital circuits, it explains that for verifying logical functionality, the ontology would include gates and terminals but exclude wires, costs, or colors as irrelevant. However, if the purpose were to debug faulty circuits, the wires would need to be included. Similarly, for resolving timing faults, gate delays would be essential, and for assessing profitability, the cost would be a key component of the ontology.

## Relationships

- **is-a-component-of**: [[knowledge-engineering|Knowledge Engineering]]
- **is-expressed-in**: [[first-order-logic|First Order Logic]]
- **is-defined-by**: [[axiom|Axiom]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*