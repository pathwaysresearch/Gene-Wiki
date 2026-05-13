---
type: concept
aliases: [Classical Planning]
summary: A planning formalism that uses a factored representation of states and action schemas, which facilitates the development of powerful domain-independent heuristics.
relationships:
  - target: domain-independent-heuristic
    type: enables
  - target: state-space-search
    type: uses
tags: [planning, artificial-intelligence, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Classical Planning

## Overview
Classical planning addresses problems by finding a sequence of actions to reach a goal state from an initial state. It uses a factored representation for states and action schemas, which distinguishes it from approaches that use atomic states or full first-order logic axioms.

## Key Advantage
The primary advantage of the classical planning formalism is its ability to support the development of very accurate domain-independent heuristics. This is because the factored representation of states and actions can be analyzed automatically by a program to derive good heuristics for a given problem, unlike atomic state representations which require human ingenuity for heuristic design.

## Complexity
The complexity of classical planning problems can vary. While finding a plan for an arbitrary worst-case problem instance can be very difficult, planning in specific domains is often much easier. For many domains, finding an optimal plan is NP-complete, while finding any valid (sub-optimal) plan can be in P, making good search heuristics crucial for practical performance.

## Relationships

- **enables**: [[domain-independent-heuristic|Domain Independent Heuristic]]
- **uses**: [[state-space-search|State Space Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*