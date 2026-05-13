---
type: concept
aliases: [Online Planning]
summary: An approach where an agent interleaves planning and execution, monitoring its progress and making repairs to the plan as unexpected situations arise.
relationships:
  - target: planex
    type: is-an-example-of
  - target: sipe
    type: is-an-example-of
tags: [planning, robotics, execution-monitoring]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Online Planning

## Definition
An online planning agent does not compute a complete plan before acting. Instead, it uses execution monitoring to track its progress and splices in repairs to its plan as needed to recover from unexpected situations.

## Handling Unexpected Events
This approach is designed to handle environments where things do not go as expected. These unexpected situations can be caused by nondeterministic actions, exogenous events (events caused by external factors), or an incorrect model of the environment.

## Historical Context
The first online planner with execution monitoring was PLANEX, which worked with the STRIPS planner. Later, the SIPE system was the first to systematically address the problem of replanning in an online context. The NASL planner unified planning and execution completely, treating a planning problem as a specification for carrying out a complex action.

## Relationships

- **is-an-example-of**: [[planex|Planex]]
- **is-an-example-of**: [[sipe|Sipe]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*