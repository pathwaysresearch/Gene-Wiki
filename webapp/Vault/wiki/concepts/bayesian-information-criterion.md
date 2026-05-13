---
type: concept
aliases: [Bayesian Information Criterion (BIC)]
summary: A criterion for model selection among a finite set of models, based on the likelihood function and penalizing complexity.
relationships:
  - target: akaike-information-criterion
    type: compared_with
  - target: likelihood-function
    type: uses
  - target: model-selection
    type: is_a_method_for
tags: [model-selection, statistics, information-theory]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Bayesian Information Criterion (BIC)

## Definition
The Bayesian Information Criterion (BIC) is a statistical measure used for model selection, such as determining the optimal number of clusters for a Gaussian Mixture Model. It functions by rewarding models that fit the data well while penalizing models that have more parameters to learn.

## Formula
The formula for BIC is given as $BIC = \log(m)p – 2 \log(\hat{L})$. In this equation, $m$ represents the number of instances, $p$ is the number of parameters learned by the model, and $\hat{L}$ is the maximized value of the model's likelihood function.

## Properties and Comparison
Both BIC and AIC penalize model complexity, but they do so differently. When their selections differ, the model chosen by BIC tends to be simpler (i.e., has fewer parameters) than the one selected by AIC. This is particularly true for larger datasets, as the penalty term in BIC grows with the number of instances. The simpler model selected by BIC may not fit the data quite as well as the more complex model chosen by AIC.

## Relationships

- **compared_with**: [[akaike-information-criterion|Akaike Information Criterion]]
- **uses**: [[likelihood-function|Likelihood Function]]
- **is_a_method_for**: [[model-selection|Model Selection]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*