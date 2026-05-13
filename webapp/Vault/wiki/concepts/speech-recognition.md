---
type: concept
aliases: [Speech Recognition]
summary: The task of identifying and transcribing a sequence of words uttered by a speaker from an acoustic signal.
relationships:
  - target: pronunciation-model
    type: uses
  - target: phone-linguistics
    type: uses
  - target: phoneme
    type: uses
tags: [speech-processing, natural-language-processing, applied-ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Speech Recognition

## Definition and Applications
Speech recognition is the task of identifying a sequence of words uttered by a speaker, given the acoustic signal. It is a major application of artificial intelligence, used by millions of people in daily applications such as navigating voice mail systems, searching the web from mobile phones, and hands-free operation of machinery.

## Key Challenges
The task is difficult due to the ambiguous and noisy nature of spoken language. One major issue is **segmentation**, as words in fast speech often lack the clear pauses or spaces found in written text. A second challenge is **coarticulation**, where the pronunciation of a sound is affected by adjacent sounds, such as the 's' in "nice" and 'b' in "beach" merging into a sound close to "sp". A third problem is the existence of **homophones**, which are words that sound identical but have different meanings and spellings, like "to," "too," and "two."

## Factors Affecting Accuracy
The performance of a speech recognition system is influenced by several factors. The quality of the acoustic signal is crucial; a high-quality microphone in a quiet environment yields better results than a phone microphone in a noisy car. The vocabulary size also matters significantly, with word error rates increasing from under 0.5% for recognizing digits (11-word vocabulary) to 10% for news stories (20,000-word vocabulary) and 20% for a 64,000-word vocabulary. Finally, the specificity of the task can mitigate errors; a system for booking flights can often succeed even with a word error rate of 10% or more because the context limits the possibilities.

## Relationships

- **uses**: [[pronunciation-model|Pronunciation Model]]
- **uses**: [[phone-linguistics|Phone Linguistics]]
- **uses**: [[phoneme|Phoneme]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*