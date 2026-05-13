---
type: concept
aliases: [Structured Output]
summary: A type of machine learning task where the output is a data structure with multiple, inter-related values, such as a sentence, a grammatical parse tree, or an image segmentation map.
relationships:
  - target: supervised-learning
    type: is_type_of
tags: [machine-learning-task, supervised-learning, output-representation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Structured Output

## Definition
Structured output tasks are a broad category of machine learning problems where the desired output is a vector or another data structure containing multiple values that have important relationships between them. Unlike simple classification which outputs a single category, structured output models must produce several values that are all tightly inter-related. For example, in image captioning, the words produced must form a coherent and grammatically correct sentence.

## Examples and Applications
This category subsumes a wide variety of tasks. One example is parsing, which involves mapping a natural language sentence into a tree that describes its grammatical structure. Another application is the pixel-wise segmentation of images, where a program assigns every pixel in an image to a specific category, such as annotating the locations of roads in aerial photographs. Image captioning, where a program observes an image and outputs a natural language sentence describing it, is also a prominent structured output task.

## Categorization
Structured output problems are traditionally considered a form of supervised learning. The output's form does not necessarily have to mirror the input's structure closely. While tasks like transcription and translation can be considered types of structured output, the category is much broader, encompassing any problem requiring a complex, multi-part output.

## Relationships

- **is_type_of**: [[supervised-learning|Supervised Learning]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*