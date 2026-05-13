---
type: concept
aliases: [Ascending-Bid Auction]
summary: A common auction format, also known as the English auction, where the price is progressively increased until only one bidder remains.
relationships:
  - target: auction
    type: is-a-type-of
tags: [mechanism-design, auctions]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Ascending-Bid Auction

## How It Works
The ascending-bid auction, or English auction, is a well-known auction mechanism. The process begins with an auctioneer announcing a minimum or reserve bid. Bidders then successively offer higher prices. The auction continues as long as there are multiple interested bidders and concludes when no one is willing to top the current highest bid. The last remaining bidder wins the item.

## Strategic Properties
This auction format has several important properties. It encourages a simple dominant strategy for bidders: continue bidding as long as the current price is below your private value `v_i`. This generally ensures that the bidder with the highest valuation for the item wins it. However, the mechanism is not perfectly truth-revealing, as the winner only reveals that their value is at least the final price plus the bid increment, not its exact amount.

## Disadvantages
From the seller's perspective, the ascending-bid auction can discourage competition. If one bidder is widely known to have a significant advantage and thus a much higher valuation, potential competitors may not bother to enter the auction, allowing the advantaged bidder to win at a low price. Another drawback is the high communication cost, as it requires all bidders to be present simultaneously, either physically or via high-speed, secure communication links.

## Relationships

- **is-a-type-of**: [[auction|Auction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*