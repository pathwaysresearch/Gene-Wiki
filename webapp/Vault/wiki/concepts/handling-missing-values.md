---
type: concept
aliases: [Handling Missing Values]
summary: A data preprocessing step that addresses datasets with missing entries by either removing the affected rows/columns or imputing the missing values with a substitute like the mean or median.
relationships:
  - target: data-preprocessing
    type: is_a_part_of
tags: [data-preprocessing, imputation, data-cleaning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Handling Missing Values

## Overview of Strategies
When faced with missing values in a dataset, there are three primary strategies. The first is to get rid of the corresponding rows that contain missing values for a particular attribute. The second option is to discard the entire attribute (column) if it has too many missing values. The third, and often preferred, option is to set the missing values to some value, such as zero, the mean, or the median, a process known as imputation.

## Imputation with Median
The text demonstrates imputation using the median of the attribute with missing values. A critical best practice is highlighted: the median must be computed on the training set only. This computed median is then saved and used to fill missing values in the training set, the test set, and any new data that the system encounters in production. This prevents data leakage from the test set into the training process.

## Implementation with Scikit-Learn
Scikit-Learn provides the `SimpleImputer` class to systematically handle missing values. A user creates an instance of the imputer, specifying a strategy like 'median'. This imputer is then 'fit' on the training data (excluding non-numerical columns), which learns the median for each attribute. Finally, the `transform` method of the imputer is used to replace the missing values with the learned medians in the dataset.

## Relationships

- **is_a_part_of**: [[data-preprocessing|Data Preprocessing]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*