---
type: concept
aliases: [Mendelian Randomization]
summary: A method that uses genetic variants as instrumental variables to investigate the causal effect of a modifiable exposure on a disease outcome.
relationships:
  - target: instrumental-variable
    type: is_an_application_of
tags: [genetics, epidemiology, causal-inference]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Mendelian Randomization

## Definition
Mendelian randomization is a causal inference method that uses naturally occurring genetic variation as an instrument to study the causal effect of a modifiable exposure (like cholesterol levels) on a disease or health outcome (like heart attacks). It leverages the fact that genes are randomly assigned at conception, mimicking a randomized controlled trial and thus avoiding many common confounding factors like lifestyle.

## How It Works
The text illustrates the method with a causal diagram for the effect of HDL cholesterol on heart attacks. A specific 'HDL Gene' (the instrument) influences 'HDL Levels' (the exposure). 'Lifestyle' is a confounder that affects both HDL Levels and the risk of a 'Heart Attack' (the outcome). Because the gene is not influenced by lifestyle and is assumed to affect heart attack risk only through its effect on HDL levels, it can be used to estimate the true causal effect of HDL on heart attacks, free from lifestyle confounding.

## Example: Cholesterol and Heart Disease
The text cites a 2012 collaborative study led by Sekar Kathiresan that used Mendelian randomization to investigate cholesterol's effect on heart attack risk. The study found no observable benefit from higher HDL ('good') cholesterol levels. In contrast, it confirmed that LDL ('bad') cholesterol has a very large causal effect, with a 34 mg/dl decrease in LDL reducing heart attack chances by about 50 percent. This demonstrates the power of the method to challenge conventional wisdom.

## Relationships

- **is_an_application_of**: [[instrumental-variable|Instrumental Variable]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*