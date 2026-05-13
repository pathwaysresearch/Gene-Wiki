---
type: concept
aliases: [Monty Hall Problem]
summary: A famous probability puzzle in which a contestant must choose whether to stick with their initial choice of three doors or switch, after the host opens another door to reveal a non-winning prize.
relationships:
  - target: collider-bias
    type: is_an_example_of
  - target: marilyn-vos-savant
    type: is_associated_with
tags: [paradox, probability-theory, causal-reasoning]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Monty Hall Problem

## The Puzzle
The Monty Hall problem involves a game show scenario with three doors: behind one is a car, and behind the other two are goats. A contestant picks a door. The host, who knows where the car is, then opens one of the other two doors to reveal a goat. The contestant is then given the choice to either stick with their original door or switch to the other unopened door. The puzzle, famously solved by Marilyn vos Savant, sparked intense debate, with many academics incorrectly arguing that switching makes no difference.

## The Causal Explanation
The text explains the problem using a causal diagram, identifying the host's action, "Door Opened," as a collider. This variable is causally influenced by two parents: "Your Door" (the contestant's choice) and "Location of Car." Because the host must open a door that is not the contestant's choice and does not contain the car, his action is dependent on both factors. When the host opens a door, the contestant gains information, and conditioning on this collider creates a spurious dependence between the contestant's initial choice and the car's actual location.

## The Source of Intuitive Error
The paradox is powerful because human intuition is wired for causal, not probabilistic, reasoning. As the text states, there is no direct causal connection between "My Door" and "Location of Car." People intuitively (and incorrectly) assume these variables remain probabilistically independent, even after the host provides new information by opening a door. This causal intuition leads to the systematic probabilistic mistake of believing the odds are 50-50 after the host's reveal, when in fact switching doubles the chance of winning.

## Relationships

- **is_an_example_of**: [[collider-bias|Collider Bias]]
- **is_associated_with**: [[marilyn-vos-savant|Marilyn Vos Savant]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*