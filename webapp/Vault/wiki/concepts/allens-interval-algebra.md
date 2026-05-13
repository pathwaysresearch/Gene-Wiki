---
type: concept
aliases: [Allen's Interval Algebra]
summary: A formal calculus for temporal reasoning that defines a complete set of mutually exclusive relations that can hold between two time intervals.
tags: [temporal-reasoning, logic, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Allen's Interval Algebra

## Overview
Proposed by Allen (1983), this calculus provides a formal language for reasoning about time by defining the relationships between time intervals. An interval is represented by its start and end time points, and the algebra consists of a set of logical predicates that describe every possible way two intervals can be related.

## The Core Relations
The text defines a set of these relations with their logical equivalences based on the start and end points of two intervals, `i` and `j`. These include: `Meet(i, j)` if `End(i) = Begin(j)`; `Before(i, j)` if `End(i) < Begin(j)`; `During(i, j)` if `i` is properly contained within `j`; `Overlap(i, j)` if `i` starts before `j` but they overlap; `Begins(i, j)` if they share a start time; `Finishes(i, j)` if they share an end time; and `Equals(i, j)` if they are the same interval. The text also notes the `After` relation as the inverse of `Before`.

## Representing Time Points
To ground these relations, the system requires a way to represent time points and durations. The text shows how time points can be mapped to a numerical scale (e.g., seconds since an epoch) and how functions like `Date(h, m, s, d, m, y)` can provide a more readable interface. The duration of an interval is then simply the difference between the time of its end and the time of its beginning.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*