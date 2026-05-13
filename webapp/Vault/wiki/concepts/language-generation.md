---
type: concept
aliases: [Language Generation]
summary: The process of constructing natural language text from a non-linguistic representation of information, essentially the reverse of parsing.
relationships:
  - target: definite-clause-grammar
    type: is-enabled-by
tags: [natural-language-generation, nlp, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Language Generation

## Definition
Language generation is the task of producing a natural language string from a more abstract, non-linguistic representation of meaning. It is the inverse process of parsing or language understanding, which takes a string and derives its meaning or structure.

## How It Works
In the context of formal grammars like Definite Clause Grammars (DCGs), language generation can sometimes be achieved by running the parsing process in reverse. Instead of providing a string and asking for its structure or meaning, one can provide a structure or a set of semantic constraints and ask the system to infer the corresponding string that satisfies the grammar.

## Connection to DCGs
The logical inference framework of Definite Clause Grammars makes them particularly suitable for language generation. Because parsing is equivalent to proving a logical theorem, the same logical system can potentially be used to construct a string that makes a given logical form true.

## Relationships

- **is-enabled-by**: [[definite-clause-grammar|Definite Clause Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*