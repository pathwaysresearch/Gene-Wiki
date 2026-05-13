---
type: concept
aliases: [Market Value Regression]
summary: A statistical method used to estimate the value of intangible assets by regressing a firm's market value on its observable capital stocks.
relationships:
  - target: intangible-capital
    type: is_used_to_estimate
  - target: q-theory-of-investment
    type: is_related_to
tags: [econometrics, valuation, corporate-finance]
sourced_from: W25148
---

# Market Value Regression

## Definition
A market value regression is an econometric technique used to infer the value of a firm's assets, including unmeasured intangible capital, from its stock market valuation. The method assumes that capital markets efficiently price corporate securities in expectation, meaning a firm's market value reflects the risk-adjusted discounted expected value of its entire asset stock, both tangible and intangible.

## How It Works
The method involves regressing the market value of firms on their observable capital types, such as R&D capital and total assets. The coefficients obtained from this regression on each capital type represent the market's "shadow value" for each dollar of that observable capital, which includes the value of any correlated intangible assets. The paper uses this approach to estimate these values on a year-by-year basis to allow for dynamic changes in the valuation of intangibles.

## Application in the Study
The study uses the coefficients from year-by-year market value regressions as a key input for calculating productivity adjustments. For instance, the time series of the R&D coefficient reveals substantial variation in the shadow value of R&D-related intangible assets. This set of estimates is then used to compute the implied productivity growth adjustments for the model, forming the basis for constructing the Productivity J-curve.

## Relationships

- **is_used_to_estimate**: [[intangible-capital|Intangible Capital]]
- **is_related_to**: [[q-theory-of-investment|Q Theory Of Investment]]

---
*Extracted from: W25148*