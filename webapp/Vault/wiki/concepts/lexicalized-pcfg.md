---
type: concept
aliases: [Lexicalized PCFG]
summary: An extension of a Probabilistic Context-Free Grammar (PCFG) where grammar rules are annotated with lexical "head" words to capture dependencies between specific words.
relationships:
  - target: probabilistic-context-free-grammar
    type: is-an-extension-of
tags: [natural-language-processing, grammar-formalism, statistical-parsing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Lexicalized PCFG

## Definition
A lexicalized PCFG is a type of probabilistic grammar that addresses the context-insensitivity of standard PCFGs. In a lexicalized grammar, each nonterminal symbol in the parse tree is annotated with a head word, which is one of the words from the phrase covered by that nonterminal.

## Motivation
Standard PCFGs fail to capture lexical dependencies. For instance, a PCFG cannot easily model the fact that the verb "eat" is much more likely to take "banana" as an object than "bandanna". A Markov model can capture this local dependency but struggles with long-distance relationships. A lexicalized PCFG is introduced to precisely capture the relation between words in a phrase.

## How It Works
By incorporating head words into the grammar rules, a lexicalized PCFG can learn probabilities for rules that are conditioned on the actual words involved. This allows the model to capture the specific relationships between words, even when they are separated by other words, as in "eat a slightly aging but still palatable banana."

## Relationships

- **is-an-extension-of**: [[probabilistic-context-free-grammar|Probabilistic Context Free Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*