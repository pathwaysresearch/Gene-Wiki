---
type: entity
aliases: [Dictionary of Occupational Titles (DOT)]
summary: A U.S. Department of Labor publication providing detailed descriptions of occupational tasks, used in research to measure occupations' exposure to automation innovations. A publication by the U.S. Department of Labor that provides standardized and detailed descriptions of jobs and occupations.
relationships:
  - target: reinstatement-effect
    type: is_a_data_source_for
  - target: automation-innovations
    type: is_data_source_for
  - target: us-department-of-labor
    type: published_by
tags: [data-source, us-department-of-labor, occupational-classification, government-publication]
sourced_from: Acss Newfrontiers 20220814
---

# Dictionary of Occupational Titles (DOT)

## Overview
The Dictionary of Occupational Titles (DOT) is a comprehensive publication by the U.S. Department of Labor's Employment and Training Administration. It provides highly detailed descriptions of the tasks that workers perform in specific occupations, making it a valuable resource for labor market research.

## Application in Measuring Automation
In the study by Autor et al., the DOT serves as the primary text corpus for identifying automation innovations. The methodology involves finding similarities between the text of U.S. patents and the detailed task descriptions contained within the DOT. This allows researchers to link specific technologies, such as an 'Automatic mail processing apparatus,' to the occupations whose tasks they are designed to automate, like 'Mail and paper handlers.'

## Versions Used in Research
To provide a representative measure of occupational tasks across the full eight-decade period of analysis, the study utilizes two different historical versions of the DOT. The 1939 edition of the DOT is employed for the 1940-1980 period, while the 1977 edition is used for the subsequent 1980–2018 period.

## Relationships

- **is_data_source_for**: [[automation-innovations|Automation Innovations]]
- **published_by**: [[us-department-of-labor|Us Department Of Labor]]

---
*Extracted from: Acss Newfrontiers 20220814*

---
*Also referenced in: Automation And New Tasks   How Technology Displace*