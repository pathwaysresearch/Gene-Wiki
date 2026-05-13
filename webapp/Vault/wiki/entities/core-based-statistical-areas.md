---
type: entity
aliases: [Core-Based Statistical Areas (CBSAs)]
summary: Geographic areas defined by the U.S. government, consisting of an urban center and adjacent counties tied by commuting, used to analyze regional economic activity.
relationships:
  - target: ai-divide
    type: used_to_measure
tags: [geography, us-government, statistical-unit]
sourced_from: Ai
---

# Core-Based Statistical Areas (CBSAs)

## Definition
A Core-Based Statistical Area (CBSA) is a formally defined geographic area in the United States. It consists of one or more counties (or equivalent administrative units) that contain an urban center with a population of at least 10,000 people. The CBSA also includes any adjacent counties that are socioeconomically tied to the urban center, a connection that is primarily determined by commuting patterns.

## Application in AI Research
CBSAs are the primary geographic unit used in the study to analyze the location of AI adoption among firms. The research finds that startups located in large CBSAs have a statistically significant higher probability of using AI compared to firms in micropolitan or rural areas. The analysis identifies specific CBSAs, including both established tech hubs and other large metro areas, that exhibit high concentrations of AI use.

## Methodological Use
For the purposes of the study, multi-unit firms were assigned to a single CBSA by identifying the zip code within the firm that had the maximum employment. To protect the confidentiality of the underlying data, some detailed reporting in the study was restricted to the 30,000 startups located in the largest CBSAs, defined as those with a population of one million or more.

## Relationships

- **used_to_measure**: [[ai-divide|Ai Divide]]

---
*Extracted from: Ai*