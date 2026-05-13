---
type: concept
aliases: [Breakthrough Innovation]
summary: A measure of a patent's novelty and impact, defined by a high ratio of its textual similarity to future patents (forward-similarity) relative to past patents (backward-similarity).
relationships:
  - target: kelly-et-al-2021
    type: developed_by
  - target: instrumental-variables-approach-for-innovation
    type: is_used_in
tags: [patent-analysis, econometrics, nlp]
sourced_from: Acss Newfrontiers 20220814
---

# Breakthrough Innovation

## Definition
A breakthrough innovation, as defined by the methodology from Kelly et al. (2021), is a patent that is both highly novel and impactful. This concept is measured quantitatively using natural language processing tools applied to the text of U.S. utility patents.

## Measurement
The measure is calculated by comparing the textual similarity of a patent to those that precede it and those that follow it. Novelty is captured by low similarity to prior patents (backward-similarity), while impact is captured by high similarity to subsequent patents (forward-similarity). A breakthrough patent is formally defined as one that has a high ratio of forward- to backward-similarity, typically measured over a ten-year window. The analysis uses the top 10 percent of patents based on this ratio as its set of breakthroughs.

## Application in the Study
Breakthrough patents are the cornerstone of the study's instrumental variables approach. The logic is that the precise timing of these breakthroughs is unanticipated. Therefore, the flow of breakthrough patents in a given technology class in a past decade can be used as a valid instrument to predict the flow of subsequent, follow-on innovations in that same class, which in turn affects the measured augmentation and automation exposure of occupations.

## Relationships

- **developed_by**: [[kelly-et-al-2021|Kelly Et Al 2021]]
- **is_used_in**: [[instrumental-variables-approach-for-innovation|Instrumental Variables Approach For Innovation]]

---
*Extracted from: Acss Newfrontiers 20220814*