# Week 04: Comparable-Company Valuation (P/E Multiples)
## Training Case: Asbury Automotive Group (ABG) with AutoNation (AN) and Group 1 Automotive (GPI)

---

## 1. Define / Discover — What P/E Can and Cannot Tell You

### Concepts and Definitions
- **Price per Share:** The current equity market price to acquire one share of common stock.
- **Earnings per Share (Diluted GAAP EPS):** The portion of net income allocated to each share of common stock after accounting for all dilutive securities (stock options, RSUs, convertible debt).
- **Price-to-Earnings Multiple ($P/E = \text{Price} \div \text{EPS}$):** The number of dollars the market pays per **\$1.00 of annual net earnings**. It standardizes equity value across different company sizes and share counts.

### Why Use P/E in Valuation?
1. **Scale Normalization:** Strips away absolute company size, allowing an apples-to-apples comparison of differently sized businesses on a common unit basis.
2. **Complement to Discounted Cash Flow (DCF):**
   - **DCF:** An absolute intrinsic valuation built on multi-year cash flow forecasts, terminal growth, and cost of capital (WACC).
   - **Comps (P/E):** A relative valuation reflecting how market participants currently price contemporaneous earnings across similar operating models.
   - **Divergence:** Highlights differences in market sentiment, capital structure, or growth expectations between your company and its peer group.

### Usefulness and Limitations
- **When Useful:** Positive, normalized earnings representing ongoing core business operations with comparable accounting and capital structures.
- **When Misleading:**
  - **Negative Earnings:** A negative P/E cannot be used to value equity (multiplying negative EPS by a negative multiple produces an absurd positive share price).
  - **One-Off / Non-Operating Items:** One-time asset sales or legal windfalls artificially depress P/E (value trap), while one-time restructuring charges artificially inflate P/E.
  - **Growth / Risk Heterogeneity:** High-growth or low-risk companies naturally command higher multiples.
- **Why a Lower P/E is Not Automatically a Bargain:** A lower multiple often reflects declining revenue, deteriorating margins, heavy debt burden, or structural headwinds. It is a prompt for investigation, not proof of mispricing.

---

## 2. Represent — Case Peer Policy & Business Evidence

### Why Franchised Retail and Parts/Service Matter
Generic industry labels (e.g., "Automotive" or "Specialty Retail") incorrectly group vehicle manufacturers (OEMs), aftermarket parts retailers (AutoZone), and online used platforms (Carvana) together. Franchised auto dealerships possess a distinct 3-part revenue model:
1. **New and Used Vehicle Sales:** High revenue volume with thin gross margins (~4%–7%).
2. **Parts and Service ("Fixed Operations"):** High gross margins (~45%–50%), recession-resilient, recurring cash flow that covers dealership overhead.
3. **Finance & Insurance (F&I):** Agency commissions on third-party vehicle financing and service contracts with ~100% gross margin.

### Peer Selection Decisions

| Company | Ticker | Role / Decision | Business Evidence & Rationale |
| :--- | :--- | :--- | :--- |
| **Asbury Automotive Group** | **ABG** | **Target Company** | Franchised auto dealership operator across new/used vehicle sales, parts/service, and F&I. |
| **AutoNation** | **AN** | **USE (Candidate Peer)** | Fits core domestic franchised dealership model across all three pillars. Operates *AutoNation Finance* (captive auto lending), which introduces some balance sheet lending exposure, but core dealership operations dominate. |
| **Group 1 Automotive** | **GPI** | **QUALIFY (Qualified Candidate Peer)** | Fits franchised retail and fixed operations model, but carries two material business differences:<br>1. **Geographic Diversification:** Substantial dealership operations in the United Kingdom, subject to UK macroeconomic trends, consumer spending, and foreign currency swings.<br>2. **2024 Acquisition:** Acquired 54 Inchcape UK dealerships during 2024, introducing integration costs, debt financing changes, and revenue run-rate noise. |

---

## 3. Implement — Frozen Case Inputs & Python Reproduction

### Input Data (December 31, 2024 Retrospective Training Case)
- **Asbury Automotive (ABG), Target:** Price = **$243.03**, FY2024 GAAP Diluted EPS = **$21.50**
- **AutoNation (AN), Candidate Peer:** Price = **$169.84**, FY2024 GAAP Diluted EPS = **$16.92**
- **Group 1 Automotive (GPI), Qualified Peer:** Price = **$421.48**, FY2024 GAAP Diluted EPS = **$36.81**

