---
type: concept
aliases: [Auction]
summary: A mechanism for selling goods to a pool of bidders, where each bidder has a value for the item and makes bids to acquire it.
relationships:
  - target: ascending-bid-auction
    type: has-type
tags: [mechanism-design, game-theory, economics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Auction

## Definition
An auction is a formal mechanism designed for selling goods, typically a single item, to a group of potential buyers known as bidders. Each bidder `i` possesses a utility value, denoted as `v_i`, which represents how much they value possessing the item. Bidders submit bids, `b_i`, and the mechanism's rules determine the winner and the price paid.

## Types of Value
The source of a bidder's value `v_i` can be categorized in two main ways. A **private value** auction is one where each bidder's valuation is unique and personal to them, independent of others' valuations. An example is a collector bidding on a broken laser pointer. In contrast, a **common value** auction involves an item that has a single true, objective value, such as an oil tract. In this case, bidders have different estimates of this common value based on their own private information.

## Mechanism Design
The design of an auction involves specifying the rules for bidding, how the winner is determined (usually the highest bid), and, crucially, the price the winner pays. The price paid does not necessarily have to be the winning bid amount; this is a key element of mechanism design.

## Relationships

- **has-type**: [[ascending-bid-auction|Ascending Bid Auction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*