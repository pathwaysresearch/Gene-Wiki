---
type: concept
aliases: [Tabu Search]
summary: A local search algorithm, considered a variant of hill climbing, that maintains a list of recently visited states to avoid cycles and help escape local minima.
tags: [local-search, optimization, operations-research]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Tabu Search

## Overview
Tabu search is a variant of the hill-climbing local search method that has gained popularity in the field of operations research. It is presented as an improvement over basic hill climbing.

## How It Works
The core mechanism of tabu search is the maintenance of a "tabu list." This list stores the *k* most recently visited states. The algorithm is prohibited from revisiting any state currently on this list.

## Purpose and Benefits
The tabu list serves two main purposes. First, it improves efficiency when searching in graphs by preventing the algorithm from getting stuck in short cycles. Second, by forbidding recent moves, it can force the search to explore new regions of the state space, allowing it to escape from some local minima that would trap a standard hill-climbing algorithm.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*