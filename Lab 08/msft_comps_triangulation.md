# Lab 08 — Deal Evidence and Valuation Triangulation
## Target Company: Microsoft Corporation (NASDAQ: MSFT)
### Valuation / Comparison Date: September 10, 2026

---

## 1. Represent — Peer Selection Policy & Business Model Screening

### A. Peer Policy Formulation
To value **Microsoft Corporation** using comparable-company Price-to-Earnings (P/E) multiples, peers must be selected based on economic comparability rather than broad sector labels:
- **Core Business Economics Required (Must Match):**
  1. Large-scale enterprise commercial cloud infrastructure (IaaS/PaaS) and enterprise productivity/collaboration software (SaaS).
  2. High-margin recurring commercial revenue streams (subscription and consumption-based licensing).
  3. Active development and deployment of generative AI foundation platforms and cloud developer ecosystems.
- **Criteria to Qualify:**
  - Candidates operating in cloud/enterprise software that also possess substantial consumer advertising, consumer hardware, or legacy database/hardware segments that alter gross margins or capital intensity.
- **Criteria to Exclude:**
  - Pure-play hardware OEMs without proprietary hyperscale cloud services (e.g., Apple).
  - Pure-play semiconductor manufacturers (e.g., Nvidia, AMD).
  - Pure-play consumer digital advertising / social media platforms without commercial B2B cloud infrastructure (e.g., Meta).

---

### B. Candidate Peer Investigation & Evidence

