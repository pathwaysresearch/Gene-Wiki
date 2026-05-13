---
type: concept
aliases: [Knowledge Base Approach]
summary: An approach to artificial intelligence that involves hard-coding knowledge about the world in formal languages and using logical inference rules to reason about statements.
relationships:
  - target: cyc
    type: exemplified_by
tags: [artificial-intelligence, symbolic-ai]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Knowledge Base Approach

## Definition
The knowledge base approach to artificial intelligence is a method where knowledge about the world is hard-coded into a computer system. This knowledge is expressed in formal languages, allowing the computer to reason about these statements automatically using logical inference rules.

## Implementation
In this approach, a database of statements is created, often by human supervisors who enter the information. An inference engine then uses this database to reason about the world. The goal is to capture a vast amount of informal, real-world knowledge in a structured, formal system.

## Limitations
This approach has proven to be unwieldy and has not led to major successes. A key challenge is the difficulty for humans to devise formal rules with enough complexity to accurately describe the world. For example, the famous Cyc project, which uses this approach, failed to understand a simple story about a person shaving, highlighting the brittleness of hard-coded rules.

## Relationships

- **exemplified_by**: [[cyc|Cyc]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*