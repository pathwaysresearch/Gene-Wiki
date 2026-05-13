---
type: concept
aliases: [Accuracy]
summary: A performance measure in machine learning, particularly for classification tasks, defined as the proportion of examples for which a model produces the correct output.
relationships:
  - target: supervised-learning
    type: is_metric_for
tags: [performance-metric, classification, evaluation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Accuracy

## Definition
Accuracy is a quantitative performance measure used to evaluate a machine learning algorithm. It is defined as the proportion of examples for which the model produces the correct output. It is a common metric for tasks where the output is a single, correct category.

## Relationship to Error Rate
Accuracy provides equivalent information to the error rate, which is the proportion of examples for which the model produces an incorrect output. The error rate is also frequently referred to as the expected 0-1 loss, where the loss on a particular example is 0 if it is correctly classified and 1 if it is not. Accuracy is simply 1 minus the error rate.

## Applicability
This performance measure is specific to certain types of tasks. It is often used for classification, classification with missing inputs, and transcription. However, for other tasks such as density estimation, measuring accuracy or any other kind of 0-1 loss is not sensible. These tasks require different performance metrics, such as the average log-probability the model assigns to examples, which provide a continuous-valued score.

## Relationships

- **is_metric_for**: [[supervised-learning|Supervised Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*