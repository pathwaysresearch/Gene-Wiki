---
type: concept
aliases: [Semantic Networks]
summary: A knowledge representation formalism that uses a graph of nodes (representing objects and categories) and labeled edges (representing relations) to model knowledge.
relationships:
  - target: procedural-attachment
    type: uses
tags: [knowledge-representation, graph-based-model, ontology]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Semantic Networks

## Definition and Structure
A semantic network is a graphical knowledge representation where nodes, typically shown in ovals or boxes, represent individual objects or categories, and labeled links between them represent relations. For example, a node for an individual 'Mary' can be connected to the category 'FemalePersons' via a 'MemberOf' link, corresponding to the logical assertion `Mary ∈ FemalePersons`. Similarly, a 'SisterOf' link can connect 'Mary' to 'John'.

## Historical Context and Relationship to Logic
The text places semantic networks in a historical context, noting a long-running debate between their advocates and advocates of traditional logic. It references Charles S. Peirce's 1909 'existential graphs' as an early graphical notation for logic. The text clarifies that semantic networks with well-defined semantics are ultimately a form of logic, with the primary difference being the convenience and visual nature of the notation for representing certain kinds of sentences.

## Expressive Power and Extensions
Standard semantic network notations are often less expressive than full first-order logic, lacking direct ways to represent negation, disjunction, or complex quantification. To overcome these limitations, many systems employ a technique called procedural attachment. This allows a query about a specific relation to trigger a call to a specialized procedure, effectively embedding procedural code within the declarative network to handle cases the network's logic cannot.

## Relationships

- **uses**: [[procedural-attachment|Procedural Attachment]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*