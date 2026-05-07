---
type: entity
aliases: [Bezos Mandate]
summary: A 2002 directive from Amazon CEO Jeff Bezos mandating that all teams expose their data and functionality through externalizable service interfaces.
tags: [directive, amazon, software-architecture, api]
sourced_from: Ai
---

# Bezos Mandate

## Overview

The Bezos Mandate refers to an email sent by Amazon's CEO, Jeff Bezos, to all development teams in 2002. The directive was issued at a time when the online retailer had reportedly "hit a wall."

## Core Directives

The mandate stipulated that all teams must expose their data and functionality through service interfaces. It explicitly forbade any other form of inter-process communication, including direct linking, direct reads of another team's data store, or shared-memory models. The only permitted communication was via service interface calls over the network.

## Externalization Requirement

A critical and non-negotiable part of the mandate was that all service interfaces had to be designed from the ground up to be externalizable. This meant teams had to plan for the possibility of exposing the interface to developers outside the company. The email concluded by stating that anyone who did not comply would be fired.

---
*Extracted from: Ai*