---
type: entity
aliases: [Dictionary of Occupational Titles (DOT)]
summary: A data source providing textual information on occupations, used in the study to measure automation by linking patent text to job task descriptions.
relationships:
  - target: classified-index-of-industries-and-occupations-cai
    type: is_contrasted_with
tags: [data-source, occupational-data]
sourced_from: Acss Newfrontiers 20220814
---

# Dictionary of Occupational Titles (DOT)

## Overview
The Dictionary of Occupational Titles (DOT) is a data source that provides detailed textual descriptions of occupations and the tasks they entail.

## Role in the Analysis
The DOT is the primary data source used to construct the study's measure of automation exposure. The methodology involves a procedure to clean the text of patents and DOT documents, represent them as vectors, and calculate the cosine similarity between them. A strong textual match between a patent and a DOT occupation description is interpreted as an innovation that automates the tasks of that occupation.

## Data Characteristics
A key limitation of the DOT mentioned in the text is that it only contains occupation-level textual information, unlike the CAI which also includes industry-level detail. As a consequence of relying on this source, the study's automation exposure measures are always defined at the occupation level, not the more granular occupation-by-industry level.

## Relationships

- **is_contrasted_with**: [[classified-index-of-industries-and-occupations-cai|Classified Index Of Industries And Occupations Cai]]

---
*Extracted from: Acss Newfrontiers 20220814*