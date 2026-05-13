---
type: entity
aliases: [Gemini Pro]
summary: A large language model used in the study to perform specific natural language processing tasks, including topic classification and language fluency assessment.
relationships:
  - target: interagency-language-roundtable
    type: uses_standard_from
tags: [large-language-model, nlp-tool, google-ai]
sourced_from: 2304.11771V2
---

# Gemini Pro

## Overview
Gemini Pro is a large language model (LLM) referenced in the study as a tool for advanced text analysis. It is used to process and score conversational text based on complex, predefined criteria.

## Role in Topic Classification
The study utilized Gemini Pro to identify the topic of each agent-customer conversation. Initially, it was prompted to define the topic of 5,000 sample conversations in one to three words. Subsequently, it was used to group these into 50 distinct categories, which were then validated by contact center personnel. Finally, the LLM classified over 98% of all conversations in the dataset into one of these topic categories.

## Role in Language Assessment
Gemini Pro was also employed to measure the comprehensibility and native-like fluency of agents' written text. It was prompted to score each agent's text on a scale of 1 to 5 based on criteria adapted from the Interagency Language Roundtable (ILR) 'functionally native' proficiency standard.

## Relationships

- **uses_standard_from**: [[interagency-language-roundtable|Interagency Language Roundtable]]

---
*Extracted from: 2304.11771V2*