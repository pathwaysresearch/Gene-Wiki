---
type: concept
aliases: [Multi-slot Next-Price Auction]
summary: An auction mechanism used by internet search engines to sell multiple ad slots, where each winner pays the price bid by the next-lower bidder. Unlike a single-item second-price auction, this mechanism is not truth-revealing.
relationships:
  - target: second-price-auction
    type: is_an_extension_of
tags: [auction-theory, online-advertising, mechanism-design]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Multi-slot Next-Price Auction

## Definition
A multi-slot next-price auction is a mechanism for selling multiple, or k, items, such as ad slots on a search engine results page. The highest bidder wins the top spot, the second-highest bidder wins the second spot, and so on for all available slots.

## Payment Rule
The payment rule is an extension of the second-price concept where each winning bidder pays the price that was bid by the next-lower bidder. For example, the winner of the top slot pays the amount bid by the second-highest bidder. In the context of online advertising, the text specifies that payment is made only if the searcher actually clicks on the ad.

## Strategic Behavior
This mechanism is not truth-revealing, meaning bidders have an incentive to bid something other than their true valuation. The text provides an example where the top slots are more valuable due to higher click probability. A bidder with the highest true valuation can increase their expected return by strategically lowering their bid to win a lower-ranked, but more profitable, slot. This forces bidders to expend significant effort analyzing the bids of others to determine their optimal bid, rather than simply bidding their true value.

## Relationships

- **is_an_extension_of**: [[second-price-auction|Second Price Auction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*