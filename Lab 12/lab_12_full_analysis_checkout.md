# Lab 12 — Pro-Forma Sensitivity: Present and Review Your Full Analysis
**Target Company:** Microsoft Corporation (NASDAQ: `MSFT`, CIK: `0000789019`)  
**Learning Partner Company:** McDonald's Corporation (NYSE: `MCD`, CIK: `0000063908`)  
**Category:** Thursday Merit Checkout (25 / 25 Rubric Target)  
**Valuation / Reference Date:** September 23, 2026 Market Close = **$500.59** *(Sept 10, 2026 Close = $491.65)*  
**Primary Files & Models Open:**
- Pro-Forma Engine & Sensitivity Script: [`Lab 11/msft_proforma.py`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/Lab%2011/msft_proforma.py)
- Sensitivity Checkout & Statement Trace: [`Lab 11/lab_11_msft_sensitivity_checkout.md`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/Lab%2011/lab_11_msft_sensitivity_checkout.md)
- Pro-Forma 5-Year Model Checkout: [`Lab 10/lab_10_msft_proforma_checkout.md`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/Lab%2010/lab_10_msft_proforma_checkout.md)
- Relative Valuation & Comps Triangulation: [`Lab 08/msft_comps_triangulation.md`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/Lab%2008/msft_comps_triangulation.md)
- Research Report & Prior-Year Track Record: [`MSFT-research/Microsoft_2026-09-03_report.md`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/MSFT-research/Microsoft_2026-09-03_report.md)

---

## D — The Core Question

> **"How did I get from choosing this company to my valuation conclusion, which assumptions drive it, and what evidence could change my mind?"**  
> **Current Conclusion:** **`WATCH / DEFER`**  
> *Base intrinsic equity value from our 5-year linked pro-forma is **$307.90 per share** (and **$365.92** in our optimistic +3% growth case), compared to today's market price of **$500.59**. We cannot justify initiating a buy position until the market price retraces closer to intrinsic cash value, or until empirical evidence confirms that Microsoft's $65B annual AI CapEx can sustain organic revenue growth above 18%–20% without compressing gross margins below 68%.*

---

## R — The Full Analysis Route (The Six Stops)

```
Stop 1: Target Selection ────► Stop 2: Company & Evidence ────► Stop 3: Pro-Forma Model
  • Enterprise SaaS / Cloud      • FY23-FY25 10-K Filings         • 3-Statement Integration
  • AAA-Rated Balance Sheet      • $281.7B Rev, $168.9B Cloud     • Unearned Rev Float ($64.6B)
  • S&P 500 Bellwether           • 68.8% Gross Margin             • Fixed AI CapEx ($65.0B/yr)
                                                                            │
                                                                            ▼
Stop 6: Interpretation   ◄──── Stop 5: Sensitivity & Drivers ◄── Stop 4: Valuation & Comps
  • Call: Watch / Defer          • OAT on Growth vs GM            • DCF Value: $307.90/sh
  • Reverse DCF Implication      • Growth Span: $110.15/sh        • Comps Median: $450.36/sh
  • What Changes Our Mind        • GM Span: $23.53/sh             • Market Price: $500.59/sh
```

### Stop 1: Target Selection Rationale & Initial View
1. **Why Selected:** Microsoft is the global bellwether for enterprise cloud infrastructure (Azure) and enterprise productivity software (M365, Windows, Dynamics, LinkedIn). It possesses a pristine AAA-rated balance sheet, unmatched enterprise distribution, and is the primary commercialization vehicle for generative AI foundation models (via OpenAI and Copilot).
2. **Suitability for Analysis:** Microsoft files transparent, audited SEC 10-K filings with consistent segment breakdowns (*Productivity & Business Processes*, *Intelligent Cloud*, *More Personal Computing*), constant-currency reconciliations in Item 7 MD&A, and clear capital allocation statements.
3. **Initial View (Lab 03 Memo):** `Watch / Defer`. While commercial cloud demand is accelerating, market pricing reflects extreme multiple expansion. We required an audited, conservative valuation to determine whether hyperscale AI infrastructure spending ($65B+/year) will generate sufficient cash returns to equity holders to justify a market price near $500.

### Stop 2: Company Economics & Grounded Evidence
1. **How Microsoft Earns Money:** 
   - **Intelligent Cloud (~40% of revenue):** Azure consumption licensing, Windows Server, enterprise services.
   - **Productivity & Business Processes (~33% of revenue):** Microsoft 365 Commercial/Consumer seats, Copilot add-ons ($30/user/mo), LinkedIn, Dynamics 365.
   - **More Personal Computing (~27% of revenue):** Windows OEM, Xbox content/services, Surface hardware, search ads.
