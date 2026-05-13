---
type: concept
aliases: [Iterative-Deepening A* (IDA*)]
summary: A memory-bounded search algorithm that adapts the idea of iterative deepening to A* search by using the f-cost (g+h) as the cutoff for each iteration instead of depth.
relationships:
  - target: a-star-search
    type: is_a_variant_of
tags: [search-algorithm, memory-bounded-search, heuristic-search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Iterative-Deepening A* (IDA*)

## How It Works
Iterative-Deepening A* (IDA*) is a method to reduce the memory requirements of A*. It performs a series of depth-first searches. In each iteration, it uses a cutoff based on the f-cost (g+h). The cutoff for the first iteration is the f-cost of the start state, and for each subsequent iteration, the cutoff value is the smallest f-cost of any node that exceeded the cutoff on the previous iteration.

## Advantages and Disadvantages
The main advantage of IDA* is its low memory usage, as it avoids the substantial overhead associated with keeping a sorted queue of nodes like standard A*. This makes it practical for many problems with unit step costs. However, a significant disadvantage is that it suffers from difficulties with real-valued costs, similar to the iterative version of uniform-cost search.

## Relationships

- **is_a_variant_of**: [[a-star-search|A Star Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*