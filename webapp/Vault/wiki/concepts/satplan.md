---
type: concept
aliases: [SATPLAN]
summary: A planning algorithm that finds a sequence of actions to achieve a goal by encoding the problem as a propositional satisfiability problem and finding a satisfying model.
relationships:
  - target: propositional-logic
    type: uses
  - target: chaff-solver
    type: can_use
tags: [planning, satisfiability, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# SATPLAN

## Overview
SATPLAN is an approach to automated planning that transforms a planning problem into a propositional satisfiability (SAT) problem. The general approach was proposed by Kautz and Selman in 1992. A SAT solver is then used to find a satisfying assignment for the propositional formula, which corresponds to a valid plan to achieve the goal.

## How It Works
The key step in using SATPLAN is the construction of a knowledge base that encodes the initial state of the world, the goal conditions, and the effects of all possible actions at different time steps. A SAT solver then searches for a model—a consistent assignment of true/false values to all propositions—that makes the entire knowledge base true. This model represents a valid sequence of actions from the initial state to the goal.

## Contrast with Entailment-Based Reasoning
SATPLAN's reliance on satisfiability differs from reasoning based on entailment (ASK). In satisfiability, an unknown proposition can be assigned any value that helps satisfy the goal. This can lead to finding plans that are technically valid but nonsensical, such as an agent being in two places at once. To prevent this, the knowledge base must include explicit axioms to rule out such possibilities, making SATPLAN a useful tool for debugging a knowledge representation.

## Relationships

- **uses**: [[propositional-logic|Propositional Logic]]
- **can_use**: [[chaff-solver|Chaff Solver]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*