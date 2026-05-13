---
type: concept
aliases: [Likelihood Function]
summary: In statistics, a function of the parameters of a statistical model given observed data, used to describe the plausibility of parameter values after an outcome is known.
relationships:
  - target: bayesian-information-criterion
    type: is_used_by
  - target: akaike-information-criterion
    type: is_used_by
tags: [statistics, probability-theory, statistical-inference]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Likelihood Function

## Definition
In statistics, the term 'likelihood' is used to describe how plausible a particular set of parameter values, $\theta$, are for a statistical model after a specific outcome, **x**, is known. The likelihood function, therefore, maps parameter values to the likelihood of observing the given data.

## Likelihood vs. Probability
The text emphasizes a key distinction between 'likelihood' and 'probability', terms often used interchangeably in everyday language. 'Probability' is used to describe how plausible a future outcome **x** is, given that the model parameters $\theta$ are known. In contrast, 'likelihood' is used to describe how plausible the parameter values $\theta$ are, given that the outcome **x** is known.

## Role in Model Selection
The likelihood function is a critical component in model evaluation and selection. For instance, in both the Bayesian Information Criterion (BIC) and Akaike Information Criterion (AIC), the term $\hat{L}$ represents the maximized value of the likelihood function. This value quantifies how well the model fits the data under the optimal parameter settings, forming the basis for comparing different models.

## Relationships

- **is_used_by**: [[bayesian-information-criterion|Bayesian Information Criterion]]
- **is_used_by**: [[akaike-information-criterion|Akaike Information Criterion]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*