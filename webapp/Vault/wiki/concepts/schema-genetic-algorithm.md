---
type: concept
aliases: [Schema (Genetic Algorithm)]
summary: A theoretical construct in genetic algorithms representing a template or substring pattern that identifies a subset of similar individuals in a population.
relationships:
  - target: genetic-algorithm
    type: is-a-concept-in
tags: [genetic-algorithm, evolutionary-computation, theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Schema (Genetic Algorithm)

## Definition
In the theory of genetic algorithms, a schema is a substring in which some positions are treated as wildcards, allowing them to be left unspecified. For example, in an 8-queens problem represented by digit strings, the schema `246*****` describes all states where the first three queens are in positions 2, 4, and 6. Individual strings that match the schema, such as `24613578`, are known as instances of that schema.

## Role in Genetic Algorithm Theory
The concept of a schema is used to explain the effectiveness of the crossover operation. The theory posits that crossover works by combining useful, high-fitness building blocks represented by schemata. It can be shown that if the average fitness of the instances of a particular schema is higher than the average fitness of the entire population, the number of instances of that schema is expected to grow in subsequent generations.

## Significance
The schema theorem provides a theoretical foundation for why genetic algorithms can be effective. It suggests that the algorithm implicitly favors and propagates beneficial sub-solutions or "building blocks." This allows the search to operate at a higher level of granularity than just individual gene positions, by combining large, independently evolved blocks of code that have proven to be useful.

## Relationships

- **is-a-concept-in**: [[genetic-algorithm|Genetic Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*