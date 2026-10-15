# Lab 13 — Thursday Merit Checkout: Meridian Foundation Reserve Mandate Checker
**Client / Account:** Meridian Foundation Reserve (\$100M Fictional Asset Pool)  
**Category:** Thursday Merit Checkout (25 / 25 Rubric Target)  
**Course:** FIN439 — Corporate Valuation & Investment Policy Analysis  
**Repository Links:** 
- Python Mandate Checker: [`Lab 13/mandate.py`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/Lab%2013/mandate.py)
- Checkout & Policy Synthesis: [`Lab 13/lab_13_meridian_mandate_checkout.md`](file:///Users/devankmahajan/.gemini/antigravity/scratch/FIN439/Lab%2013/lab_13_meridian_mandate_checkout.md)

---

## D — The Core Question

> **"Which of these portfolios does the Meridian Foundation's mandate permit — and what must the CIO answer before anyone optimizes?"**

### Executive Summary & Answer
1. **Permitted Portfolios:**
   - **Candidate A** is the **only** candidate portfolio among A, B, and C that the Meridian Foundation's mandate permits. Candidate A passes all five checkable hard constraints (100% weight sum, long-only, 14.0% reserve-eligible vs. 3.0% minimum, 100.0% 5-day liquidity vs. 90.0% minimum, and 0.0% corporate issuer concentration vs. 8.0% cap).
   - **Candidate B fails 3 rules:** Reserve-eligible weight (1.0% vs. 3.0%), 5-day liquidity (85.0% vs. 90.0% due to 15% private real estate), and single-issuer concentration (9.0% Acme Corp vs. 8.0% cap).
   - **Candidate C fails 1 rule:** Reserve-eligible weight (2.0% vs. 3.0%).
2. **What the CIO Must Answer Before Optimization:**
   - The CIO must specify the **exact objective function** for the portfolio optimizer—specifically, whether to minimize tracking error against the 60/40 policy benchmark (S4), maximize Sharpe ratio / real return net of fees (S2), or minimize downside tail risk / shortfall probability below -10% (S9).

---

## R — Statement Sorting: The Ten CIO Statements (S1–S10)

Before writing code or constructing portfolios, each statement uttered by the CIO must be classified into its formal Investment Policy Statement (IPS) category: **Objective**, **Hard Constraint**, **Preference**, **Unverifiable Promise**, or **Missing**.

| ID | Exact CIO Statement | Statement Category | One-Line Economic & Governance Rationale |
| :--- | :--- | :--- | :--- |
| **S1** | *"Horizon seven years; annual rebalancing."* | **Hard constraint** | Establishes an uncompromisable 7-year strategic investment horizon and a rigid operational governance rule enforcing annual rebalancing. |
| **S2** | *"Objective: CPI + 4% a year, net of costs, over rolling five-year periods."* | **Objective** | Defines the primary, measurable real return target that justifies taking investment risk over five-year evaluation cycles. |
| **S3** | *"Pays out \$0.75 million every quarter; twelve months of payouts held in cash or daily-liquid government securities."* | **Hard constraint** | Enforces a non-negotiable cash flow disbursement policy requiring a 3.0% (\$3.0M) liquid liquidity reserve at all times. |
| **S4** | *"Benchmark: 60% global equities, 40% U.S. investment-grade bonds."* | **Preference** | Defines the strategic policy baseline and asset allocation reference mix against which performance and active risk are measured, rather than a hard boundary. |
| **S5** | *"Long-only: no borrowing, short sales or derivatives."* | **Hard constraint** | Imposes an absolute legal and execution barrier prohibiting leverage, negative weights, short exposure, or synthetic instruments. |
| **S6** | *"No single issuer above 8%."* | **Hard constraint** | Establishes a mathematical concentration ceiling limiting exposure to any single non-exempt corporate issuer to 8.0% across all security types. |
| **S7** | *"Annual turnover at most 25% without committee approval."* | **Hard constraint** | Caps portfolio rebalancing churn at 25% per year to control transaction drag and execution costs unless an explicit governance exception is granted. |
| **S8** | *"At least 90% redeemable within five business days."* | **Hard constraint** | Mandates a strict structural liquidity floor requiring $\ge 90\%$ of total fund capital to convert to cash within five trading days. |
| **S9** | *"The reserve cannot have a calendar-year loss greater than 10%. No measure, no breach rule."* | **Unverifiable promise** | Represents an ex-ante unenforceable aspiration; without risk-free put guarantees, tail loss cannot be prohibited by fiat, lacks a statistical confidence measure (e.g. 95% CVaR), and specifies no remediation rule. |
| **S10** | *"No sector, ESG, tax or home-bias preference; nobody has said what the pilot should optimize."* | **Missing** | Confirms the absence of secondary constraints while explicitly highlighting that the mathematical objective function is entirely missing. |

---

## I — Build the Checker: `mandate.py`

The mandate checker is written in Python using the standard library only. It computes all thresholds and metrics dynamically from inputs and evaluates the candidate portfolios.

### Command to Execute
```bash
python3 "mandate.py"
```

### Full Source Code Architecture ([`mandate.py`](file:///Users/devankmahajan/Desktop/mandate.py))
```python
"""
mandate.py - Meridian Foundation Reserve Mandate Checker
Standard library only.
"""

# Reserve and Distribution Parameters
RESERVE_SIZE = 100.0             # USD millions
QUARTERLY_DISTRIBUTION = 0.75    # USD millions
QUARTERS_TO_COVER = 4            # Number of quarters
LIQUIDITY_WINDOW = 5             # Business days
MIN_LIQUID_SHARE = 90.0          # Minimum liquid percentage
ISSUER_LIMIT = 8.0               # Maximum exposure to single corporate issuer (%)

# Holdings Master Table
HOLDINGS = [
    {"holding": "Cash",                        "issuer": "none",             "days": 0,  "reserve_eligible": True},
    {"holding": "Treasury bills",              "issuer": "U.S. Treasury",    "days": 1,  "reserve_eligible": True},
    {"holding": "Treasury 10-year note",       "issuer": "U.S. Treasury",    "days": 1,  "reserve_eligible": True},
    {"holding": "Global equity index fund",    "issuer": "diversified fund", "days": 2,  "reserve_eligible": False},
    {"holding": "Investment-grade bond fund",  "issuer": "diversified fund", "days": 3,  "reserve_eligible": False},
    {"holding": "Private real estate fund",    "issuer": "diversified fund", "days": 90, "reserve_eligible": False},
    {"holding": "Acme Corp bonds",             "issuer": "Acme Corp",        "days": 4,  "reserve_eligible": False},
    {"holding": "Acme Corp stock",             "issuer": "Acme Corp",        "days": 1,  "reserve_eligible": False},
]

EXEMPT_ISSUERS = {"none", "u.s. treasury", "diversified fund"}
```

### Mandate Quiz: Testing the Most Complex Logic Line
- **The Line Most People Stumble On:**
  ```python
  if issuer.strip().lower() not in EXEMPT_ISSUERS:
      company_totals[issuer] = company_totals.get(issuer, 0.0) + w
  ```
- **The Quiz Question:** *Why do Acme Corp bonds (4 days to redeem) and Acme Corp stock (1 day to redeem) aggregate together into a single total, while Cash, Treasury bills, and Diversified index funds bypass this aggregation entirely?*
- **The Answer:** *The mandate cap (S6) governs **economic entity risk (default and bankruptcy risk)**, not security-type risk. If Acme Corp files Chapter 11, both its equity and debt undergo severe impairments regardless of instrument maturity. Cash and Treasuries carry zero corporate default risk, and diversified mutual funds eliminate idiosyncratic issuer risk through statutory diversification, making them legally and economically exempt.*

---

## V — Verification: Proof on the Known Answer

### 1. Computed Threshold
$$\text{Reserve Minimum} = \frac{\text{Quarters to Cover} \times \text{Quarterly Distribution}}{\text{Reserve Size}} = \frac{4 \times \$0.75\text{M}}{\$100.0\text{M}} = \mathbf{3.0\%}$$

### 2. Candidate Evaluation Matrix

| Rule Evaluated | Candidate A | Candidate B | Candidate C | Candidate D (Attack) |
| :--- | :---: | :---: | :---: | :---: |
| **Weights sum to 100** | 100.0 **pass** | 100.0 **pass** | 100.0 **pass** | 100.0 **pass** |
| **Long-only (lowest weight)** | 0.0 **pass** | 0.0 **pass** | 0.0 **pass** | 0.0 **pass** |
| **Reserve $\ge$ 3.0%** | 14.0 **pass** | 1.0 **FAIL** | 2.0 **FAIL** | 3.0 **pass** |
| **Redeemable in 5 days $\ge$ 90%** | 100.0 **pass** | 85.0 **FAIL** | 100.0 **pass** | 100.0 **pass** |
| **Largest single company $\le$ 8%** | 0.0 **pass** | 9.0 **FAIL** | 8.0 **pass** | 0.0 **pass** |
| **Calendar-year loss** | *requires CIO clarification* | *requires CIO clarification* | *requires CIO clarification* | *requires CIO clarification* |
| **Verdict** | **passes every checkable rule** | **fails 3 rule(s)** | **fails 1 rule(s)** | **passes every checkable rule** |

### 3. Detailed Failure Diagnostics
- **Candidate B:**
  1. *Reserve Minimum Failure:* Cash is only 1.0% (and 0% Treasuries), leaving \$2.0M of mandated distributions uncovered.
  2. *Liquidity Window Failure:* 15.0% is allocated to Private Real Estate Fund, which takes 90 business days to redeem. Total 5-day liquid share is only 85.0%, breaching the 90.0% requirement.
  3. *Single Issuer Failure:* Acme Corp bonds (5.0%) and Acme Corp stock (4.0%) combine to 9.0%, breaching the 8.0% single-company limit.
- **Candidate C:**
  1. *Reserve Minimum Failure:* Cash (1.0%) + T-bills (1.0%) = 2.0%, which is \$1.0M below the 3.0% minimum liquid payout buffer. Acme Corp stock is at exactly 8.0% (passes).

### 4. Probe Verification: Proving the Checker Catches Violations
Following the course instructions, Candidate A was tested with:
$$\text{Cash} = -2.0\%, \quad \text{Global Equity Fund} = 64.0\%$$
- **Probe Results:**
  - `Weights sum to 100`: `100.0 pass`
  - `Long-only (lowest weight)`: `-2.0 FAIL`
  - `Reserve ≥ 3.0%`: `10.0 pass` (T-bills 2.0% + T-notes 10.0% − Cash 2.0% = 10.0% $\ge$ 3.0%)
  - `Redeemable in 5 days ≥ 90%`: `100.0 pass`
  - `Largest single company ≤ 8%`: `0.0 pass`
  - `Verdict`: `fails 1 rule(s)`
- **Conclusion:** The long-only rule caught the violation cleanly without triggering false positives on any other checkable rule. Weights were restored to baseline.

---

## E — The Attack: Attacking the Checker (Candidate D)

### 1. Candidate D Specification
Using only the holdings in the master table, Candidate D is defined as:
- **Cash:** 3.0%
- **Treasury bills:** 0.0%
- **Treasury 10-year note:** 0.0%
- **Global equity index fund:** 97.0%
- **Investment-grade bond fund:** 0.0%
- **Private real estate fund:** 0.0%
- **Acme Corp bonds:** 0.0%
- **Acme Corp stock:** 0.0%

### 2. Mandate Checker Verification
Running `mandate.py` confirms that Candidate D **passes every checkable rule**:
- Weights sum: $3.0\% + 97.0\% = 100.0\%$ (`pass`)
- Lowest weight: $0.0\%$ (`pass`)
- Reserve-eligible: $3.0\% \ge 3.0\%$ (`pass`)
- 5-day liquid share: $100.0\% \ge 90.0\%$ (`pass`)
- Largest single company: $0.0\% \le 8.0\%$ (`pass`)
- Verdict: **`passes every checkable rule`**

### 3. Sceptical Partner Dialogue & Judgment
- **My Judgment of Candidate D:**  
  *The objection firmly holds because allocating 97% of a foundation reserve to equities exposes the portfolio to catastrophic cyclical drawdowns, completely violating the capital preservation mandate. **Statement S4** (Benchmark: 60% equities / 40% bonds) and **Statement S9** (Calendar-year loss $\le 10\%$) decide this rejection, as a 97% equity portfolio runs untenable tracking error and routinely suffers 20%–40% equity market drawdowns.*

- **Partner Swap (Critique Against Sceptical Colleague's Candidate D):**
  - *Colleague's Candidate D:* An all-fixed-income/cash portfolio (Cash 3.0%, T-Bills 47.0%, T-10yr 10.0%, IG Bonds 40.0%, Equities 0.0%). It passes every checkable rule in `mandate.py`.
  - *My Objection:* **Statement S2** (*Objective: CPI + 4% a year net of costs over rolling five-year periods*) decisively rejects my colleague's portfolio. With 0% allocated to equities, an ultra-safe fixed income portfolio yielding 3.5%–4.5% nominal cannot mathematically clear inflation plus a 400 bps net real hurdle over rolling five-year periods.

---

## The One Question for the CIO

> **"What is the exact mathematical objective function for the optimizer—are we minimizing tracking error relative to the 60/40 benchmark (S4), maximizing expected Sharpe ratio subject to the CPI + 4% hurdle (S2), or minimizing downside shortfall probability below a 10% annual loss (S9)?"**

### The Answer That Changes the Portfolio
- **If the CIO answers "Minimize tracking error to the 60/40 benchmark":**  
  The optimizer will construct a portfolio anchored tightly to 60% Global Equity and 40% Investment-Grade Bonds/Treasuries, accepting whatever tail volatility equity markets deliver in order to eliminate active risk against the board-approved benchmark.
- **If the CIO answers "Minimize the probability of a calendar-year loss exceeding 10%":**  
  The optimizer will dramatically slash equities (down to 25%–35%), heavily overweight short-duration Treasuries and cash, and intentionally absorb high tracking error against S4 in order to build an ironclad capital preservation floor.

---

## Investment Policy Statement (IPS) — Learn On Your Own

### 1. What is an Investment Policy Statement (IPS)?
An **Investment Policy Statement** is the foundational governance contract between an asset owner (e.g., foundation board, endowment, pension trustee) and the investment manager. It defines the client's financial purpose, governs risk tolerance, sets performance benchmarks, and circumscribes allowable investment behaviors before a single dollar is deployed.

### 2. How Does an IPS Work?
An IPS operates through a two-part framework:
1. **Objectives:** What the portfolio must accomplish.
   - *Return Objective:* Real return requirements, hurdle rates, and spending support.
   - *Risk Tolerance:* Willingness and ability to bear losses, volatility limits, and maximum drawdown constraints.
2. **Constraints:** The operational boundaries the manager must respect.
   - *Time Horizon:* Investment duration and lifecycle.
   - *Liquidity Requirements:* Cash distributions and reserve requirements.
   - *Tax Considerations:* Tax status (exempt for foundations vs. taxable).
   - *Legal & Regulatory:* Fiduciary standards (e.g., UPMIFA, ERISA) and borrowing restrictions.
   - *Unique Circumstances:* ESG screens, concentration caps, and asset class exclusions.

### 3. Mapping S1–S10 into the Standard IPS Framework

```
                       ┌────────────────────────────────────────┐
                       │     INVESTMENT POLICY STATEMENT (IPS)  │
                       └───────────────────┬────────────────────┘
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
┌─────────────────────────────────┐                         ┌─────────────────────────────────┐
│           OBJECTIVES            │                         │           CONSTRAINTS           │
├─────────────────────────────────┤                         ├─────────────────────────────────┤
│ Return:                         │                         │ Time Horizon:                   │
│ • S2: CPI + 4% net over 5 yrs   │                         │ • S1: 7-Year Horizon; Rebalance │
│                                 │                         │                                 │
│ Risk:                           │                         │ Liquidity:                      │
│ • S9: Max 10% loss (Promise)    │                         │ • S3: $0.75M/qtr (12-mo reserve)│
│                                 │                         │ • S8: >=90% redeemable in 5 days│
│ Benchmark:                      │                         │                                 │
│ • S4: 60/40 Policy Preference   │                         │ Legal & Regulatory:             │
│                                 │                         │ • S5: Long-only, no derivatives │
│ Missing:                        │                         │                                 │
│ • S10: Missing Optimizer Target │                         │ Unique Circumstances:           │
│                                 │                         │ • S6: 8% Issuer Cap             │
│                                 │                         │ • S7: 25% Turnover Limit        │
└─────────────────────────────────┘                         └─────────────────────────────────┘
```

---

## Reflection

### 1. Why a Portfolio Can Pass Every Checkable Rule and Still Be Wrong for This Client
Compliance checkers test **necessary conditions**, not **sufficient conditions**. A computer script checking static arithmetic constraints (e.g. non-negative weights, liquidity percentages, and issuer caps) cannot evaluate:
- **Suitability and Risk Balance:** Candidate D passed 100% of the checkable rules while holding 97% equities, which completely violates the client's risk profile and downside sensitivity.
- **Goal Attainability:** An all-cash/Treasury portfolio also passes all checkable constraints, but guarantees the destruction of the foundation's real purchasing power by failing the S2 return objective.
Passing mandate checks merely proves a portfolio is *legally permissible*; it does not prove it is *fiduciary sound*.

### 2. The S1–S10 Type I Was Least Sure Of
I was least sure of **Statement S4** (*"Benchmark: 60% global equities, 40% U.S. investment-grade bonds"*).  
While intuitive to read as a hard constraint (mandating exactly 60% equities and 40% bonds), in institutional asset management, a benchmark is formally a **Preference (Policy Reference)**. Unless the mandate specifies a hard tracking error band (e.g., active share $\le 10\%$), the manager has tactical discretion to deviate from 60/40 to harvest alpha or protect capital. Treating it as a strict mathematical constraint would render dynamic optimization meaningless.

---

## Project 2 Mandate: Horizon Endowment Fund

In preparation for Project 2 (starting Week 9), here is the formal client mandate draft:

### 1. Client Profile
- **Entity:** Horizon University Endowment Fund (\$250M AUM)
- **Time Horizon:** Perpetual (intergenerational equity)

### 2. Return Objective
- **Target:** Maintain intergenerational purchasing power after inflation and university distributions:  
  $$\text{Target Return} = \text{HEPI (Higher Education Price Index)} + 5.0\% \text{ net of all management fees}$$

### 3. Hard Constraints
1. **Spending Policy & Liquidity:** Distribute 4.5% of trailing 12-quarter average endowment value annually; hold at least 18 months of projected capital calls and operating distributions in daily-liquid cash and sovereign paper.
2. **Leverage & Shorting:** Long-only portfolio; no structural leverage or speculative derivative positions; currency hedging permitted up to 100% of foreign exposure.
3. **Issuer & Illiquidity Caps:** Maximum 5% exposure to any single non-government corporate issuer; maximum 20% exposure to illiquid alternative investments (private equity, venture capital, and unlisted infrastructure with lockups $>1$ year).
4. **Turnover & Volatility:** Maximum annual portfolio turnover of 20%; annualized portfolio volatility capped at 12.0%.

### 4. The One Question for the Client
> **"Does the University Board prioritize stabilizing annual operating budget payouts through smoothed spending rules, or does it prioritize preserving the inflation-adjusted terminal capital value of the endowment principal during extended stagflationary regimes?"**
