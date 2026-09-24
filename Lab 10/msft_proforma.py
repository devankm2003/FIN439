"""Five-Year Pro-Forma Integrated Financial Statement Model and Valuation Engine.

Lab 10 — Thursday Merit Checkout: Microsoft Corporation (NASDAQ: MSFT) Case.
Built on the verified Lab 09 3-statement engine using FY2025 Form 10-K opening
balances and defended operating/financing judgments.
Computes Income Statement, Balance Sheet, Cash Flow (FCFE), Balance Checks,
and Equity DCF Valuation using standard library Python only.
"""

from typing import Dict, List, Tuple


# ==============================================================================
# ASSUMPTION SET — MICROSOFT CORPORATION (NASDAQ: MSFT, FY2025 Form 10-K Base)
# ==============================================================================

# Opening Balance Sheet & Base Year FY2025 (Ended June 30, 2025, USD Millions)
# Sourced from Microsoft FY2025 Form 10-K, Item 8 (Consolidated Financial Statements)
OPENING_REVENUE = 281724.0          # FY2025 Revenue (Item 8, p. 59)
OPENING_INVENTORY = 938.0           # FY2025 Inventories (Item 8, p. 61)
OPENING_PPE = 204966.0              # FY2025 Property and equipment, net (Item 8, p. 61)
OPENING_OTHER_ASSETS = 318534.0     # FY2025 Other assets (Total Assets 619,003 - Cash/STI 94,565 - Inv 938 - PP&E 204,966)
OPENING_CASH = 94565.0              # FY2025 Cash & cash equivalents (30,242) + Short-term investments (64,323) (Item 8, p. 61)

# Company-Specific Working Capital Liability Line (replaces ABG's Floor Plan Notes Payable):
# Microsoft has NO floor plan debt ("none"). Instead, its signature operating liability is
# Short-Term Unearned Revenue (upfront customer billings for Azure & M365 cloud subscriptions).
OPENING_UNEARNED_REV = 64555.0      # FY2025 Short-term unearned revenue (Item 8, p. 61)
OPENING_TERM_DEBT = 43151.0         # FY2025 Current portion of LT debt (2,999) + Long-term debt (40,152) (Item 8, p. 61)
OPENING_OTHER_LIABILITIES = 167818.0  # FY2025 Other liabilities (Total Liab 275,524 - Unearned Rev 64,555 - Debt 43,151)
OPENING_EQUITY = 343479.0           # FY2025 Total stockholders' equity (Item 8, p. 61)
OPENING_REVOLVER = 0.0              # FY2025 Short-term revolving credit facility drawn ($0.0M)

# Forecast Period (Fiscal Years Ending June 30, 2026E–2030E)
YEARS = [2026, 2027, 2028, 2029, 2030]

# Operating Judgments & Historical Ratios
ORGANIC_REVENUE_GROWTH = 0.130      # 13.0% a year organic cloud & AI software growth (judgment)
GROSS_MARGIN = 0.6850               # 68.50% blended gross margin, reflecting AI infrastructure scale (judgment)
# Cash OpEx (R&D + S&M + G&A ex-PP&E Depreciation) ÷ Gross Profit:
# FY25 GAAP OpEx ($65,365M) minus Note 7 PP&E Depreciation ($22,000M) = $43,365M (22.37% of GP)
SGA_RATIOS = [0.225, 0.220, 0.215, 0.210, 0.210]  # Operating leverage tapering from 22.5% to 21.0% of GP (judgment)
DEPRECIATION_RATIO = 22000.0 / 204966.0  # FY2025 Note 7 PP&E depreciation ($22,000M) ÷ ending PP&E ($204,966M) (~10.7335%, history)
IMPAIRMENT = 0.0                    # $0.0M non-cash goodwill/intangible impairment (history: zero in FY23-FY25)
CAPEX = 65000.0                     # $65,000.0M a year cash additions to PP&E for AI datacenters/GPUs (guidance)
TAX_RATE = 0.180                    # 18.0% effective corporate tax rate (judgment: 3-yr avg 18.28%)

