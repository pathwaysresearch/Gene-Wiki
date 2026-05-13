---
type: entity
aliases: [Traveling Salesperson Problem (TSP)]
summary: A classic combinatorial optimization problem that asks for the shortest possible route that visits a given set of cities and returns to the origin city.
relationships:
  - target: a-star-search
    type: is_solved_by
tags: [combinatorial-problem, np-hard, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Traveling Salesperson Problem (TSP)

## Overview
The Traveling Salesperson Problem (TSP) is a standard combinatorial problem in theoretical computer science and a subject of extensive research. The problem requires finding the shortest tour that visits each city in a given list exactly once and returns to the starting city.

## Computational Complexity
In 1972, Richard Karp proved that the TSP is NP-hard. This classification means that finding an optimal solution is computationally intractable for all but the smallest instances, as the time required is believed to grow exponentially with the number of cities. Consequently, research has focused on finding good approximate solutions.

## Solution Methods
Due to its NP-hard nature, TSP is often solved using heuristic approximation methods. Effective heuristics were developed by researchers like Lin and Kernighan. For Euclidean TSPs, a fully polynomial approximation scheme was devised by Arora. The problem can also be tackled with informed search algorithms like A* graph search, using a heuristic such as the minimum-spanning-tree (MST) cost of the unvisited cities to estimate the remaining path cost.

## Relationships

- **is_solved_by**: [[a-star-search|A Star Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*