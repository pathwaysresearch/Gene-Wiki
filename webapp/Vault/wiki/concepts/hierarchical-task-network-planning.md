---
type: concept
aliases: [Hierarchical Task Network (HTN) Planning]
summary: A planning method where high-level actions (HLAs) are decomposed into sequences of lower-level actions, allowing for the creation of large, complex plans.
relationships:
  - target: angelic-semantics
    type: uses
  - target: abstrips
    type: influenced-by
  - target: strips
    type: influenced-by
  - target: sipe
    type: is-an-example-of
tags: [planning, hierarchical-planning, ai-algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Hierarchical Task Network (HTN) Planning

## Overview
Hierarchical task network (HTN) planning is an approach that allows an agent to accept advice from a domain designer in the form of high-level actions (HLAs). These HLAs can then be implemented in various ways through sequences of more primitive, lower-level actions, enabling the creation of very large plans required by real-world applications.

## Key Mechanisms
A core idea in HTN planning is the abstraction hierarchy, where planning at higher levels can ignore lower-level preconditions of actions to first establish the general structure of a plan. The effects of HLAs can be defined using angelic semantics, which enables the derivation of provably correct high-level plans without needing to consider the specifics of their lower-level implementations.

## Historical Development
The concept of hierarchical planning first appeared with "macrops" (macro-operators) in the STRIPS program. The idea of an abstraction hierarchy was introduced by the ABSTRIPS system. The modern form of HTN planning was developed in the work of Austin Tate and Earl Sacerdoti. Many practical planners, such as O-PLAN and SIPE, are HTN planners.

## Relationships

- **uses**: [[angelic-semantics|Angelic Semantics]]
- **influenced-by**: [[abstrips|Abstrips]]
- **influenced-by**: [[strips|Strips]]
- **is-an-example-of**: [[sipe|Sipe]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*