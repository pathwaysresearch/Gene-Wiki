---
type: entity
aliases: [ColumnTransformer]
summary: A Scikit-Learn estimator that applies different transformers to different columns of an array or pandas DataFrame.
tags: [scikit-learn, preprocessing, feature-engineering]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# ColumnTransformer

## Purpose
The `ColumnTransformer` is a Scikit-Learn class designed to apply different preprocessing steps to different columns of a dataset. This is essential in pipelines where numerical and categorical features require distinct transformations, such as scaling for numerical data and one-hot encoding for categorical data.

## How It Works
The `ColumnTransformer` constructor requires a list of tuples. Each tuple specifies a unique name for the transformation step, the transformer object to be applied (e.g., a pipeline for numerical features or a `OneHotEncoder`), and a list of column names or indices to which the transformer should be applied. When its `fit_transform` method is called, it applies each specified transformer to the appropriate columns and concatenates the results along the second axis to form a single output array.

## Handling Mixed Data Types
A key feature of `ColumnTransformer` is its ability to handle a mix of sparse and dense matrices returned by different transformers. For instance, a `OneHotEncoder` might return a sparse matrix while a numerical pipeline returns a dense matrix. The `ColumnTransformer` estimates the density of the final concatenated matrix and returns a sparse matrix if the density is below a certain threshold (by default, 0.3), optimizing memory usage.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*