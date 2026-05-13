---
type: concept
aliases: [Multi-task Learning]
summary: A machine learning approach where a single model is trained on multiple tasks simultaneously, leveraging shared representations to improve generalization.
tags: [deep-learning, model-architecture, transfer-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Multi-task Learning

## How It Works
In a deep learning framework, multi-task learning often involves sharing the lower layers of a network across several tasks, while task-specific parameters and layers are learned on top. This creates a shared representation that is beneficial for all tasks. For example, a model might have a shared set of hidden units, h(shared), which feed into separate, specialized hidden units (e.g., h(1) and h(2)) that are each responsible for predicting a different target variable (e.g., y(1) and y(2)).

## Underlying Assumption
The core assumption behind multi-task learning is that there is a common pool of factors that explain the variations in the input data, and each individual task is associated with a subset of these factors. By learning a shared representation, the model can capture this common pool of factors more effectively, leveraging data from all tasks to learn a better representation than it could from any single task alone.

## Benefits
A key benefit of multi-task learning is improved generalization. Because parameters in the shared layers are trained with data from all tasks, the model gains greater statistical strength. This sharing mechanism can lead to better generalization performance and improved generalization error bounds compared to training separate models for each task.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*