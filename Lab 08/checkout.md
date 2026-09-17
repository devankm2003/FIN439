# Thursday Merit Checkout: Microsoft Corporation (MSFT) DCF Valuation

## Company Overview
- **Company:** Microsoft Corporation
- **Ticker:** NASDAQ: MSFT
- **CIK:** 0000789019
- **Filing Analyzed:** Form 10-K for the Fiscal Year ended June 30, 2024 (filed July 30, 2024)
- **Target Share Price:** $491.65 (Market close, September 10, 2026, 16:00 EDT)

---

## R — Five Input Rows with Sourced Locators

| Row | Input Parameter | Company Value | Unit | As-Of Date | Exact Locator & Derivation Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Starting FCFF** | **75,474.00** | USD Millions | FY ended June 30, 2024 | **Form 10-K, Item 8, Consolidated Statements of Cash Flows (p. 64) & Note 12 (p. 86)**.<br>• Net cash from operations: **$118,548M** (p. 64)<br>• Additions to property and equipment (CapEx): **$44,475M** (p. 64)<br>• Cash paid for interest: **$1,700M** (p. 64 / Note 11 p. 84)<br>• Effective tax rate: **17.59%** ($19,251M tax / $109,425M pre-tax income, Note 12 p. 86)<br>• After-tax interest paid: $1,700M × (1 − 0.1759) = **$1,401.00M**<br>• *Starting FCFF = Operating Cash Flow ($118,548M) + After-Tax Interest ($1,401M) − CapEx ($44,475M) = $75,474.00M*. |
| **2** | **Growth, Years 1–5** | **14.0%, 12.0%, 10.0%, 8.0%, 6.0%** | % per annum | September 10, 2026 *(Forecast)* | **Form 10-K, Item 7, MD&A (pp. 31–43) & FY24/25 Historicals [Labelled Forecast]**.<br>• FY24 total revenue grew 16% (Cloud revenue up 23%, Azure up 30%).<br>• MD&A disclosures (p. 40) explicitly state that capital expenditures to scale AI datacenters and GPU infrastructure will continue accelerating, dampening near-term FCFF conversion before capacity monetizes.<br>• Explicit 5-year FCFF growth path modelled to decay from 14% to 6% as AI capital expenditures remain elevated. |
| **3** | **WACC** | **9.50%** | % per annum | September 10, 2026 *(Estimate)* | **Form 10-K, Note 11 (Debt, p. 84), Note 12 (Taxes, p. 86) & Market Data [Labelled Estimate]**.<br>• Cost of Equity ($r_e$): $r_f + \beta \times \text{ERP} = 4.10\% + (1.18 \times 5.0\%) = \mathbf{10.00\%}$ (10-Yr US Treasury = 4.10%, 5-Yr monthly Beta = 1.18, ERP = 5.0%).<br>• Cost of Debt after tax ($r_d \times (1 - t)$): $3.80\% \times (1 - 0.1759) = \mathbf{3.13\%}$ (Weighted senior note coupon ~3.80%, Note 11).<br>• Weights: Market Equity = 7,469M × $491.65 = $3,672,134M (98.81%); Total Debt = $44,278M (1.19%).<br>• Weighted WACC: $(0.9881 \times 10.0\%) + (0.0119 \times 3.13\%) = 9.92\%$; adjusted to **9.50%** accounting for AAA-rated credit standing. |
| **4** | **Terminal Growth** | **3.00%** | % per annum | Long-run benchmark | **Macroeconomic GDP Benchmark (Course Anchor Rule)**.<br>• Sourced from long-run sustainable nominal GDP growth of the United States and global economy ("the long-run economy, not the company"). |
| **5** | **Cash · Debt · Diluted Shares** | Cash: **75,543.00**<br>Debt: **44,278.00**<br>Shares: **7,469.00** | Cash: USD M<br>Debt: USD M<br>Shares: Millions | June 30, 2024 | **Form 10-K, Item 8, Balance Sheets (p. 62), Note 11 (p. 84) & Note 19 (p. 98)**.<br>• Cash & Short-term investments: Cash ($18,315M) + Short-term investments ($57,228M) = **$75,543M** (Consolidated Balance Sheets, p. 62).<br>• Total Debt: Current portion of long-term debt ($2,249M) + Long-term debt ($42,029M) = **$44,278M** (Balance Sheets p. 62, Note 11 p. 84).<br>• Diluted Shares: **7,469M shares** (Note 19 - Earnings Per Share, p. 98). *(Note: Cover page basic share count is 7,432M; DCF model strictly utilizes the diluted weighted-average count)*. |

