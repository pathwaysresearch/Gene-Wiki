---
type: concept
aliases: [Supervised Machine Learning]
summary: A machine learning approach where an algorithm learns from labeled data to make predictions about binary outcomes or numerical quantities.
relationships:
  - target: data-preparation
    type: depends_on
tags: [machine-learning, ai, data-science]
sourced_from: Ai
---

# Supervised Machine Learning

## Definition

Supervised machine learning is a process where an algorithm learns from labeled data—that is, data with validated, known outcomes—to make a prediction. The goal is to predict either a binary outcome, such as whether a picture contains a cat or a dog, or a numerical quantity, like the sales forecast for a specific product.

## The Iterative Process

The development of a supervised learning model is an iterative process. An algorithmic model's prediction is compared to the validated labeled outcomes to measure its error rate. If the error rate is unsatisfactory, developers can iterate by choosing a different statistical approach, acquiring more data, or identifying other features that might help make a more accurate prediction. This cycle continues until the model's accuracy is deemed sufficient.

## Applications and Examples

Supervised machine learning is used in many common applications. Examples include email providers using user-labeled spam to update their filters, social media platforms like Facebook or Baidu suggesting photo tags based on prior labeled photos, credit card companies using past purchasing habits to approve or deny transactions, and smart thermostats like Nest learning a user's schedule from their arrival and departure times.

## Relationships

- **depends_on**: [[data-preparation|Data Preparation]]

---
*Extracted from: Ai*