---
type: concept
aliases: [Resolution (inference rule)]
summary: A single, powerful inference rule that can produce a complete inference algorithm for propositional logic when combined with a complete search method. A complete inference rule for first-order logic that proves a sentence by refutation, i.e., by showing that the knowledge base combined with the negation of the sentence leads to a contradiction.
relationships:
  - target: inference-in-logic
    type: is-a-rule-for
  - target: conjunctive-normal-form-cnf
    type: operates-on
  - target: completeness-of-inference
    type: provides
  - target: set-of-support-strategy
    type: can-be-optimized-with
  - target: answer-literal
    type: can-be-extended-with
tags: [logic, inference, rule, automated-reasoning, inference-rule, first-order-logic, theorem-proving, proof-by-refutation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Resolution (inference rule)

## Overview
Resolution is an inference rule used in automated theorem proving. Its key advantage is that it alone can form the basis of a complete inference algorithm for propositional logic, simplifying the need for multiple different inference rules.

## How It Works
The resolution rule operates on sentences in Conjunctive Normal Form (CNF), which are conjunctions of clauses (disjunctions of literals). The basic version takes two clauses containing complementary literals (e.g., P and ¬P) and produces a new clause containing all the literals from both original clauses except for the complementary pair.

## Completeness
When coupled with any complete search algorithm, the resolution rule yields a complete inference algorithm. This means it is guaranteed to find a proof if one exists. To use resolution, sentences in the knowledge base must first be converted into CNF.

## Relationships

- **is-a-rule-for**: [[inference-in-logic|Inference In Logic]]
- **operates-on**: [[conjunctive-normal-form-cnf|Conjunctive Normal Form Cnf]]
- **provides**: [[completeness-of-inference|Completeness Of Inference]]
- **can-be-optimized-with**: [[set-of-support-strategy|Set Of Support Strategy]]
- **can-be-extended-with**: [[answer-literal|Answer Literal]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*