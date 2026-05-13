---
type: concept
aliases: [Patent-to-Occupation Linking Methodology]
summary: A computational linguistics process used to measure the similarity between the text of patents and occupational descriptions, thereby linking specific innovations to the jobs they are most likely to affect.
relationships:
  - target: census-alphabetical-index-of-occupations
    type: uses_data_from
  - target: augmentation-vs-automation-innovation
    type: enables_measurement_of
tags: [natural-language-processing, econometrics, methodology]
sourced_from: Acss Newfrontiers 20220814
---

# Patent-to-Occupation Linking Methodology

## Overview
The paper employs a specific five-step methodology to systematically link the textual content of patents to the descriptions of occupations and industries, as illustrated in a flowchart in Figure 4. This process allows the researchers to quantify the exposure of different jobs to specific technological innovations documented in patents.

## Process Steps
The methodology begins with cleaning the text from both the patent corpus and the Census Alphabetical Index of Occupations (CAI) corpus. This involves stripping punctuation, removing common "stop words," retaining only nouns and verbs, and performing lemmatization. In the second step, vectors of word embeddings are extracted from the cleaned text. The third step involves generating a single document vector for each patent and occupation by taking a TF-IDF weighted average of its word vectors.

## Similarity Calculation
The core of the linking process is the fourth step, where the cosine similarity between each patent's document vector and each occupation's document vector is calculated. This provides a quantitative measure of the textual similarity between an innovation and a line of work. In the final step, the top 15% most similar patent-occupation pairs are retained to create the final linkage data used for analysis.

## Relationships

- **uses_data_from**: [[census-alphabetical-index-of-occupations|Census Alphabetical Index Of Occupations]]
- **enables_measurement_of**: [[augmentation-vs-automation-innovation|Augmentation Vs Automation Innovation]]

---
*Extracted from: Acss Newfrontiers 20220814*