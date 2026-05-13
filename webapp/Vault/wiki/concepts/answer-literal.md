---
type: concept
aliases: [Answer Literal]
summary: A special literal added to a negated goal in a resolution proof to extract the specific variable bindings that satisfy an existential query.
relationships:
  - target: resolution-inference-rule
    type: is-a-technique-for
tags: [resolution, theorem-proving, query-answering]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Answer Literal

## Purpose
Resolution can sometimes produce nonconstructive proofs for existential goals. For example, it might prove that *someone* killed a victim without identifying the killer. The answer literal is a technique designed to extract a specific, constructive answer from the proof process.

## How It Works
To use this method, a special literal, `Answer(v)`, where `v` is the variable of interest, is added to the negated goal clause. For instance, the query $\neg \text{Kills}(w, \text{Tuna})$ is modified to become $\neg \text{Kills}(w, \text{Tuna}) \vee \text{Answer}(w)$. The resolution process then proceeds as normal, carrying the `Answer` literal along in the resolvents.

## Extracting the Answer
The proof successfully finds an answer when it generates a clause that contains only a single answer literal. For example, deriving the clause `Answer(Curiosity)` provides the specific binding for the query variable. This avoids the ambiguity of a nonconstructive proof, which might otherwise result in a disjunctive clause like `Answer(Curiosity) \vee Answer(Jack)` that does not constitute a single, concrete answer.

## Relationships

- **is-a-technique-for**: [[resolution-inference-rule|Resolution Inference Rule]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*