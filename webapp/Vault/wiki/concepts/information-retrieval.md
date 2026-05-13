---
type: concept
aliases: [Information Retrieval (IR)]
summary: The task of finding documents containing information relevant to a user's query from within a large collection of documents.
relationships:
  - target: bm25-scoring-function
    type: uses
tags: [information-retrieval, search-engines, natural-language-processing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Information Retrieval (IR)

## Core Task
Information retrieval is the task of finding documents that are relevant to a query. The query can be a question, a topic area, or a concept. The output is typically a ranked list of documents, ordered by their relevance to the query.

## Scoring and Ranking Models
Early IR systems often used a Boolean model, where a document was considered either relevant or not. Most modern IR systems have abandoned this in favor of models based on the statistics of word counts, such as the BM25 scoring function. These functions take a document and a query and return a numeric score, which is then used to rank the documents.

## Evaluation Metrics
The performance of IR systems is commonly measured using precision and recall. Precision is the fraction of retrieved documents that are relevant, while recall is the fraction of all relevant documents in the collection that are retrieved. The F1 score, which is the harmonic mean of precision and recall, is often used as a single summary measure of a system's accuracy.

## Relationships

- **uses**: [[bm25-scoring-function|Bm25 Scoring Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*