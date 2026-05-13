---
type: concept
aliases: [AdaBoost]
summary: A specific boosting algorithm that sequentially trains weak learners, where each subsequent learner pays more attention to the instances that were misclassified by its predecessor by increasing their relative weights.
relationships:
  - target: boosting
    type: is_a_type_of
tags: [machine-learning, boosting, ensemble-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# AdaBoost

## Overview
AdaBoost is a boosting algorithm where each new predictor corrects its predecessor by focusing on the training instances that were previously misclassified. This is achieved by updating the weights of the training instances at each step. Initially, all instances have equal weight.

## The Algorithm Step-by-Step
The process begins by training a base classifier and calculating its weighted error rate on the training set. Based on this error rate, a predictor weight, α, is computed; more accurate predictors receive higher weights. The algorithm then increases the weights of the misclassified instances by multiplying them by exp(α). These updated weights are normalized and used to train the next predictor in the sequence. This cycle is repeated until the desired number of predictors is reached or a perfect predictor is found.

## Prediction
To make predictions, AdaBoost computes the predictions of all the individual predictors in the ensemble and weights them using their respective predictor weights (α). The final prediction is the class that receives the highest weighted vote.

## Relationships

- **is_a_type_of**: [[boosting|Boosting]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*