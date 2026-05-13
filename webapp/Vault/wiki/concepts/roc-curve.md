---
type: concept
aliases: [ROC Curve]
summary: The Receiver Operating Characteristic (ROC) curve is a graphical plot used to evaluate binary classifiers by plotting the true positive rate (recall) against the false positive rate at various threshold settings.
relationships:
  - target: recall
    type: uses
tags: [classification, model-evaluation, visualization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# ROC Curve

## Definition
The Receiver Operating Characteristic (ROC) curve is a common tool used with binary classifiers. It plots the true positive rate (TPR), which is another name for recall, against the false positive rate (FPR). The FPR is the ratio of negative instances that are incorrectly classified as positive.

## How It Is Plotted
To plot the ROC curve, one must first compute the TPR and FPR for various decision threshold values. The curve visualizes the classifier's performance across this entire range of thresholds. The FPR is equal to one minus the true negative rate (TNR), which is also called specificity. Therefore, the ROC curve plots sensitivity (recall) versus 1 – specificity.

## Usage and Comparison
The ROC curve is very similar to the precision/recall curve but is used to visualize a different tradeoff. It is a common tool for comparing various models. A summary metric derived from the curve is the Area Under the Curve (ROC AUC), which provides a single score to represent the model's performance across all thresholds.

## Relationships

- **uses**: [[recall|Recall]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*