# Working Capital & Financing History / Judgments
# Inventory days = 938.0 / (281,724.0 - 193,893.0) * 365 = 3.8982 days
INVENTORY_DAYS = (938.0 / 87831.0) * 365.0  # FY2025 inventory ÷ cost of revenue × 365 (history)
UNEARNED_REV_RATIO = 64555.0 / 281724.0     # FY2025 short-term unearned revenue ÷ revenue (~22.9143%, history)
OWC_RATE = 0.040                    # Other working capital = 4.0% of change in revenue (judgment)

MINIMUM_CASH = 15000.0              # $15,000.0M minimum operating cash floor (judgment)
REVOLVER_LIMIT = 10000.0            # $10,000.0M backup credit facility capacity (judgment)
REVOLVER_RATE = 0.050               # 5.0% commercial paper / revolver borrowing rate (judgment)

DEBT_REPAYMENT = 3000.0             # $3,000.0M a year scheduled senior debt maturities repaid (judgment; FY25 was $3,216M)
SHARE_BUYBACK = 42502.0             # $42,502.0M a year total equity cash distributions: FY25 buybacks ($18,420M) + dividends ($24,082M) (history/judgment)

UNEARNED_REV_RATE = 0.0000          # 0.00% interest on unearned revenue (non-interest-bearing customer float, history)
TERM_DEBT_RATE = 2385.0 / 43151.0   # ~5.5271% effective interest rate on total debt (FY25 interest $2,385M ÷ $43,151M debt, history)

# Valuation Judgments & Fact
COST_OF_EQUITY = 0.095              # 9.50% CAPM cost of equity: Rf 4.10% + Beta 1.08 × ERP 5.00% (judgment)
TERMINAL_GROWTH = 0.030             # 3.00% perpetual nominal GDP growth anchor (judgment)
SHARES_OUTSTANDING = 7465.0         # 7,465.0 million diluted weighted-average shares (fact: FY2025 Form 10-K, Item 8, p. 59)
CURRENT_MARKET_PRICE = 500.59       # MSFT market close on September 23, 2026 ($)