### Script Architecture (`comps.py`)
- Standard-library Python (`statistics`, `typing`).
- Deduplicates peers and excludes target company automatically.
- Validates strictly positive prices and EPS (labels invalid values as "not meaningful").
- Preserves full floating-point precision throughout all intermediate calculations.
- Formats multiples to 6 decimal places and prices/deltas to cents (\$0.01).
- Never bridges P/E with cash or debt (P/E is strictly an equity multiple).

---

## 4. Validate — Reproduction Checks

Execution Command:
```bash
python3 comps.py
```

### Output Results
```text
======================================================================
COMPARABLE COMPANY VALUATION: PRICE-TO-EARNINGS (P/E)
======================================================================
Target Company: Asbury Automotive Group (ABG)
Target Price:   $243.03
Target EPS:     $21.50

----------------------------------------------------------------------
Peer Company               Ticker   Price ($)    Diluted EPS    P/E Multiple  
----------------------------------------------------------------------
AutoNation                 AN       $169.84      $16.92         10.037825     ×
Group 1 Automotive         GPI      $421.48      $36.81         11.450149     ×
----------------------------------------------------------------------

PEER MULTIPLES & IMPLIED VALUATION
----------------------------------------------------------------------
Usable peer count: 2
Peer median P/E:   10.743987×
Peer P/E range:    10.037825× to 11.450149×
Asbury Automotive Group at peer median:   $231.00
Asbury Automotive Group peer-implied range: $215.81–$246.18

----------------------------------------------------------------------
LEAVE-ONE-PEER-OUT SENSITIVITY (Unrounded calculations)
----------------------------------------------------------------------
Remove AN: remaining GPI estimate: $246.18 (change from full-peer estimate: +15.18)
Remove GPI: remaining AN estimate: $215.81 (change from full-peer estimate: -15.18)
======================================================================
Note: Never bridge P/E with cash/debt; P/E is an equity multiple.
======================================================================
```

### Verification Checklist
| Metric Check | Case Benchmark | Script Output | Status |
| :--- | :--- | :--- | :--- |
| **AutoNation P/E** | 10.037825× | 10.037825× | **Match** |
| **Group 1 P/E** | 11.450149× | 11.450149× | **Match** |
| **Peer Median P/E** | 10.743987× | 10.743987× | **Match** |
| **Asbury Implied Range** | \$215.81–\$246.18 | \$215.81–\$246.18 | **Match** |
| **Asbury at Peer Median** | \$231.00 | \$231.00 | **Match** |
| **Remove GPI: Remaining AN Estimate** | \$215.81 | \$215.81 | **Match** |
| **Dollar Change from Midpoint** | −\$15.18 | −\$15.18 | **Match** |

---

## 5. Evolve — Leave-One-Out Sensitivity Analysis

1. **Prediction:**
   Because Group 1 trades at a higher multiple (11.45×) than AutoNation (10.04×), removing Group 1 must pull the median down to AutoNation’s standalone multiple, lowering the implied share price from **\$231.00** to **\$215.81** (a decline of **−\$15.18**).
2. **Loss of Valuation Range:**
   A valuation range requires at least two distinct peer multiples to form a lower and upper bound. With Group 1 excluded, only AutoNation remains, collapsing the range into a single point **reference estimate** (\$215.81).
3. **Market Price Context:**
   Asbury’s actual market price on December 31, 2024 was **\$243.03**. 
   - Against AutoNation alone (\$215.81), Asbury traded at a premium of +\$27.22 (+12.6%).
   - Against the full peer range (\$215.81 to \$246.18), Asbury traded comfortably inside the upper half, priced at an effective multiple of **11.30×**, very close to Group 1's 11.45×.

---

## 6. Reflect — Partner Discussion Script

- **What P/E measures:** P/E quantifies how many dollars of equity market capitalization investors pay per dollar of GAAP diluted earnings, standardizing comparison across disparate firm sizes.
- **Why peers belong or require qualification:**
  - AutoNation fits the core domestic model but carries captive finance exposure.
  - Group 1 fits the business model but requires explicit qualification due to UK geographical exposure and 2024 Inchcape acquisition noise.
- **Why comps do not prove mispricing:**
  P/E multiples reflect market consensus pricing on a given date. Asbury trading at \$243.03 within the \$215.81–\$246.18 band demonstrates market consistency with dealership peers, but cannot evaluate whether the entire dealership sector is cyclically mispriced. That requires fundamental cash flow and margin analysis (DCF).

