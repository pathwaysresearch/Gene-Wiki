---
type: concept
aliases: [Precision/Recall Tradeoff]
summary: The fundamental inverse relationship in classification models where increasing precision tends to decrease recall, and vice versa, often controlled by adjusting a decision threshold.
relationships:
  - target: precision
    type: involves
  - target: recall
    type: involves
tags: [classification, model-evaluation, tradeoff]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Precision/Recall Tradeoff

## Core Concept
The precision/recall tradeoff is a core concept in binary classification that describes the inverse relationship between precision and recall. As a model is adjusted to be more precise (making fewer false positive errors), it typically becomes less comprehensive, missing more true positives and thus lowering its recall.

## The Role of the Decision Threshold
This tradeoff is directly manipulated by adjusting the classifier's decision threshold. Classifiers often output a score for each instance; if the score is above the threshold, the instance is classified as positive. Raising this threshold makes the classifier more 'strict', increasing precision but decreasing recall. Lowering the threshold has the opposite effect, increasing recall at the cost of precision.

## Practical Implications
In practice, it is easy to create a classifier with nearly any desired precision by setting a high enough threshold. However, a high-precision classifier is not very useful if its recall is too low. Therefore, when evaluating a model, it is crucial to consider both metrics simultaneously, for instance by asking 'at what recall?' when a certain precision is achieved.

## Relationships

- **involves**: [[precision|Precision]]
- **involves**: [[recall|Recall]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*