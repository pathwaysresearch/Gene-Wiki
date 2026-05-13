---
type: concept
aliases: [CYK Algorithm]
summary: A bottom-up, dynamic programming algorithm for parsing strings using a context-free grammar, named after its inventors John Cocke, Daniel Younger, and Tadeo Kasami.
relationships:
  - target: probabilistic-context-free-grammar
    type: applies-to
tags: [parsing-algorithm, dynamic-programming, nlp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# CYK Algorithm

## Overview
The CYK algorithm, named after its inventors John Cocke, Daniel Younger, and Tadeo Kasami, is a type of chart parser. Chart parsers use dynamic programming to efficiently parse strings by storing the results of analyzing substrings in a data structure called a chart, thus avoiding redundant computations.

## How It Works
The CYK algorithm is a bottom-up parser. It starts with the words of the sentence and systematically finds all possible constituents that can be formed. For example, after identifying that a sequence of words forms a noun phrase (NP), it records this finding in the chart. This recorded result can then be reused in any other branch of the search space without re-computation, which addresses a major source of inefficiency in parsing.

## Requirements
The standard version of the CYK algorithm requires the grammar to be in a specific format where all rules are either lexical or in a specific binary structure. The text notes that this format is required for the algorithm to work.

## Relationships

- **applies-to**: [[probabilistic-context-free-grammar|Probabilistic Context Free Grammar]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*