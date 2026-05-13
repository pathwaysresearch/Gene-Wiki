---
type: concept
aliases: [FOIL (First-Order Inductive Learner)]
summary: A top-down ILP algorithm that learns Horn clauses by starting with a general rule and iteratively specializing it by adding literals that best improve classification accuracy.
relationships:
  - target: inductive-logic-programming
    type: is-a-method-in
tags: [ilp, machine-learning-algorithm, rule-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# FOIL (First-Order Inductive Learner)

## Overview
FOIL (First-Order Inductive Learner) is an Inductive Logic Programming algorithm that learns a set of Horn clauses that imply a target predicate. It operates by performing a top-down, general-to-specific search, starting with a clause that classifies every example as positive and progressively specializing it to correctly classify the examples.

## How It Works
The specialization process in FOIL involves adding literals one at a time to the left-hand side of the current clause. To decide which literal to add, the `CHOOSE-LITERAL` function uses a heuristic somewhat similar to information gain to select the literal that best discriminates between positive and negative examples. For instance, when learning the `Grandfather(x,y)` predicate, it might add `Father(x,z)` and then `Parent(z,y)` to arrive at a correct definition, preferring these over less informative literals.

## Avoiding Overfitting
FOIL incorporates a mechanism based on Ockham's razor to prevent the creation of overly complex clauses that might fit noise in the data. A clause is discarded if its length, according to some metric, becomes greater than the total length of the positive examples it explains. This technique helps ensure the learned hypotheses are general and robust. FOIL has been used to learn a wide variety of definitions, including a long sequence of list-processing functions from a Prolog textbook.

## Relationships

- **is-a-method-in**: [[inductive-logic-programming|Inductive Logic Programming]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*