---
type: concept
aliases: [Substitution (Binding List)]
summary: An assignment of values to variables in a logical expression, typically returned as the result of a query to a knowledge base.
relationships:
  - target: first-order-logic
    type: is-a-concept-in
tags: [logic-programming, inference, knowledge-representation, unification]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Substitution (Binding List)

## Definition
A substitution, also referred to as a binding list, is the answer to a query that contains variables. It provides a specific assignment of constants to those variables that makes the queried sentence true according to the contents of the knowledge base. For example, for a query `Person(x)`, a substitution might be `{x/John}`.

## Function in Queries
The text describes a function, `ASKVARS`, which takes a knowledge base and a query with variables and returns a stream of substitutions. For instance, `ASKVARS(KB, Person(x))` might yield two answers, `{x/John}` and `{x/Richard}`, if both John and Richard are known to be persons in the knowledge base. Each answer represents one way to satisfy the query.

## Scope and Limitations
This mechanism of answering with a binding list is most common in knowledge bases composed of Horn clauses, as is typical in logic programming. The text points out that in full first-order logic, a query can be true without there being a specific binding for its variables. For example, if the knowledge base contains `King(John) ∨ King(Richard)`, the existential query `∃x King(x)` is true, but there is no single substitution for `x` that can be returned as the answer.

## Relationships

- **is-a-concept-in**: [[first-order-logic|First Order Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*