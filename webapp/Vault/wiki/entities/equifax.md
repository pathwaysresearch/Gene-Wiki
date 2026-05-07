---
type: entity
aliases: [Equifax]
summary: A credit-reporting company that suffered a massive 2017 data breach, exposing the personal information of nearly half the US population.
relationships:
  - target: apache-struts
    type: used
tags: [company, data-breach, cybersecurity]
sourced_from: Ai
---

# Equifax

## Overview
Equifax is a credit-reporting company that, under the leadership of CEO Richard Smith starting in 2005, transformed from a staid business into one focused on expanding the amount of consumer data it stored and monetizing it. This strategy of centralizing vast amounts of sensitive personal data created what one former manager called a "nightmare scenario" for a potential breach.

## The 2017 Data Breach
In September 2017, Equifax disclosed a major data breach that exposed the sensitive personal information of 147.9 million consumers. The compromised data included names, Social Security numbers, birth dates, addresses, driver's license numbers, and credit card numbers.

## Cause of the Breach
According to the US Government Accountability Office, the breach was not the result of a targeted attack on Equifax specifically. Instead, attackers were conducting a wide-ranging search for a known vulnerability in an open-source framework called Apache Struts. This vulnerability allowed for remote code execution, enabling the attackers to install programs and access or alter data. The vulnerability had been identified by the National Cybersecurity and Communications Integration Center two days before the attackers exploited it on Equifax's systems.

## Relationships

- **used**: [[apache-struts|Apache Struts]]

---
*Extracted from: Ai*