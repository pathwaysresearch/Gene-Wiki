---
type: concept
aliases: [F-score]
summary: A performance metric for classification tasks that calculates the harmonic mean of precision and recall, providing a single score that summarizes both.
relationships:
  - target: precision
    type: combines
  - target: recall
    type: combines
tags: [performance-metrics, classification, machine-learning-evaluation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# F-score

## Definition and Purpose
The F-score is a metric used to summarize the performance of a classifier with a single number, which is particularly useful when there is a trade-off between precision and recall. By varying a classification threshold, one can often increase recall at the expense of precision, or vice-versa. The F-score provides a balanced measure of a model's performance across this trade-off.

## Formula
The F-score is calculated as the harmonic mean of precision (p) and recall (r). The formula is given by:
`F = 2pr / (p + r)`
This is also known as the F1-score, as it gives equal weight to both precision and recall.

## Application Context
This metric is commonly used in situations like medical disease detection, where a model outputs a probability score. A threshold is chosen to make a binary decision, and changing this threshold affects the precision and recall. The F-score, or alternatively the area under the precision-recall (PR) curve, can be used to evaluate and compare models without having to analyze the entire curve.

## Relationships

- **combines**: [[precision|Precision]]
- **combines**: [[recall|Recall]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*