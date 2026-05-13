---
type: concept
aliases: [AND-OR Graph]
summary: A graphical representation of logical expressions, often used to visualize knowledge bases, where nodes are propositions and links represent conjunctions (AND) or disjunctions (OR).
tags: [data-structure, knowledge-representation, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# AND-OR Graph

## Structure

An AND-OR graph is a way to visually represent a knowledge base, such as a set of Horn clauses. In this structure, propositions are nodes. Multiple links from a set of premises to a conclusion that are joined by an arc represent a conjunction (AND), meaning all premises must be proven. Multiple links that are not joined by an arc represent a disjunction (OR), meaning any one of the premises is sufficient to prove the conclusion.

## Role in Inference

These graphs clarify the operation of inference algorithms. For instance, forward chaining can be understood as a process where truth propagates up the graph from known leaf nodes (facts). Backward chaining can be seen as a search down the graph from the query node to find a path to the known facts.

## Example

The text refers to a figure showing a simple knowledge base of Horn clauses and its corresponding AND-OR graph, illustrating how known facts like A and B can be used to infer other propositions in the system.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*