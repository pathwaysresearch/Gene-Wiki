---
type: concept
aliases: [Log Loss]
summary: The cost function used for training a Logistic Regression model, which penalizes incorrect probability estimates. It is a special case of the Cross Entropy cost function for two classes.
relationships:
  - target: logistic-regression
    type: is_cost_function_for
  - target: cross-entropy
    type: is_a_special_case_of
tags: [cost-function, classification, logistic-regression]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Log Loss

## Definition
Log Loss is the name given to the cost function used to train a Logistic Regression model. It is calculated as the average cost over all training instances and is designed to drive the model's parameters to a state where it estimates high probabilities for the correct classes and low probabilities for incorrect ones.

## Calculation
For a single training instance, the cost is calculated based on the true label (y) and the model's estimated probability (p̂). If the instance is positive (y=1), the cost is -log(p̂). If the instance is negative (y=0), the cost is -log(1-p̂). This structure ensures the cost is large when the model is confidently wrong and close to zero when it is correct. The overall cost function for the training set is the average of these individual costs.

## Relationship to Cross Entropy
Log Loss is a specific instance of the more general Cross Entropy cost function. The text explicitly states that when there are just two classes (K=2), the Cross Entropy cost function is equivalent to the Logistic Regression's Log Loss function.

## Relationships

- **is_cost_function_for**: [[logistic-regression|Logistic Regression]]
- **is_a_special_case_of**: [[cross-entropy|Cross Entropy]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*