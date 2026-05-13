---
type: concept
aliases: [Backus-Naur Form]
summary: A formal notation for describing the syntax of languages, using a set of rewrite rules to define how symbols can be combined into valid sequences.
tags: [formal-languages, syntax, computer-science]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Backus-Naur Form

## Definition and Syntax
Backus-Naur Form (BNF) is a notation used to define a grammar through a set of rewrite rules. A rule, such as 'Sentence -> NounPhrase VerbPhrase', specifies that a sequence of symbols on the right-hand side can be categorized as the symbol on the left-hand side. The arrow '->' is the rewrite operator, and the vertical bar '|' is used as an abbreviation for multiple rules with the same left-hand side, such as 'S -> A | B'.

## Example: Arithmetic Expressions
The text provides a BNF grammar for simple arithmetic expressions to illustrate its use. The grammar includes rules like 'Expr -> Expr Operator Expr | ( Expr ) | Number', which recursively define what constitutes a valid expression. It also defines terminals like digits ('Digit -> 0 | 1 | ... | 9') and operators ('Operator -> + | - | × | ÷').

## Notational Variations
It is noted that different authors may use slightly different notations for BNF. Common variations include using angle brackets for nonterminal symbols (e.g., '<Digit>' instead of 'Digit'), using quotes for terminal symbols (e.g., 'word' instead of **word**), or using '::=' as the rewrite operator instead of '->'.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*