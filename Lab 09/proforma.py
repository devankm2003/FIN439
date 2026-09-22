"""Five-Year Pro-Forma Integrated Financial Statement Model and Valuation Engine.

Lab 09 — Pro-Forma Build: Asbury Automotive Group (ABG) Case.
Computes Income Statement, Balance Sheet, Cash Flow (FCFE), Balance Checks,
and Equity DCF Valuation using standard library Python only.
"""

from typing import Dict, List, Tuple


# ==============================================================================
# ASSUMPTION SET (ABG Case from Lab 09)
# ==============================================================================

# Opening Balance Sheet & Base Year FY2025 (USD Millions)
OPENING_REVENUE = 17999.0
OPENING_INVENTORY = 2135.8
OPENING_PPE = 3070.4
OPENING_OTHER_ASSETS = 6371.6
OPENING_CASH = 40.4
OPENING_FLOOR_PLAN = 2027.0
OPENING_TERM_DEBT = 3572.0
OPENING_OTHER_LIABILITIES = 2127.5
OPENING_EQUITY = 3891.7
OPENING_REVOLVER = 0.0

# Forecast Period
YEARS = [2026, 2027, 2028, 2029, 2030]

# Operating Judgments & Ratios
ORGANIC_REVENUE_GROWTH = 0.018  # 1.8% a year (judgment)
GROSS_MARGIN = 0.1705           # 17.05% (judgment)
SGA_RATIOS = [0.665, 0.655, 0.645, 0.645, 0.645]  # SG&A % of gross profit 2026-2030 (judgment)
DEPRECIATION_RATIO = 82.4 / 3070.4  # FY2025 depreciation / year-end PP&E (history)
IMPAIRMENT = 120.0              # 120 a year non-cash (judgment)
CAPEX = 250.0                   # 250 a year capital spending (guidance)
TAX_RATE = 0.255                # 25.5% (judgment)

# Working Capital & Financing History / Judgments
# Inventory days = 2,135.8 / (17,999.0 - 3,071.7) * 365
INVENTORY_DAYS = (2135.8 / (17999.0 - 3071.7)) * 365.0
FLOOR_PLAN_RATIO = 2027.0 / 2135.8  # Floor plan loans / inventory (history)
OWC_RATE = 0.008                    # Other working capital = 0.8% of change in revenue (judgment)

MINIMUM_CASH = 25.0             # 25 USD million (history)
REVOLVER_LIMIT = 850.0          # 850 USD million (judgment)
REVOLVER_RATE = 0.06            # 6.0% (judgment)

DEBT_REPAYMENT = 150.0          # 150 a year (judgment)
SHARE_BUYBACK = 150.0           # 150 a year (judgment)

FLOOR_PLAN_RATE = 0.0467        # 4.67% interest rate (history)
TERM_DEBT_RATE = 0.0544         # 5.44% interest rate (history)

# Valuation Judgments & Fact
COST_OF_EQUITY = 0.10           # 10.0% (judgment)
TERMINAL_GROWTH = 0.025         # 2.5% (judgment)
SHARES_OUTSTANDING = 17.951349  # 17.951349 million shares (fact: 10-Q, 30 June 2026)


