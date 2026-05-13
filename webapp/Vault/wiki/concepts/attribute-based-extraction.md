---
type: concept
aliases: [Attribute-Based Extraction]
summary: A type of information extraction that assumes a text refers to a single object and aims to extract its attributes, such as price or model number, using predefined templates.
relationships:
  - target: regular-expression
    type: uses
tags: [information-extraction, natural-language-processing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Attribute-Based Extraction

## Definition
Attribute-based extraction is one of the simplest types of information extraction systems. It operates under the assumption that the entire text being analyzed refers to a single object, and the goal is to extract specific attributes of that object.

## How It Works
The process works by defining a template, also known as a pattern, for each attribute that needs to be extracted. These templates are defined using a finite state automaton, with the regular expression being the simplest and most common example of such a pattern.

## Example
For a text like "IBM ThinkBook 970. Our price: $399.00", an attribute-based extraction system would aim to extract the set of attributes {Manufacturer=IBM, Model=ThinkBook970, Price=$399.00}. This is achieved by applying predefined templates, likely built with regular expressions, to match and capture the value for each attribute.

## Relationships

- **uses**: [[regular-expression|Regular Expression]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*