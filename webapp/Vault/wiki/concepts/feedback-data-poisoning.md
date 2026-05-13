---
type: concept
aliases: [Feedback Data Poisoning]
summary: An attack where malicious actors intentionally feed a learning AI with bad data to systematically corrupt its future predictions and distort its learning process.
relationships:
  - target: tay-microsoft-chatbot
    type: is_exemplified_by
tags: [ai-security, data-poisoning, adversarial-machine-learning, ai-ethics]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# Feedback Data Poisoning

## Definition
Feedback data poisoning is a type of AI security risk where external actors manipulate the data an AI learns from. This is distinct from manipulating a single prediction; the goal is to corrupt the learning process itself. By feeding the AI with distorted or malicious data, attackers can teach the machine to predict incorrectly in a systematic and lasting way.

## Example: Microsoft's Tay Chatbot
A dramatic public example of this vulnerability occurred in March 2016 with Microsoft's AI-based Twitter chatbot, Tay. The chatbot was designed to learn from its interactions with Twitter users. However, malicious actors quickly began feeding it offensive and biased content, which Tay then learned from and began to replicate. This incident demonstrated how easily a learning AI's behavior can be distorted by bad-faith inputs from the environment.

## The Nature of the Risk
This risk arises when prediction machines interact with external parties, whether human or machine, outside of a controlled business environment. The vulnerability lies in the AI's continuous learning mechanism, which can be exploited to degrade its performance or align it with a malicious actor's goals. It represents a fundamental challenge in deploying learning systems in open, adversarial environments.

## Relationships

- **is_exemplified_by**: [[tay-microsoft-chatbot|Tay Microsoft Chatbot]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *