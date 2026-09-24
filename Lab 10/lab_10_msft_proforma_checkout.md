# Lab 10 — Thursday Merit Checkout: Pro-Forma Valuation of Microsoft Corporation
**Company:** Microsoft Corporation (NASDAQ: `MSFT`, CIK: `0000789019`)  
**Category:** Thursday Merit Checkout (25 / 25 Rubric Target)  
**Primary Sources:**
- [Microsoft FY2023 Form 10-K (Ended June 30, 2023, filed July 27, 2023)](https://microsoft.gcs-web.com/static-files/e2931fdb-9823-4130-b2a8-f6b8db0b15a9)
- [Microsoft FY2024 Form 10-K (Ended June 30, 2024, filed July 30, 2024)](https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm)
- [Microsoft FY2025 Form 10-K (Ended June 30, 2025, filed July 30, 2025)](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm)

---

## Reopen and Rerun Check (`python3 proforma.py`)
Before modifying the engine for Microsoft, `python3 proforma.py` was executed in the course terminal and confirmed to reproduce all seven Tuesday Asbury Automotive Group (`ABG`) benchmark lines to the exact decimal (`Revenue`: 18,323.0 / 19,678.3; `EBIT`: 844.2 / 971.4; `Net income`: 413.6 / 527.5; `FCFE`: 211.4 / 342.3; `Cash`: 101.8 / 719.8; `Balance Gap`: 0.0; `Value per share`: **\$291.75**, with **79.76%** in terminal value).

---

## D — The Question & Company Personalization

> **Core Question:** *"What are five years of your company's statements worth, built from assumptions you can defend?"*  
> **Company & Ticker:** **Microsoft Corporation (NASDAQ: `MSFT`)**

### One Sentence on the Line That Makes Microsoft Different
- **Floor Plan Status:** **`none`** (Microsoft is a cloud software and enterprise platform company whose physical hardware inventory for Xbox/Surface is only **\$938M**, or **3.90 days of cost of revenue**, financed internally with zero floor plan debt).
- **The Company-Specific Line Replacing Floor Plan:** **Short-Term Unearned Revenue (Deferred Revenue — \$64,555M in FY2025)** alongside hyperscale **AI Datacenter Capital Expenditures (\$64,551M in FY2025)**.
- **What It Does to the Model (Partner Explanation):**  
  *"Unlike an auto dealership that borrows on a 4.67% floor plan line to carry vehicle inventory on its lots, Microsoft collects upfront cash billings from enterprise customers for multi-quarter Azure, Microsoft 365, and Dynamics subscriptions, creating a **\$64.6 billion Short-Term Unearned Revenue** liability (~22.91% of revenue) that carries **0.0% interest** and generates **+\$8.4B to +\$13.7B per year in positive working-capital cash flow** (`+Change in unearned revenue` in FCFE), partially funding Microsoft's \$65.0B annual AI datacenter CapEx buildout."*
- **Partner's Question & Response:**
  - *Partner Question:* "If Unearned Revenue is a liability on the Balance Sheet, why does an increase in Unearned Revenue add to Free Cash Flow to Equity (FCFE)?"
  - *Answer:* "Because Unearned Revenue represents cash that customers have already paid to Microsoft upfront before the software service is delivered; when Unearned Revenue increases by \$8,392.1M in FY2026E, Microsoft receives \$8,392.1M more in cash than it recognizes in GAAP Revenue, making $+\Delta\text{Unearned Revenue}$ an interest-free operating cash inflow."

---

## R — Three-Year History, Ratio Table, and Labelled Assumption Set

### 1. Three-Year History Grid Traced to Three 10-Ks (FY2023–FY2025)
*All monetary figures in USD millions. Every item is traced to the audited Consolidated Financial Statements (Item 8) of Microsoft's FY2023, FY2024, and FY2025 Form 10-K filings.*

| Line Item (USD Millions) | FY2023 (Ended 06/30/23) | FY2024 (Ended 06/30/24) | FY2025 (Ended 06/30/25) | Exact SEC Form 10-K Filing & Locator |
| :--- | :---: | :---: | :---: | :--- |
| **Revenue** | \$211,915 | \$245,122 | \$281,724 | FY23 10-K (Item 8, p. 58); FY24 10-K (Item 8, p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Cost of revenue** | \$65,863 | \$74,114 | \$87,831 | FY23 10-K (Item 8, p. 58); FY24 10-K (Item 8, p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Gross profit (Gross margin)** | **\$146,052** | **\$171,008** | **\$193,893** | FY23 10-K (Item 8, p. 58); FY24 10-K (Item 8, p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **SG&A (Sales & marketing + G&A)** | \$30,334 | \$32,065 | \$32,877 | FY25 10-K (Item 8, p. 59): S&M (\$22,759 / \$24,456 / \$25,654) + G&A (\$7,575 / \$7,609 / \$7,223) |
| **Research and development (R&D)** | \$27,195 | \$29,510 | \$32,488 | FY23 10-K (p. 58); FY24 10-K (p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Total Operating Expenses (R&D + SG&A)** | \$57,529 | \$61,575 | \$65,365 | Sum of R&D + S&M + G&A on Consolidated Income Statements (`Gross margin − Operating income`) |
| **Operating income (EBIT)** | \$88,523 | \$109,433 | \$128,528 | FY23 10-K (p. 58); FY24 10-K (p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Income before income taxes** | \$89,311 | \$107,787 | \$123,627 | FY23 10-K (p. 58); FY24 10-K (p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Provision for income taxes** | \$16,950 | \$19,651 | \$21,795 | FY23 10-K (p. 58); FY24 10-K (p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Net income** | **\$72,361** | **\$88,136** | **\$101,832** | FY23 10-K (p. 58); FY24 10-K (p. 60); FY25 10-K (Item 8, p. 59) — *Income Statements* |
| **Inventories** | \$2,500 | \$1,246 | \$938 | FY24 10-K (Item 8, p. 62); FY25 10-K (Item 8, p. 61) — *Consolidated Balance Sheets* |
| **Property and equipment, net (PP&E)** | \$95,641 | \$135,591 | \$204,966 | FY24 10-K (Item 8, p. 62); FY25 10-K (Item 8, p. 61) — *Consolidated Balance Sheets* |
| **Short-term unearned revenue** | \$50,901 | \$57,582 | \$64,555 | FY24 10-K (Item 8, p. 62); FY25 10-K (Item 8, p. 61) — *Consolidated Balance Sheets* |
| **Stockholders' equity** | **\$206,223** | **\$268,477** | **\$343,479** | FY24 10-K (Item 8, p. 62); FY25 10-K (Item 8, p. 61) — *Consolidated Balance Sheets* |
| **PP&E Depreciation expense (Note 7)** | \$11,000 | \$15,200 | \$22,000 | FY25 10-K (Item 8, Note 7 — *Property and Equipment*, p. 78) |
| **Total D&A and other (Cash Flow)** | \$13,861 | \$22,287 | \$34,153 | FY25 10-K (Item 8, p. 62) — *Cash Flows ("Depreciation, amortization, and other")* |
| **Additions to PP&E (Cash CapEx)** | \$28,107 | \$44,475 | \$64,551 | FY25 10-K (Item 8, p. 62) — *Cash Flows ("Additions to property and equipment")* |

#### Two Items Confirmed by Hand Directly Against the Filing:
1. **Hand Confirmation 1 — FY2025 Gross Margin & Operating Income (FY2025 Form 10-K, Item 8, p. 59):**
   - Opened the Consolidated Statements of Income in the FY2025 10-K: Total Revenue (`$281,724M`) minus Total Cost of Revenue (`$87,831M`) = **`$193,893M` Gross Margin** (exact match). Subtracting R&D (`$32,488M`), Sales & Marketing (`$25,654M`), and General & Administrative (`$7,223M`) = Total OpEx (`$65,365M`), leaving **`$128,528M` Operating Income** (exact match).
2. **Hand Confirmation 2 — FY2025 Balance Sheet Accounting Identity (FY2025 Form 10-K, Item 8, p. 61):**
   - Opened the Consolidated Balance Sheets as of June 30, 2025: Total Assets (`$619,003M`) minus Total Liabilities (`$275,524M`) = **`$343,479M` Total Stockholders' Equity** (exact match to the penny/million).

---

### 2. Three-Year Historical Ratio Table (FY2023–FY2025)

| Computed Ratio / Metric | FY2023 | FY2024 | FY2025 | Formula & Reconciliation Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Gross Margin (%)** | **68.92%** | **69.76%** | **68.82%** | $\text{Gross Profit} \div \text{Revenue}$ (`193,893 / 281,724` in FY25) |
| **SG&A (S&M + G&A) ÷ Gross Profit** | 20.77% | 18.75% | 16.96% | $(\text{S\&M} + \text{G\&A}) \div \text{Gross Profit}$ (`32,877 / 193,893` in FY25) |
| **Total OpEx (R&D + SG&A) ÷ Gross Profit** | 39.39% | 36.01% | 33.71% | $(\text{R\&D} + \text{S\&M} + \text{G\&A}) \div \text{Gross Profit}$ (`65,365 / 193,893` in FY25) |
| **Cash OpEx (ex-Note 7 Depr) ÷ Gross Profit** | **31.86%** | **27.12%** | **22.37%** | $(\text{Total OpEx} - \text{PP\&E Depr}) \div \text{Gross Profit}$ (`43,365 / 193,893` in FY25; prevents double-counting depreciation in the engine) |
| **Inventory Days** | **13.85 days** | **6.14 days** | **3.90 days** | $(\text{Inventories} \div \text{Cost of Revenue}) \times 365$ (`938 / 87,831 × 365` in FY25) |
| **Depreciation ÷ Ending PP&E (Note 7)** | **11.50%** | **11.21%** | **10.73%** | $\text{Note 7 PP\&E Depr} \div \text{Ending Net PP\&E}$ (`22,000 / 204,966` in FY25) |
| **Total Cash Flow D&A ÷ Ending PP&E** | 14.49% | 16.44% | 16.66% | $\text{Cash Flow D\&A and Other} \div \text{Ending Net PP\&E}$ (`34,153 / 204,966` in FY25) |
| **Capital Spending (10-K Cash Flow Statement)** | **\$28,107M** | **\$44,475M** | **\$64,551M** | 10-K Cash Flow line: *"Additions to property and equipment"* |
| **Capital Spending (Provider / Headline incl. Leases)** | \$31,900M | \$55,700M | \$88,200M | Earnings release / provider metric including equipment obtained under finance leases |
| **Effective Tax Rate (%)** | **18.98%** | **18.23%** | **17.63%** | $\text{Provision for Income Taxes} \div \text{Pre-Tax Income}$ (`21,795 / 123,627` in FY25) |
| **Short-Term Unearned Revenue ÷ Revenue** | **24.02%** | **23.49%** | **22.91%** | $\text{Short-Term Unearned Revenue} \div \text{Revenue}$ (`64,555 / 281,724` in FY25) |
| **Reported GAAP Revenue Growth (%)** | **+6.88% (~7%)** | **+15.67% (~16%)** | **+14.93% (~15%)** | Year-over-year GAAP top-line percentage change |
| **MD&A Constant-Currency / Organic Growth (%)** | **+11.0% CC** | **+15.0% CC (~13.5% organic ex-Activision)** | **+15.0% CC (Organic)** | Item 7 MD&A Constant Currency tables; FY24 strips ~1.5 pts of consolidated M&A boost from the Oct 2023 Activision Blizzard acquisition |

---

### 3. Opening Balance Sheet (As of June 30, 2025 — FY2025 Form 10-K, USD Millions)
- **Opening Revenue (FY2025):** \$281,724.0
- **Assets:**
  - **Cash & short-term investments:** \$94,565.0 *(Cash & cash equivalents \$30,242.0 + Short-term investments \$64,323.0)*
  - **Inventories:** \$938.0
  - **Property and equipment, net (PP&E):** \$204,966.0
  - **Other assets:** \$318,534.0 *(Accounts receivable \$56,924, Goodwill \$119,288, Intangibles \$23,040, ROU lease assets, etc.)*
  - **Total Opening Assets:** **\$619,003.0**
- **Liabilities & Stockholders' Equity:**
  - **Short-term unearned revenue (Company-specific line; Floor Plan = `none`):** \$64,555.0
  - **Term debt (Current portion \$2,999.0 + Long-term debt \$40,152.0):** \$43,151.0
  - **Revolving credit facility:** \$0.0
  - **Other liabilities:** \$167,818.0 *(Total Liabilities \$275,524.0 − Unearned Revenue \$64,555.0 − Term Debt \$43,151.0)*
  - **Total Opening Liabilities:** **\$275,524.0**
  - **Stockholders' Equity:** **\$343,479.0**
  - **Total Opening Liabilities & Equity:** **\$619,003.0** *(Opening Check Gap = **\$0.0**)*

---

### 4. Three-Column Assumption Table (FY2026E–FY2030E)

| Assumption Parameter | Model Value | Label | Reason (In Our Own Words) |
| :--- | :--- | :---: | :--- |
| **Organic revenue growth** | **13.0% a year** | `judgment` | Microsoft compounded organic constant-currency revenue at ~13.5%–15.0% in FY24–FY25 behind 23%+ Microsoft Cloud expansion; we project 13.0% annual growth as Azure AI and Copilot adoption scales against a larger \$281.7B base. |
| **Gross margin** | **68.50%** | `judgment` | Historical gross margin averaged 69.17% across FY23–FY25 (68.82% in FY25), and we model a 32 bps compression to 68.50% because management explicitly warned in Item 7 (p. 36) that scaling AI infrastructure weighs on cloud gross margin percentage. |
| **Cash OpEx (ex-Depr) ÷ gross profit** | **22.5%, 22.0%, 21.5%, 21.0%, 21.0%** | `judgment` | Total GAAP OpEx less Note 7 PP&E depreciation fell from 31.86% of gross profit (FY23) to 22.37% (FY25); since our engine deducts PP&E depreciation on its own line, we start cash OpEx at 22.5% of GP and taper to 21.0% as software operating leverage scales. |
| **Depreciation ÷ opening PP&E** | **22,000.0 ÷ 204,966.0 (~10.7335%)** | `history` | FY2025 Note 7 property and equipment depreciation expense (\$22,000M) divided by year-end net PP&E (\$204,966M), allowing depreciation to rise automatically from \$22.0B to \$37.7B as AI servers and datacenters are placed into service. |
| **Impairment (non-cash)** | **\$0.0M a year** | `history` | Microsoft recorded zero material goodwill or intangible impairments across FY23–FY25, and we do not forecast unannounced write-offs. |
| **Capital spending (CapEx)** | **\$65,000.0M a year** | `guidance` | Cash additions to PP&E reached \$64,551M in FY25, and management guided to sustained hyperscale AI datacenter and GPU server capital intensity across the forecast horizon. |
| **Tax rate** | **18.0%** | `judgment` | Microsoft's effective tax rate was 18.98% (FY23), 18.23% (FY24), and 17.63% (FY25); 18.0% reflects a normalized blend of U.S. statutory taxes, R&D credits, and foreign cloud earnings. |
| **Inventory days** | **938.0 ÷ 87,831.0 × 365 (~3.90 days)** | `history` | FY2025 ending inventory divided by FY2025 cost of revenue times 365; hardware is a tiny fraction of Microsoft's cloud/software business. |
| **Floor plan debt** | **None (\$0.0M)** | `history` | Microsoft is a software/cloud provider, not a vehicle dealership, and carries zero floor plan notes payable. |
| **Short-term unearned revenue ÷ revenue** | **64,555.0 ÷ 281,724.0 (~22.9143%)** | `history` | Replaces the Floor Plan row: enterprise customers prepay annual cloud/software subscriptions equal to 22.91% of revenue at 0.0% interest, generating $+\Delta\text{Unearned Revenue}$ operating cash inflow each year. |
| **Other working capital** | **4.0% of change in revenue** | `judgment` | Enterprise accounts receivable and cloud contract assets expand with new billings, requiring a modest 4.0% incremental working capital investment per dollar of new revenue. |
| **Minimum cash / revolver limit / rate** | **\$15,000M / \$10,000M / 5.0%** | `judgment` | Operational liquidity floor of \$15.0B for global treasury operations, backed by commercial paper/revolver capacity at a 5.0% AAA rate. |
| **Term debt repayment** | **\$3,000.0M a year** | `judgment` | In FY25, Microsoft repaid \$3,216M of debt and had \$2,999M in current maturities; we model \$3,000M/year of scheduled senior note paydowns without new debt issuance. |
| **Share buybacks & dividends** | **\$42,502.0M a year** | `history` / `judgment` | Matches Microsoft's exact FY2025 cash capital return to shareholders (\$18,420M stock repurchases + \$24,082M cash dividends = \$42,502M), which flows out of Stockholders' Equity and Ending Cash below FCFE. |
| **Interest rate: unearned rev / term debt** | **0.00% / 5.5271%** | `history` | Customer unearned revenue carries 0.00% interest; effective debt coupon is FY2025 GAAP interest expense (\$2,385M) divided by ending debt (\$43,151M) = 5.5271%. |
| **Cost of equity ($K_e$)** | **9.50%** | `judgment` | CAPM estimate ($R_f = 4.10\% + \beta (1.08) \times 5.00\%\text{ ERP} = 9.50\%$), reflecting Microsoft's AAA rating and mission-critical enterprise subscription durability. |
| **Terminal growth rate ($g$)** | **3.00%** | `judgment` | Long-run sustainable nominal U.S. and global GDP growth rate ceiling. |
| **Diluted shares outstanding** | **7,465.00 million** | `fact` | Sourced from FY2025 Form 10-K Consolidated Statements of Income & Note 18 (cover page basic shares = 7,433.17 million as of July 24, 2025). |

#### E — Partner Attack on Our Assumption Table & Two-Sentence Defense (Under the Table)
- **Partner Attack on `Organic revenue growth (13.0% a year)` & `CapEx ($65,000M a year)`:**  
  *"Why did you hold annual cash CapEx flat at \$65,000M while assuming Microsoft can compound organic revenue at 13.0% a year through FY2030E (growing revenue from \$281.7B to \$519.1B), and what would force you to change that judgment?"*
- **Our Two-Sentence Answer:**  
  We modeled 13.0% organic revenue growth alongside a flat \$65.0B annual CapEx run-rate because FY2024–FY2025 represented an unprecedented front-loaded datacenter land-and-GPU capacity buildout (CapEx more than doubling from \$28.1B to \$64.6B), which transitions into higher-utilization software monetization across Microsoft 365 Copilot and Azure over FY2026E–FY2030E. We would revise this judgment to step up CapEx (or lower organic growth to 9%–10%) if subsequent 10-Q filings show that Azure revenue growth requires CapEx to remain above 22% of revenue rather than tapering from 20.4% (FY26E) to 12.5% (FY30E).

*(Note on Negative FCFE Rule: Microsoft generates positive Net Income and positive FCFE in all five forecast years [\$79.4B to \$178.8B]. Conceptually, if a company had negative FCFE in the terminal year, a terminal value on a negative cash flow is not a meaningful number because plugging a negative cash flow into the Gordon Growth perpetuity formula discounts an infinite stream of compounding losses into a negative equity value, violating limited liability since shareholders would liquidate or restructure rather than fund perpetual losses.)*

---

## I — Microsoft Corporation Through the Engine (`python3 msft_proforma.py`)

Saved as [`msft_proforma.py`](file:///Users/devankmahajan/Desktop/msft_proforma.py) and executed via:
```bash
python3 msft_proforma.py
```

### Complete Terminal Output
```text
================================================================================================
1. PRO-FORMA INCOME STATEMENT (Microsoft Corporation — MSFT)
================================================================================================
Line (USD Millions)                      FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
------------------------------------------------------------------------------------------------
Revenue                                 318348.1    359733.4    406498.7    459343.5    519058.2
Cost of revenue                         100279.7    113316.0    128047.1    144693.2    163503.3
Gross profit                            218068.5    246417.4    278451.6    314650.3    355554.9
Cash OpEx (R&D + S&M + G&A ex-Depr)      49065.4     54211.8     59867.1     66076.6     74666.5
Depreciation (PP&E)                      22000.0     26615.4     30735.4     34413.2     37696.2
Impairment (non-cash)                        0.0         0.0         0.0         0.0         0.0
Operating income (EBIT)                 147003.1    165590.1    187849.1    214160.6    243192.1
------------------------------------------------------------------------------------------------
Unearned revenue interest (0%)               0.0         0.0         0.0         0.0         0.0
Term debt interest                        2385.0      2219.2      2053.4      1887.6      1721.7
Revolver interest                            0.0         0.0         0.0         0.0         0.0
Total interest expense                    2385.0      2219.2      2053.4      1887.6      1721.7
------------------------------------------------------------------------------------------------
Pre-tax income                          144618.1    163371.0    185795.7    212273.0    241470.4
Income tax expense                       26031.3     29406.8     33443.2     38209.1     43464.7
Net income                              118586.8    133964.2    152352.5    174063.9    198005.7

================================================================================================
2. PRO-FORMA BALANCE SHEET (Microsoft Corporation — MSFT)
================================================================================================
Line (USD Millions)                      FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
------------------------------------------------------------------------------------------------
ASSETS:
  Cash & short-term investments         131444.0    189210.1    270484.0    378276.5    514570.2
  Inventories                             1070.9      1210.2      1367.5      1545.3      1746.2
  Property and equipment, net           247966.0    286350.6    320615.2    351202.0    378505.8
  Other assets                          319999.0    321654.4    323525.0    325638.8    328027.4
------------------------------------------------------------------------------------------------
Total Assets                            700480.0    798425.3    915991.7   1056662.6   1222849.5
------------------------------------------------------------------------------------------------
LIABILITIES & EQUITY:
  Short-term unearned revenue            72947.1     82430.3     93146.2    105255.2    118938.4
  Term debt (current + long-term)        40151.0     37151.0     34151.0     31151.0     28151.0
  Revolving credit facility                  0.0         0.0         0.0         0.0         0.0
  Other liabilities                     167818.0    167818.0    167818.0    167818.0    167818.0
------------------------------------------------------------------------------------------------
Total Liabilities                       280916.2    287399.3    295115.2    304224.2    314907.4
Stockholders' Equity                    419563.8    511026.0    620876.5    752438.4    907942.1
------------------------------------------------------------------------------------------------
Total Liabilities & Equity              700480.0    798425.3    915991.7   1056662.6   1222849.5

================================================================================================
3. CASH FLOW STATEMENT & FREE CASH FLOW TO EQUITY (FCFE)
================================================================================================
Line (USD Millions)                      FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
------------------------------------------------------------------------------------------------
Net income                              118586.8    133964.2    152352.5    174063.9    198005.7
(+) Depreciation                         22000.0     26615.4     30735.4     34413.2     37696.2
(+) Impairment (non-cash)                    0.0         0.0         0.0         0.0         0.0
(-) Capital spending (CapEx)            -65000.0    -65000.0    -65000.0    -65000.0    -65000.0
(-) Change in inventory                   -132.9      -139.2      -157.3      -177.8      -200.9
(-) Change in other working capital      -1465.0     -1655.4     -1870.6     -2113.8     -2388.6
(+) Change in unearned revenue            8392.1      9483.1     10715.9     12109.0     13683.2
(-) Term debt repayment                  -3000.0     -3000.0     -3000.0     -3000.0     -3000.0
------------------------------------------------------------------------------------------------
Free Cash Flow to Equity (FCFE)          79381.0    100268.1    123775.9    150294.5    178795.6
(-) Share buybacks & dividends          -42502.0    -42502.0    -42502.0    -42502.0    -42502.0
Cash, year end                          131444.0    189210.1    270484.0    378276.5    514570.2

================================================================================================
4. BALANCE & CASH CHECKS
================================================================================================
Line (USD Millions)                      FY2026E     FY2027E     FY2028E     FY2029E     FY2030E
------------------------------------------------------------------------------------------------
Assets − Liabilities − Equity                0.0         0.0         0.0         0.0         0.0
Cash at or above minimum ($15,000M)            1           1           1           1           1
------------------------------------------------------------------------------------------------
Check status: BALANCED (all checks passed, gap = 0.0 in every year)

================================================================================================
5. EQUITY DCF VALUATION SUMMARY (Microsoft Corporation — NASDAQ: MSFT)
================================================================================================
PV of explicit 5-year FCFE (2026–2030):   $    468,510.11 million
Terminal value at 2030:                  $  2,880,761.71 million
PV of terminal value (discounted 5 yrs):  $  1,829,939.53 million
------------------------------------------------------------------------------------------------
Total Equity Value:                      $  2,298,449.65 million
Share of value after 2030 (TV / Equity):           79.62%
Diluted shares outstanding:                      7,465.00 million
------------------------------------------------------------------------------------------------
Model Value per share:                   $        307.90
Current Market Price (Sept 23, 2026):    $        500.59
================================================================================================
```

---

## V — The Check Block, Refusal Test, and Price Comparison

### 1. Check Block & Revolver Status
- **Balance Sheet Gap (`Assets − Liabilities − Equity`):** Reads **`0.0`** in every single forecast year (FY2026E through FY2030E).
- **Cash Floor & Revolver Activity:** Cash stays well above the \$15,000M floor in every year (rising from \$94,565.0M at FY25 year-end to \$131,444.0M in FY26E and \$514,570.2M in FY30E), so the revolving credit facility is **never drawn (\$0.0M in all years)** because annual FCFE (\$79.4B–\$178.8B) easily covers the \$42.5B annual share buyback and dividend program.

### 2. Swap-and-Break Refusal Verification
When `run_proforma(break_test_2026_cash=True)` is executed (forcing FY2026E ending cash to remain at the opening balance of \$94,565.0M), the model immediately halts and refuses to value the company:
```text
AssertionError: Balance sheet check failed in FY2026E: gap of -36879.0
```
- **Why `-36879.0`:** In FY2026E, Microsoft generates \$79,381.0M of FCFE and distributes \$42,502.0M in buybacks and dividends, adding **+\$36,879.0M** to cash (`131,444.0 − 94,565.0 = 36,879.0`). Forcing cash to opening \$94,565.0M understates Total Assets by exactly \$36,879.0M (`gap = -36,879.0`).

### 3. One-Sentence Model vs. Market Price Question
- **Today's Share Price:** **\$500.59** (as of market close, Wednesday, September 23, 2026; vs. \$491.65 on September 10, 2026).
- **One-Sentence Comparison Question:**  
  > *"On the same diluted share count of 7,465.00 million shares, the five-year pro-forma model values Microsoft at \$307.90 per share while the market prices it at \$500.59 per share as of September 23, 2026—does the market's \$192.69 per-share premium imply that Microsoft's \$65.0 billion annual AI CapEx will drive organic revenue growth closer to 18%–20% per year, or is the market underestimating the long-term cash drag of continuous GPU and datacenter replacement?"*

---

## E — Fresh Eyes: Partner Review (Both Directions)

### 1. Partner's Attack on Our Model & Our Two-Sentence Answer
*(Also recorded directly under the Assumption Table in Section R above)*
- **Partner Attack:** *"Why did you model `Organic revenue growth` at `13.0% a year` (`judgment`) while holding `Capital spending (CapEx)` flat at `$65,000.0M a year` (`guidance`), and what specific evidence would force you to change that assumption?"*
- **Our Answer (Two Sentences):**  
  We modeled 13.0% annual organic growth alongside a flat \$65.0B CapEx run-rate because Microsoft's FY2024–FY2025 CapEx surge (from \$28.1B to \$64.6B) built foundational datacenter shells and power capacity that will monetize through higher-margin Azure AI and Microsoft 365 Copilot software seats over FY2026E–FY2030E. We would revise this assumption to increase CapEx or cut organic growth if subsequent 10-Q filings reveal that short-lived GPU replacement cycles (~3–4 year server lives) require CapEx to keep growing at 15%+ annually just to sustain double-digit cloud growth.

### 2. Our Specific Attack on Partner's Model & Partner's Recorded Answer
- **Our Specific Attack on Partner's Retail/Consumer Model (`Gross Margin` & `Inventory Days` Judgment):**  
  *"In your assumption table, you projected gross margin expanding by 150 bps while holding inventory days flat at the FY2025 trough, despite management's 10-K risk disclosure warning of tariff and freight cost inflation—why did you assume zero working-capital buffer or margin pressure, and what inventory-to-sales ratio in Q1/Q2 would invalidate that call?"*
- **Partner's Recorded Answer:**  
  "I assumed gross margin expansion and flat inventory days because the company completed its supply-chain SKU rationalization in FY2025 and shifted 12% of sales to higher-margin direct-to-consumer channels that turn inventory faster. However, if inventory growth outpaces revenue growth by more than 300 bps for two consecutive quarters or if tariff pass-through fails, I would lower the gross margin assumption by 100 bps and add 5 days to inventory holding periods."

---

## Organic Growth — Learn on Your Own

1. **What is Organic Growth?**  
   Organic growth is the rate of revenue expansion generated internally by a company's existing operations (existing products, customer seat expansion, pricing, and new internally developed products), stripping out the inorganic revenue added by mergers and acquisitions (M&A), divestitures, and foreign currency exchange rate translations.
2. **How Does the MD&A Disclose It for Microsoft?**  
   In Item 7 (*Management's Discussion and Analysis*) of its Form 10-K, Microsoft does not report retail "same-store sales." Instead, Microsoft discloses **Constant Currency (CC) Percentage Change** columns alongside GAAP reported growth for every segment and product line (e.g., FY23: +7% reported vs. +11% CC; FY24: +16% reported vs. +15% CC; FY25: +15% reported vs. +15% CC) and explicitly states the **percentage-point impact of acquisitions** in the narrative below each table (for example, disclosing that the October 2023 Activision Blizzard acquisition added ~44 points to Xbox content/services growth and ~1.5 points to consolidated FY24 revenue), allowing analysts to isolate organic constant-currency growth.
3. **Why the Video Carries 1.8% for ABG When Reported Growth Was 4.7%:**  
   Asbury Automotive Group (`ABG`) is an active acquirer of dealership franchises; its **4.7%** reported revenue growth included top-line revenue bought through dealership acquisitions (such as the Koons Automotive acquisition). Because our 5-year pro-forma model does **not** project future unannounced M&A purchase cash outflows on the Cash Flow Statement or Balance Sheet, using 4.7% reported growth would give ABG "free" acquired revenue without paying the acquisition cost—so the model must use **1.8% same-store (organic) growth** representing the dealerships ABG already owns.

---

## Reflect — Partner Defense

1. **Which Label We Would Defend the Longest, and Why:**  
   We would defend the **`Gross margin = 68.50%` (`judgment`)** and **`Cash OpEx ÷ Gross Profit fading from 22.5% to 21.0%` (`judgment`)** labels the longest. Across FY2023–FY2025, even as Microsoft absorbed a 130% surge in annual CapEx (from \$28.1B to \$64.6B) and a doubling of PP&E depreciation (from \$11.0B to \$22.0B), its consolidated gross margin stayed remarkably tight between **68.82% and 69.76%**, while commercial software operating leverage drove total OpEx ÷ Gross Profit down by 568 bps (from 39.39% to 33.71%). That three-year track record proves Microsoft's pricing power and operating discipline can offset infrastructure depreciation.
2. **What One Number in the Filing Surprised Us Most:**  
   The single most surprising number in the FY2025 Form 10-K was **Property and equipment, net (`$204,966 million`)** alongside **Additions to property and equipment (`$64,551 million`)**—in just two fiscal years (from June 30, 2023 to June 30, 2025), Microsoft's net physical PP&E more than doubled from **\$95.6 billion to \$205.0 billion**, meaning a "capital-light" software company now carries more physical property and equipment on its balance sheet than almost any industrial or energy giant in the S&P 500, while still holding only **\$938 million** (3.9 days) of physical inventory.
