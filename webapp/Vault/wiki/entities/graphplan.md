---
type: entity
aliases: [GRAPHPLAN]
summary: A specific planning algorithm that uses a planning graph data structure to find a plan by alternating between expanding the graph and searching for a solution within it.
relationships:
  - target: planning-graph
    type: uses
tags: [planning-algorithm, ai, graph-algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# GRAPHPLAN

## Overview
The GRAPHPLAN algorithm is a planning method that directly utilizes a planning graph. The process involves incrementally constructing the graph, layer by layer, starting from the initial state. This graph encodes possible actions, literals, and their mutual exclusion (mutex) relations at each time step.

## Role in Planning History
The introduction of GRAPHPLAN in the mid-1990s, along with SATPLAN, represented a significant shift in the field of planning. It was one of the new, faster methods that challenged the two-decade dominance of partial-order planning and was featured prominently in surveys of the era.

## Performance Characteristics
According to analysis by Helmert (2001), constraint-based approaches such as GRAPHPLAN are best suited for NP-hard domains where finding a feasible solution may require significant search. Like SATPLAN, GRAPHPLAN can have difficulty in domains with many objects because this requires the creation of many actions, which can make the planning graph very large.

## Relationships

- **uses**: [[planning-graph|Planning Graph]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*