def run_proforma(break_test_2026_cash: bool = False) -> Tuple[Dict[str, List[float]], Dict[str, float]]:
    """Project 5-year financial statements and equity valuation for Microsoft (MSFT).

    If break_test_2026_cash is True, forces FY2026E cash to opening cash (94,565.0)
    to verify the balance-check assertion failure.
    """
    prior_rev = OPENING_REVENUE
    prior_inv = OPENING_INVENTORY
    prior_ppe = OPENING_PPE
    prior_oa = OPENING_OTHER_ASSETS
    prior_cash = OPENING_CASH
    prior_ur = OPENING_UNEARNED_REV
    prior_debt = OPENING_TERM_DEBT
    prior_ol = OPENING_OTHER_LIABILITIES
    prior_eq = OPENING_EQUITY
    prior_revolver = OPENING_REVOLVER

    rows: Dict[str, List[float]] = {
        "revenue": [],
        "cgs": [],
        "gross_profit": [],
        "sga": [],
        "depreciation": [],
        "impairment": [],
        "operating_income": [],
        "interest_unearned_rev": [],
        "interest_term_debt": [],
        "interest_revolver": [],
        "total_interest": [],
        "pretax_income": [],
        "income_tax": [],
        "net_income": [],
        "inventory": [],
        "unearned_rev": [],
        "ppe": [],
        "other_assets": [],
        "term_debt": [],
        "revolver": [],
        "other_liabilities": [],
        "equity": [],
        "fcfe": [],
        "cash": [],
        "total_assets": [],
        "total_liabilities": [],
        "total_liab_equity": [],
        "check_gap": [],
        "check_min_cash": [],
    }

    for i, year in enumerate(YEARS):
        # 1. Income Statement Order
        rev = prior_rev * (1.0 + ORGANIC_REVENUE_GROWTH)
        gp = rev * GROSS_MARGIN
        cgs = rev - gp
        sga = gp * SGA_RATIOS[i]
        depr = prior_ppe * DEPRECIATION_RATIO
        imp = IMPAIRMENT
        ebit = gp - sga - depr - imp

        int_ur = prior_ur * UNEARNED_REV_RATE
        int_debt = prior_debt * TERM_DEBT_RATE
        int_rev = prior_revolver * REVOLVER_RATE
        total_interest = int_ur + int_debt + int_rev

        pretax = ebit - total_interest
        tax = max(0.0, pretax) * TAX_RATE
        ni = pretax - tax

        # 2. Balance Sheet Except Cash
        inv = cgs * INVENTORY_DAYS / 365.0
        ur = rev * UNEARNED_REV_RATIO
        ppe = prior_ppe + CAPEX - depr
        chg_rev = rev - prior_rev
        oa = prior_oa + (OWC_RATE * chg_rev) - imp
        debt = prior_debt - DEBT_REPAYMENT
        ol = prior_ol  # Other liabilities held flat
        eq = prior_eq + ni - SHARE_BUYBACK

        # 3. Free Cash Flow to Equity (FCFE)
        chg_inv = inv - prior_inv
        chg_owc = OWC_RATE * chg_rev
        chg_ur = ur - prior_ur
        fcfe = (
            ni
            + depr
            + imp
            - CAPEX
            - chg_inv
            - chg_owc
            + chg_ur
            - DEBT_REPAYMENT
        )

        # 4. Cash and Revolver Mechanics
        cash_pre_revolver = prior_cash + fcfe - SHARE_BUYBACK
        revolver = prior_revolver

        if cash_pre_revolver < MINIMUM_CASH:
            draw = MINIMUM_CASH - cash_pre_revolver
            revolver += draw
            cash = MINIMUM_CASH
        else:
            surplus = cash_pre_revolver - MINIMUM_CASH
            if revolver > 0.0:
                repay = min(surplus, revolver)
                revolver -= repay
                cash = cash_pre_revolver - repay
            else:
                cash = cash_pre_revolver

        # In break-test mode: override 2026 cash to opening 94,565.0
        if break_test_2026_cash and year == 2026:
            cash = OPENING_CASH

        # 5. Checks
        total_assets = cash + inv + ppe + oa
        total_liabilities = ur + debt + revolver + ol
        total_liab_equity = total_liabilities + eq
        gap = total_assets - total_liabilities - eq

        # Store to row dictionaries
        rows["revenue"].append(rev)
        rows["cgs"].append(cgs)
        rows["gross_profit"].append(gp)
        rows["sga"].append(sga)
        rows["depreciation"].append(depr)
        rows["impairment"].append(imp)
        rows["operating_income"].append(ebit)
        rows["interest_unearned_rev"].append(int_ur)
        rows["interest_term_debt"].append(int_debt)
        rows["interest_revolver"].append(int_rev)
        rows["total_interest"].append(total_interest)
        rows["pretax_income"].append(pretax)
        rows["income_tax"].append(tax)
        rows["net_income"].append(ni)

        rows["inventory"].append(inv)
        rows["unearned_rev"].append(ur)
        rows["ppe"].append(ppe)
        rows["other_assets"].append(oa)
        rows["term_debt"].append(debt)
        rows["revolver"].append(revolver)
        rows["other_liabilities"].append(ol)
        rows["equity"].append(eq)

        rows["fcfe"].append(fcfe)
        rows["cash"].append(cash)
        rows["total_assets"].append(total_assets)
        rows["total_liabilities"].append(total_liabilities)
        rows["total_liab_equity"].append(total_liab_equity)
        rows["check_gap"].append(gap)
        rows["check_min_cash"].append(1.0 if cash >= MINIMUM_CASH else 0.0)

        # Advance state to next year
        prior_rev = rev
        prior_inv = inv
        prior_ppe = ppe
        prior_oa = oa
        prior_cash = cash
        prior_ur = ur
        prior_debt = debt
        prior_ol = ol
        prior_eq = eq
        prior_revolver = revolver

    # 6. Assert Balanced Before Valuation
    assert_balanced(rows["check_gap"], rows["check_min_cash"], YEARS)

    # 7. Valuation (Only positive FCFE valued; all 5 years are positive)
    pv_explicit_fcfe = sum(
        cf / ((1.0 + COST_OF_EQUITY) ** t)
        for t, cf in enumerate(rows["fcfe"], start=1)
        if cf > 0.0
    )
    fcfe_2030 = rows["fcfe"][-1]
    terminal_value = (
        (fcfe_2030 + DEBT_REPAYMENT)
        * (1.0 + TERMINAL_GROWTH)
        / (COST_OF_EQUITY - TERMINAL_GROWTH)
    )
    pv_terminal_value = terminal_value / ((1.0 + COST_OF_EQUITY) ** 5)
    equity_value = pv_explicit_fcfe + pv_terminal_value
    value_per_share = equity_value / SHARES_OUTSTANDING
    share_of_val_after_2030 = pv_terminal_value / equity_value

    val_summary = {
        "pv_explicit_fcfe": pv_explicit_fcfe,
        "terminal_value": terminal_value,
        "pv_terminal_value": pv_terminal_value,
        "equity_value": equity_value,
        "share_of_val_after_2030": share_of_val_after_2030,
        "value_per_share": value_per_share,
    }

    return rows, val_summary


