---
type: entity
aliases: [SATPLAN]
summary: A planning approach that solves planning problems by translating them into a Boolean satisfiability (SAT) problem and using a SAT solver.
relationships:
  - target: planning-as-constraint-satisfaction
    type: related-to
tags: [planning-algorithm, satisfiability, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# SATPLAN

## Overview
SATPLAN is an approach to planning that transforms a bounded planning problem into a Boolean satisfiability (SAT) problem. The resulting logical formula is then passed to a standard SAT solver to find a satisfying assignment, which corresponds to a valid plan.

## Translation Process
The translation to a SAT problem requires several types of axioms. Successor-state axioms are added for each fluent to define how its truth value changes over time. Precondition axioms are added for each ground action, stating that if an action is taken, its preconditions must have been true. Finally, action exclusion axioms are needed to assert that every action is distinct from every other action at a given time step.

## Performance Characteristics
Comparative analyses show that constraint-based approaches like SATPLAN and GRAPHPLAN are particularly effective for NP-hard planning domains. A significant challenge for these methods arises in domains with many objects, as this leads to the creation of a very large number of propositionalized actions, potentially harming performance.

## Relationships

- **related-to**: [[planning-as-constraint-satisfaction|Planning As Constraint Satisfaction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*