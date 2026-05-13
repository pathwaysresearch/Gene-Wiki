---
type: concept
aliases: [Logic Programming]
summary: A programming paradigm based on automated reasoning where programs are expressed as sets of logical clauses and computation is performed via inference.
relationships:
  - target: backward-chaining
    type: uses
  - target: prolog
    type: exemplified_by
tags: [programming-paradigm, automated-reasoning, declarative-programming]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Logic Programming

## Overview
Logic programming is described as the most widely used form of automated reasoning. It utilizes backward-chaining inference algorithms to execute programs, which are written as sets of definite clauses.

## Core Principle
The paradigm is captured by the equation `Algorithm = Logic + Control`. The 'Logic' component is the set of clauses provided by the programmer, while the 'Control' component is the inference mechanism, such as backward chaining, that executes the logic.

## Prominent Examples
Prolog is the most widely used logic programming language. Prolog compilers can generate a miniature, specialized theorem prover for each predicate, eliminating much of the overhead of a general interpreter. This can be further optimized by open-coding the unification routine for specific calls.

## Relationships

- **uses**: [[backward-chaining|Backward Chaining]]
- **exemplified_by**: [[prolog|Prolog]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*