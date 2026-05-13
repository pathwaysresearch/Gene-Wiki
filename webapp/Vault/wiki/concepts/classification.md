---
type: concept
aliases: [Classification]
summary: A supervised learning problem where the output variable is a category from a finite set of values. If there are only two categories, it is called binary classification.
relationships:
  - target: supervised-learning
    type: is_a
  - target: learning-from-examples
    type: is-a-type-of
  - target: regression
    type: is-distinct-from
tags: [machine-learning, supervised-learning, prediction]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Classification

## Definition
Classification is a type of learning problem where the goal is to predict a categorical output, y, from a given input, x. The output y must belong to a finite set of predefined values or classes, such as *sunny*, *cloudy*, or *rainy*.

## Binary Classification
A specific and common type of classification is binary classification. This occurs when there are only two possible output values for the target variable. The text distinguishes this as a special case of the broader classification problem.

## Relation to Regression
Classification is distinguished from regression, another primary type of learning problem. While classification deals with discrete, categorical outputs, regression deals with continuous, numerical outputs, such as predicting tomorrow's temperature. Both are forms of learning from examples.

## Relationships

- **is-a-type-of**: [[learning-from-examples|Learning From Examples]]
- **is-distinct-from**: [[regression|Regression]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*