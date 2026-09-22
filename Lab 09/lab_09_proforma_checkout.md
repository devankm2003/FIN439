# Lab 09 — Pro-Forma Build: the Engine and the Known Answer
## Case: Asbury Automotive Group (ABG) Three-Statement Engine & Equity Valuation
**Category:** Tuesday Completion Checkout (25 / 25)

---

## D — The Core Question

> **"What are five years of a company's statements worth, built from assumptions you can defend, and how do you know the statements are right?"**

### Partner Discussion Summary
1. **The Three Judgments that Carry the ABG Value:**
   - **Organic Revenue Growth (1.8% a year):** Establishes the scale and compounding top-line foundation across all five projection years (2026–2030).
   - **Gross Margin (17.05%):** Determines gross profit dollars available across new/used vehicle sales, parts/service, and F&I.
   - **SG&A as a % of Gross Profit (66.5% fading to 64.5%):** Represents operating cost discipline and operating leverage. Because SG&A consumes ~65% of gross profit, a 100 bps shift in SG&A efficiency shifts operating profit and FCFE significantly.
2. **Why Cash is the Last Line the Model Computes:**
   - Cash is the **balance sheet reconciler (the "plug")**. 
   - A financial model cannot determine cash until every operational, investment, working capital, and financing decision has been computed:
     $$\text{Ending Cash} = \text{Opening Cash} + \text{FCFE} - \text{Buybacks} \pm \text{Revolver Draws/Repayments}$$
   - If ending cash were hardcoded or forecasted independently, Assets would not equal Liabilities plus Equity. Computing cash last guarantees mathematical balance across all three statements.

---

## R — The Assumption Set

### 1. Operating Assumptions & Judgments
| Assumption | ABG Value | Label | Economic Rationale |
| :--- | :--- | :--- | :--- |
| **Organic revenue growth** | **1.8% a year** | judgment | Mature dealership volume growth tracking long-term replacement demand. |
| **Gross margin** | **17.05%** | judgment | Blended margin across new vehicles, used vehicles, parts/service, and F&I. |
| **SG&A ÷ gross profit** | **66.5%, 65.5%, 64.5%, 64.5%, 64.5%** | judgment | Operating efficiency improving by 200 bps from 2026 to 2028, then flattening. |
| **Depreciation ÷ opening PP&E** | **82.4 ÷ 3,070.4** (~2.6837%) | history | FY2025 depreciation divided by year-end PP&E. |
| **Impairment, non-cash** | **120.0 a year** | judgment | Expected non-cash franchise/goodwill amortized write-downs. |
| **Capital spending (CapEx)** | **250.0 a year** | guidance | Management forward guidance for dealership maintenance and facility investments. |
| **Tax rate** | **25.5%** | judgment | Normalized federal plus state effective corporate tax rate. |

### 2. Working Capital & Financing Assumptions
| Assumption | ABG Value | Label | Economic Rationale |
| :--- | :--- | :--- | :--- |
| **Inventory days** | **2,135.8 ÷ (17,999.0 − 3,071.7) × 365** (~52.224 days) | history | FY2025 inventory ÷ cost of sales. |
| **Floor plan loans ÷ inventory** | **2,027.0 ÷ 2,135.8** (~94.9059%) | history | Dealership inventory loan advance rate. |
| **Other working capital** | **0.8% of change in revenue** | judgment | Non-inventory working capital requirement. |
| **Minimum cash / revolver limit / rate** | **25.0 / 850.0 / 6.0%** | history / judgment / judgment | Liquidity cushion, credit facility capacity, and borrowing cost. |
| **Debt repayment / share buyback** | **150.0 / 150.0 a year** | judgment | Capital allocation: $150M term debt paydown and $150M equity repurchase annually. |
| **Interest: floor plan / term debt** | **4.67% / 5.44%** | history | Effective contractual borrowing rates from debt notes. |

### 3. Valuation Parameters & Fact
| Assumption | ABG Value | Label | Source |
| :--- | :--- | :--- | :--- |
| **Cost of equity ($K_e$)** | **10.0%** | judgment | Cost of equity discount rate. |
| **Terminal growth rate ($g$)** | **2.5%** | judgment | Long-run sustainable GDP anchor. |
| **Shares outstanding** | **17.951349 million** | fact | Form 10-Q as of June 30, 2026. |

### 4. Opening Balance Sheet (FY2025, USD Millions)
- **Revenue:** \$17,999.0
- **Cash:** \$40.4
- **Inventories:** \$2,135.8
- **Property, Plant & Equipment (PP&E):** \$3,070.4
- **Other Assets:** \$6,371.6
- **Total Assets:** **\$11,618.2**
- **Floor Plan Notes Payable:** \$2,027.0
- **Term Debt:** \$3,572.0
- **Revolving Credit Facility:** \$0.0
- **Other Liabilities:** \$2,127.5
- **Total Liabilities:** **\$7,726.5**
- **Stockholders' Equity:** **\$3,891.7**
- **Total Liabilities & Equity:** **\$11,618.2** *(Check: Assets − Liab − Equity = \$0.0)*

