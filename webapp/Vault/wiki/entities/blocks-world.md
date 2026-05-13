---
type: entity
aliases: [Blocks World]
summary: A famous and canonical planning domain in artificial intelligence involving a robot arm stacking blocks on a table.
relationships:
  - target: pddl
    type: can_be_described_by
  - target: classical-planning
    type: is_example_domain_for
tags: [planning, benchmark-problem, toy-problem]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Blocks World

## Overview
The blocks world is one of the most famous planning domains in artificial intelligence research. It provides a simplified, well-defined environment for developing and testing planning algorithms.

## Domain Description
The domain consists of a set of cube-shaped blocks on a table and a robot arm. The blocks can be stacked, but only one block can be directly on top of another. The robot arm can pick up only one block at a time, and only if that block is clear (has nothing on it).

## Actions and Goals
Actions in the blocks world involve the robot arm moving a block from one position (e.g., the table or another block) to a new position. The goals are typically specified as a desired configuration of stacked blocks, such as building a specific tower. The text provides a PDDL formulation for a problem of building a three-block tower.

## Relationships

- **can_be_described_by**: [[pddl|Pddl]]
- **is_example_domain_for**: [[classical-planning|Classical Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*