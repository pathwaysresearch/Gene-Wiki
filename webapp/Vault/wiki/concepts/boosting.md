---
type: concept
aliases: [Boosting]
summary: An ensemble learning method that sequentially trains weak learners, with each subsequent model focusing more on the examples that previous models misclassified.
relationships:
  - target: adaboost
    type: includes_method
  - target: bagging
    type: contrasts_with
  - target: ensemble-learning
    type: is-a-type-of
tags: [ensemble-learning, machine-learning, supervised-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Boosting

## Overview
Boosting is a specific and powerful method of ensemble learning. It works by building an ensemble of hypotheses sequentially. As illustrated in the text's description of Figure 18.33, the algorithm proceeds in stages. In each stage, a new hypothesis (a weak learner, like a small decision tree) is trained on the data. The weights of the training examples are then adjusted, increasing the weight of examples that were misclassified by the current hypothesis. This forces the next learner in the sequence to focus more on the difficult-to-classify examples.

## Theoretical Guarantee
A key result for the ADABOOST algorithm, a popular boosting method, is its ability to "boost" the accuracy of a weak learning algorithm. The text states that if the base learning algorithm can consistently produce a hypothesis with an accuracy slightly better than random guessing (50%), then boosting can combine these weak hypotheses to produce a final model that perfectly classifies the training data, given a large enough ensemble.

## Performance on Unseen Data
Boosting exhibits a surprising and beneficial property regarding model complexity and generalization. The text notes that even as more hypotheses are added to the ensemble, making the overall model more complex, the prediction accuracy on test data often continues to improve rather than suffering from overfitting. One explanation is that boosting approximates Bayesian learning, which is an optimal learning algorithm. Another is that adding hypotheses allows the ensemble to become more "definite" in its classifications, improving its performance on new examples.

## Relationships

- **is-a-type-of**: [[ensemble-learning|Ensemble Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*