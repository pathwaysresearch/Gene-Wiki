---
type: concept
aliases: [Open-Universe Probability Models]
summary: Probabilistic models based on first-order logic that can handle uncertainty about the existence of objects and the identity of references, where possible worlds can vary in the objects they contain.
relationships:
  - target: existence-uncertainty
    type: addresses
  - target: identity-uncertainty
    type: addresses
tags: [probabilistic-models, first-order-logic, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Open-Universe Probability Models

## Definition
Open-universe probability models (OUPMs) are a class of models based on the standard semantics of first-order logic. Unlike closed-universe models that assume a fixed set of objects, OUPMs allow for possible worlds that vary in the objects they contain and in the mappings from symbols to those objects. (Chunk 306)

## Rationale
OUPMs are necessary for domains where existence uncertainty and identity uncertainty are prevalent. A major part of cognition involves learning what objects exist and connecting observations to hypothesized objects. OUPMs provide a formal framework for this type of reasoning, which is essential for applications like vision systems exploring new environments, text understanding, and intelligence analysis. (Chunk 306)

## Goal
The primary goal of a language for OUPMs is to provide a way to write these complex models easily while guaranteeing a unique, consistent probability distribution over the potentially infinite space of possible worlds. This transfers the principles of how Bayesian networks define a unique probability model to the more expressive first-order setting. (Chunk 306)

## Relationships

- **addresses**: [[existence-uncertainty|Existence Uncertainty]]
- **addresses**: [[identity-uncertainty|Identity Uncertainty]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*