---
type: concept
aliases: [Forward Chaining]
summary: A data-driven inference algorithm that works forward from known facts in a knowledge base of definite clauses to derive new conclusions until the query is proven. An inference algorithm that starts with known facts in a knowledge base and applies rules in the forward direction to derive new facts until no more inferences can be made. An inference algorithm that works forward from known facts in a knowledge base to derive new facts until the goal is reached or no new inferences can be made. A data-driven inference method that starts with known facts and applies inference rules to derive new facts until a goal is reached.
relationships:
  - target: backward-chaining
    type: related-to
  - target: and-or-graph
    type: can-be-visualized-by
  - target: backward-chaining
    type: alternative_to
  - target: unification
    type: uses
  - target: rete-algorithm
    type: improved_by
  - target: generalized-modus-ponens
    type: uses
  - target: deductive-databases
    type: used_in
  - target: production-systems
    type: used_in
  - target: datalog
    type: is_complete_for
  - target: first-order-logic
    type: is_a_method_in
  - target: backward-chaining
    type: is_distinct_from
tags: [inference-algorithm, logical-reasoning, horn-clauses, inference, first-order-logic, algorithm, data-driven-reasoning, logic, data-driven, reasoning, expert-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Forward Chaining

## Definition

Forward chaining is an algorithm, formally named PL-FC-ENTAILS?, designed to determine if a single proposition symbol, known as the query, is entailed by a knowledge base composed of definite clauses.

## How It Works

The algorithm operates in a data-driven manner, starting from the known facts (positive literals) present in the knowledge base. It repeatedly applies modus ponens: if all the premises of an implication are found to be in the set of known facts, its conclusion is added to the set. This inferential process continues until the query itself is added to the set of known facts, or until no new inferences can be made.

## Properties and Performance

Forward chaining can be visualized as propagating inferences upward through an AND-OR graph representation of the knowledge base. It is noted that humans use a controlled form of this reasoning to avoid being overwhelmed by irrelevant consequences. For definite clauses, the algorithm is highly efficient, running in time that is linear in the size of the knowledge base.

## Relationships

- **related-to**: [[backward-chaining|Backward Chaining]]
- **can-be-visualized-by**: [[and-or-graph|And Or Graph]]
- **alternative_to**: [[backward-chaining|Backward Chaining]]
- **uses**: [[unification|Unification]]
- **improved_by**: [[rete-algorithm|Rete Algorithm]]
- **uses**: [[generalized-modus-ponens|Generalized Modus Ponens]]
- **used_in**: [[deductive-databases|Deductive Databases]]
- **used_in**: [[production-systems|Production Systems]]
- **is_complete_for**: [[datalog|Datalog]]
- **is_a_method_in**: [[first-order-logic|First Order Logic]]
- **is_distinct_from**: [[backward-chaining|Backward Chaining]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*