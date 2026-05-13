---
type: entity
aliases: [FASTUS System]
summary: An information extraction system that uses a cascaded finite-state transducer to extract information from natural language text.
relationships:
  - target: interpretation-as-abduction
    type: implements-principles-of
tags: [information-extraction, natural-language-processing, finite-state-transducer]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# FASTUS System

## Overview
FASTUS is a system designed for extracting structured information from unstructured natural language text. It was developed by Jerry R. Hobbs and colleagues, as described in a 1997 publication.

## Architecture
The core architecture of FASTUS is a "cascaded finite-state transducer." This approach processes text through a series of levels or stages, each implemented as a finite-state machine, to progressively identify and structure information, from basic phrases to complex events.

## Theoretical Foundations
The design of FASTUS is connected to a broader theory of "Interpretation as abduction," proposed by Hobbs, Stickel, Appelt, and Martin in a 1993 AIJ paper. This theory frames the process of understanding text as finding the best logical explanation (abduction) for the linguistic phenomena observed, a principle that informs the design of practical systems like FASTUS.

## Relationships

- **implements-principles-of**: [[interpretation-as-abduction|Interpretation As Abduction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*