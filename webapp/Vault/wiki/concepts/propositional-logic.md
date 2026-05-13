---
type: concept
aliases: [Propositional Logic]
summary: A formal logical system that represents propositions as atomic symbols and combines them using logical connectives to form complex sentences. A formal system of logic where formulas represent propositions that can be either true or false, and complex formulas are built using logical connectives.
relationships:
  - target: semantics-in-logic
    type: has
  - target: truth-table
    type: uses
  - target: resolution-inference-rule
    type: is-an-inference-rule-for
  - target: model-checking
    type: is-an-inference-method-for
  - target: george-boole
    type: developed_by
  - target: gottlob-frege
    type: developed_by
  - target: satplan
    type: is_used_by
tags: [logic, knowledge-representation, reasoning, formal-language]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Propositional Logic

## Syntax
The syntax of propositional logic defines what constitutes a valid sentence. It begins with atomic sentences, which are single proposition symbols (e.g., P, Q, W₁,₃) that represent propositions that can be true or false. Complex sentences are built from these atomic sentences using five logical connectives: ¬ (negation), ∧ (conjunction/and), ∨ (disjunction/or), ⇒ (implication), and ⇔ (biconditional).

## Semantics
The semantics of propositional logic are defined by truth tables, which specify the truth value of a complex sentence for every possible combination of truth values of its constituent parts. For example, P ∧ Q is true if and only if both P and Q are true. A model in propositional logic is a specific assignment of true or false to every proposition symbol.

## Inference
Inference in propositional logic aims to determine if a knowledge base entails another sentence. Algorithms for this task include model checking (like `TT-ENTAILS?`), which enumerates all possible models, and proof-based methods like resolution. While sound and complete algorithms exist, the problem of propositional entailment is co-NP-complete, meaning all known algorithms have worst-case exponential time complexity.

## Relationships

- **has**: [[semantics-in-logic|Semantics In Logic]]
- **uses**: [[truth-table|Truth Table]]
- **is-an-inference-rule-for**: [[resolution-inference-rule|Resolution Inference Rule]]
- **is-an-inference-method-for**: [[model-checking|Model Checking]]
- **developed_by**: [[george-boole|George Boole]]
- **developed_by**: [[gottlob-frege|Gottlob Frege]]
- **is_used_by**: [[satplan|Satplan]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*