---

## I — Implementation (`proforma.py`)

The engine is implemented in standard-library Python in [`proforma.py`](file:///Users/devankmahajan/Desktop/proforma.py).

### Execution Command:
```bash
python3 proforma.py
```

### Complete Printed Output:

```text
==============================================================================================
1. PRO-FORMA INCOME STATEMENT
==============================================================================================
Line (USD Millions)                    FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
----------------------------------------------------------------------------------------------
Revenue                                18323.0     18652.8     18988.5     19330.3     19678.3
Cost of sales                          15198.9     15472.5     15751.0     16034.5     16323.1
Gross profit                            3124.1      3180.3      3237.5      3295.8      3355.1
SG&A expenses                           2077.5      2083.1      2088.2      2125.8      2164.1
Depreciation                              82.4        86.9        91.3        95.5        99.7
Impairment (non-cash)                    120.0       120.0       120.0       120.0       120.0
Operating income (EBIT)                  844.2       890.3       938.1       954.5       971.4
----------------------------------------------------------------------------------------------
Floor plan interest                       94.7        96.4        98.1        99.9       101.7
Term debt interest                       194.3       186.2       178.0       169.8       161.7
Revolver interest                          0.0         0.0         0.0         0.0         0.0
Total interest expense                   289.0       282.5       276.1       269.7       263.4
----------------------------------------------------------------------------------------------
Pre-tax income                           555.2       607.8       661.9       684.8       708.0
Income tax expense                       141.6       155.0       168.8       174.6       180.5
Net income                               413.6       452.8       493.1       510.1       527.5

==============================================================================================
2. PRO-FORMA BALANCE SHEET
==============================================================================================
Line (USD Millions)                    FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
----------------------------------------------------------------------------------------------
ASSETS:
  Cash & cash equivalents                101.8       206.9       356.6       527.5       719.8
  Inventories                           2174.7      2213.8      2253.7      2294.2      2335.5
  Property, plant & equipment           3238.0      3401.1      3559.8      3714.3      3864.6
  Other assets                          6254.2      6136.8      6019.5      5902.3      5785.0
----------------------------------------------------------------------------------------------
Total Assets                           11768.7     11958.6     12189.6     12438.2     12704.9
----------------------------------------------------------------------------------------------
LIABILITIES & EQUITY:
  Floor plan notes payable              2063.9      2101.0      2138.9      2177.4      2216.5
  Term debt                             3422.0      3272.0      3122.0      2972.0      2822.0
  Revolving credit facility                0.0         0.0         0.0         0.0         0.0
  Other liabilities                     2127.5      2127.5      2127.5      2127.5      2127.5
----------------------------------------------------------------------------------------------
Total Liabilities                       7613.4      7500.5      7388.4      7276.9      7166.0
Stockholders' Equity                    4155.3      4458.1      4801.2      5161.4      5538.9
----------------------------------------------------------------------------------------------
Total Liabilities & Equity             11768.7     11958.6     12189.6     12438.2     12704.9

==============================================================================================
3. CASH FLOW STATEMENT & FREE CASH FLOW TO EQUITY (FCFE)
==============================================================================================
Line (USD Millions)                    FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
----------------------------------------------------------------------------------------------
Net income                               413.6       452.8       493.1       510.1       527.5
(+) Depreciation                          82.4        86.9        91.3        95.5        99.7
(+) Impairment (non-cash)                120.0       120.0       120.0       120.0       120.0
(-) Capital spending (CapEx)            -250.0      -250.0      -250.0      -250.0      -250.0
(-) Change in inventory                  -38.9       -39.1       -39.8       -40.6       -41.3
(-) Change in other working capital        -2.6        -2.6        -2.7        -2.7        -2.8
(+) Change in floor plan                  36.9        37.1        37.8        38.5        39.2
(-) Term debt repayment                 -150.0      -150.0      -150.0      -150.0      -150.0
----------------------------------------------------------------------------------------------
Free Cash Flow to Equity (FCFE)          211.4       255.1       299.7       320.9       342.3
(-) Share buybacks                      -150.0      -150.0      -150.0      -150.0      -150.0
Cash, year end                           101.8       206.9       356.6       527.5       719.8

==============================================================================================
4. BALANCE & CASH CHECKS
==============================================================================================
Line (USD Millions)                    FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
----------------------------------------------------------------------------------------------
Assets − Liabilities − Equity             -0.0         0.0         0.0         0.0         0.0
Cash at or above minimum ($25M)              1           1           1           1           1
----------------------------------------------------------------------------------------------
Check status: BALANCED (all checks passed, gap = 0.0)

==============================================================================================
5. EQUITY DCF VALUATION SUMMARY (Asbury Automotive Group — ABG)
==============================================================================================
PV of explicit 5-year FCFE (2026–2030):   $    1,059.87 million
Terminal value at 2030:                  $    6,727.85 million
PV of terminal value (discounted 5 yrs):  $    4,177.46 million
----------------------------------------------------------------------------------------------
Total Equity Value:                      $    5,237.34 million
Share of value after 2030 (TV / Equity):         79.76%
Diluted shares outstanding:                   17.951349 million
----------------------------------------------------------------------------------------------
Value per share:                         $      291.75
==============================================================================================
```

---

## V — Verification Against Known Answers

| Check Line | Case Benchmark FY2026E | Model Result FY2026E | Case Benchmark FY2030E | Model Result FY2030E | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Revenue** | 18,323.0 | **18,323.0** | 19,678.3 | **19,678.3** | **Exact Match** |
| **Operating income** | 844.2 | **844.2** | 971.4 | **971.4** | **Exact Match** |
| **Net income** | 413.6 | **413.6** | 527.5 | **527.5** | **Exact Match** |
| **Free cash flow to equity (FCFE)** | 211.4 | **211.4** | 342.3 | **342.3** | **Exact Match** |
| **Cash, year end** | 101.8 | **101.8** | 719.8 | **719.8** | **Exact Match** |
| **Assets − Liabilities − Equity** | 0.0 | **0.0** | 0.0 | **0.0** | **Exact Match** |
| **Value per share** | **$291.75** | **$291.75** | — | — | **Exact Match** |
| **Share of value after 2030** | ~80% | **79.76%** | — | — | **Exact Match** |

---

## Swap and Break Test: Refusal of Broken Balance Sheet

To verify that the model enforces integrity rather than blindly accepting bad numbers, we execute the "swap and break" test:
1. In `proforma.py`, set FY2026 cash to opening **\$40.4M** instead of the computed **\$101.8M**.
2. Run the model.

### Error Output:
```text
AssertionError: Balance sheet check failed in FY2026E: gap of -61.4
```

### Analysis of the −61.4 Gap:
- In FY2026E, net cash generated after buybacks is:
  $$\Delta \text{Cash} = \$101.8\text{M} - \$40.4\text{M} = +\mathbf{\$61.4\text{M}}$$
- If ending cash is falsely held at opening cash (\$40.4M), Total Assets is understated by exactly \$61.4M.
- Therefore, $\text{Assets} - \text{Liabilities} - \text{Equity} = -\mathbf{\$61.4\text{M}}$.
- The gap of **−61.4** is the year's net change in cash with the sign flipped.

---

## Floor Plan Financing — Learn on Your Own

1. **What is it?**
   - Floor plan financing consists of short-term revolving collateralized inventory loans provided by automakers' captive finance subsidiaries (e.g., Ford Credit, GM Financial) and commercial banks.
2. **How does it work?**
   - The borrowing facility rises and falls automatically with vehicle inventory (~94.9% of vehicle inventory is debt-financed).
   - Interest is calculated on the opening balance at 4.67%.
   - In cash flow modeling, floor plan borrowing is classified as an **operating cash flow** inside FCFE:
     $$\text{Net Working Capital Drain} = -\Delta \text{Inventory} + \Delta \text{Floor Plan}$$
     Because floor plan financing covers ~94.9% of inventory, an inventory increase of \$38.9M in 2026 is offset by \$36.9M of floor plan borrowing, leaving a net cash drag of only **\$2.0M**.
3. **Why removing floor plan sends cash to ~-$1.1 billion:**
   - If floor plan debt financing is removed, the dealership must fund 100% of vehicle inventory using internal equity cash.
   - Financing \$2.1B+ of vehicle inventory with zero credit backing forces the company to max out its \$850M revolving credit facility, causing cash to collapse to **~-$1.1 billion**.

---

## Reflect — Explaining to Your Partner

1. **Why the model computes cash last:**
   - Cash is the balance sheet's cumulative reservoir. It absorbs all operating net income, non-cash charges, capital investments, working capital shifts, debt service, and equity distributions. Computing cash last guarantees that the balance sheet balances automatically without fudge factors.
2. **What the −61.4 tells you before opening a single cell:**
   - A gap of −61.4 immediately indicates that the balance sheet is missing exactly the year's net cash generation (\$61.4M). Because Assets are lower by \$61.4M while Liabilities and Equity reflect full net income, the equation produces an exact deficit of −61.4. It proves the balance check works.

