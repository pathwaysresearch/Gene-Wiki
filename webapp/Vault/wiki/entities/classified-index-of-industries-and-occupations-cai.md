---
type: entity
aliases: [Classified Index of Industries and Occupations (CAI)]
summary: A data source providing textual information on occupations by industry, used in the study to measure augmentation by linking patent text to job descriptions.
relationships:
  - target: dictionary-of-occupational-titles-dot
    type: is_contrasted_with
tags: [data-source, occupational-data]
sourced_from: Acss Newfrontiers 20220814
---

# Classified Index of Industries and Occupations (CAI)

## Overview
The Classified Index of Industries and Occupations (CAI) is a data source containing textual descriptions of jobs. A key feature of the CAI is that it provides information at the occupation-by-industry level, offering more granular detail than sources like the DOT.

## Role in the Analysis
The study leverages the CAI to construct its primary measure of augmentation. The methodology involves textually linking patents to CAI occupation-by-industry descriptions. By calculating the cosine similarity between patent text and CAI text, the researchers identify innovations that are relevant to the outputs and tasks of specific jobs in specific industries, which they classify as augmentation.

## Data Characteristics
The text notes that the CAI's update schedule influences the study's time periods. Specifically, it was largely not updated between 2000 and 2010 and then was substantially updated in 2018. This leads the authors to define the last time interval of their sample as 2000-2018 rather than a single decade.

## Relationships

- **is_contrasted_with**: [[dictionary-of-occupational-titles-dot|Dictionary Of Occupational Titles Dot]]

---
*Extracted from: Acss Newfrontiers 20220814*