---
type: entity
aliases: [O*NET]
summary: A database providing detailed information on U.S. occupations, including tasks and Detailed Worker Activities (DWAs), used as the primary source for job task data in this study. A source of occupational information, including a database and a framework for defining basic skills required for learning and work.
relationships:
  - target: ai-occupational-exposure
    type: provides_data_for
  - target: exposure-to-llms
    type: is_data_source_for
  - target: bureau-of-labor-statistics
    type: is_linked_to
  - target: o-net-basic-skills
    type: defines
tags: [database, us-government, labor-data, occupational-information]
sourced_from: 2303.10130V5
---

# O*NET

## Overview
O*NET is a comprehensive database that serves as a primary source of occupational information in the United States. It contains detailed descriptions of various jobs, breaking them down into their constituent components.

## Data Structure
The dataset used in this study from O*NET included 19,265 tasks and 2,087 Detailed Worker Activities (DWAs). Each task is described and linked to a corresponding occupation. Most DWAs are connected to one or more tasks, providing a granular view of the activities that constitute a job.

## Use in the Study
The O*NET task and DWA data formed the foundational dataset for measuring LLM exposure. Both human annotators and GPT-4 applied an exposure rubric to these tasks and DWAs to determine the extent to which they could be affected by LLMs. To connect this task-level analysis with broader economic data, the O*NET dataset was linked to wage and employment data from the Bureau of Labor Statistics using a recommended crosswalk.

## Relationships

- **is_data_source_for**: [[exposure-to-llms|Exposure To Llms]]
- **is_linked_to**: [[bureau-of-labor-statistics|Bureau Of Labor Statistics]]
- **defines**: [[o-net-basic-skills|O Net Basic Skills]]

---
*Extracted from: 2303.10130V5*

---
*Also referenced in: Occupational Industry And Geographic Exposure To A*