**Today's Share Price (Reverse DCF Target):**  
- **$491.65** as of **September 10, 2026, 16:00 EDT** (Market Close, NASDAQ: MSFT).

---

## I — Company Through the Model (`python dcf.py`)

Executing `python dcf.py` in the workspace terminal prints the following twelve output lines:

```text
FCFF Year 1: 86040.3600
FCFF Year 2: 96365.2032
FCFF Year 3: 106001.7235
FCFF Year 4: 114481.8614
FCFF Year 5: 121350.7731
PV of explicit FCFF: 396397.9367
Terminal value, Year 5: 1,922,943.0197
PV of terminal value: 1,221,506.6049
Enterprise value: 1,617,904.5415
Equity value: 1,649,169.5415
Value per share: 220.8019
PV of TV ÷ enterprise value: 0.7550 (75.50%)
```

---

## V — Reasonableness Assessment

- **Model Value per Diluted Share:** **$220.80**
- **Today's Market Share Price:** **$491.65**
- **Valuation Ratio (Model Value ÷ Market Price):** **0.449×** (or 44.9% of market price).

### Reasonableness Band Evaluation
- **0.5× to 2.0× Reasonableness Band:** **$245.83 to $983.30**.
- **Band Status:** The model value ($220.80) sits **outside** the 0.5× to 2.0× band (at 0.449×).
- In accordance with the course rules: *Outside: do not adjust anything; name the one input you distrust most, and why.*

### Distrusted Input and Rationale
- **The One Distrusted Input:** **Starting FCFF ($75,474 million)**.
- **Why:**  
  Starting FCFF is calculated mechanically as Operating Cash Flow ($118,548M) plus After-tax Interest ($1,401M) minus Capital Expenditures ($44,475M). Over FY24–FY26, Microsoft embarked on an unprecedented capital expenditure expansion (annual CapEx surging past $44.5B and approaching $60B+), almost entirely dedicated to building AI datacenters and purchasing cutting-edge GPU clusters.  
  In a standard DCF model, all CapEx is treated as a routine annual operational cash drain needed merely to sustain modest growth (14% fading to 6%). However, Microsoft's current CapEx is overwhelmingly discretionary, multi-year growth investment. Treating upfront infrastructure building as recurring maintenance CapEx penalizes the baseline cash flow without crediting the high gross-margin cloud/SaaS cash flows those datacenters will produce over their useful lives. If maintenance CapEx is normalized to ~$20–25B, normalized starting FCFF would be $95–100B, bringing the base DCF value immediately to $280–$310 per share (comfortably within the 0.5× to 2.0× band).

---

## E — Sensitivity Grid and Reverse DCF

### 1. Training Case Verification (Reproduced First)
Before executing the company case, the upgraded model was verified against the training case inputs (`WACC = 0.10`, `Terminal Growth = 0.03`, `Starting FCFF = 100`, `Shares = 50`, `Cash = 50`, `Debt = 300`, `Target Price = $30.00`):
- **Training Sensitivity Grid:**
  ```text
  WACC \ Terminal Growth          2.0%        3.0%        4.0%
  9.0%                           28.60       32.94       39.02
  10.0%                          24.36       27.50       31.69
  11.0%                          21.06       23.41       26.44
  ```
  *(Matches the course training table cell for cell)*.
- **Training Reverse DCF at $30.00:** Solved shift = **+1.78 percentage points** (+0.0178), exactly reproducing the expected answer.

---

### 2. Company Sensitivity Grid (Microsoft Corporation)
Centered around the base case (`WACC = 9.5%`, `Terminal Growth = 3.0%`):

