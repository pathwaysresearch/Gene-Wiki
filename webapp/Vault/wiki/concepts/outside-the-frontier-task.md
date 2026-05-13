---
type: concept
aliases: [Outside-the-Frontier Task]
summary: An experimental task designed to be beyond the known capabilities of an AI model, where the AI may negatively impact human performance.
relationships:
  - target: jagged-capability-frontier
    type: is_an_instance_of
  - target: gpt-4
    type: tested_on
  - target: inside-the-frontier-task
    type: is_contrasted_with
tags: [experimental-design, ai-limitations, human-ai-interaction]
sourced_from: Ssrn 4573321
---

# Outside-the-Frontier Task

## Definition
An "outside-the-frontier" task, as defined in the Ssrn 4573321 experiment, is a task that falls outside the reliable capabilities of the AI model (GPT-4). On these tasks, AI is hypothesized to act as a "disruptor," potentially harming performance (Chunk 14).

## Performance Effects on Correctness
The study found that AI assistance negatively impacted performance on these tasks. The primary metric was "correctness," a binary variable. Subjects in the control group were correct 84.5% of the time, while the AI-assisted groups scored significantly lower, at 60% and 70.6%. Linear regression analysis confirmed that both AI treatments had a significant negative impact on correctness (Chunk 10).

## Impact on Subjective Quality
Despite the drop in correctness, AI assistance had a positive effect on the perceived quality of the work. Table 9 shows that recommendations produced with AI help received significantly higher scores for "Subjective Coherence Quality." This was true independent of whether the underlying solution was correct, suggesting AI can make incorrect answers appear more persuasive and coherent (Chunk 12).

## Relationships

- **is_an_instance_of**: [[jagged-capability-frontier|Jagged Capability Frontier]]
- **tested_on**: [[gpt-4|Gpt 4]]
- **is_contrasted_with**: [[inside-the-frontier-task|Inside The Frontier Task]]

---
*Extracted from: Ssrn 4573321*