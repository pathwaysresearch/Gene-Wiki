---
type: concept
aliases: [Training Curve]
summary: A plot that measures a machine learning model's performance on a fixed training set as the learning process proceeds on that same set.
relationships:
  - target: perceptron
    type: visualizes-learning-of
tags: [machine-learning, model-evaluation, visualization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Training Curve

## Definition
A training curve is a graph that shows the performance of a classifier on a fixed training set as the learning process progresses. It is used to visualize how a model's performance on the data it is being trained on changes over time or with more training steps, such as the number of weight updates.

## How It Works
Typically, a learning rule like stochastic gradient descent is applied one example at a time, and the model's performance metric (e.g., error) is plotted against the number of updates or epochs. This allows for observation of the learning process. For example, it can show whether a model is converging to a solution.

## Example Application
The text provides an example of a training curve for a perceptron learning rule applied to earthquake/explosion data. For linearly separable data, the curve shows the update rule converging to a zero-error linear separator. For non-linearly separable data, the curve shows the learning rule failing to converge, with the error fluctuating even after many steps.

## Relationships

- **visualizes-learning-of**: [[perceptron|Perceptron]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*