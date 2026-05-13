---
type: entity
aliases: [8-Puzzle]
summary: A classic sliding block puzzle on a 3x3 grid with eight numbered tiles and one blank space, used as a standard problem for AI search algorithms. A classic sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty space, used as a standard test problem for search algorithms.
relationships:
  - target: problem-formulation
    type: is-an-example-of
  - target: manhattan-distance
    type: uses_heuristic
  - target: relaxed-problem
    type: is_an_example_for
tags: [toy-problem, search, benchmark, puzzle, benchmark-problem, search-problem]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# 8-Puzzle

## Overview
The 8-puzzle is a well-known problem in artificial intelligence used to illustrate and test search algorithms. It consists of a 3x3 grid with eight square tiles labeled 1 through 8 and one blank space. The goal is to reach a specific goal configuration of the tiles by repeatedly sliding a tile adjacent to the blank space into the blank space's position.

## Formal Problem Formulation
The 8-puzzle is easily defined for a problem-solving agent. The **states** are specified by the location of each of the eight tiles and the blank. The **initial state** can be any configuration. The **actions** are the movements of the blank space: Left, Right, Up, or Down. The **transition model** defines the resulting state when an action is applied (e.g., swapping the blank with an adjacent tile). The **goal test** checks if the current state matches the desired goal configuration. Finally, the **path cost** is typically defined as 1 for each step, so the total cost is the number of moves.

## Significance in AI
The 8-puzzle serves as a standard benchmark problem because its state space is large enough to be interesting but small enough to be solved. It is an excellent example of how a physical problem can be modeled through abstraction, where the continuous physical movement of sliding a tile is simplified into a discrete action of swapping positions in the grid representation.

## Relationships

- **is-an-example-of**: [[problem-formulation|Problem Formulation]]
- **uses_heuristic**: [[manhattan-distance|Manhattan Distance]]
- **is_an_example_for**: [[relaxed-problem|Relaxed Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*