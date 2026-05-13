---
type: concept
aliases: [Hierarchical Planning]
summary: A planning method that organizes plans by decomposing high-level actions into more detailed steps, allowing for efficient problem-solving at multiple levels of abstraction.
relationships:
  - target: high-level-action
    type: uses
tags: [planning, artificial-intelligence, htn]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Hierarchical Planning

## Overview
Hierarchical Planning is a method that moves beyond a fixed set of atomic actions to solve complex problems. It allows human experts to communicate knowledge about how to solve a problem by defining high-level actions and their refinements. This approach lends itself to efficient plan construction because the planner can solve a problem at an abstract level before delving into the details, making it possible to generate solutions containing thousands of actions.

## How It Works
The core of hierarchical planning is the use of High-Level Actions (HLAs), which are abstract actions that can be refined into sequences of more primitive actions. An HLA refinement that contains only primitive actions is called an implementation of that HLA. A high-level plan, which is a sequence of HLAs, is considered to achieve a goal if at least one of its possible implementations achieves that goal. The agent executing the plan has the choice of which implementation to follow.

## Computational Benefits
Hierarchical planning can offer significant computational savings compared to nonhierarchical, state-space planning. In an idealized case, where a nonhierarchical planner's cost is O(b^d), a hierarchical planner's cost can be reduced to approximately the k-th root of that cost, where k is the number of actions in a refinement. This efficiency is achieved by having a library of HLAs with a small number of possible refinements (small r) where each refinement breaks down into a large number of lower-level actions (large k).

## Relationships

- **uses**: [[high-level-action|High Level Action]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*