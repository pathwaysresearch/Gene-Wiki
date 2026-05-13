---
type: concept
aliases: [Laplace Smoothing]
summary: A simple smoothing technique, also known as add-one smoothing, that adjusts probability estimates for unseen events by adding a pseudo-count to the observed frequency of every possible outcome.
relationships:
  - target: smoothing-in-language-models
    type: is-a-type-of
  - target: pierre-simon-laplace
    type: developed-by
tags: [natural-language-processing, language-modeling, smoothing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Laplace Smoothing

## Definition
Laplace smoothing, also called add-one smoothing, is the simplest type of smoothing used to adjust probability estimates in statistical models. It was first suggested by Pierre-Simon Laplace in the 18th century to address the problem of zero-frequency events.

## How It Works
The method is based on the principle of adding a pseudo-count (typically one) to the observed frequency of every possible outcome before calculating probabilities. For a random Boolean variable X that has been observed as false in all `n` trials, Laplace's suggestion estimates the probability of X being true as `1/(n+2)`, effectively assuming two additional trials where one is true and one is false.

## Performance and Limitations
While Laplace smoothing provides a straightforward way to prevent zero-probability estimates and improve a model's ability to generalize, it is noted to perform relatively poorly in practice. More advanced techniques, such as backoff models, generally yield better results for language modeling tasks.

## Relationships

- **is-a-type-of**: [[smoothing-in-language-models|Smoothing In Language Models]]
- **developed-by**: [[pierre-simon-laplace|Pierre Simon Laplace]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*