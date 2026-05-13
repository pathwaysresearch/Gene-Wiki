---
type: entity
aliases: [Bonaparte (Software)]
summary: A software system based on Bayesian networks, used by the Netherlands Forensic Institute for DNA identification in criminal, missing-person, and disaster-victim cases.
relationships:
  - target: bayesian-networks
    type: is_an_application_of
  - target: netherlands-forensic-institute
    type: used_by
tags: [software, forensics, dna-analysis, bayesian-networks]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Bonaparte (Software)

## Overview

Bonaparte is a software tool used daily by the Netherlands Forensic Institute for complex DNA identification tasks. It is particularly powerful in mass disaster scenarios, such as the crash of Malaysia Airlines Flight 17, where victims cannot be identified through simple database matching.

## How It Works

Bonaparte's core innovation is its ability to use DNA information from distant or multiple relatives. It achieves this by converting a family's pedigree (family tree) into a causal Bayesian network. This allows it to integrate partial DNA matches from various family members (e.g., aunts, second cousins) to calculate the likelihood of an identification, overcoming the limitations of conventional methods like the Paternity Index which only work for close, specified relations.

## Key Advantages

The system is described as integrative, reacting as a whole to new information like a "living organic tissue." It is also transparent, allowing investigators to understand how each piece of evidence influences the final result, unlike "black box" machine learning approaches. While it provides a ranked list of likely identifications and likelihood ratios, the final decision is still made by human experts who can combine the DNA evidence with other information.

## Relationships

- **is_an_application_of**: [[bayesian-networks|Bayesian Networks]]
- **used_by**: [[netherlands-forensic-institute|Netherlands Forensic Institute]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*