2. **Audited Primary Sources & Reporting Periods (USD Millions, FY ends June 30):**
   - **Revenue:** FY23: $211,915M $\rightarrow$ FY24: $245,122M $\rightarrow$ FY25: **$281,724M** (*Item 8, p. 59*). Organic constant-currency growth was **+15.0%** in FY25 (*Item 7, p. 33*).
   - **Gross Profit & Margin:** FY23: $146,052M (68.92%) $\rightarrow$ FY24: $171,008M (69.76%) $\rightarrow$ FY25: **$193,893M (68.82%)** (*Item 8, p. 59*).
   - **Net Income:** FY23: $72,361M $\rightarrow$ FY24: $88,136M $\rightarrow$ FY25: **$101,832M** (*Item 8, p. 59*).
   - **Cash CapEx (Additions to PP&E):** FY23: $28,107M $\rightarrow$ FY24: $44,475M $\rightarrow$ FY25: **$64,551M** (*Item 8 Cash Flow, p. 62*).
   - **Diluted Share Count:** **7,465.00 million shares** (*FY25 10-K, Note 18*).

### Stop 3: The Five-Year Pro-Forma Model & Company-Specific Dynamics
1. **How History Became Forecast Assumptions:**
   - *Organic Revenue Growth:* 13.00% / year (`judgment`), reflecting Azure AI expansion tempered against a \$281.7B baseline.
   - *Gross Margin:* 68.50% (`judgment`), modeling 32 bps of compression from FY25's 68.82% due to management's disclosure (*Item 7, p. 36*) that AI datacenter electricity and GPU server costs weigh on cloud margins.
   - *Cash OpEx ÷ Gross Profit:* Tapering from 22.5% to 21.0% (`judgment`), down from 31.86% in FY23 and 22.37% in FY25 as commercial software operating leverage continues.
   - *Depreciation ÷ Opening PP&E:* Fixed at 10.7335% (`history`), matching FY25 Note 7 PP&E depreciation (\$22,000M ÷ \$204,966M).
   - *CapEx:* \$65,000M / year flat (`guidance`), matching FY25 cash additions (\$64,551M).
2. **The Company-Specific Line That Replaces Floor Plan:**
   - **Short-Term Unearned Revenue (\$64,555M in FY25, 22.9143% of revenue).**
   - Microsoft collects enterprise cloud subscriptions upfront before software delivery. This 0.0% interest customer liability generates **+$8.4B to +$13.7B per year in positive working-capital cash inflows** (`+Δ Unearned Revenue` in FCFE), providing internal financing for Microsoft's \$65B annual AI CapEx.
3. **Accounting Integrity:** Balance sheet gap (`Assets − Liabilities − Equity`) is exactly **0.0** in all five forecast years. Ending cash grows from \$94.6B to \$514.6B, comfortably exceeding the \$15.0B minimum cash floor (revolver is drawn \$0.0).

### Stop 4: Valuation Methods, Peer Comparison, and Reverse DCF
1. **Valuation Basis & Stated Results:**
   - **Valuation Date:** September 23, 2026 | **Currency:** USD Millions | **Share Basis:** 7,465.00M diluted shares.
   - **DCF Method:** Free Cash Flow to Equity (`FCFE`), discounted at **Cost of Equity $K_e = 9.50\%$** ($R_f = 4.10\% + 1.08\,\beta \times 5.00\%\text{ ERP}$) and **Terminal Growth $g = 3.00\%$**.
   - **Explicit 5-Yr FCFE PV:** \$468,510.1M | **Terminal Value PV:** \$1,829,939.5M (79.62% of value).
   - **Model Equity Value per Share:** **$307.90**.
2. **Peer Comps Triangulation (Lab 08):**
   - **Peers Chosen:** Alphabet (`GOOGL`, P/E 41.09×) and Oracle (`ORCL`, P/E 35.24×). Peer Median P/E = **38.17×**.
   - **Peer-Implied Valuation per Share:** **$450.36** (Range: \$415.83 to \$484.90).
   - **Why the Methods Differ:** Comps value Microsoft on accounting earnings, ignoring the cash penalty of \$65B in capital expenditures. The DCF rigorously deducts all cash CapEx, exposing the near-term cash drag that high P/E multiples obscure.
3. **Market Price & Reverse-DCF Result:**
   - **Market Price:** **$500.59** (September 23, 2026).
   - **Reverse-DCF Implication:** To solve for \$500.59 while holding CapEx at \$65B and $K_e$ at 9.50%, Microsoft would need organic revenue growth to exceed **19.5%–20.0% compounded annually** through 2030, or terminal growth would need to be an unrealistic 4.5%+. Alternatively, it assumes AI CapEx will drop dramatically to <\$30B by FY28.

