---
type: concept
aliases: [Genetic Programming]
summary: An evolutionary computation technique, related to genetic algorithms, that evolves populations of computer programs represented as expression trees through operations like crossover and mutation.
relationships:
  - target: john-koza
    type: popularized-by
tags: [evolutionary-computation, search, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Genetic Programming

## Definition and Relation to Genetic Algorithms
Genetic programming is a field closely related to genetic algorithms. The principal difference is that the individuals being evolved are computer programs, rather than bit strings.

## Representation and Operations
In genetic programming, programs are represented as expression trees, which can be in a language like Lisp or a specially designed format. Genetic operations are adapted for this structure; for example, crossover involves splicing together subtrees from two parent programs. This method of manipulation guarantees that the resulting offspring are always well-formed, syntactically correct expressions.

## History and Applications
While interest in the field was significantly spurred by the work of John Koza in the 1990s, its origins trace back to earlier experiments with machine code and finite-state automata. The technique has been applied to practical problems, such as the design of circuit devices.

## Relationships

- **popularized-by**: [[john-koza|John Koza]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*