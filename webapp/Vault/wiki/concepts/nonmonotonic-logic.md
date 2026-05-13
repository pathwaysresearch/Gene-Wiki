---
type: concept
aliases: [Nonmonotonic Logic]
summary: A form of logical inference where adding new information can cause previously valid conclusions to be retracted.
relationships:
  - target: answer-set-programming
    type: related-to
tags: [knowledge-representation, logic, reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Nonmonotonic Logic

## Core Idea
Nonmonotonic logic provides a formal framework for reasoning where conclusions are defeasible. Unlike standard monotonic logic, where the set of conclusions only grows with new information, nonmonotonic systems allow for the invalidation of old conclusions when new axioms are added.

## Key Formalisms
The three primary formalisms for nonmonotonic inference were all introduced in a 1980 special issue of the AI Journal. These are circumscription, developed by John McCarthy; default logic, developed by Raymond Reiter; and modal nonmonotonic logic, developed by Drew McDermott and John Doyle.

## Applications and Extensions
Nonmonotonic logics have seen renewed interest for use in large-scale knowledge representation systems. A notable commercial application is the BENINQ system, which handles insurance-benefit inquiries using a nonmonotonic inheritance system. The formalism is also related to answer set programming, which can be viewed as an extension of the negation-as-failure approach or a refinement of circumscription.

## Relationships

- **related-to**: [[answer-set-programming|Answer Set Programming]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*