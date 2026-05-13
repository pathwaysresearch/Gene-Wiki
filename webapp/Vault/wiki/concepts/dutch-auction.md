---
type: concept
aliases: [Dutch Auction]
summary: An auction format where the seller starts at a high price and progressively lowers it until a buyer accepts the current price and wins the item.
relationships:
  - target: english-auction
    type: is_the_opposite_of
tags: [auction-theory, mechanism-design, pricing]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Dutch Auction

## Definition
A Dutch auction is a type of auction that operates in descending price order. It is presented in contrast to an English auction, where bidding starts at a low price and increases.

## How It Works
The seller begins by announcing a high price for an item. This price is then gradually lowered by set increments, $d$. The auction ends as soon as a buyer agrees to pay the currently announced price. That buyer becomes the winner and pays that price. If multiple bidders accept the same price simultaneously, one is chosen arbitrarily to be the winner.

## Strategic Considerations
The text poses the question of whether a Dutch auction, assuming rational bidders and arbitrarily small price decrements, guarantees that the bidder with the highest valuation for the item will win. This highlights the strategic element for bidders, who must decide the optimal price point at which to accept, balancing the risk of losing the item to another bidder against the benefit of paying a lower price.

## Relationships

- **is_the_opposite_of**: [[english-auction|English Auction]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*