def assert_balanced(check_gaps: List[float], check_min_cashes: List[float], years: List[int]) -> None:
    """Raise an error naming the year and the gap if any balance or cash check fails."""
    for gap, min_cash_ok, year in zip(check_gaps, check_min_cashes, years):
        if abs(gap) > 0.01:
            raise AssertionError(
                f"Balance sheet check failed in FY{year}E: gap of {gap:.1f}"
            )
        if min_cash_ok < 0.5:
            raise AssertionError(
                f"Minimum cash check failed in FY{year}E: cash below {MINIMUM_CASH:.1f}"
            )


def print_proforma_tables(rows: Dict[str, List[float]], val_summary: Dict[str, float]) -> None:
    """Format and print the three statements, check block, and valuation summary."""
    headers = [f"FY{y}E" for y in YEARS]
    col_w = 12
    label_w = 36
    total_w = label_w + len(YEARS) * col_w
    sep = "=" * total_w
    sub_sep = "-" * total_w

    def print_line(label: str, values: List[float], decimals: int = 1) -> None:
        val_strs = "".join(f"{v:>{col_w}.{decimals}f}" for v in values)
        print(f"{label:<{label_w}}{val_strs}")

    def print_header(title: str) -> None:
        print("\n" + sep)
        print(title)
        print(sep)
        header_str = "".join(f"{h:>{col_w}}" for h in headers)
        print(f"{'Line (USD Millions)':<{label_w}}{header_str}")
        print(sub_sep)

    # 1. Income Statement
    print_header("1. PRO-FORMA INCOME STATEMENT (Microsoft Corporation — MSFT)")
    print_line("Revenue", rows["revenue"])
    print_line("Cost of revenue", rows["cgs"])
    print_line("Gross profit", rows["gross_profit"])
    print_line("Cash OpEx (R&D + S&M + G&A ex-Depr)", rows["sga"])
    print_line("Depreciation (PP&E)", rows["depreciation"])
    print_line("Impairment (non-cash)", rows["impairment"])
    print_line("Operating income (EBIT)", rows["operating_income"])
    print(sub_sep)
    print_line("Unearned revenue interest (0%)", rows["interest_unearned_rev"])
    print_line("Term debt interest", rows["interest_term_debt"])
    print_line("Revolver interest", rows["interest_revolver"])
    print_line("Total interest expense", rows["total_interest"])
    print(sub_sep)
    print_line("Pre-tax income", rows["pretax_income"])
    print_line("Income tax expense", rows["income_tax"])
    print_line("Net income", rows["net_income"])

    # 2. Balance Sheet
    print_header("2. PRO-FORMA BALANCE SHEET (Microsoft Corporation — MSFT)")
    print("ASSETS:")
    print_line("  Cash & short-term investments", rows["cash"])
    print_line("  Inventories", rows["inventory"])
    print_line("  Property and equipment, net", rows["ppe"])
    print_line("  Other assets", rows["other_assets"])
    print(sub_sep)
    print_line("Total Assets", rows["total_assets"])
    print(sub_sep)
    print("LIABILITIES & EQUITY:")
    print_line("  Short-term unearned revenue", rows["unearned_rev"])
    print_line("  Term debt (current + long-term)", rows["term_debt"])
    print_line("  Revolving credit facility", rows["revolver"])
    print_line("  Other liabilities", rows["other_liabilities"])
    print(sub_sep)
    print_line("Total Liabilities", rows["total_liabilities"])
    print_line("Stockholders' Equity", rows["equity"])
    print(sub_sep)
    print_line("Total Liabilities & Equity", rows["total_liab_equity"])

    # 3. Cash Flow / FCFE Statement
    print_header("3. CASH FLOW STATEMENT & FREE CASH FLOW TO EQUITY (FCFE)")
    print_line("Net income", rows["net_income"])
    print_line("(+) Depreciation", rows["depreciation"])
    print_line("(+) Impairment (non-cash)", rows["impairment"])
    print_line("(-) Capital spending (CapEx)", [-CAPEX] * len(YEARS))
    print_line(
        "(-) Change in inventory",
        [-(rows["inventory"][i] - (OPENING_INVENTORY if i == 0 else rows["inventory"][i - 1])) for i in range(len(YEARS))],
    )
    print_line(
        "(-) Change in other working capital",
        [-(OWC_RATE * (rows["revenue"][i] - (OPENING_REVENUE if i == 0 else rows["revenue"][i - 1]))) for i in range(len(YEARS))],
    )
    print_line(
        "(+) Change in unearned revenue",
        [(rows["unearned_rev"][i] - (OPENING_UNEARNED_REV if i == 0 else rows["unearned_rev"][i - 1])) for i in range(len(YEARS))],
    )
    print_line("(-) Term debt repayment", [-DEBT_REPAYMENT] * len(YEARS))
    print(sub_sep)
    print_line("Free Cash Flow to Equity (FCFE)", rows["fcfe"])
    print_line("(-) Share buybacks & dividends", [-SHARE_BUYBACK] * len(YEARS))
    print_line("Cash, year end", rows["cash"])

    # 4. Check Block
    print_header("4. BALANCE & CASH CHECKS")
    print_line("Assets − Liabilities − Equity", rows["check_gap"])
    print_line("Cash at or above minimum ($15,000M)", rows["check_min_cash"], decimals=0)
    print(sub_sep)
    print("Check status: BALANCED (all checks passed, gap = 0.0 in every year)")

    # 5. Valuation Block
    print("\n" + sep)
    print("5. EQUITY DCF VALUATION SUMMARY (Microsoft Corporation — NASDAQ: MSFT)")
    print(sep)
    print(f"PV of explicit 5-year FCFE (2026–2030):   ${val_summary['pv_explicit_fcfe']:>14,.2f} million")
    print(f"Terminal value at 2030:                  ${val_summary['terminal_value']:>14,.2f} million")
    print(f"PV of terminal value (discounted 5 yrs):  ${val_summary['pv_terminal_value']:>14,.2f} million")
    print(sub_sep)
    print(f"Total Equity Value:                      ${val_summary['equity_value']:>14,.2f} million")
    print(f"Share of value after 2030 (TV / Equity):  {val_summary['share_of_val_after_2030']:>15.2%}")
    print(f"Diluted shares outstanding:               {SHARES_OUTSTANDING:>15,.2f} million")
    print(sub_sep)
    print(f"Model Value per share:                   ${val_summary['value_per_share']:>14.2f}")
    print(f"Current Market Price (Sept 23, 2026):    ${CURRENT_MARKET_PRICE:>14.2f}")
    print(sep)


def main() -> None:
    """Run MSFT pro-forma model, verify balance assertions, and print statements and valuation."""
    rows, val_summary = run_proforma(break_test_2026_cash=False)
    print_proforma_tables(rows, val_summary)


if __name__ == "__main__":
    main()
