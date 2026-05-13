---
type: concept
aliases: [Pronunciation Model]
summary: A model in speech recognition that represents a word as a sequence of phone models, accounting for variations in pronunciation.
relationships:
  - target: phone-linguistics
    type: uses
  - target: speech-recognition
    type: component_of
tags: [speech-recognition, probabilistic-models, linguistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Pronunciation Model

## Definition
A pronunciation model, also known as a lexicon model, represents a word by stringing together a sequence of phone models. It essentially provides a mapping from a word to one or more sequences of phones that represent how that word can be spoken.

## Modeling Pronunciation Variation
Pronunciation models are crucial for handling the variability in human speech. They can be structured as transition diagrams to account for dialectal differences. For example, the word "tomato" can be modeled to allow for both the pronunciation [t ow mey tow] and [t ow maa t ow], with probabilities assigned to each path. The model can also capture coarticulation effects, where a sound is altered by its neighbors, by allowing for alternative phones within the sequence.

## Structure
The model is typically represented as a probabilistic state machine, such as a Hidden Markov Model (HMM). Each major state or node in the word's pronunciation model corresponds to a complete phone model. That phone model is itself a smaller state machine, often with three states (onset, middle, end) and self-loops to model variable duration. By connecting these phone models in sequence, a complete and flexible representation of a word's pronunciation is formed.

## Relationships

- **uses**: [[phone-linguistics|Phone Linguistics]]
- **component_of**: [[speech-recognition|Speech Recognition]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*