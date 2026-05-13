---
type: concept
aliases: [Recursive Best-First Search (RBFS)]
summary: A recursive, linear-space search algorithm that mimics standard best-first search by keeping track of the f-value of the best alternative path available from any ancestor of the current node.
tags: [search-algorithm, memory-bounded-search, recursive-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Recursive Best-First Search (RBFS)

## How It Works
Recursive best-first search (RBFS) is a simple recursive algorithm that attempts to replicate the operation of standard best-first search using only linear space. Its structure is similar to a recursive depth-first search. It uses an `f_limit` variable to keep track of the f-value of the best alternative path available from any ancestor of the current node.

## Behavior
Rather than continuing indefinitely down the current path, RBFS compares the f-value of the current node to its `f_limit`. If the current node's f-value exceeds this limit, the recursion unwinds back to the ancestor node from which the alternative path was available. The algorithm then proceeds to explore that more promising alternative path. This mechanism allows it to simulate the behavior of best-first search while maintaining a small memory footprint.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*