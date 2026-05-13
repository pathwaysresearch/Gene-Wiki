---
type: concept
aliases: [Question Answering]
summary: A natural language processing task focused on providing a short, direct answer to a question posed in natural language, rather than a list of relevant documents.
relationships:
  - target: information-retrieval
    type: leverages
  - target: askmsr-system
    type: exemplified-by
tags: [natural-language-processing, information-retrieval, nlp-task]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Question Answering

## Definition
Question answering is a task distinct from information retrieval. While IR finds documents relevant to a query, the goal of question answering is to provide a short, specific response—such as a sentence or even just a phrase—to a direct question posed by a user.

## Web-Based Approach
Modern question-answering systems, developed since 2001, leverage Web information retrieval to achieve broad coverage. The core intuition behind this approach is that most questions have likely been answered many times on the Web. This reframes the problem as one of precision (finding one of the existing correct answers) rather than recall (having to formulate an answer from scratch).

## Example System
The ASKMSR system is cited as a typical example of a Web-based question-answering system. It operates on the principle of finding existing answers on the Web, which demonstrates the shift in approach from earlier NLP systems that relied on more limited, curated knowledge bases.

## Relationships

- **leverages**: [[information-retrieval|Information Retrieval]]
- **exemplified-by**: [[askmsr-system|Askmsr System]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*