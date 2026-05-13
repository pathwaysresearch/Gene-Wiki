---
type: concept
aliases: [Adversarial Training]
summary: A regularization method that improves model robustness by training on adversarial examples, which are inputs intentionally perturbed to cause misclassification.
relationships:
  - target: regularization
    type: is_a_type_of
  - target: semi-supervised-learning
    type: is_a_method_for
tags: [regularization, robustness, semi-supervised-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Adversarial Training

## Definition and Goal
Adversarial training is a regularization technique that discourages a model from exhibiting highly sensitive, locally linear behavior. It achieves this by encouraging the network to be locally constant in the neighborhood of the training data. This can be seen as explicitly introducing a local constancy prior into the model, making it more robust to small, worst-case perturbations in the input.

## How It Works
This method trains a model on adversarial examples, which are inputs slightly modified to maximize the model's error. By including these examples in the training process, the model learns to resist such local perturbations. Neural networks are particularly well-suited for this, as their large function family has the flexibility to capture linear trends in the data while still learning to be locally constant where needed. In contrast, purely linear models like logistic regression are forced to be linear everywhere and thus cannot effectively resist adversarial examples.

## Application in Semi-Supervised Learning
Adversarial training also provides a mechanism for semi-supervised learning. For an unlabeled data point, the model's own prediction can be used as a provisional label. The training algorithm can then search for an adversarial example that would cause the classifier to change its prediction for this point. By training the model to be robust to this perturbation, it effectively regularizes the decision boundary in regions of low data density, leveraging the unlabeled data to improve generalization.

## Relationships

- **is_a_type_of**: [[regularization|Regularization]]
- **is_a_method_for**: [[semi-supervised-learning|Semi Supervised Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*