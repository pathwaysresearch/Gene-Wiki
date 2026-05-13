---
type: concept
aliases: [Adversarial Machine Learning]
summary: A machine learning technique where AIs are trained by competing against each other, with one AI (the adversary) attempting to foil the objective of the main AI.
relationships:
  - target: google
    type: developed_by
tags: [machine-learning, ai-training, simulation, cybersecurity]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# Adversarial Machine Learning

## Definition
Adversarial machine learning is a training approach that pits a primary AI and its objective against another AI that serves as an adversary. The adversary's role is to try to foil the main AI's objective, which in turn trains the main AI to become more robust and effective in its task.

## Example in Cryptography
The text cites an example from Google researchers where this technique was used for encryption. One AI sent messages to another using a shared key, while a third adversarial AI, which had the messages but not the key, tried to decode them. Through many simulations, the adversary's attempts trained the main AIs to communicate in ways that are increasingly difficult to decode without the key.

## Simulated vs. Real-World Learning
This method is a form of simulated learning that takes place in a controlled, laboratory-like environment rather than in the real world. The primary advantage is that it mitigates risks to the user experience or even to the users themselves. The disadvantage is that simulations may not provide feedback that is as rich or comprehensive as real-world data, meaning that at some point, the AI must still be released 'in the wild' to continue its learning.

## Relationships

- **developed_by**: [[google|Google]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *