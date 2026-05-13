---
type: concept
aliases: [Model Compression]
summary: A technique to reduce the computational cost of inference by replacing a large, complex model with a smaller, faster one that approximates its function.
tags: [inference, efficiency, model-deployment]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Model Compression

## Definition
Model compression is a strategy for reducing the cost of inference by replacing an original, computationally expensive model with a smaller model. The new model requires less memory to store and less runtime to evaluate, making it more efficient.

## How It Works
The technique involves training a new, smaller model to mimic the function, f(x), learned by the original large model. After the large model is trained, it can be used to generate a vast, effectively infinite, labeled training set by applying it to randomly sampled inputs x. The smaller model is then trained on this new dataset to match the outputs of the larger model.

## Applicability and Rationale
Model compression is particularly applicable when the original model's large size is primarily a means to prevent overfitting, rather than a necessity for representing the learned function. For example, an ensemble of several models or a single large model regularized with dropout might have high generalization performance but be too slow for inference. To best use the smaller model's capacity, the new training inputs should be sampled from a distribution that resembles the actual test data.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*