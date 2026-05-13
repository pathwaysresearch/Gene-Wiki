---
type: concept
aliases: [Identity Uncertainty]
summary: A type of uncertainty in probabilistic models concerning whether different symbols, observations, or references correspond to the same underlying real-world object.
relationships:
  - target: open-universe-probability-models
    type: is-addressed-by
  - target: sibyl-attack
    type: is-a-result-of
tags: [probabilistic-reasoning, uncertainty, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Identity Uncertainty

## Definition
Identity uncertainty is the problem of determining which symbols or observations refer to the same real-world object. This challenge arises because observations in many domains do not come with unique, reliable identifiers, forcing a system to reason about the true identity of the things it perceives. (Chunk 304, 306)

## Examples
The text illustrates identity uncertainty with several scenarios. A book retailer may not know if different ISBNs refer to the same logical book. A text-understanding system must reason about whether phrases like "Mary," "Dr. Smith," and "his cardiologist" all refer to the same person. An intelligence analyst must try to determine if various pseudonyms, phone numbers, and sightings belong to a single individual. (Chunk 304, 306)

## Modeling Challenges
Identity uncertainty, along with existence uncertainty, is a key reason that simple relational probability models can fail. It necessitates more powerful formalisms, such as open-universe probability models, which are based on the semantics of first-order logic and can explicitly model the mappings from symbols to objects. (Chunk 304, 306)

## Relationships

- **is-addressed-by**: [[open-universe-probability-models|Open Universe Probability Models]]
- **is-a-result-of**: [[sibyl-attack|Sibyl Attack]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*