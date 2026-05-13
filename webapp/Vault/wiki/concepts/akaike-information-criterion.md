---
type: concept
aliases: [Akaike Information Criterion (AIC)]
summary: A criterion for model selection among a finite set of models, which estimates the prediction error and thus the relative quality of statistical models for a given set of data.
relationships:
  - target: bayesian-information-criterion
    type: compared_with
  - target: likelihood-function
    type: uses
  - target: model-selection
    type: is_a_method_for
tags: [model-selection, statistics, information-theory]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Akaike Information Criterion (AIC)

## Definition
The Akaike Information Criterion (AIC) is a statistical measure used for model selection. It is applied in contexts like finding the best number of clusters for a Gaussian Mixture Model by balancing model fit with model complexity.

## Formula
The formula for AIC is given as $AIC = 2p - 2 \log(\hat{L})$. In this formula, $p$ stands for the number of parameters learned by the model, and $\hat{L}$ is the maximized value of the model's likelihood function.

## Properties and Comparison
Like BIC, AIC penalizes models with more parameters. However, its penalty for complexity is less severe than BIC's, especially on large datasets. Consequently, when AIC and BIC disagree, the model selected by AIC often has more parameters and fits the data better than the simpler model preferred by BIC.

## Relationships

- **compared_with**: [[bayesian-information-criterion|Bayesian Information Criterion]]
- **uses**: [[likelihood-function|Likelihood Function]]
- **is_a_method_for**: [[model-selection|Model Selection]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*