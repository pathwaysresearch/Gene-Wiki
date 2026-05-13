---
type: concept
aliases: [Jaro-Winkler Algorithm]
summary: A string distance metric used for fuzzy matching that measures similarity based on character transpositions and gives higher weight to strings that match from the beginning.
tags: [computer-science, string-matching, data-cleaning]
sourced_from: Acss Newfrontiers 20220814
---

# Jaro-Winkler Algorithm

## Definition
The Jaro-Winkler algorithm is a method for fuzzy string matching that calculates a similarity score between two strings. It is designed to be particularly effective for short strings like names or titles. The algorithm works by assigning high similarity (i.e., low distance) scores to strings where a small number of single-character transpositions are required to change one word into the other, making it robust to common typographical errors.

## Key Properties
A distinguishing feature of the Jaro-Winkler algorithm is its prefix bonus. It gives a higher similarity score to strings that match from the beginning up to a specified length. The text notes that the implementation used in the study sets the constant scaling factor that determines this prefix weight at the standard value of 0.1. This property is useful for correctly matching titles with minor variations, such as “Mechanotheraplst” and “Mechanotherapist”.

## Application in the Study
This algorithm is a key component of the methodology for identifying new job titles from historical data. After an initial exact match fails, the Jaro-Winkler algorithm is used to perform a fuzzy match between "candidate-new" titles in a given period and all cleaned titles from the preceding period. This step helps to accurately distinguish genuinely new job titles from those that are merely variations or misspellings of existing ones. The study utilized an R implementation of the algorithm from the `stringdist` package.

---
*Extracted from: Acss Newfrontiers 20220814*