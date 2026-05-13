---
type: concept
aliases: [Supervised Pretraining]
summary: A training strategy where a model is first trained on a simpler task or as a simpler model before being trained on the final, more complex task, often to find a better initialization.
tags: [training-strategy, optimization, deep-learning, transfer-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Supervised Pretraining

## Definition
Supervised pretraining is a collection of strategies used when directly training a complex model for a difficult task is too ambitious. The approach involves first training a simpler model to solve the task, or training the desired model to solve a simpler task, before confronting the final challenge. This initial training phase helps to initialize the model in a more favorable region of the parameter space.

## Greedy Pretraining
A common form of pretraining involves greedy algorithms. This approach breaks a large problem into many components and then solves for the optimal version of each component in isolation. While combining these individually optimal components does not guarantee a globally optimal solution for the full problem, it is computationally much cheaper and often provides a high-quality initial solution.

## Fine-Tuning
Greedy pretraining is often followed by a fine-tuning stage. In this phase, a joint optimization algorithm is applied to the full problem, starting from the solution provided by the greedy pretraining. Initializing the joint optimization with this greedy solution can greatly speed up the process and improve the quality of the final solution compared to starting from a random initialization.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*