def run_proforma(break_test_2026_cash: bool = False) -> Tuple[Dict[str, List[float]], Dict[str, float]]:
    """Project 5-year financial statements and equity valuation.

    If break_test_2026_cash is True, sets 2026 cash to opening 40.4 to verify
    the balance-check assertion failure.
    """
    prior_rev = OPENING_REVENUE
    prior_inv = OPENING_INVENTORY
    prior_ppe = OPENING_PPE
    prior_oa = OPENING_OTHER_ASSETS
    prior_cash = OPENING_CASH
    prior_fp = OPENING_FLOOR_PLAN
    prior_debt = OPENING_TERM_DEBT
    prior_ol = OPENING_OTHER_LIABILITIES
    prior_eq = OPENING_EQUITY
    prior_revolver = OPENING_REVOLVER

    # Containers for projection rows
    rows: Dict[str, List[float]] = {
        "revenue": [],
        "cgs": [],
        "gross_profit": [],
        "sga": [],
        "depreciation": [],
        "impairment": [],
        "operating_income": [],
        "interest_floor_plan": [],
        "interest_term_debt": [],
        "interest_revolver": [],
        "total_interest": [],
        "pretax_income": [],
        "income_tax": [],
        "net_income": [],
        "inventory": [],
        "floor_plan": [],
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

        int_fp = prior_fp * FLOOR_PLAN_RATE
        int_debt = prior_debt * TERM_DEBT_RATE
        int_rev = prior_revolver * REVOLVER_RATE
        total_interest = int_fp + int_debt + int_rev

        pretax = ebit - total_interest
        tax = max(0.0, pretax) * TAX_RATE
        ni = pretax - tax

        # 2. Balance Sheet Except Cash
        inv = cgs * INVENTORY_DAYS / 365.0
        fp = inv * FLOOR_PLAN_RATIO
        ppe = prior_ppe + CAPEX - depr
        chg_rev = rev - prior_rev
        oa = prior_oa + (OWC_RATE * chg_rev) - imp
        debt = prior_debt - DEBT_REPAYMENT
        ol = prior_ol  # other liabilities flat
        eq = prior_eq + ni - SHARE_BUYBACK

        # 3. Free Cash Flow to Equity (FCFE)
        chg_inv = inv - prior_inv
        chg_owc = OWC_RATE * chg_rev
        chg_fp = fp - prior_fp
        fcfe = (
            ni
            + depr
            + imp
            - CAPEX
            - chg_inv
            - chg_owc
            + chg_fp
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

        # In break-test mode: override 2026 cash to opening 40.4
        if break_test_2026_cash and year == 2026:
            cash = OPENING_CASH

        # 5. Checks
        total_assets = cash + inv + ppe + oa
        total_liabilities = fp + debt + revolver + ol
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
        rows["interest_floor_plan"].append(int_fp)
        rows["interest_term_debt"].append(int_debt)
        rows["interest_revolver"].append(int_rev)
        rows["total_interest"].append(total_interest)
        rows["pretax_income"].append(pretax)
        rows["income_tax"].append(tax)
        rows["net_income"].append(ni)

        rows["inventory"].append(inv)
        rows["floor_plan"].append(fp)
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
        prior_fp = fp
        prior_debt = debt
        prior_ol = ol
        prior_eq = eq
        prior_revolver = revolver

    # 6. Assert Balanced Before Valuation
    assert_balanced(rows["check_gap"], rows["check_min_cash"], YEARS)

    # 7. Valuation
    pv_explicit_fcfe = sum(
        cf / ((1.0 + COST_OF_EQUITY) ** t)
        for t, cf in enumerate(rows["fcfe"], start=1)
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
    label_w = 34
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
    print_header("1. PRO-FORMA INCOME STATEMENT")
    print_line("Revenue", rows["revenue"])
    print_line("Cost of sales", rows["cgs"])
    print_line("Gross profit", rows["gross_profit"])
    print_line("SG&A expenses", rows["sga"])
    print_line("Depreciation", rows["depreciation"])
    print_line("Impairment (non-cash)", rows["impairment"])
    print_line("Operating income (EBIT)", rows["operating_income"])
    print(sub_sep)
    print_line("Floor plan interest", rows["interest_floor_plan"])
    print_line("Term debt interest", rows["interest_term_debt"])
    print_line("Revolver interest", rows["interest_revolver"])
    print_line("Total interest expense", rows["total_interest"])
    print(sub_sep)
    print_line("Pre-tax income", rows["pretax_income"])
    print_line("Income tax expense", rows["income_tax"])
    print_line("Net income", rows["net_income"])

    # 2. Balance Sheet
    print_header("2. PRO-FORMA BALANCE SHEET")
    print("ASSETS:")
    print_line("  Cash & cash equivalents", rows["cash"])
    print_line("  Inventories", rows["inventory"])
    print_line("  Property, plant & equipment", rows["ppe"])
    print_line("  Other assets", rows["other_assets"])
    print(sub_sep)
    print_line("Total Assets", rows["total_assets"])
    print(sub_sep)
    print("LIABILITIES & EQUITY:")
    print_line("  Floor plan notes payable", rows["floor_plan"])
    print_line("  Term debt", rows["term_debt"])
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
    print_line("(-) Change in inventory", [-(rows["inventory"][i] - (OPENING_INVENTORY if i == 0 else rows["inventory"][i - 1])) for i in range(len(YEARS))])
    print_line("(-) Change in other working capital", [-(OWC_RATE * (rows["revenue"][i] - (OPENING_REVENUE if i == 0 else rows["revenue"][i - 1]))) for i in range(len(YEARS))])
    print_line("(+) Change in floor plan", [(rows["floor_plan"][i] - (OPENING_FLOOR_PLAN if i == 0 else rows["floor_plan"][i - 1])) for i in range(len(YEARS))])
    print_line("(-) Term debt repayment", [-DEBT_REPAYMENT] * len(YEARS))
    print(sub_sep)
    print_line("Free Cash Flow to Equity (FCFE)", rows["fcfe"])
    print_line("(-) Share buybacks", [-SHARE_BUYBACK] * len(YEARS))
    print_line("Cash, year end", rows["cash"])

    # 4. Check Block
    print_header("4. BALANCE & CASH CHECKS")
    print_line("Assets − Liabilities − Equity", rows["check_gap"])
    print_line("Cash at or above minimum ($25M)", rows["check_min_cash"], decimals=0)
    print(sub_sep)
    print("Check status: BALANCED (all checks passed, gap = 0.0)")

    # 5. Valuation Block
    print("\n" + sep)
    print("5. EQUITY DCF VALUATION SUMMARY (Asbury Automotive Group — ABG)")
    print(sep)
    print(f"PV of explicit 5-year FCFE (2026–2030):   ${val_summary['pv_explicit_fcfe']:>12,.2f} million")
    print(f"Terminal value at 2030:                  ${val_summary['terminal_value']:>12,.2f} million")
    print(f"PV of terminal value (discounted 5 yrs):  ${val_summary['pv_terminal_value']:>12,.2f} million")
    print(sub_sep)
    print(f"Total Equity Value:                      ${val_summary['equity_value']:>12,.2f} million")
    print(f"Share of value after 2030 (TV / Equity):  {val_summary['share_of_val_after_2030']:>13.2%}")
    print(f"Diluted shares outstanding:               {SHARES_OUTSTANDING:>13.6f} million")
    print(sub_sep)
    print(f"Value per share:                         ${val_summary['value_per_share']:>12.2f}")
    print(sep)


def main() -> None:
    """Run model, verify balance assertions, and print statements and valuation."""
    rows, val_summary = run_proforma(break_test_2026_cash=False)
    print_proforma_tables(rows, val_summary)


if __name__ == "__main__":
    main()

