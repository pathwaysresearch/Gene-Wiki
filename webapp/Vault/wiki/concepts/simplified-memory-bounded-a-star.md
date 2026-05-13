---
type: concept
aliases: [Simplified Memory-Bounded A* (SMA*)]
summary: A memory-bounded search algorithm that uses all available memory, proceeding like A* until memory is full, at which point it prunes the worst leaf node to make space for new nodes.
relationships:
  - target: a-star-search
    type: is_a_variant_of
tags: [search-algorithm, memory-bounded-search, heuristic-search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Simplified Memory-Bounded A* (SMA*)

## How It Works
SMA* (Simplified Memory-Bounded A*) is an algorithm designed to use all available memory for a search. It proceeds just like A*, expanding the best leaf node (the one with the lowest f-value) until memory is full. At this point, to add a new node to the search tree, it must drop an old one. SMA* always drops the *worst leaf node*—the one with the highest f-value.

## Handling Forgotten Nodes
When SMA* drops or 'forgets' a node, it backs up the f-value of that forgotten node to its parent. This provides the parent with information about the quality of the best path within the forgotten subtree. The algorithm will only regenerate the forgotten subtree if all other available paths are shown to look worse than the path it has forgotten, allowing it to reconsider previously pruned paths if they become promising again.

## Tie-Breaking Rule
To avoid a situation where the algorithm might select the same node for both deletion and expansion (e.g., if all leaf nodes have the same f-value), SMA* employs a specific tie-breaking rule. It expands the *newest* best leaf and deletes the *oldest* worst leaf. This ensures progress in the search.

## Relationships

- **is_a_variant_of**: [[a-star-search|A Star Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*