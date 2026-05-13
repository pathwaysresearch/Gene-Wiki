---
type: entity
aliases: [Census Alphabetical Index of Occupations and Industries (CAI)]
summary: An internal U.S. Census Bureau reference volume used to classify job descriptions, which serves as the primary data source for identifying the emergence of new work over decades.
relationships:
  - target: new-work
    type: is_data_source_for
  - target: augmentation-innovations
    type: is_data_source_for
tags: [data-source, us-census-bureau, occupational-classification]
sourced_from: Acss Newfrontiers 20220814
---

# Census Alphabetical Index of Occupations and Industries (CAI)

## Overview
The Census Alphabetical Index of Occupations and Industries (CAI) is an internal reference tool used by the U.S. Census Bureau. It contains tens of thousands of detailed 'micro-titles' for occupations and industries. Its purpose is to help Census employees classify the free-text job descriptions written by respondents into the several hundred standardized 'macro-titles' that appear in public use data and official tabulations.

## Role in Identifying New Work
The CAI is the foundational data source for the study's measurement of 'new work.' The authors track the emergence of new job specializations by comparing successive editions of the CAI from 1930 to 2018. Newly added micro-titles, which reflect previously unseen or uncommon work activities, are identified as the creation of new work. This methodology builds on the approach pioneered by Lin (2011) but extends it across eight decades.

## Update Process
The CAI is a dynamic document, updated during the processing of each decade's Census. When Census coders detect a sufficient number of respondents reporting a specific, previously unlisted work activity, a new title is added to the index. This organic process captures the emergence of new specializations in the economy, such as 'Mental-Health Counselor' being added in 1970 or 'Sommelier' in 2010, once they become common enough to warrant their own classification.

## Relationships

- **is_data_source_for**: [[new-work|New Work]]
- **is_data_source_for**: [[augmentation-innovations|Augmentation Innovations]]

---
*Extracted from: Acss Newfrontiers 20220814*