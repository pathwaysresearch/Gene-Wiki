---
type: concept
aliases: [BM25 Scoring Function]
summary: A ranking function used by search engines to estimate the relevance of documents to a given search query, based on the statistics of word counts.
tags: [information-retrieval, ranking-algorithm, search-engines]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# BM25 Scoring Function

## Overview
The BM25 scoring function is a model used in information retrieval systems to score and rank documents based on their relevance to a user's query. It is a probabilistic model based on the statistics of word counts, and it represents a significant advancement over simpler Boolean retrieval models.

## Origin and Use
The function originates from the Okapi project of Stephen Robertson and Karen Sparck Jones at London's City College. It has been widely adopted in the field of information retrieval and has been used in prominent search engine software, including the open-source Lucene project.

## Limitations and Refinements
The standard BM25 function uses a word model that treats all words as completely independent, ignoring semantic correlations between related words like "couch" and "sofa." Additionally, simple document length normalization schemes can overly favor short documents. Refinements such as pivoted document length normalization have been proposed to correct for this by adjusting scores for documents that are shorter or longer than an ideal "pivot" length.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*