---
type: entity
aliases: [Census Alphabetical Index of Occupations]
summary: A publication by the US Census Bureau that lists occupational titles, used in the study to identify the emergence of "new work" over time.
relationships:
  - target: us-census-bureau
    type: published_by
  - target: new-work-vs-existing-work
    type: provides_data_for
  - target: patent-to-occupation-linking-methodology
    type: provides_data_for
tags: [data-source, government-publication, occupational-classification]
sourced_from: Acss Newfrontiers 20220814
---

# Census Alphabetical Index of Occupations

## Overview
The Census Alphabetical Index of Occupations is a data source published by the US Census Bureau between 1915 and 2018. It provides a comprehensive list of job titles used in the United States, serving as a key historical record of the occupational landscape.

## Role in the Research
This index is a foundational data source for the study's analysis of "new work." The researchers identify the creation of new jobs by tracking the appearance of "New Occupational Titles" added to the index in each decade. Figure 1 plots the relative usage frequency of these new titles in published texts to validate their novelty and significance.

## Use in Methodology
The text of the occupational titles from the index is a core input for the "Patent-to-Occupation Linking Methodology." As shown in Figure 4, the "Cleaned CAI corpus" (CAI standing for Census Alphabetical Index) is processed through natural language processing techniques to create document vectors representing each occupation, which are then compared to patent vectors.

## Relationships

- **published_by**: [[us-census-bureau|Us Census Bureau]]
- **provides_data_for**: [[new-work-vs-existing-work|New Work Vs Existing Work]]
- **provides_data_for**: [[patent-to-occupation-linking-methodology|Patent To Occupation Linking Methodology]]

---
*Extracted from: Acss Newfrontiers 20220814*