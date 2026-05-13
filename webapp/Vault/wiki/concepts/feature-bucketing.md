---
type: concept
aliases: [Feature Bucketing]
summary: A feature engineering technique that transforms a continuous numerical feature into a discrete categorical feature by grouping values into predefined bins or 'buckets'.
relationships:
  - target: tensorflow-feature-columns
    type: enabled_by
tags: [feature-engineering, data-preprocessing, tensorflow]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Feature Bucketing

## Definition

Feature bucketing, also known as bucketization, is a data preprocessing technique used to convert a numerical feature into a categorical one. This is accomplished by defining a set of boundaries that partition the range of the numerical feature into a finite number of intervals, or buckets. Each numerical value is then mapped to the bucket it falls into, effectively discretizing the feature.

## Implementation in TensorFlow

In TensorFlow, this technique can be implemented using the Feature Column API, specifically with `tf.feature_column.bucketized_column`. This function takes a `numeric_column` as input along with a list of boundaries. For example, providing a list of four boundaries will create five distinct buckets for the feature values.

## Strategies for Defining Boundaries

Choosing the right boundaries is key to effective bucketization and can be somewhat of an art. One common approach is to use percentiles of the data's distribution (e.g., the 10th, 20th, 30th percentiles, etc.) to ensure an even distribution of instances across buckets. Another strategy, particularly for multimodal distributions (those with multiple peaks), is to place boundaries in the valleys between the peaks, creating a separate bucket for each mode.

## Relationships

- **enabled_by**: [[tensorflow-feature-columns|Tensorflow Feature Columns]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*