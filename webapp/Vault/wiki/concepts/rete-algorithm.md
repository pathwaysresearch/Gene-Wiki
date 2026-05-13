---
type: concept
aliases: [Rete Algorithm]
summary: An efficient pattern matching algorithm used in forward-chaining systems to avoid redundant work by retaining and completing partial matches as new facts arrive. An efficient pattern matching algorithm for implementing rule-based systems by solving the "many patterns/many objects match problem."
relationships:
  - target: forward-chaining
    type: improves
  - target: ops5
    type: used-in
tags: [algorithm, pattern-matching, inference-engine, optimization, rule-based-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Rete Algorithm

## Problem Addressed
In typical forward-chaining systems, a great deal of redundant work is performed by repeatedly constructing partial matches for rules on each iteration, even if only a few new facts have been added. These partial matches are discarded and then rebuilt on subsequent iterations.

## How It Works
The Rete algorithm addresses this inefficiency by preprocessing the set of rules in the knowledge base to construct a dataflow network. In this network, each node represents a literal from a rule's premise. This structure allows the system to retain and gradually complete partial matches as new facts are added, rather than re-evaluating all rules from scratch.

## Etymology
The name 'Rete' is derived from the Latin word for 'net'. The text specifies that its English pronunciation rhymes with 'treaty'.

## Relationships

- **improves**: [[forward-chaining|Forward Chaining]]
- **used-in**: [[ops5|Ops5]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*