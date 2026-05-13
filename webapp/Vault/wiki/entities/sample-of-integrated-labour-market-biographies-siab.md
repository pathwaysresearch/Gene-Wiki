---
type: entity
aliases: [Sample of Integrated Labour Market Biographies (SIAB)]
summary: A 2% random sample of German social security records provided by the Institute for Employment Research (IAB), used for worker-level wage analysis.
relationships:
  - target: dynamic-artificial-intelligence-occupational-exposure-daioe-index
    type: combined_with
tags: [administrative-data, germany, labor-economics]
sourced_from: 1 S2.0 S0048733325001143 Main
---

# Sample of Integrated Labour Market Biographies (SIAB)

## Overview

The Sample of Integrated Labour Market Biographies (SIAB) is a large-scale administrative dataset provided by the Institute for Employment Research (IAB) in Germany. It consists of a 2% random sample of all individuals who have ever been registered in the German social security system.

## Data Characteristics

The SIAB contains granular, longitudinal information on individual workers, including their wages, employment history, and basic demographic and educational characteristics. The paper uses a sample restricted to full-time workers aged 20-60 for the years 2010 to 2017. Wages are deflated and imputed for top-coded values following established methodologies.

## Application in the Study

The SIAB is the primary data source for the paper's final analytical step: providing worker-level evidence on the wage implications of AI. By combining the SIAB with the time-varying DAIOE index, the researchers can investigate the relationship between increasing AI exposure and individual wages while controlling for a rich set of worker, plant, and occupation fixed effects.

## Relationships

- **combined_with**: [[dynamic-artificial-intelligence-occupational-exposure-daioe-index|Dynamic Artificial Intelligence Occupational Exposure Daioe Index]]

---
*Extracted from: 1 S2.0 S0048733325001143 Main*