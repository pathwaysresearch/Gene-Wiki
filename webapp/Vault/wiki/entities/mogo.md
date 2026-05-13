---
type: entity
aliases: [MOGO]
summary: A leading Go-playing program as of 2009 that utilized Monte Carlo search methods and the UCT algorithm to play at a high level.
relationships:
  - target: go
    type: plays
  - target: uct-upper-confidence-bounds-on-trees
    type: uses
tags: [computer-program, go-engine]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# MOGO

## Overview
MOGO, developed by Gelly and Silver, was considered the strongest Go program as of 2009. It represented the state-of-the-art in computer Go, which had moved away from traditional search algorithms like alpha-beta.

## Technical Approach
Unlike chess programs, MOGO used Monte Carlo methods based on the UCT (upper confidence bounds on trees) scheme. This approach involves using random sampling to evaluate moves, which is better suited to Go's massive branching factor and difficult evaluation problem.

## Performance and Achievements
In August 2008, MOGO achieved a surprising win against a top professional player, Myungwan Kim, although it received a nine-stone handicap. For this match, it ran on an 800-processor, 15 teraflop supercomputer, which was 1000 times the power of Deep Blue. Kim estimated its strength at the low end of advanced amateur (2-3 dan). On the smaller 9x9 version of Go, MOGO played at approximately the 1-dan professional level.

## Relationships

- **plays**: [[go|Go]]
- **uses**: [[uct-upper-confidence-bounds-on-trees|Uct Upper Confidence Bounds On Trees]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*