### Stop 5: Sensitivity & Drivers (Lab 11 Results)
1. **Two Tested Operating Drivers (One-at-a-Time):**
   - **Driver 1: Organic Revenue Growth Rate** (`10.00%` $\rightarrow$ `13.00%` $\rightarrow$ `16.00% / yr`, 6.0 pt range).
     - *2030E EBIT Span:* **$74,677.3M** | *2030E FCFE Span:* **$68,735.0M** | *Value/Share Span:* **$110.15** ($255.77 to $365.92).
   - **Driver 2: Gross Margin Percentage** (`66.50%` $\rightarrow$ `68.50%` $\rightarrow$ `70.50% of rev`, 4.0 pt range).
     - *2030E EBIT Span:* **$16,402.2M** | *2030E FCFE Span:* **$13,475.3M** | *Value/Share Span:* **$23.53** ($296.13 to $319.66).
2. **Causal Statement Trace (+3% Growth: 13% $\rightarrow$ 16%):**
   - FY2030E Revenue +$72,658.4M $\rightarrow$ Cost of Revenue +$22,887.4M $\rightarrow$ Gross Profit +$49,771.0M $\rightarrow$ Cash OpEx +$10,451.9M $\rightarrow$ Depreciation unchanged ($0.0) $\rightarrow$ **EBIT +$39,319.1M** $\rightarrow$ Taxes (18%) +$7,077.4M $\rightarrow$ **Net Income +$32,241.7M**.
   - Working Capital boost: `+Δ Unearned Revenue` (+18,701.7M vs +13,683.2M base = **+$5,018.6M**) minus OWC (-$876.1M) minus Inventory (-$73.7M) = **+$4,068.8M** net working capital cash inflow.
   - **FY2030E FCFE rises +$36,310.5M** ($178,795.6M $\rightarrow$ $215,106.1M).
   - PV of cash flows lifts Equity Value by +$433,178.4M, adding **+$58.03 per share** ($307.90 $\rightarrow$ $365.92).
3. **What the Ranking Establishes vs. Limitations:**
   - Growth dominates over Gross Margin by **4.68×** on output span ($110.15 vs $23.53).
   - Even normalized to **1.00 percentage point**, Growth is **3.12× more powerful** (+$18.36/sh vs +$5.88/sh) because growth compounds over 5 years ($(1+g)^5$) against a high 68.5% margin and pulls in unearned revenue float.
   - *Limitation:* The OAT table is a deterministic map, not a probability distribution; it does not model joint correlations (e.g., cloud growth decelerating while gross margins compress simultaneously during an enterprise tech spending slowdown).

### Stop 6: Interpretation, Recommendation & Evolution
1. **Conditional Recommendation:** **`WATCH / DEFER`**. Even under the most aggressive historical growth scenario (16.0% compounded for 5 years, reaching $591.7B revenue), the intrinsic value of **$365.92** is **26.9% below** the market price of **$500.59**.
2. **How My View Evolved:** Initially (Lab 03), I assumed AI software monetization would quickly overwhelm infrastructure costs. After modeling the integrated 3-statement pro-forma in Lab 10 and tracing CapEx in Lab 11, I realized that physical PP&E doubling from $95.6B to $205.0B in two years locks in $37.7B of annual depreciation by 2030. Microsoft has become a capital-intensive utility for AI workloads, creating a persistent free cash flow drag that equity markets are currently overlooking.
3. **What Would Change My Mind:**
   - Move to **`Initiate Buy`** if the market price pulls back below **$310.00**, OR if subsequent 10-Q filings demonstrate that Copilot and Azure AI drive commercial Cloud Gross Margin above **72%** while annual CapEx stabilizes below 15% of revenue.

---

## I — Presenter's Walkthrough Script

*(Spoken directly to learning partner in plain language)*

