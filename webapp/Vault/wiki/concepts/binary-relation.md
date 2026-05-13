---
type: concept
aliases: [Binary Relation]
summary: A concept that describes a relationship between two objects, represented either as a set of ordered pairs in mathematics or as a (subject, verb, object) triplet in AI.
tags: [knowledge-representation, mathematics, ai]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Binary Relation

## Mathematical Definition
In mathematics, a binary relation is formally defined as a set of ordered pairs of objects. If a pair of objects, such as (1, 2), is in the set defining the "is less than" relation, then the objects are said to have that relation. If a pair, such as (2, 1), is not in the set, they do not have the relation.

## Representation in AI
In the context of artificial intelligence and knowledge bases, a relation is conceptualized as a sentence in a simple, highly structured language. It typically takes the form of a triplet of tokens: (subject, verb, object), with values like (entity_i, relation_j, entity_k). In this structure, the relation plays the role of the verb connecting two entities.

## Examples and Usage
The entities involved in a relation are not limited to numbers. For example, a relation `is_a_type_of` could contain the tuple (dog, mammal). This structured representation is fundamental for applications that require representing knowledge and reasoning about it, particularly within the context of neural networks.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*