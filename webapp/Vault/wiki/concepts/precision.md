---
type: concept
aliases: [Precision]
summary: A classification metric that measures the accuracy of positive predictions, calculated as the ratio of true positives to the total number of positive predictions (TP / (TP + FP)).
relationships:
  - target: recall
    type: is_traded_off_with
  - target: confusion-matrix
    type: is_derived_from
tags: [classification, model-evaluation, metric]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Precision

## Definition
Precision is a metric that evaluates the accuracy of a classifier's positive predictions. It is defined by the equation: precision = TP / (TP + FP), where TP is the number of true positives and FP is the number of false positives. It answers the question, 'Of all the instances the classifier labeled as positive, what proportion was correct?'

## Relationship with Recall
Precision is typically used alongside another metric called recall. A classifier can achieve perfect precision by making only a single, highly confident positive prediction and ensuring it is correct. However, this would not be a useful model as it would ignore all other positive instances. Therefore, precision must be considered in the context of recall to get a complete picture of performance.

## The Precision/Recall Tradeoff
There is an inherent tradeoff between precision and recall, often controlled by a model's decision threshold. Increasing the threshold to achieve higher precision will generally lower recall. Because of this relationship, it is insufficient to state a precision target (e.g., '99% precision') without also specifying the corresponding recall level.

## Relationships

- **is_traded_off_with**: [[recall|Recall]]
- **is_derived_from**: [[confusion-matrix|Confusion Matrix]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*