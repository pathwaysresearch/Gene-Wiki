---
type: concept
aliases: [Label Smoothing]
summary: A regularization technique for classification models that replaces hard one-hot-encoded labels (0s and 1s) with soft labels, preventing the model from becoming overconfident.
relationships:
  - target: regularization
    type: is_a
  - target: l2-parameter-regularization
    type: is_an_alternative_to
tags: [classification, softmax, noise-robustness]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Label Smoothing

## Definition and Motivation
Label smoothing is a regularization technique designed to improve a model's robustness to noise in the training data labels. Many datasets contain some amount of mislabeled examples, and training a model to maximize the log-likelihood of these incorrect labels can be harmful. Label smoothing addresses this by explicitly modeling the uncertainty in the labels.

## How It Works
For a classification model with a softmax output and $k$ classes, label smoothing modifies the target labels used during training. Instead of using 'hard' targets (1 for the correct class, 0 for all others), it uses 'soft' targets. It assumes that for a small constant $\epsilon$, the true label is correct with probability $1 - \epsilon$. The target for the correct class is thus changed to $1 - \epsilon$, and the targets for the other $k-1$ classes are changed to $\frac{\epsilon}{k-1}$ (or $\frac{\epsilon}{k}$ as stated in the text). The model is then trained using the standard cross-entropy loss function with these softened target probabilities.

## Benefits and Effects
Label smoothing prevents a softmax classifier from becoming overconfident. Without regularization, a softmax model may never converge, as it continually increases the magnitude of its weights to produce output probabilities that are ever closer to exactly 0 or 1. Label smoothing discourages this by preventing the model from pursuing these hard probabilities, but it does so without discouraging correct classification. This effect can also be achieved by other regularizers like weight decay, but label smoothing provides a direct mechanism for handling label noise.

## Relationships

- **is_a**: [[regularization|Regularization]]
- **is_an_alternative_to**: [[l2-parameter-regularization|L2 Parameter Regularization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*