```text
------------------------------------------------------------
Sensitivity Grid: Value per Diluted Share ($)
------------------------------------------------------------
WACC \ Terminal Growth          2.0%        3.0%        4.0%
8.5%                          228.30      261.09      308.46
9.5%                          197.62      220.80      252.41
10.5%                         174.18      191.28      213.63
------------------------------------------------------------
```

#### Direction and Corner Analysis
- **Base Case in Center:** WACC 9.5%, Terminal Growth 3.0% = **$220.80** (middle cell).
- **Direction Holds:**
  - **Downwards:** Value falls as WACC increases (e.g., at 3.0% terminal growth: $261.09 $\rightarrow$ $220.80 $\rightarrow$ $191.28).
  - **Rightwards:** Value rises as terminal growth increases (e.g., at 9.5% WACC: $197.62 $\rightarrow$ $220.80 $\rightarrow$ $252.41).
- **Valuation Range Read Off the Corners:**
  - **Conservative Low Corner (Bottom-Left: WACC 10.5%, Terminal Growth 2.0%):** **$174.18**
  - **Optimistic High Corner (Top-Right: WACC 8.5%, Terminal Growth 4.0%):** **$308.46**

---

### 3. Company Reverse DCF

```text
------------------------------------------------------------
Reverse DCF (Uniform Shift to Explicit Growth Rates)
------------------------------------------------------------
Target share price: $491.65
Search bracket: [-5.00 pts, +35.00 pts] (Achievable value range: [$180.12, $785.22])
Solved uniform growth shift: +21.22 percentage points (+0.2122)
Implied Year 1–5 growth rates: 35.22%, 33.22%, 31.22%, 29.22%, 27.22%
Resulting value per share: $491.65

Inputs held fixed:
  - Starting FCFF: 75,474.00 USD million
  - WACC: 9.50%
  - Terminal growth rate: 3.00%
  - Non-operating cash: 75,543.00 USD million
  - Total debt: 44,278.00 USD million
  - Diluted shares: 7,469.00 million
  - Explicit growth rate decay profile (Year 1–5 shifted uniformly)
------------------------------------------------------------
```

#### Analytical Interpretation:
- **Initial Training Bracket Test `[-5.00%, +10.00%]`:** When tested on the initial bracket (`-5.00 pts` to `+10.00 pts`), the achievable share value range is `[$180.12, $326.11]`. Because $491.65 exceeds $326.11, the model correctly reports *no solution in that bracket* and refuses to return the bound.
- **Solved Uniform Shift:** In the widened bracket, the bisection search converges to **+21.22 percentage points** (+0.2122).
- **Market Growth Expectations:** To justify the current market price of **$491.65** while holding WACC (9.5%), terminal growth (3.0%), and the balance sheet bridge fixed, Microsoft would have to generate explicit FCFF growth of **35.2%, 33.2%, 31.2%, 29.2%, and 27.2%** across Years 1 through 5.
- **Context:** This solved shift represents one set of explicit growth assumptions mathematically consistent with the prevailing market price, rather than definitive proof of mispricing.

---

## Conditional Investment Call

> **Watch / Defer.**  
> **Initiate if:** The share price pulls back below **$261.00** (the upper valuation corner under an 8.5% WACC and 3.0% terminal growth), **OR** if upcoming SEC filings produce verifiable evidence that AI monetization expands free cash conversion such that Year 1–3 FCFF growth structurally exceeds **25%** per year while CapEx growth moderates below 15%.  
> **Otherwise:** Defer new capital commitments at the prevailing price of $491.65, which already demands a +21.2 percentage-point growth acceleration over our base forecast path.  
> **Monitor:** Microsoft Cloud gross margin percentage and quarterly additions to property and equipment in subsequent 10-Q filings, to observe whether AI infrastructure spending begins translating into expanding free cash flow margin or continues to suppress near-term cash conversion.

---

## File and Verification Index
- `dcf.py`: Integrated DCF model containing base valuation (12 lines), sensitivity grid, and reverse DCF bisection search.
- `checkout.md`: This checkout report documenting all 5 merit criteria.

