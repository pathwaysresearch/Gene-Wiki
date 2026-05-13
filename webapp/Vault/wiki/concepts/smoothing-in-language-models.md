---
type: concept
aliases: [Smoothing (in Language Models)]
summary: A set of techniques used in statistical language models to assign a small non-zero probability to sequences that were not observed in the training data, improving generalization to new texts.
relationships:
  - target: backoff-model
    type: has-type
  - target: laplace-smoothing
    type: has-type
tags: [natural-language-processing, language-modeling, statistical-technique]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Smoothing (in Language Models)

## Definition and Purpose
Smoothing is the process of adjusting the probability estimates of low-frequency events in a language model. Its primary purpose is to solve the problem of generalization: without smoothing, any n-gram not seen in the training corpus would be assigned a probability of zero, which is an inaccurate and brittle assumption. Smoothing ensures that the model can assign a small, non-zero probability to novel sequences.

## Laplace Smoothing
The simplest type of smoothing was suggested by Pierre-Simon Laplace in the 18th century. Also known as add-one smoothing, this technique adjusts counts to avoid zero probabilities. For example, if a Boolean variable has been false in all n observations, Laplace smoothing estimates the probability of it being true as 1/(n+2). While historically important, this method performs relatively poorly compared to modern techniques.

## Advanced Approaches
A more effective approach is a backoff model, where the model relies on lower-order n-grams when data for a higher-order n-gram is scarce. For any sequence with a low or zero count, the model "backs off" to an (n-1)-gram for its probability estimate. Linear interpolation smoothing is a specific type of backoff model that combines trigram, bigram, and unigram models via linear interpolation.

## Relationships

- **has-type**: [[backoff-model|Backoff Model]]
- **has-type**: [[laplace-smoothing|Laplace Smoothing]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*