> "Hey! Today I'm walking you through my full analysis of **Microsoft (`MSFT`)**. My bottom-line conclusion is **Watch / Defer**: my 5-year DCF values Microsoft at **$307.90 per share**, and even in my optimistic growth case it reaches **$365.92**, while today's market trades at **$500.59**. Here is the journey of how I reached that conclusion:
> 
> "I chose Microsoft because it is the premier AAA-rated software platform leading commercial generative AI. From their FY2025 10-K, they generated **$281.7 billion in revenue** and **$101.8 billion in net income** at a **68.8% gross margin**. But the most shocking number was their balance sheet: physical property and equipment more than doubled from **$95.6 billion in FY23 to $205.0 billion in FY25**, driven by **$64.6 billion in annual cash CapEx** for AI datacenters and GPUs.
> 
> "When translating this into my 5-year pro-forma model, I replaced the auto dealership 'Floor Plan' line with Microsoft's true company-specific engine: **Short-Term Unearned Revenue ($64.6B, ~22.9% of revenue)**. Because enterprise customers pay upfront for multi-year Azure and M365 contracts at 0% interest, this creates an annual positive cash inflow of **$8.4B to $13.7B**, which helps fund their massive **$65.0 billion annual CapEx**.
> 
> "In valuation, when I ran peer comps against Alphabet and Oracle, the median 38.2× P/E gave an implied price of **$450.36**. But comps only look at accounting earnings! When you run an intrinsic FCFE DCF that deducts the actual cash spent on datacenters, the cash-backed value drops to **$307.90**. 
> 
> "In Lab 11, I tested my two main operating drivers: **Organic Revenue Growth (10% to 16%)** and **Gross Margin (66.5% to 70.5%)**. Revenue growth completely dominated the model, creating a **$110.15 per-share span** versus only **$23.53** for Gross Margin. Why? Because a 3-point shift in growth compounds over 5 years, dropping $39.3B straight to EBIT and pulling in an extra $5.0B of unearned customer cash float.
> 
> "My conclusion remains **Watch / Defer**. Today's market price of $500.59 is baking in over 19% compound growth through 2030 or an immediate end to AI CapEx—neither of which is supported by management's guidance."

---

## V — Question and Check as the Reviewer (Partner Company: McDonald's Corporation — `MCD`)

