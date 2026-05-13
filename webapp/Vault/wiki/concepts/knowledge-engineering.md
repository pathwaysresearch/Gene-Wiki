---
type: concept
aliases: [Knowledge Engineering]
summary: The process of building a knowledge base by translating human expertise about a domain into a formal, machine-readable representation.
relationships:
  - target: ontology-in-knowledge-representation
    type: produces
  - target: axiom
    type: uses
  - target: first-order-logic
    type: uses
tags: [knowledge-representation, expert-systems, artificial-intelligence]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Knowledge Engineering

## Overview
Knowledge engineering is the methodology for constructing a knowledge base for an AI system. It involves a series of steps to translate domain-level concepts and general knowledge into a formal language like first-order logic, which a reasoning system can then use to solve problems.

## The Process
The text outlines a five-step process for knowledge engineering:
1. **Identify the task**: Determine the goals and scope of the knowledge-based system.
2. **Assemble the relevant knowledge**: Gather the necessary information about the domain, often from human experts.
3. **Decide on a vocabulary**: Create an ontology by choosing the predicates, functions, and constants to represent the domain's concepts.
4. **Encode general knowledge**: Write axioms for the vocabulary terms to define their meanings and relationships.
5. **Encode the specific problem instance**: Add simple atomic sentences that describe the particular problem to be solved.

## Iterative Nature
The process is not strictly linear but is often iterative. The text notes that the step of encoding general knowledge (writing axioms) frequently reveals misconceptions or gaps in the vocabulary. This discovery forces the knowledge engineer to return to the previous step and refine the ontology. This iterative cycle of defining, encoding, and refining is central to building a robust and accurate knowledge base.

## Relationships

- **produces**: [[ontology-in-knowledge-representation|Ontology In Knowledge Representation]]
- **uses**: [[axiom|Axiom]]
- **uses**: [[first-order-logic|First Order Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*