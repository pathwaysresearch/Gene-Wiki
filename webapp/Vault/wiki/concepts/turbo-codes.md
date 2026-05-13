---
type: concept
aliases: [Turbo Codes]
summary: A class of high-performance error-correcting codes used in telecommunications, whose decoding process can be represented as belief propagation on a Bayesian network.
relationships:
  - target: bayesian-networks
    type: is_an_application_of
  - target: belief-propagation
    type: uses_method
tags: [telecommunications, error-correction, coding-theory]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Turbo Codes

## Overview

Turbo codes are a type of error-correcting code used to protect information transmitted over a noisy channel. Their decoding process was independently discovered by Claude Berrou and can be modeled using a Bayesian network.

## Bayesian Network Representation

The process can be represented as a Bayesian network where hidden information bits are encoded into two separate, scrambled codewords. These are transmitted and received as noisy, visible versions. The decoding process aims to recover the original hidden information bits from the noisy received data.

## Decoding via Belief Propagation

Decoding of turbo codes is achieved through an iterative process of belief propagation on this network. Two processors, each observing one of the noisy codewords, pass information back and forth. Each processor uses the information from the other to improve its own guess of the hidden codeword, repeating the process until a reliable estimate is reached.

## Relationships

- **is_an_application_of**: [[bayesian-networks|Bayesian Networks]]
- **uses_method**: [[belief-propagation|Belief Propagation]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*