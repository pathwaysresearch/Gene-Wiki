---
type: entity
aliases: [Apache Struts]
summary: An open-source framework for creating enterprise Java web applications, which was the source of the vulnerability that led to the 2017 Equifax data breach.
relationships:
  - target: equifax
    type: vulnerability_exploited_in_breach_of
tags: [software-framework, open-source, cybersecurity-vulnerability]
sourced_from: Ai
---

# Apache Struts

## Overview
Apache Struts is an open-source software framework used by companies to create enterprise applications. It is a widely used technology, making any vulnerabilities within it a significant target for attackers.

## Role in the Equifax Breach
The massive 2017 data breach at Equifax occurred because of a specific vulnerability in the Apache Struts framework. Attackers were conducting a broad search for any sites using the vulnerable version of the software.

## The Vulnerability
The flaw in Apache Struts allowed for remote code execution. This critical vulnerability gave third-party attackers the ability to install their own programs, view, change, or delete data, and even create new user accounts on the compromised system. The problem had been identified by the National Cybersecurity and Communications Integration Center (NCCIC) just two days before the attackers found and exploited the vulnerability on Equifax's servers.

## Relationships

- **vulnerability_exploited_in_breach_of**: [[equifax|Equifax]]

---
*Extracted from: Ai*