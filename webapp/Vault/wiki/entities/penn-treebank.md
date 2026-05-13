---
type: entity
aliases: [Penn Treebank]
summary: A large, annotated corpus of American English text, widely used in computational linguistics for training and evaluating natural language processing models. An influential, publicly available corpus of American English text that has been manually annotated with syntactic structure in the form of parse trees.
relationships:
  - target: treebank
    type: is-an-instance-of
  - target: probabilistic-context-free-grammar
    type: is-a-dataset-for
tags: [linguistic-corpus, nlp-dataset, computational-linguistics, nlp-resource, corpus, linguistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Penn Treebank

## Overview
The Penn Treebank is a specific, widely-used treebank, which is a corpus of text where sentences are annotated with their syntactic structure. It serves as a standard dataset for research in natural language processing.

## Role and Content
It is used as a source of data for learning the probabilities of Probabilistic Context-Free Grammars (PCFGs) and for training other statistical models. The annotations in the Penn Treebank are detailed, distinguishing between different types of phrases (e.g., subject noun phrases `NP-SBJ` versus object noun phrases `NP`) and capturing complex phenomena like the movement of a phrase from one part of a tree to another.

## Example from Text
The text provides an example of an annotated tree from the Penn Treebank for the sentence "Her eyes were glazed as if she didn't hear or even see him." This example illustrates the richness of the grammatical annotations, including markers for missing objects (`*-1`) that refer to other phrases in the sentence (`[NP-1 him]`).

## Relationships

- **is-an-instance-of**: [[treebank|Treebank]]
- **is-a-dataset-for**: [[probabilistic-context-free-grammar|Probabilistic Context Free Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*