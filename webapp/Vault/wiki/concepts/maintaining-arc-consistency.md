---
type: concept
aliases: [Maintaining Arc Consistency (MAC)]
summary: An inference algorithm used within backtracking search that re-establishes arc consistency after each variable assignment to prune the search space.
relationships:
  - target: backtracking-search
    type: is-used-by
tags: [constraint-propagation, csp-solver, inference-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Maintaining Arc Consistency (MAC)

## Definition
Maintaining Arc Consistency, or MAC, is an algorithm used as the `INFERENCE` procedure within a backtracking search for CSPs. It actively enforces arc consistency throughout the search process, detecting inconsistencies earlier than simpler methods.

## How It Works
After a variable Xi is assigned a value, the MAC procedure initiates the AC-3 algorithm. However, instead of starting with a queue of all arcs in the CSP, it begins with a queue containing only the arcs (Xj, Xi) for all unassigned variables Xj that are neighbors of the just-assigned variable Xi. From there, AC-3 propagates constraints in the usual way. If any variable's domain is reduced to the empty set during this process, the inference fails, triggering an immediate backtrack.

## Comparison to Forward Checking
MAC is strictly more powerful than forward checking. Forward checking performs the initial step of checking neighbors of the newly assigned variable, but it does not recursively propagate the constraints when the domains of those neighbors are reduced. MAC's recursive propagation allows it to detect inconsistencies that forward checking would miss at that stage of the search.

## Relationships

- **is-used-by**: [[backtracking-search|Backtracking Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*