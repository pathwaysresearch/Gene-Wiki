---
type: entity
aliases: [Prolog]
summary: The most widely used logic programming language, used for rapid prototyping, symbol-manipulation tasks, and expert systems. A logic programming language based on backward chaining, originally developed by Alain Colmerauer for natural language processing. A logic programming language strongly associated with artificial intelligence and computational linguistics, particularly for its use in implementing Definite Clause Grammars.
relationships:
  - target: logic-programming
    type: is_an_instance_of
  - target: warren-abstract-machine
    type: uses
  - target: backward-chaining
    type: is_based_on
  - target: alain-colmerauer
    type: developed_by
  - target: robert-kowalski
    type: influenced_by
  - target: warren-abstract-machine
    type: is_implemented_with
  - target: definite-clause-grammar
    type: was-motivated-by
tags: [programming-language, logic-programming, declarative-language, artificial-intelligence]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Prolog

## Overview
Prolog is the most widely used logic programming language. A Prolog program consists of a set of definite clauses. It is used for a variety of symbol-manipulation tasks and as a rapid-prototyping language.

## Syntax
Prolog's syntax differs from standard first-order logic. It uses uppercase letters for variables and lowercase for constants. Conjuncts in a rule's premise are separated by commas, and a rule of the form `A ∧ B ⇒ C` is written as `C :- A, B.`. Lists are denoted with syntax like `[E|L]`, where `E` is the first element and `L` is the rest of the list.

## Applications and Implementation
Applications of Prolog include writing compilers, parsing natural language, and building expert systems for legal, medical, and financial domains. Most Prolog compilers do not compile directly to machine language but to an intermediate language, the most popular of which is the Warren Abstract Machine (WAM).

## Relationships

- **is_an_instance_of**: [[logic-programming|Logic Programming]]
- **uses**: [[warren-abstract-machine|Warren Abstract Machine]]
- **is_based_on**: [[backward-chaining|Backward Chaining]]
- **developed_by**: [[alain-colmerauer|Alain Colmerauer]]
- **influenced_by**: [[robert-kowalski|Robert Kowalski]]
- **is_implemented_with**: [[warren-abstract-machine|Warren Abstract Machine]]
- **was-motivated-by**: [[definite-clause-grammar|Definite Clause Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*