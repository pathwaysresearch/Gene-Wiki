---
type: concept
aliases: [Content-Based Addressing]
summary: A memory access mechanism where the weight used to read from or write to a memory cell is a function of that cell's content, enabling retrieval based on partial matches.
relationships:
  - target: neural-turing-machine
    type: component-of
tags: [memory-augmented-networks, attention-mechanisms, ntm]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Content-Based Addressing

## Definition
Content-based addressing is a method for accessing an external memory in models like the Neural Turing Machine. Unlike location-based addressing, which refers to a memory cell by its position, content-based addressing allows the network to find and retrieve information based on the data stored within the memory cells themselves.

## How It Works
This mechanism functions by comparing a query pattern produced by the network with the contents of all memory cells. The weight assigned to each cell for reading or writing is a function of the similarity between the query and the cell's content. This allows the model to retrieve a complete vector-valued memory even if the query pattern matches only some of its elements. An analogy is a person recalling the full lyrics of a song after being prompted with just a few words from the chorus.

## Advantages
Content-based addressing is particularly useful when the objects stored in memory are large, such as vectors. By allowing retrieval based on partial information, it provides a flexible and powerful way for a neural network to interact with a knowledge base. This capability is crucial for tasks that require associating and recalling complex, structured information.

## Relationships

- **component-of**: [[neural-turing-machine|Neural Turing Machine]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*