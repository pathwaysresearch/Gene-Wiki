---
type: concept
aliases: [Regular Expression]
summary: A sequence of characters that specifies a search pattern, often used in information extraction as a simple type of finite-state automaton to define templates for finding specific attributes in text.
tags: [information-extraction, text-processing, pattern-matching]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Regular Expression

## Definition and Role
A regular expression, or regex, is a sequence of characters that defines a search pattern. It is considered the simplest example of a finite state automaton. In the context of information extraction, regular expressions are used to define templates or patterns for extracting specific attributes from unstructured text.

## How It Works
Regular expressions are constructed using a special syntax of characters and metacharacters to match patterns. For example, `[0-9]+` matches one or more digits, and `?` makes a preceding group optional. By combining these elements, a complex pattern like `[$][0-9]+([.][0-9][0-9])?` can be constructed to match various dollar price formats, such as $249.99 or $1000000.

## Applications
Regular expressions are a fundamental tool in computing and are widely used in many applications. They are found in Unix command-line tools like `grep`, are a core feature of programming languages such as Perl, and are used for find-and-replace operations in word processors like Microsoft Word.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*