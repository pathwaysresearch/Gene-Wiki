---
type: concept
aliases: [Angelic Semantics]
summary: A semantic framework for High-Level Actions (HLAs) where the agent itself chooses the best implementation of an action to achieve a goal, as opposed to an adversary making the choice. A method for defining the effects of high-level actions (HLAs) in HTN planning, allowing for the creation of provably correct high-level plans without specifying lower-level details.
relationships:
  - target: high-level-action
    type: describes-semantics-of
  - target: reachable-set
    type: uses
  - target: hierarchical-task-network-planning
    type: is-a-component-of
tags: [planning, semantics, nondeterminism, ai-theory, hierarchical-planning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Angelic Semantics

## Definition
Angelic semantics define the effects of a High-Level Action (HLA) based on the principle that the agent executing the plan can choose the most favorable implementation. This is contrasted with "demonic nondeterminism," where an external adversary makes the choice. Under angelic semantics, an HLA is considered successful if there exists at least one implementation that leads to a desired outcome.

## The Role of the Reachable Set
The core concept for understanding angelic semantics is the reachable set. For a given state and an HLA, the reachable set includes all possible outcome states that can be reached by executing any valid implementation of that HLA. A sequence of HLAs achieves a goal if the final reachable set for the sequence intersects with the set of goal states.

## Use in Planning Algorithms
Planning algorithms can leverage angelic semantics to find solutions. For instance, the `ANGELIC-SEARCH` algorithm operates by refining HLAs and checking if a plan can achieve the goal. It uses pessimistic approximations of the reachable set to determine if a goal state is guaranteed to be reachable, reflecting the agent's ability to make the right choices during execution.

## Relationships

- **describes-semantics-of**: [[high-level-action|High Level Action]]
- **uses**: [[reachable-set|Reachable Set]]
- **is-a-component-of**: [[hierarchical-task-network-planning|Hierarchical Task Network Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*