*(Specific questions and checks executed for learning partner analyzing McDonald's)*

### 1. Specific Reviewer Questions Asked to McDonald's Partner:
1. **Selection & Evidence Area:**  
   *"In McDonald's FY2024/FY2025 Form 10-K, roughly 95% of restaurants are franchised while only 5% are company-operated. How does your model separate franchised revenues (rents, royalties, initial fees) from company-operated sales, and which specific filing table did you use to benchmark your baseline same-store sales growth?"*
2. **Model & Valuation Area:**  
   *"McDonald's balance sheet carries **negative stockholders' equity** (~-$4.5B) due to decades of debt-financed share repurchases, and carries over $35B in long-term debt. Given this negative book equity, how did your pro-forma engine balance assets against liabilities and equity, and why did you choose FCFF/WACC (or FCFE) rather than letting negative equity distort your cost of capital?"*
3. **Sensitivity & Interpretation Area:**  
   *"In your Lab 11 sensitivity table, did Franchised Margin % or Systemwide Same-Store Sales Growth rank as your #1 driver? Does that ranking hold true because your tested range on sales growth was wider, and what specific evidence regarding franchisee store margin compression or beef/wage inflation would force you to change your call?"*

### 2. Evidence Check & Calculation Trace Performed Together:
- **Cited Source Opened:** [**McDonald's Form 10-K (Item 8 — Consolidated Statements of Income)**](https://www.sec.gov/edgar/search/).
- **Calculation Traced:** Partner's **Franchised Restaurant Margin %** calculation:
  $$\text{Franchised Margin} = \frac{\text{Franchised Revenues} - \text{Franchised Occupancy Expenses}}{\text{Franchised Revenues}}$$
- **Checked Numbers:** Traced FY2024 Franchised Revenues (\$15,400M) minus Occupancy Costs (\$2,550M) = \$12,850M margin, yielding **~83.4% franchised operating margin**.
- **Verification Result:** **SUPPORTED.** The partner's pro-forma model correctly applied this high ~83% margin to franchised royalties rather than confusing it with company-operated restaurant margins (~16%), preserving the cash flow mechanics of McDonald's core real-estate and royalty engine.

---

## E — Explain Back, Feedback, and Response & Revision

### 1. Reviewer Explaining Back Partner's Analysis (McDonald's `MCD`):
- **Partner's Valuation Conclusion:** **`HOLD / FAIRLY VALUED`** at an intrinsic DCF value of **$295.00 per share** vs. a market price of ~$305.00 (within a ~5% margin of safety).
- **Partner's Main Driver:** **Global Comparable Guest Counts & Same-Store Sales Growth** (tested between 1.5% and 5.0% / yr), generating a \$42.00/share valuation span.
- **Partner's Biggest Limitation:** High leverage ($37B in debt) and negative book equity make equity DCF sensitive to refinancing rates; if interest rates stay higher for longer, debt service will crowd out free cash flow for share buybacks.
- **One Evidence-Backed Strength:** Outstanding modeling of McDonald's master lease structure—accurately reflecting that McDonald's owns/leases the underlying real estate and collects minimum base rents even if franchisee store sales fluctuate.
- **One Specific Actionable Improvement:** Explicitly model a refinancing schedule for McDonald's upcoming debt maturities over 2026–2028 rather than holding interest expense flat, to capture the rollover from 2.5% maturing notes to 5.0%+ current debt yields.

---

### 2. Presenter's Record of Feedback Received on Microsoft (`MSFT`):

#### A. Questions Received from Partner:
1. *Partner Question 1:* "You assumed CapEx stays flat at \$65.0 billion per year through FY2030E, but Satya Nadella announced in the July 2026 earnings call that they added 31 datacenters in one quarter alone. If AI datacenter demand is compounding, isn't holding CapEx flat an artificial floor that overstates your FCFE?"
2. *Partner Question 2:* "Your pro-forma ending cash reaches **$514.6 billion** by FY2030E because Microsoft generates more FCFE than its \$42.5B annual buyback/dividend program. Why didn't you model higher share buybacks, and does that massive cash hoard distort your valuation?"

#### B. Presenter's Answers Given & Scoped Gaps:
- *Answer to Q1 (CapEx Flat at \$65B):*  
  "I held CapEx flat at \$65.0B because FY24–FY25 represented an unprecedented 130% surge (from \$28B to \$65B) to secure land, power interconnection, and datacenter shells. Once those shells are built, subsequent CapEx is modular server installation. However, **this is an acknowledged limitation:** if GPU life-cycles remain short (~3 years), ongoing server replacement will require CapEx to scale with revenue (e.g. 18%–20% of revenue, reaching \$90B–\$100B+ by 2030), which would reduce my intrinsic value from \$307.90 to ~$240–$250."
- *Answer to Q2 (Cash Accumulation & Buybacks):*  
  "In my FCFE model, all free cash flow generated is discounted back to equity holders regardless of whether it sits in cash or gets paid out as dividends (Miller-Modigliani cash equivalence). Holding buybacks constant at \$42.5B/yr simply reflects conservative historical practice without assuming management initiates debt-funded buybacks or massive M&A."

#### C. Post-Review Decision: What We Will Keep, Revise, and Investigate

| Decision Area | Action | Detailed Rationale & Model Effect |
| :--- | :---: | :--- |
| **Keep** | **`KEEP`** | **Keep the `Watch / Defer` valuation conclusion.** The review confirmed that our DCF intrinsic value (\$307.90) and our optimistic growth case (\$365.92) both sit far below the \$500.59 market price. There is no basis to upgrade to Buy. |
| **Keep** | **`KEEP`** | **Keep `Organic Revenue Growth` as the primary sensitivity driver.** Partner agreed that multi-year exponential compounding and unearned revenue float make top-line growth the fundamental driver of Microsoft's value over gross margin. |
| **Revise** | **`REVISE`** | **Revise the CapEx schedule to test a 'Variable CapEx' scenario (% of revenue).** Rather than only testing flat \$65.0B CapEx, create a secondary sensitivity case linking CapEx to 18.0% of revenue (\$57B in FY26E rising to \$93.4B in FY30E) to capture the shorter GPU hardware replacement cycle raised in the partner's critique. |
| **Investigate** | **`INVESTIGATE`** | **Investigate Commercial Remaining Performance Obligations (cRPO).** In the upcoming Q1 FY27 Form 10-Q, audit the growth rate of long-term and short-term unearned revenue to see if customer commitments are accelerating fast enough to support the market's implied 20% growth rate. |

---

## Reflect — Partner Defense & Deeper Understanding

1. **Which question made you reconsider something?**  
   My partner's question about **CapEx remaining flat at \$65B while datacenters are doubling** forced me to confront the physical reality of AI hardware. In traditional software, code is written once and distributed at zero marginal cost. In generative AI, software requires physical electricity, cooling, and Nvidia GPUs that depreciate over 3 to 4 years. Modeling CapEx as a flat dollar amount likely overstates free cash flow in the outer years (FY28–FY30).
2. **What do you now understand better about your own company?**  
   I now understand that **Microsoft's valuation disconnect is fundamentally a clash between accounting multiples and cash conversion.** The market is pricing Microsoft at 38×–42× P/E because it looks only at GAAP Net Income ($100B+ and growing). But an intrinsic DCF accounts for the \$65 billion in cash ripped away from shareholders every year to pay for datacenters. Until Microsoft can prove that Copilot software seats convert that hardware into pure high-margin cash flow, paying \$500+ per share offers zero margin of safety.
