---
type: concept
aliases: [Monte Carlo Dropout]
summary: A technique that uses dropout at inference time to produce multiple predictions for the same input, allowing for an estimation of the model's uncertainty.
relationships:
  - target: dropout
    type: is_an_application_of
tags: [bayesian-deep-learning, uncertainty-quantification, model-inference]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Monte Carlo Dropout

## Definition
Monte Carlo (MC) Dropout is a method that leverages a standard dropout-regularized model to estimate prediction uncertainty. Instead of deactivating dropout during inference, it is kept active, and the model is run multiple times on the same input instance to generate a distribution of predictions.

## How It Works
To get a prediction for a single instance, the model is run a set number of times (e.g., 100), with dropout applied differently in each pass. This generates a collection of slightly different predictions, such as a set of probability vectors in a classification task. The final prediction can be taken as the average of these individual predictions. More importantly, the standard deviation across these predictions can be calculated to quantify the model's uncertainty about its output.

## Benefits and Trade-offs
The primary benefit of MC Dropout is that it provides a measure of uncertainty without requiring changes to the model architecture or training process. This is crucial for risk-sensitive applications like medical or financial systems, where an uncertain prediction should be treated with caution. The main trade-off is increased latency at inference time, as making a single prediction requires running the model multiple times. The number of Monte Carlo samples is a hyperparameter that balances the accuracy of the uncertainty estimate against this increased inference time.

## Relationships

- **is_an_application_of**: [[dropout|Dropout]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*