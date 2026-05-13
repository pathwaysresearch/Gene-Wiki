---
type: concept
aliases: [Recall]
summary: A classification metric, also known as sensitivity or true positive rate (TPR), that measures the proportion of actual positive instances that were correctly identified by the classifier (TP / (TP + FN)).
relationships:
  - target: precision
    type: is_traded_off_with
  - target: confusion-matrix
    type: is_derived_from
tags: [classification, model-evaluation, metric]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Recall

## Definition
Recall, also known as sensitivity or the true positive rate (TPR), is a metric that measures a classifier's ability to detect all positive instances. It is calculated as the ratio of true positives to the sum of true positives and false negatives: recall = TP / (TP + FN). It answers the question, 'Of all the actual positive instances, what proportion did the classifier correctly identify?'

## Relationship with Precision
Recall is evaluated in conjunction with precision. A model that has very high recall might achieve it by classifying many instances as positive, thus correctly identifying most true positives but also generating many false positives, leading to low precision. A useful classifier must balance both metrics.

## Role in Evaluation
Recall is a fundamental component of classifier evaluation. It forms one axis of the precision/recall curve, which visualizes the tradeoff between the two metrics. It is also the vertical axis (sensitivity) of the Receiver Operating Characteristic (ROC) curve, where it is plotted against the false positive rate.

## Relationships

- **is_traded_off_with**: [[precision|Precision]]
- **is_derived_from**: [[confusion-matrix|Confusion Matrix]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*