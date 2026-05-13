---
type: entity
aliases: [1940 Census Complete Count]
summary: A historical U.S. Census dataset containing individual-level data, including unmasked self-reported job titles, used to study employment in newly created occupations.
relationships:
  - target: new-work-creation
    type: provides_data_for
tags: [dataset, us-census, historical-data, labor-history]
sourced_from: Acss Newfrontiers 20220814
---

# 1940 Census Complete Count

## Overview
The 1940 Census Complete Count (CCC) is an individual-level dataset from the U.S. Census. A key feature utilized in the research is that workers' self-reported job titles are unmasked and keyed, providing a rich source for analyzing historical occupational structures without the constraints of pre-defined classifications.

## Role in Research on New Work
This dataset is used to empirically investigate the phenomenon of new work. Researchers leverage it to compare 'occupational new title shares' with the actual distribution of individual-level employment in new versus preexisting job titles. This exercise serves to document that the new title shares are informative about the occupational distribution of employment in new work.

## Data Processing Methodology
The raw, self-reported titles in the CCC file are noted to be frequently vague or replete with misspellings. To overcome this, the research implements a combination of 'fuzzy-matching and term-frequency-inverse-document-frequency (TF-IDF) techniques.' These methods allow researchers to systematically link the unstructured, self-reported job titles to standardized occupation classifications for analysis.

## Relationships

- **provides_data_for**: [[new-work-creation|New Work Creation]]

---
*Extracted from: Acss Newfrontiers 20220814*