---
type: concept
aliases: [Probabilistic Context-Free Grammar]
summary: A type of phrase structure grammar where each rule is assigned a probability, allowing the model to calculate the probability of a sentence or a parse tree. An extension of a context-free grammar where each production rule is assigned a probability, enabling the calculation of the most likely parse tree for an ambiguous sentence.
relationships:
  - target: lexicalized-pcfg
    type: extended-by
  - target: cyk-algorithm
    type: used-by
  - target: treebank
    type: learned-from
  - target: penn-treebank
    type: is-trained-on
tags: [natural-language-processing, grammar-formalism, statistical-parsing, nlp, parsing, statistical-models, grammar]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Probabilistic Context-Free Grammar

## Definition
A Probabilistic Context-Free Grammar (PCFG) is a context-free grammar where each rule is augmented with a probability. The sum of the probabilities for all rules with the same left-hand side symbol must be 1. This allows the grammar to define a probability distribution over all possible sentences and parse trees.

## How It Works
A PCFG consists of a lexicon with probabilities for each word belonging to a lexical category (e.g., `Noun -> wumpus [0.15]`) and a set of phrase structure rules with associated probabilities (e.g., `S -> NP VP [0.90]`). The probability of a specific parse tree is the product of the probabilities of all the rules used to generate that tree. The probability of a sentence is the sum of the probabilities of all the parse trees that generate that sentence.

## Limitations
A key problem with PCFGs is their context-free nature. The probability of a phrase depends only on its constituent parts, not on the surrounding words. For example, the difference in probability between "eat a banana" and "eat a bandanna" is determined solely by the individual probabilities of "banana" and "bandanna" as nouns, ignoring the semantic relationship with the verb "eat". PCFGs also tend to have a strong preference for generating shorter sentences compared to the longer sentences often found in real-world corpora like the *Wall Street Journal*.

## Relationships

- **extended-by**: [[lexicalized-pcfg|Lexicalized Pcfg]]
- **used-by**: [[cyk-algorithm|Cyk Algorithm]]
- **learned-from**: [[treebank|Treebank]]
- **is-trained-on**: [[penn-treebank|Penn Treebank]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*