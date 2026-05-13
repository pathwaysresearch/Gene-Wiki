---
type: entity
aliases: [TEXTRUNNER]
summary: A representative machine-reading system that uses a domain-independent approach to extract relational information from large-scale, unlabeled text.
relationships:
  - target: cotraining
    type: uses
tags: [information-extraction-system, machine-reading, natural-language-processing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# TEXTRUNNER

## Overview
TEXTRUNNER is presented as a representative machine-reading system designed to extract relational information from text. Its goal is to identify and extract factual tuples, such as ("Einstein," "received," "Nobel Prize"), from sentences. A key characteristic of the system is its domain-independent nature.

## Methodology
TEXTRUNNER's process is bootstrapped from a set of labeled examples that are initially extracted from a parsed corpus, the Penn Treebank. It then employs cotraining to enhance its performance by learning from unlabeled text. The core of its extraction mechanism is a linear-chain Conditional Random Field (CRF) that is trained to identify and extract further relational examples.

## Domain Independence
The system achieves domain independence by training its CRF on features that are not tied to a specific subject area. Instead of relying on predefined lists of nouns and verbs, its features include function words like "to," "of," and "the." This approach, combined with a small set of very general syntactic templates, allows TEXTRUNNER to cover a wide variety of relationships as they are expressed in English, without needing domain-specific knowledge.

## Relationships

- **uses**: [[cotraining|Cotraining]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*