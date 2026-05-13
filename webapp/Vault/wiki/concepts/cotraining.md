---
type: concept
aliases: [Cotraining]
summary: A semi-supervised machine learning technique where a small set of labeled examples is used to bootstrap a learning process that simultaneously extracts new examples and new patterns from unlabeled data.
relationships:
  - target: textrunner
    type: used-by
tags: [machine-learning, information-extraction, bootstrapping, semi-supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Cotraining

## Definition
Cotraining is a technique that bootstraps an information extraction process from a handful of labeled examples. The core idea is to use these initial seeds to simultaneously find and extract new examples and new extraction patterns or templates from a large corpus of unlabeled text, iteratively growing the set of known facts and patterns.

## Historical Development
The concept was developed independently and at the same time by two research groups. Blum and Mitchell (1998) named it "cotraining," while Brin (1998) referred to it as DIPRE (Dual Iterative Pattern Relation Extraction). The text notes that the term "cotraining" has become more common. Similar early work on this iterative, semi-supervised approach was also conducted under the name of "bootstrapping."

## Application in Systems
Cotraining has been a foundational technique for several information extraction and machine reading systems. The TEXTRUNNER system, for example, uses cotraining to boost its performance. The method was also advanced and utilized by subsequent systems such as QXTRACT and KNOWITALL.

## Relationships

- **used-by**: [[textrunner|Textrunner]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*