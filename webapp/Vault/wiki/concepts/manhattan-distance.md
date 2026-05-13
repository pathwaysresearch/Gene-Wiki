---
type: concept
aliases: [Manhattan Distance]
summary: A distance metric calculated as the sum of the absolute differences of Cartesian coordinates, often used as an admissible heuristic in grid-based problems like the 8-puzzle.
relationships:
  - target: admissible-heuristic
    type: is_an_example_of
  - target: 8-puzzle
    type: is_used_in
tags: [heuristic-function, distance-metric, 8-puzzle]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Manhattan Distance

## Definition
Also known as the city block distance, the Manhattan distance is the sum of the horizontal and vertical distances between two points on a grid. It is named this way because it represents the distance a car would drive in a city laid out in a grid plan, where diagonal movement is not possible.

## Application as a Heuristic
For the 8-puzzle, the Manhattan distance heuristic, denoted as h2, is calculated as the sum of the distances of each individual tile from its correct goal position. This provides an estimate of the minimum number of moves required to solve the puzzle from a given state.

## Admissibility
The Manhattan distance is an admissible heuristic for the 8-puzzle. This is because any single move of a tile can only change its Manhattan distance to its goal position by at most one. It is also the exact solution cost for a relaxed version of the puzzle where a tile could move one square in any direction, even onto an occupied square, which formally proves its admissibility.

## Relationships

- **is_an_example_of**: [[admissible-heuristic|Admissible Heuristic]]
- **is_used_in**: [[8-puzzle|8 Puzzle]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*