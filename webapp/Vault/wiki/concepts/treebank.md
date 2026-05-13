---
type: concept
aliases: [Treebank]
summary: A corpus of text in which each sentence has been annotated with its syntactic parse tree, used for training and evaluating parsers and learning grammar probabilities.
relationships:
  - target: penn-treebank
    type: example-of
  - target: probabilistic-context-free-grammar
    type: used-to-train
tags: [linguistic-corpus, nlp-data, machine-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Treebank

## Definition
A treebank is a corpus of sentences that have been manually or semi-manually parsed and annotated with their grammatical structure. These annotations typically take the form of parse trees, showing the hierarchical constituent structure of each sentence.

## Role in Learning
Treebanks are essential for data-driven approaches to natural language processing, particularly for learning the probabilities of a Probabilistic Context-Free Grammar (PCFG). By analyzing the frequency of different grammatical rules and structures in a large, annotated corpus, it is possible to estimate the probabilities for each rule in the grammar.

## Example
The Penn Treebank is a prominent example of such a corpus. The text provides an example of an annotated tree from the Penn Treebank for the sentence "Her eyes were glazed as if she didn't hear or even see him," which illustrates complex grammatical phenomena like subject-object distinctions (NP vs. NP-SBJ) and phrase movement.

## Relationships

- **example-of**: [[penn-treebank|Penn Treebank]]
- **used-to-train**: [[probabilistic-context-free-grammar|Probabilistic Context Free Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*