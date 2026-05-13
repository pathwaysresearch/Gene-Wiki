---
type: concept
aliases: [Backward Chaining]
summary: A goal-directed inference algorithm that works backward from a query, attempting to prove it by finding implications that conclude the query and then recursively proving their premises. A goal-directed inference algorithm that works backward from a query, chaining through rules to find known facts that support the proof. A goal-driven inference algorithm that works backward from a query to find facts in the knowledge base that support it.
relationships:
  - target: forward-chaining
    type: related-to
  - target: and-or-graph
    type: can-be-visualized-by
  - target: forward-chaining
    type: alternative_to
  - target: logic-programming
    type: used_in
  - target: unification
    type: uses
  - target: generalized-modus-ponens
    type: uses
  - target: logic-programming-systems
    type: used_in
  - target: prolog
    type: is_basis_for
  - target: planner
    type: first_appeared_in
tags: [inference-algorithm, logical-reasoning, goal-directed-reasoning, inference, first-order-logic, algorithm, logic, goal-driven]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Backward Chaining

## Definition

Backward chaining is an inference algorithm that, as its name suggests, works backward from a given query. It is characterized as a form of goal-directed reasoning.

## How It Works

The process begins with the query. If the query is not already established as a known fact, the algorithm searches the knowledge base for implications that have the query as their conclusion. It then takes the premises of one such implication and attempts to prove each of them by recursively applying the backward-chaining algorithm. This continues until it grounds the proof in a set of known facts.

## Properties and Applications

The algorithm is described as being essentially identical to the AND-OR-GRAPH-SEARCH algorithm. Like forward chaining, an efficient implementation runs in linear time. It is particularly useful for answering specific questions, such as "What shall I do now?" or "Where are my keys?".

## Relationships

- **related-to**: [[forward-chaining|Forward Chaining]]
- **can-be-visualized-by**: [[and-or-graph|And Or Graph]]
- **alternative_to**: [[forward-chaining|Forward Chaining]]
- **used_in**: [[logic-programming|Logic Programming]]
- **uses**: [[unification|Unification]]
- **uses**: [[generalized-modus-ponens|Generalized Modus Ponens]]
- **used_in**: [[logic-programming-systems|Logic Programming Systems]]
- **is_basis_for**: [[prolog|Prolog]]
- **first_appeared_in**: [[planner|Planner]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*