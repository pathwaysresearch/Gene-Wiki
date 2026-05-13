---
type: concept
aliases: [Partition (in Ontology)]
summary: A division of a category into a set of subclasses that are both mutually exclusive (disjoint) and collectively exhaustive.
relationships:
  - target: category
    type: is-a-property-of
tags: [knowledge-representation, ontology, set-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Partition (in Ontology)

## Definition
In the context of knowledge representation, a partition is a set of subclasses that form a disjoint exhaustive decomposition of a parent category. This means that every member of the parent category belongs to exactly one of the subclasses in the partition.

## Constituent Concepts
A partition is defined by two key properties. First, the subclasses must be **disjoint**, meaning they have no members in common. For example, the categories *Animals* and *Vegetables* are disjoint. Second, the subclasses must form an **exhaustive decomposition**, meaning that taken together, they cover all members of the parent category.

## Example
The categories {*Males*, *Females*} form a partition of the category *Animals*. They are disjoint (an animal cannot be both male and female) and their decomposition is exhaustive (any animal is either male or female). In contrast, {*Americans*, *Canadians*, *Mexicans*} is an exhaustive decomposition of *NorthAmericans* but not a partition, because a person can have dual citizenship and thus belong to more than one subclass.

## Relationships

- **is-a-property-of**: [[category|Category]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*