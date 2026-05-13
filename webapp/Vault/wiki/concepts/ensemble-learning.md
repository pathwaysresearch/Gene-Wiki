---
type: concept
aliases: [Ensemble Learning]
summary: A machine learning technique that combines the predictions from a collection of models to achieve better predictive performance than any single constituent model.
tags: [machine-learning, meta-algorithm, supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
relationships:
  - target: random-forest
    type: is_a_type_of
  - target: bagging
    type: includes_method
  - target: boosting
    type: includes_method
  - target: law-of-large-numbers
    type: based_on
---

# Ensemble Learning

## Definition
Ensemble learning is a machine learning paradigm that deviates from using a single, chosen hypothesis to make predictions. Instead, it involves selecting a collection, or ensemble, of hypotheses from the hypothesis space and then combining their individual predictions to form a final prediction. The goal is to produce a more accurate and robust model.

## How It Works
The combination of predictions can be done in several ways. A simple and common example provided in the text is to generate multiple different decision trees, perhaps during cross-validation, and then have them vote on the classification for a new example. The final classification is determined by the majority vote of the individual models in the ensemble.

## Key Idea
The underlying principle is that by combining multiple, diverse models, the weaknesses of individual models can be averaged out. Different models may make different errors, and a combined approach can lead to a more stable and accurate outcome, especially if the individual models are diverse and their errors are uncorrelated.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*