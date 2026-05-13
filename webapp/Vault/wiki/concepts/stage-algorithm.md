---
type: concept
aliases: [STAGE Algorithm]
summary: An improvement on random-restart hill climbing that fits a smooth surface to found local maxima to analytically determine a better global restart point.
tags: [local-search, optimization, hill-climbing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# STAGE Algorithm

## Overview
The STAGE algorithm is presented as a useful improvement on the hill-climbing search technique, particularly when combined with random restarts.

## How It Works
The algorithm's strategy is to gain an understanding of the overall shape of the search landscape. It does this by first running random-restart hill climbing to find a set of local maxima. It then fits a smooth surface to this collection of points to model the landscape.

## Key Feature
After modeling the landscape with a smooth surface, the STAGE algorithm calculates the global maximum of that surface analytically. This calculated point is then used as the new restart point for the search. The text notes that this algorithm has been demonstrated to be effective in practice on hard problems.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*