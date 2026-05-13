---
type: concept
aliases: [Definite Clause Grammar]
summary: A formalism for representing grammars using definite clauses in first-order logic, which allows parsing to be viewed as a process of logical inference.
relationships:
  - target: prolog
    type: motivated-development-of
  - target: language-generation
    type: enables
tags: [grammar-formalism, logic-programming, parsing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Definite Clause Grammar

## Definition
A Definite Clause Grammar (DCG) is a way of writing grammar rules as logical statements called definite clauses. This translation recasts the problem of parsing a sentence as a problem of logical inference. For example, a rule like `NP -> Article Adjs Noun` can be translated into a definite clause that states if certain predicates for `Article`, `Adjs`, and `Noun` are true for parts of a string, then the `NP` predicate is true for the whole string.

## Parsing as Inference
The representation of a grammar as definite clauses means that parsing can be implemented using standard logical inference mechanisms. A bottom-up parse corresponds to a forward chaining inference process, while a top-down parse corresponds to a backward chaining process. This connection provides a powerful and flexible framework for reasoning about language.

## Role in Prolog
The development of parsing natural language with DCGs was one of the primary motivations for the creation of the Prolog logic programming language. The logical foundation of DCGs maps directly onto Prolog's execution model.

## Relationships

- **motivated-development-of**: [[prolog|Prolog]]
- **enables**: [[language-generation|Language Generation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*