| Candidate Company | Ticker | Decision | Primary-Source Link & Section | Core Business Difference from Microsoft | Latest Annual Diluted GAAP EPS Public by 09/10/2026 | Fiscal Period & Publication Date | Sept 10, 2026 Closing Price |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Alphabet Inc.** | **GOOGL** | **`QUALIFY`** | [Alphabet Form 10-K, Item 1 (Business)](https://www.sec.gov/edgar/search/) — Google Cloud & Google Workspace sections. | Dominant revenue engine (>75%) is **digital advertising** (Google Search, YouTube), whereas Microsoft's core profit engine is commercial B2B software, enterprise cloud subscriptions, and OS licensing. | **$8.04** | FY ended Dec 31, 2024 *(Filed Feb 4, 2025, Form 10-K, Item 8 Note 11)* | **$330.39** |
| **Oracle Corporation** | **ORCL** | **`USE`** | [Oracle Form 10-K, Item 1 (Business)](https://www.sec.gov/edgar/search/) — Cloud Services and License Support, OCI, and Cloud Applications. | Substantially higher **debt leverage** ($80B+ total debt; BBB credit rating vs. Microsoft's AAA balance sheet) and smaller cloud infrastructure scale (~3% market share vs. Azure's ~20%). | **$4.34** | FY ended May 31, 2025 *(Filed June 20, 2025, Form 10-K, Item 8 Note 13)* | **$152.94** |

---

## 2. Implement — Running `comps.py` for Microsoft

Target and peer data were entered into [`comps.py`](file:///Users/devankmahajan/Desktop/comps.py):
- **Target (Microsoft - MSFT):** Closing Price = **$491.65**; FY2024 GAAP Diluted EPS = **$11.80** *(Form 10-K, Item 8 Note 19 p. 98)*.
- **Peer 1 (Alphabet - GOOGL):** Closing Price = **$330.39**; Diluted EPS = **$8.04** *(FY2024 Form 10-K, Note 11)*.
- **Peer 2 (Oracle - ORCL):** Closing Price = **$152.94**; Diluted EPS = **$4.34** *(FY2025 Form 10-K, Note 13)*.

### Terminal Run Output:
```text
======================================================================
COMPARABLE COMPANY VALUATION: PRICE-TO-EARNINGS (P/E)
======================================================================
Target Company: Microsoft Corporation (MSFT)
Target Price:   $491.65
Target EPS:     $11.80

----------------------------------------------------------------------
Peer Company               Ticker   Price ($)    Diluted EPS    P/E Multiple  
----------------------------------------------------------------------
Alphabet Inc.              GOOGL    $330.39      $8.04          41.093284     ×
Oracle Corporation         ORCL     $152.94      $4.34          35.239631     ×
----------------------------------------------------------------------

PEER MULTIPLES & IMPLIED VALUATION
----------------------------------------------------------------------
Usable peer count: 2
Peer median P/E:   38.166457×
Peer P/E range:    35.239631× to 41.093284×
Microsoft Corporation at peer median:   $450.36
Microsoft Corporation peer-implied range: $415.83–$484.90

----------------------------------------------------------------------
LEAVE-ONE-PEER-OUT SENSITIVITY (Unrounded calculations)
----------------------------------------------------------------------
Remove GOOGL: remaining ORCL estimate: $415.83 (change from full-peer estimate: -34.54)
Remove ORCL: remaining GOOGL estimate: $484.90 (change from full-peer estimate: +34.54)
======================================================================
Note: Never bridge P/E with cash/debt; P/E is an equity multiple.
======================================================================
```

---

## 3. Validate — Hand Check & Leave-One-Out Sensitivity

### A. Hand Calculation Check (Oracle):
1. **Oracle P/E Multiple:**
   $$\text{P/E}_{\text{ORCL}} = \frac{\$152.94}{\$4.34} = 35.239631336...\times \approx \mathbf{35.239631\times}$$
2. **Microsoft Implied Share Price at Oracle Multiple:**
   $$P_{\text{MSFT}} = 35.239631336... \times \$11.80 = \mathbf{\$415.8276...} \approx \mathbf{\$415.83}$$
3. **Full Precision Peer Median & Implied Price:**
   $$\text{Median P/E} = \frac{41.093284 + 35.239631}{2} = 38.166457498...\times$$
   $$P_{\text{MSFT, Median}} = 38.166457498... \times \$11.80 = \mathbf{\$450.364...} \approx \mathbf{\$450.36}$$

### B. Leave-One-Out Sensitivity Analysis
- **Predicted Effect of Removing Alphabet (GOOGL):**  
  Alphabet has the higher multiple ($41.09\times$). Removing it leaves Oracle ($35.24\times$) as the sole benchmark, pulling Microsoft’s implied price down from **\$450.36** to **\$415.83** (a change of **−\$34.54**).
- **Predicted Effect of Removing Oracle (ORCL):**  
  Removing Oracle leaves Alphabet as the sole benchmark, pushing Microsoft’s implied price up from **\$450.36** to **\$484.90** (a change of **+\$34.54**).
- **Loss of Information:**  
  With only two peers, removing either peer collapses the valuation range ($415.83–$484.90) into a single point **reference estimate**. A valuation range requires at least two distinct peers.

---

## 4. Evolve — Valuation Triangulation Table & Skeptical Review

### Lab 08 Deal Triangulation Table

| Valuation Method | Primary Metric / Multiple | Implied Valuation per Share | Valuation Range | Current Market Price (09/10/2026) | Price Implication |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DCF (Intrinsic Cash Flow)** | 5-Yr FCFF, WACC = 9.50%, $g = 3.00\%$ | **$220.80** | **$174.18 – $308.46** *(Corner range)* | **$491.65** | Market trades at a **+122.7% premium** to base DCF. Demands +21.2 percentage points of growth shift across all 5 years. |
| **P/E Comps (Relative Valuation)** | Peer Median P/E = **38.166457×** | **$450.36** | **$415.83 – $484.90** *(Peer range)* | **$491.65** | Market trades at a **+9.2% premium** to peer median comps, and slightly above the top peer ($484.90). |

---

### Skeptical Colleague Review

> **Skeptical Colleague Critique:**
> 
> "Your valuation comparison reveals two severe methodological vulnerabilities:
> 1. **Temporal / Date Mismatch:** You are pairing Microsoft's **September 10, 2026 market price ($491.65)** with its **FY2024 10-K diluted EPS ($11.80)**, which reflects the period ending June 30, 2024. That is an unadjusted two-year lag! In a fast-growing cloud and AI software giant, trailing-year earnings drastically understate the forward earnings base that the 2026 stock price is discounting.
> 2. **Divergence Between DCF and Comps:** Your DCF yields **$220.80**, while your P/E comps yield **$450.36**. You have essentially constructed two models answering two different questions without reconciling them: the DCF assumes CapEx will permanently drain free cash flow ($44.5B CapEx), whereas the market P/E comps (~38×) assume net income will compound rapidly without suffering a cash flow penalty from infrastructure investment.
> 
> **My Skeptical Question:**  
> *If Microsoft's multi-billion dollar AI datacenter buildout is a permanent capital requirement needed just to defend Azure market share against AWS and GCP, why should Microsoft command a premium 38×–41× P/E multiple when its true cash conversion to equity holders only supports a $220 intrinsic valuation?*"

---

### Author's Response to Skeptical Critique

| Critique Point | Judgment | Rationale & Evidence |
| :--- | :--- | :--- |
| **1. Temporal / Date Mismatch** | **`ACCEPT`** | Valid criticism. Using FY2024 reported GAAP EPS ($11.80) against a September 2026 price inflates the trailing P/E multiple (~41.7×). If Microsoft's FY2026 net income grows to ~$14.50 EPS (as implied by consensus), the effective forward multiple at $491.65 is ~33.9×, bringing Microsoft's multiple in line with Oracle's 35.2× and below Alphabet's 41.1×. In formal handoff, this temporal lag must be explicitly disclosed as a historical trailing comparison rather than forward-adjusted. |
| **2. Valuation Divergence (DCF vs Comps)** | **`ACCEPT`** | Fully accepted. The divergence between $220.80 (DCF) and $450.36 (Comps) is not an error, but the core economic finding of this triangulation: the market is valuing Microsoft on an accounting earnings basis (P/E ~38×), completely ignoring the near-term cash drain from $45B+ AI CapEx. The DCF rigorously subtracts all CapEx from cash flow, exposing the cash drag that P/E obscures. |
| **3. Sourced Obstacle & Skeptical Question** | **`ACCEPT (with qualification)`** | If AI CapEx remains at 15%–20% of revenue permanently with declining ROI, Microsoft will experience a sharp downward multiple re-rating toward its DCF intrinsic floor ($220–$260). Conversely, if CapEx is upfront growth investment that monetizes into high-margin Copilot/Azure software cash flows by FY27, free cash flow will surge to match net income, validating the $450–$490 price. |

---

## 5. Reflect — Defending the Investment Conclusion

### Partner Discussion Summary
1. **Why Peers Belong:**
   - **Alphabet (GOOGL)** and **Oracle (ORCL)** represent the premier enterprise cloud and software platform peers. Both share hyperscale cloud infrastructure investments and AI software development, but Alphabet requires qualification due to advertising exposure and Oracle requires qualification due to debt leverage.
2. **What Comps Add to the DCF:**
   - The DCF tells us what Microsoft is worth based purely on cash flows generated and reinvested ($220.80).
   - Comps tell us how the broader market is pricing earnings across the enterprise software sector ($450.36 at a 38.2× median multiple).
   - Combining both shows that **today's market price ($491.65) reflects aggressive optimism:** it prices Microsoft at a premium to both its intrinsic DCF cash floor (+122.7%) and peer median comps (+9.2%).
3. **Defensible Call & Boundary:**
   - **Call: `WATCH / DEFER`**
   - **Initiate Buy if:** The share price pulls back below **$261.00** (the upper boundary of our conservative DCF at 8.5% WACC / 3% g), **OR** if subsequent 10-Q filings show that Microsoft Cloud gross margin expands past 72% while CapEx growth slows below 15%, demonstrating that AI investment has shifted from cash drain to high-margin cash realization.
   - **Otherwise:** Defer initiating new positions at $491.65.
   - **Key Metric to Monitor:** Microsoft Cloud Gross Margin % and quarterly additions to property and equipment in upcoming Form 10-Q filings.

