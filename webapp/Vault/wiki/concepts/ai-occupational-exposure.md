---
type: concept
aliases: [AI Occupational Exposure (AIOE)]
summary: A novel measure of an occupation's exposure to artificial intelligence, based on linking AI applications to the specific human abilities required for that occupation.
relationships:
  - target: o-net
    type: uses_data_from
  - target: the-eff-ai-progress-measurement
    type: uses_data_from
  - target: ai-industry-exposure
    type: is_used_to_construct
tags: [measurement, labor-economics, artificial-intelligence]
sourced_from: Occupational Industry And Geographic Exposure To A
---

# AI Occupational Exposure (AIOE)

## Definition
The AI Occupational Exposure (AIOE) is a measure created to quantify an occupation's exposure to artificial intelligence. It is designed to capture the extent to which the abilities required for a given occupation are related to the capabilities of modern AI applications, and it can be used to construct firm-level measures of AI exposure.

## Methodology
The AIOE is constructed by first linking 10 specific AI applications, as categorized by the EFF, to 52 occupational abilities defined in the O*NET database. This creates an "application-ability relatedness" matrix. An "ability-level exposure" is then calculated for each ability by summing the relatedness scores across all 10 AI applications. To calculate the final AIOE score for an occupation, the aggregate exposure across all its required abilities is scaled by the breadth of abilities that occupation requires. This adjustment accounts for differences in the scope of occupations, distinguishing between those that rely on a narrow set of abilities versus a broad portfolio, as illustrated by the different AIOE scores for surgeons and physicists despite similar aggregate exposure.

## Key Characteristics and Findings
The AIOE measure suggests that exposure to AI is highest in white-collar occupations such as genetic counselors, financial examiners, and actuaries, while being lowest in occupations like dancers and fitness trainers. The measure emphasizes that the presence of cognitive abilities, such as problem sensitivity, reasoning, and information ordering, plays a large role in determining an occupation's AI exposure. For example, surgeons are rated as far more exposed than meat slaughterers, despite similar physical ability requirements, due to the high importance of cognitive abilities for surgeons, which are more related to AI capabilities.

## Relationships

- **uses_data_from**: [[o-net|O Net]]
- **uses_data_from**: [[the-eff-ai-progress-measurement|The Eff Ai Progress Measurement]]
- **is_used_to_construct**: [[ai-industry-exposure|Ai Industry Exposure]]

---
*Extracted from: Occupational Industry And Geographic Exposure To A*