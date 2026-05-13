---
type: concept
aliases: [Stratified K-Fold]
summary: A variation of K-fold cross-validation that returns stratified folds, meaning each fold contains approximately the same percentage of samples of each target class as the complete set.
relationships:
  - target: k-fold-cross-validation
    type: is_a_variant_of
tags: [cross-validation, classification, stratified-sampling]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Stratified K-Fold

## Definition
`StratifiedKFold` is a cross-validation class in Scikit-Learn that performs stratified sampling to generate folds. This is a crucial technique for classification problems, especially when dealing with datasets where class distribution is not uniform.

## Purpose and Mechanism
The primary goal of stratified sampling in this context is to ensure that each fold is representative of the overall dataset's class distribution. It produces folds that contain a proportional ratio of each class. This prevents situations where a fold might, by random chance, contain an unrepresentative number of samples from a particular class, which would make evaluation on that fold unreliable.

## Usage
In a manual cross-validation loop, an instance of the `StratifiedKFold` class is created, specifying the number of splits. Its `split` method is then used to generate indices for the training and test sets for each iteration. This ensures that when the model is cloned and trained in each step of the loop, it is trained and evaluated on data that maintains the original class balance.

## Relationships

- **is_a_variant_of**: [[k-fold-cross-validation|K Fold Cross Validation]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*