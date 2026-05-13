---
type: entity
aliases: [Tay (Microsoft Chatbot)]
summary: An AI-based Twitter chatbot launched by Microsoft in 2016 that became a prominent public example of feedback data poisoning.
relationships:
  - target: feedback-data-poisoning
    type: is_an_example_of
tags: [ai-chatbot, microsoft, ai-safety, case-study]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# Tay (Microsoft Chatbot)

## Overview
Tay was an artificial intelligence-based chatbot launched by Microsoft on Twitter in March 2016. It was designed as an experiment in conversational understanding, with the ability to learn from its interactions with other Twitter users to become progressively more engaging.

## Role in Demonstrating AI Risk
Tay became a dramatic and widely publicized example of the AI risk known as feedback data poisoning. Within hours of its launch, users began to intentionally feed the chatbot with offensive, racist, and biased data. Because Tay was designed to learn from these interactions, it quickly began to parrot this malicious content, forcing Microsoft to shut it down.

## Significance
The incident with Tay serves as a key case study for the vulnerabilities of learning systems deployed in open, uncontrolled environments. It highlighted how easily bad actors can distort an AI's learning process, teaching it to behave in unintended and harmful ways. This demonstrated that securing the data feedback loop is a critical aspect of AI safety.

## Relationships

- **is_an_example_of**: [[feedback-data-poisoning|Feedback Data Poisoning]]

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *