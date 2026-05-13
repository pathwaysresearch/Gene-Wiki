---
type: concept
aliases: [Sibyl Attack]
summary: A type of attack on a reputation system where a single malicious entity creates a large number of pseudonymous identities (sibyls) to gain a disproportionately large influence.
relationships:
  - target: identity-uncertainty
    type: is-a-cause-of
tags: [computer-security, reputation-systems, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Sibyl Attack

## Definition
A sibyl attack is the use of multiple fake identities, known as sibyls, by a dishonest entity to confound a reputation system. The term is prominent in the computer security field and represents a significant challenge for systems that rely on user identity. (Chunk 304)

## Mechanism
The attack is executed by a single user creating a large number, potentially thousands, of distinct login IDs or other identifiers. This proliferation of identities makes it difficult for a system to determine the true number of distinct participants, allowing the attacker to subvert trust and reputation mechanisms that assume a one-to-one correspondence between identifiers and real-world entities. (Chunk 304)

## Impact
A successful sibyl attack leads to identity uncertainty, where the system cannot be sure which symbols (e.g., login IDs) refer to the same underlying person. This undermines applications like recommendation systems, where a dishonest customer could use many IDs to manipulate ratings, or other online domains that rely on a community's reputation. (Chunk 304)

## Relationships

- **is-a-cause-of**: [[identity-uncertainty|Identity Uncertainty]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*