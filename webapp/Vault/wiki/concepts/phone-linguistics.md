---
type: concept
aliases: [Phone (Linguistics)]
summary: A distinct speech sound that can be composed to form words, corresponding roughly to a single vowel or consonant.
relationships:
  - target: phoneme
    type: contrasted_with
  - target: pronunciation-model
    type: component_of
tags: [linguistics, phonetics, speech-recognition]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Phone (Linguistics)

## Definition
A phone is a distinct speech sound that serves as a basic unit for forming words. Linguists have identified approximately 100 different phones that can be combined to create all the words in all known human languages. A phone roughly corresponds to the sound of a single vowel or consonant, although some letter combinations like "th" produce a single phone, and some single letters can produce different phones in different contexts.

## Role in Speech Recognition
In speech recognition, phones are the fundamental building blocks used to model words. The acoustic signal is processed to identify sequences of phones, which are then assembled into words. A phone model represents the acoustic properties of a particular speech sound. For example, the phone [m] can be modeled as a sequence of three states: an onset, a middle, and an end. The model includes self-loops on these states to account for variations in the duration of the sound, from a short "m" to a long "mmmmmmmmmmm".

## Distinction from Phonemes
While a phone is any distinct speech sound, a phoneme is a sound unit that creates a distinction in meaning within a specific language. A speech recognition system for a particular language needs to distinguish between different phonemes, but can often ignore nonphonemic variations between different phones.

## Relationships

- **contrasted_with**: [[phoneme|Phoneme]]
- **component_of**: [[pronunciation-model|Pronunciation Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*