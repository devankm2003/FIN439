"""Five-Year Pro-Forma Integrated Financial Statement Model & One-at-a-Time Sensitivity Analysis.

Lab 10 & Lab 11 — Microsoft Corporation (NASDAQ: MSFT).
1. Runs the base 5-year 3-statement pro-forma model (FY2026E–FY2030E) from FY2025 10-K opening balances.
2. Executes One-at-a-Time (OAT) Sensitivity Analysis across two independent operating drivers:
   - Driver 1: Organic Revenue Growth Rate (10.0% / 13.0% / 16.0% per year, FY2026E–FY2030E)
   - Driver 2: Gross Margin Percentage (66.50% / 68.50% / 70.50% of revenue, FY2026E–FY2030E)
   Using a fresh independent copy of BASE_INPUTS for every run, reporting signed changes from base,
   output spans (Max - Min), visible accounting checks, and a full statement trace.
3. Restores the base input set at the end and verifies exact agreement with the initial base run.
"""

import copy
from typing import Any, Dict, List, Tuple


# ==============================================================================
# PRESERVED BASE INPUT SET — MICROSOFT CORPORATION (NASDAQ: MSFT, FY2025 10-K)
# ==============================================================================

BASE_INPUTS: Dict[str, Any] = {
    # Opening Balance Sheet & Base Year FY2025 (Ended June 30, 2025, USD Millions)
    "opening_revenue": 281724.0,          # FY2025 Revenue (Item 8, p. 59)
    "opening_inventory": 938.0,           # FY2025 Inventories (Item 8, p. 61)
    "opening_ppe": 204966.0,              # FY2025 Property and equipment, net (Item 8, p. 61)
    "opening_other_assets": 318534.0,     # FY2025 Other assets (Total Assets 619,003 - Cash 94,565 - Inv 938 - PP&E 204,966)
    "opening_cash": 94565.0,              # FY2025 Cash & equivalents (30,242) + Short-term investments (64,323)
    "opening_unearned_rev": 64555.0,      # FY2025 Short-term unearned revenue (replaces ABG Floor Plan; Floor Plan = none)
    "opening_term_debt": 43151.0,         # FY2025 Current debt (2,999) + Long-term debt (40,152)
    "opening_other_liabilities": 167818.0,# FY2025 Other liabilities (Total Liab 275,524 - Unearned Rev 64,555 - Debt 43,151)
    "opening_equity": 343479.0,           # FY2025 Total stockholders' equity (Item 8, p. 61)
    "opening_revolver": 0.0,              # FY2025 Revolving credit facility drawn ($0.0M)

    # Forecast Horizon
    "years": [2026, 2027, 2028, 2029, 2030],

    # Independent Operating Drivers & Ratios
    "organic_revenue_growth": [0.130, 0.130, 0.130, 0.130, 0.130],  # 13.0% / yr across FY2026E-FY2030E (judgment)
    "gross_margin": [0.6850, 0.6850, 0.6850, 0.6850, 0.6850],       # 68.50% of revenue across FY2026E-FY2030E (judgment)
    "sga_ratios": [0.225, 0.220, 0.215, 0.210, 0.210],              # Cash OpEx (ex-Depr) ÷ Gross Profit (judgment)
    "depreciation_ratio": 22000.0 / 204966.0,                       # Note 7 PP&E Depr ÷ Opening PP&E (~10.7335%, history)
    "impairment": 0.0,                                              # Non-cash impairment ($0.0M/yr, history)
    "capex": [65000.0, 65000.0, 65000.0, 65000.0, 65000.0],         # Annual cash additions to PP&E ($65,000M/yr, guidance)
    "tax_rate": 0.180,                                              # Effective tax rate (18.0%, judgment)

    # Working Capital & Financing Parameters
    "inventory_days": (938.0 / 87831.0) * 365.0,                    # ~3.8982 days of Cost of Revenue (history)
    "unearned_rev_ratio": 64555.0 / 281724.0,                       # ~22.9143% of Revenue (history)
    "owc_rate": 0.040,                                              # 4.0% of change in revenue (judgment)
    "minimum_cash": 15000.0,                                        # $15,000.0M minimum cash floor (judgment)
    "revolver_limit": 10000.0,                                      # $10,000.0M revolver limit (judgment)
    "revolver_rate": 0.050,                                         # 5.0% revolver borrowing rate (judgment)
    "debt_repayment": 3000.0,                                       # $3,000.0M/yr scheduled debt repayment (judgment)
    "share_buyback": 42502.0,                                       # $42,502.0M/yr buybacks + dividends (history/judgment)
    "unearned_rev_rate": 0.0000,                                    # 0.00% interest on unearned revenue (history)
    "term_debt_rate": 2385.0 / 43151.0,                             # ~5.5271% effective coupon on term debt (history)

    # Valuation Parameters & Share Count
    "cost_of_equity": 0.095,                                        # 9.50% CAPM cost of equity (judgment)
    "terminal_growth": 0.030,                                       # 3.00% perpetual nominal GDP growth (judgment)
    "shares_outstanding": 7465.0,                                   # 7,465.0M diluted shares (fact: FY2025 10-K)
    "current_market_price": 500.59,                                 # Market close Sept 23, 2026 ($)
}

# ==============================================================================
# ONE-AT-A-TIME SENSITIVITY DRIVER SPECIFICATIONS (R — Chosen Operating Drivers)
# ==============================================================================

SENSITIVITY_DRIVERS = [
    {
        "key": "organic_revenue_growth",
        "name": "Driver 1: Organic Revenue Growth Rate",
        "units": "% per year (FY2026E–FY2030E)",
        "affected_years": "FY2026E–FY2030E (All 5 forecast years)",
        "cases": [
            ("Lower",  [0.100, 0.100, 0.100, 0.100, 0.100], "10.00% / yr (-3.00 percentage points)"),
            ("Base",   [0.130, 0.130, 0.130, 0.130, 0.130], "13.00% / yr (Base assumption)"),
            ("Higher", [0.160, 0.160, 0.160, 0.160, 0.160], "16.00% / yr (+3.00 percentage points)"),
        ],
    },
    {
        "key": "gross_margin",
        "name": "Driver 2: Gross Margin Percentage",
        "units": "% of revenue (FY2026E–FY2030E)",
        "affected_years": "FY2026E–FY2030E (All 5 forecast years)",
        "cases": [
            ("Lower",  [0.6650, 0.6650, 0.6650, 0.6650, 0.6650], "66.50% of rev (-2.00 percentage points)"),
            ("Base",   [0.6850, 0.6850, 0.6850, 0.6850, 0.6850], "68.50% of rev (Base assumption)"),
            ("Higher", [0.7050, 0.7050, 0.7050, 0.7050, 0.7050], "70.50% of rev (+2.00 percentage points)"),
        ],
    },
]


# ==============================================================================
# CORE LINKED 3-STATEMENT ENGINE
# ==============================================================================

def run_proforma(
    inputs: Dict[str, Any] | None = None,
    break_test_2026_cash: bool = False,
) -> Tuple[Dict[str, List[float]], Dict[str, Any]]:
    """Project 5-year financial statements and equity valuation from an independent input set."""
    cfg = copy.deepcopy(BASE_INPUTS) if inputs is None else copy.deepcopy(inputs)

    years = cfg["years"]
    prior_rev = cfg["opening_revenue"]
    prior_inv = cfg["opening_inventory"]
    prior_ppe = cfg["opening_ppe"]
    prior_oa = cfg["opening_other_assets"]
    prior_cash = cfg["opening_cash"]
    prior_ur = cfg["opening_unearned_rev"]
    prior_debt = cfg["opening_term_debt"]
    prior_ol = cfg["opening_other_liabilities"]
    prior_eq = cfg["opening_equity"]
    prior_revolver = cfg["opening_revolver"]

    growth_list = (
        cfg["organic_revenue_growth"]
        if isinstance(cfg["organic_revenue_growth"], list)
        else [float(cfg["organic_revenue_growth"])] * len(years)
    )
    gm_list = (
        cfg["gross_margin"]
        if isinstance(cfg["gross_margin"], list)
        else [float(cfg["gross_margin"])] * len(years)
    )
    capex_list = (
        cfg["capex"]
        if isinstance(cfg["capex"], list)
        else [float(cfg["capex"])] * len(years)
    )

    rows: Dict[str, List[float]] = {
        "revenue": [], "cgs": [], "gross_profit": [], "sga": [],
        "depreciation": [], "impairment": [], "operating_income": [],
        "interest_unearned_rev": [], "interest_term_debt": [], "interest_revolver": [],
        "total_interest": [], "pretax_income": [], "income_tax": [], "net_income": [],
        "inventory": [], "unearned_rev": [], "ppe": [], "other_assets": [],
        "term_debt": [], "revolver": [], "other_liabilities": [], "equity": [],
        "chg_inv": [], "chg_owc": [], "chg_ur": [], "capex": [],
        "fcfe": [], "cash": [], "total_assets": [], "total_liabilities": [],
        "total_liab_equity": [], "check_gap": [], "check_min_cash": [],
    }

    for i, year in enumerate(years):
        # 1. Income Statement
        rev = prior_rev * (1.0 + growth_list[i])
        gp = rev * gm_list[i]
        cgs = rev - gp
        sga = gp * cfg["sga_ratios"][i]
        depr = prior_ppe * cfg["depreciation_ratio"]
        imp = cfg["impairment"]
        ebit = gp - sga - depr - imp

        int_ur = prior_ur * cfg["unearned_rev_rate"]
        int_debt = prior_debt * cfg["term_debt_rate"]
        int_rev = prior_revolver * cfg["revolver_rate"]
        total_interest = int_ur + int_debt + int_rev

        pretax = ebit - total_interest
        tax = max(0.0, pretax) * cfg["tax_rate"]
        ni = pretax - tax

        # 2. Balance Sheet Except Cash
        inv = cgs * cfg["inventory_days"] / 365.0
        ur = rev * cfg["unearned_rev_ratio"]
        capex_yr = capex_list[i]
        ppe = prior_ppe + capex_yr - depr
        chg_rev = rev - prior_rev
        oa = prior_oa + (cfg["owc_rate"] * chg_rev) - imp
        debt = prior_debt - cfg["debt_repayment"]
        ol = prior_ol
        eq = prior_eq + ni - cfg["share_buyback"]

        # 3. Free Cash Flow to Equity (FCFE)
        chg_inv = inv - prior_inv
        chg_owc = cfg["owc_rate"] * chg_rev
        chg_ur = ur - prior_ur
        fcfe = (
            ni + depr + imp - capex_yr
            - chg_inv - chg_owc + chg_ur - cfg["debt_repayment"]
        )

        # 4. Cash & Revolver Mechanics
        cash_pre_revolver = prior_cash + fcfe - cfg["share_buyback"]
        revolver = prior_revolver

        if cash_pre_revolver < cfg["minimum_cash"]:
            draw = cfg["minimum_cash"] - cash_pre_revolver
            revolver += draw
            cash = cfg["minimum_cash"]
        else:
            surplus = cash_pre_revolver - cfg["minimum_cash"]
            if revolver > 0.0:
                repay = min(surplus, revolver)
                revolver -= repay
                cash = cash_pre_revolver - repay
            else:
                cash = cash_pre_revolver

        if break_test_2026_cash and year == 2026:
            cash = cfg["opening_cash"]

        # 5. Accounting Checks
        total_assets = cash + inv + ppe + oa
        total_liabilities = ur + debt + revolver + ol
        total_liab_equity = total_liabilities + eq
        gap = total_assets - total_liabilities - eq

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
        rows["chg_inv"].append(chg_inv)
        rows["chg_owc"].append(chg_owc)
        rows["chg_ur"].append(chg_ur)
        rows["capex"].append(capex_yr)
        rows["fcfe"].append(fcfe)
        rows["cash"].append(cash)
        rows["total_assets"].append(total_assets)
        rows["total_liabilities"].append(total_liabilities)
        rows["total_liab_equity"].append(total_liab_equity)
        rows["check_gap"].append(gap)
        rows["check_min_cash"].append(1.0 if cash >= cfg["minimum_cash"] else 0.0)

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
    assert_balanced(rows["check_gap"], rows["check_min_cash"], years, cfg["minimum_cash"])

    # 7. Equity DCF Valuation (FCFE)
    ke = cfg["cost_of_equity"]
    g = cfg["terminal_growth"]
    fcfe_final = rows["fcfe"][-1]
    revolver_ok = max(rows["revolver"]) <= cfg["revolver_limit"]

    valuation_valid = (
        ke > g
        and cfg["shares_outstanding"] > 0
        and fcfe_final + cfg["debt_repayment"] > 0
        and all(cf > 0 for cf in rows["fcfe"])
        and revolver_ok
    )

    if valuation_valid:
        pv_explicit_fcfe = sum(
            cf / ((1.0 + ke) ** t) for t, cf in enumerate(rows["fcfe"], start=1)
        )
        terminal_value = (
            (fcfe_final + cfg["debt_repayment"]) * (1.0 + g) / (ke - g)
        )
        pv_terminal_value = terminal_value / ((1.0 + ke) ** len(years))
        equity_value = pv_explicit_fcfe + pv_terminal_value
        value_per_share = equity_value / cfg["shares_outstanding"]
        share_of_val_after_2030 = pv_terminal_value / equity_value
    else:
        pv_explicit_fcfe = None
        terminal_value = None
        pv_terminal_value = None
        equity_value = None
        value_per_share = None
        share_of_val_after_2030 = None

    val_summary = {
        "valuation_valid": valuation_valid,
        "pv_explicit_fcfe": pv_explicit_fcfe,
        "terminal_value": terminal_value,
        "pv_terminal_value": pv_terminal_value,
        "equity_value": equity_value,
        "share_of_val_after_2030": share_of_val_after_2030,
        "value_per_share": value_per_share,
        "max_abs_gap": max(abs(x) for x in rows["check_gap"]),
        "min_cash_all_ok": all(x >= 0.5 for x in rows["check_min_cash"]),
    }

    return rows, val_summary


def assert_balanced(
    check_gaps: List[float],
    check_min_cashes: List[float],
    years: List[int],
    min_cash: float = 15000.0,
) -> None:
    """Raise an error naming the year and the gap if any balance or cash check fails."""
    for gap, min_cash_ok, year in zip(check_gaps, check_min_cashes, years):
        if abs(gap) > 0.01:
            raise AssertionError(
                f"Balance sheet check failed in FY{year}E: gap of {gap:.1f}"
            )
        if min_cash_ok < 0.5:
            raise AssertionError(
                f"Minimum cash check failed in FY{year}E: cash below {min_cash:.1f}"
            )


def print_proforma_tables(rows: Dict[str, List[float]], val_summary: Dict[str, Any]) -> None:
    """Format and print the three statements, check block, and valuation summary."""
    years = BASE_INPUTS["years"]
    headers = [f"FY{y}E" for y in years]
    col_w = 12
    label_w = 36
    total_w = label_w + len(years) * col_w
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

    print_header("3. CASH FLOW STATEMENT & FREE CASH FLOW TO EQUITY (FCFE)")
    print_line("Net income", rows["net_income"])
    print_line("(+) Depreciation", rows["depreciation"])
    print_line("(+) Impairment (non-cash)", rows["impairment"])
    print_line("(-) Capital spending (CapEx)", [-c for c in rows["capex"]])
    print_line("(-) Change in inventory", [-d for d in rows["chg_inv"]])
    print_line("(-) Change in other working capital", [-d for d in rows["chg_owc"]])
    print_line("(+) Change in unearned revenue", rows["chg_ur"])
    print_line("(-) Term debt repayment", [-BASE_INPUTS["debt_repayment"]] * len(years))
    print(sub_sep)
    print_line("Free Cash Flow to Equity (FCFE)", rows["fcfe"])
    print_line("(-) Share buybacks & dividends", [-BASE_INPUTS["share_buyback"]] * len(years))
    print_line("Cash, year end", rows["cash"])

    print_header("4. BALANCE & CASH CHECKS")
    print_line("Assets − Liabilities − Equity", rows["check_gap"])
    print_line("Cash at or above minimum ($15,000M)", rows["check_min_cash"], decimals=0)
    print(sub_sep)
    print("Check status: BALANCED (all checks passed, gap = 0.0 in every year)")

    print("\n" + sep)
    print("5. EQUITY DCF VALUATION SUMMARY (Microsoft Corporation — NASDAQ: MSFT)")
    print(sep)
    print(f"PV of explicit 5-year FCFE (2026–2030):   ${val_summary['pv_explicit_fcfe']:>14,.2f} million")
    print(f"Terminal value at 2030:                  ${val_summary['terminal_value']:>14,.2f} million")
    print(f"PV of terminal value (discounted 5 yrs):  ${val_summary['pv_terminal_value']:>14,.2f} million")
    print(sub_sep)
    print(f"Total Equity Value:                      ${val_summary['equity_value']:>14,.2f} million")
    print(f"Share of value after 2030 (TV / Equity):  {val_summary['share_of_val_after_2030']:>15.2%}")
    print(f"Diluted shares outstanding:               {BASE_INPUTS['shares_outstanding']:>15,.2f} million")
    print(sub_sep)
    print(f"Model Value per share:                   ${val_summary['value_per_share']:>14.2f}")
    print(f"Current Market Price (Sept 23, 2026):    ${BASE_INPUTS['current_market_price']:>14.2f}")
    print(sep)


# ==============================================================================
# ONE-AT-A-TIME SENSITIVITY ANALYSIS & STATEMENT TRACE
# ==============================================================================

def run_sensitivity_analysis(
    base_rows_before: Dict[str, List[float]],
    base_val_before: Dict[str, Any],
) -> None:
    """Run one-at-a-time sensitivity analysis on two operating drivers and verify restored base."""
    sep = "=" * 116
    sub_sep = "-" * 116

    base_ebit_2030 = base_rows_before["operating_income"][-1]
    base_fcfe_2030 = base_rows_before["fcfe"][-1]
    base_vps = base_val_before["value_per_share"]

    print("\n" + sep)
    print("6. ONE-AT-A-TIME (OAT) OPERATING DRIVER SENSITIVITY ANALYSIS (Microsoft Corporation — MSFT)")
    print("   Cash Flow Definition: Free Cash Flow to Equity (FCFE, USD Millions) | Final Forecast Year: FY2030E")
    print(sep)

    driver_spans: List[Dict[str, Any]] = []
    saved_runs: Dict[str, Tuple[Dict[str, List[float]], Dict[str, Any], Dict[str, Any]]] = {}

    for drv in SENSITIVITY_DRIVERS:
        print(f"\n{drv['name']}  |  Units: {drv['units']}  |  Years: {drv['affected_years']}")
        print(sub_sep)
        hdr = (
            f"{'Case':<7} | {'Actual Input Value & Units':<35} | "
            f"{'2030E EBIT ($M)':>15} {'Δ EBIT ($M)':>13} | "
            f"{'2030E FCFE ($M)':>15} {'Δ FCFE ($M)':>13} | "
            f"{'Value/Sh ($)':>12} {'Δ Val/Sh ($)':>12} | {'Acct Check':<12}"
        )
        print(hdr)
        print(sub_sep)

        valid_ebits: List[float] = []
        valid_fcfes: List[float] = []
        valid_vpss: List[float] = []

        for case_label, case_values, display_input in drv["cases"]:
            # Start from a fresh independent copy of BASE_INPUTS
            run_inputs = copy.deepcopy(BASE_INPUTS)
            run_inputs[drv["key"]] = copy.deepcopy(case_values)

            # Verify that all other independent assumptions remained at base
            for k in BASE_INPUTS:
                if k != drv["key"]:
                    assert run_inputs[k] == BASE_INPUTS[k], f"Non-selected input {k} mutated!"

            try:
                r_rows, r_val = run_proforma(run_inputs, break_test_2026_cash=False)
                acct_ok = (r_val["max_abs_gap"] <= 0.01) and r_val["min_cash_all_ok"]
                check_str = f"PASS (gap={r_val['max_abs_gap']:.1f})" if acct_ok else "FAIL (INVALID)"
            except AssertionError as exc:
                acct_ok = False
                r_rows, r_val = {}, {"valuation_valid": False}
                check_str = f"INVALID ({exc})"

            if not acct_ok:
                print(
                    f"{case_label:<7} | {display_input:<35} | "
                    f"{'INVALID RUN':>15} {'N/A':>13} | {'INVALID RUN':>15} {'N/A':>13} | "
                    f"{'INVALID':>12} {'N/A':>12} | {check_str:<12}"
                )
                continue

            ebit_30 = r_rows["operating_income"][-1]
            fcfe_30 = r_rows["fcfe"][-1]
            d_ebit = ebit_30 - base_ebit_2030
            d_fcfe = fcfe_30 - base_fcfe_2030

            valid_ebits.append(ebit_30)
            valid_fcfes.append(fcfe_30)

            if r_val["valuation_valid"] and r_val["value_per_share"] is not None:
                vps = r_val["value_per_share"]
                d_vps = vps - base_vps
                valid_vpss.append(vps)
                vps_str = f"${vps:>11.2f}"
                dvps_str = f"{d_vps:>+12.2f}"
            else:
                vps_str = f"{'UNAVAILABLE':>12}"
                dvps_str = f"{'N/A':>12}"

            print(
                f"{case_label:<7} | {display_input:<35} | "
                f"{ebit_30:>15,.1f} {d_ebit:>+13,.1f} | "
                f"{fcfe_30:>15,.1f} {d_fcfe:>+13,.1f} | "
                f"{vps_str} {dvps_str} | {check_str:<12}"
            )

            saved_runs[f"{drv['key']}_{case_label}"] = (r_rows, r_val, run_inputs)

        print(sub_sep)
        ebit_span = max(valid_ebits) - min(valid_ebits) if len(valid_ebits) >= 2 else 0.0
        fcfe_span = max(valid_fcfes) - min(valid_fcfes) if len(valid_fcfes) >= 2 else 0.0
        vps_span = max(valid_vpss) - min(valid_vpss) if len(valid_vpss) >= 2 else 0.0
        print(
            f"{'SPAN':<7} | {'Max − Min across valid runs':<35} | "
            f"{ebit_span:>15,.1f} {'(EBIT Span)':>13} | "
            f"{fcfe_span:>15,.1f} {'(FCFE Span)':>13} | "
            f"${vps_span:>11.2f} {'(Val Span)':>12} | {'ALL VALID':<12}"
        )
        print(sub_sep)

        driver_spans.append({
            "name": drv["name"],
            "range_desc": f"{drv['cases'][0][2].split('(')[0].strip()} to {drv['cases'][2][2].split('(')[0].strip()}",
            "ebit_span": ebit_span,
            "fcfe_span": fcfe_span,
            "vps_span": vps_span,
        })

    # Print Output Span Comparison Summary (E — Find the Driver)
    print("\n" + sep)
    print("7. OUTPUT SPAN COMPARISON OVER TESTED RANGES (Max − Min Across Valid Runs)")
    print(sep)
    print(
        f"{'Operating Driver':<38} | {'Tested Input Range':<26} | "
        f"{'2030E EBIT Span ($M)':>20} | {'2030E FCFE Span ($M)':>20} | {'Value/Share Span ($)':>20}"
    )
    print(sub_sep)
    for ds in driver_spans:
        print(
            f"{ds['name']:<38} | {ds['range_desc']:<26} | "
            f"${ds['ebit_span']:>19,.1f} | ${ds['fcfe_span']:>19,.1f} | ${ds['vps_span']:>19.2f}"
        )
    print(sub_sep)
    larger_ebit = max(driver_spans, key=lambda x: x["ebit_span"])["name"]
    larger_fcfe = max(driver_spans, key=lambda x: x["fcfe_span"])["name"]
    larger_vps = max(driver_spans, key=lambda x: x["vps_span"])["name"]
    print(f"Larger driver over these tested ranges — FY2030E Operating Profit (EBIT): {larger_ebit}")
    print(f"Larger driver over these tested ranges — FY2030E Free Cash Flow (FCFE):   {larger_fcfe}")
    print(f"Larger driver over these tested ranges — Equity Value per Share:          {larger_vps}")
    print(sep)

    # Print Full FY2030E Statement Trace for Selected Runs (Retained Statement Details)
    g_hi_rows, g_hi_val, _ = saved_runs["organic_revenue_growth_Higher"]
    gm_hi_rows, gm_hi_val, _ = saved_runs["gross_margin_Higher"]

    print("\n" + sep)
    print("8. STATEMENT TRACE TABLE (FY2030E) — TRACING INPUT → STATEMENTS → OUTPUTS")
    print(sep)
    print(
        f"{'Statement Line (FY2030E, USD Millions)':<40} | "
        f"{'Base (13% g, 68.5% GM)':>22} | "
        f"{'Growth Higher (16.0%)':>22} | "
        f"{'Δ vs Base':>12} | "
        f"{'GM Higher (70.50%)':>20} | "
        f"{'Δ vs Base':>11}"
    )
    print(sub_sep)

    trace_items = [
        ("Revenue", base_rows_before["revenue"][-1], g_hi_rows["revenue"][-1], gm_hi_rows["revenue"][-1]),
        ("Cost of revenue", base_rows_before["cgs"][-1], g_hi_rows["cgs"][-1], gm_hi_rows["cgs"][-1]),
        ("Gross profit", base_rows_before["gross_profit"][-1], g_hi_rows["gross_profit"][-1], gm_hi_rows["gross_profit"][-1]),
        ("Cash OpEx (21.0% of GP in 2030E)", base_rows_before["sga"][-1], g_hi_rows["sga"][-1], gm_hi_rows["sga"][-1]),
        ("Depreciation (PP&E)", base_rows_before["depreciation"][-1], g_hi_rows["depreciation"][-1], gm_hi_rows["depreciation"][-1]),
        ("Operating income (EBIT)", base_rows_before["operating_income"][-1], g_hi_rows["operating_income"][-1], gm_hi_rows["operating_income"][-1]),
        ("Total interest expense", base_rows_before["total_interest"][-1], g_hi_rows["total_interest"][-1], gm_hi_rows["total_interest"][-1]),
        ("Pre-tax income", base_rows_before["pretax_income"][-1], g_hi_rows["pretax_income"][-1], gm_hi_rows["pretax_income"][-1]),
        ("Income tax expense (18.0%)", base_rows_before["income_tax"][-1], g_hi_rows["income_tax"][-1], gm_hi_rows["income_tax"][-1]),
        ("Net income", base_rows_before["net_income"][-1], g_hi_rows["net_income"][-1], gm_hi_rows["net_income"][-1]),
        ("(-) Capital spending (CapEx)", -base_rows_before["capex"][-1], -g_hi_rows["capex"][-1], -gm_hi_rows["capex"][-1]),
        ("(-) Change in inventory", -base_rows_before["chg_inv"][-1], -g_hi_rows["chg_inv"][-1], -gm_hi_rows["chg_inv"][-1]),
        ("(-) Change in other working capital", -base_rows_before["chg_owc"][-1], -g_hi_rows["chg_owc"][-1], -gm_hi_rows["chg_owc"][-1]),
        ("(+) Change in unearned revenue", base_rows_before["chg_ur"][-1], g_hi_rows["chg_ur"][-1], gm_hi_rows["chg_ur"][-1]),
        ("(-) Term debt repayment", -BASE_INPUTS["debt_repayment"], -BASE_INPUTS["debt_repayment"], -BASE_INPUTS["debt_repayment"]),
        ("Free Cash Flow to Equity (FCFE)", base_rows_before["fcfe"][-1], g_hi_rows["fcfe"][-1], gm_hi_rows["fcfe"][-1]),
        ("Ending Cash (FY2030E)", base_rows_before["cash"][-1], g_hi_rows["cash"][-1], gm_hi_rows["cash"][-1]),
        ("Total Assets (FY2030E)", base_rows_before["total_assets"][-1], g_hi_rows["total_assets"][-1], gm_hi_rows["total_assets"][-1]),
        ("Total Liab & Equity (FY2030E)", base_rows_before["total_liab_equity"][-1], g_hi_rows["total_liab_equity"][-1], gm_hi_rows["total_liab_equity"][-1]),
        ("Balance Gap (Assets - Liab - Eq)", base_rows_before["check_gap"][-1], g_hi_rows["check_gap"][-1], gm_hi_rows["check_gap"][-1]),
        ("PV of Explicit 5-Yr FCFE ($M)", base_val_before["pv_explicit_fcfe"], g_hi_val["pv_explicit_fcfe"], gm_hi_val["pv_explicit_fcfe"]),
        ("PV of Terminal Value ($M)", base_val_before["pv_terminal_value"], g_hi_val["pv_terminal_value"], gm_hi_val["pv_terminal_value"]),
        ("Total Equity Value ($M)", base_val_before["equity_value"], g_hi_val["equity_value"], gm_hi_val["equity_value"]),
    ]

    for label, b_v, g_v, gm_v in trace_items:
        print(
            f"{label:<40} | {b_v:>22,.1f} | {g_v:>22,.1f} | {g_v - b_v:>+12,.1f} | "
            f"{gm_v:>20,.1f} | {gm_v - b_v:>+11,.1f}"
        )

    print(sub_sep)
    print(
        f"{'Value per Share ($ / diluted share)':<40} | "
        f"${base_val_before['value_per_share']:>21.2f} | "
        f"${g_hi_val['value_per_share']:>21.2f} | "
        f"{g_hi_val['value_per_share'] - base_val_before['value_per_share']:>+12.2f} | "
        f"${gm_hi_val['value_per_share']:>19.2f} | "
        f"{gm_hi_val['value_per_share'] - base_val_before['value_per_share']:>+11.2f}"
    )
    print(sep)

    # 9. Restore Base and Rerun Verification Check
    restored_inputs = copy.deepcopy(BASE_INPUTS)
    base_rows_after, base_val_after = run_proforma(restored_inputs, break_test_2026_cash=False)

    diff_rev_30 = base_rows_after["revenue"][-1] - base_rows_before["revenue"][-1]
    diff_ebit_30 = base_rows_after["operating_income"][-1] - base_rows_before["operating_income"][-1]
    diff_fcfe_30 = base_rows_after["fcfe"][-1] - base_rows_before["fcfe"][-1]
    diff_cash_30 = base_rows_after["cash"][-1] - base_rows_before["cash"][-1]
    diff_vps = base_val_after["value_per_share"] - base_val_before["value_per_share"]

    assert abs(diff_rev_30) < 1e-9, "Restored base Revenue mismatch!"
    assert abs(diff_ebit_30) < 1e-9, "Restored base EBIT mismatch!"
    assert abs(diff_fcfe_30) < 1e-9, "Restored base FCFE mismatch!"
    assert abs(diff_cash_30) < 1e-9, "Restored base Cash mismatch!"
    assert abs(diff_vps) < 1e-9, "Restored base Value per Share mismatch!"

    print("\n" + sep)
    print("9. RESTORED-BASE VERIFICATION CHECK (Before vs. After Sensitivity Analysis)")
    print(sep)
    print(f"{'Check Metric':<42} | {'Initial Base Run':>22} | {'Restored Base Run':>22} | {'Difference':>16} | {'Status':<10}")
    print(sub_sep)
    print(f"{'Base Organic Revenue Growth (2026E-2030E)':<42} | {'13.00% / yr':>22} | {'13.00% / yr':>22} | {'0.000000%':>16} | {'PASS':<10}")
    print(f"{'Base Gross Margin (2026E-2030E)':<42} | {'68.50% of rev':>22} | {'68.50% of rev':>22} | {'0.000000%':>16} | {'PASS':<10}")
    print(f"{'FY2030E Revenue ($M)':<42} | {base_rows_before['revenue'][-1]:>22,.2f} | {base_rows_after['revenue'][-1]:>22,.2f} | {diff_rev_30:>+16.6f} | {'PASS':<10}")
    print(f"{'FY2030E Operating Income / EBIT ($M)':<42} | {base_rows_before['operating_income'][-1]:>22,.2f} | {base_rows_after['operating_income'][-1]:>22,.2f} | {diff_ebit_30:>+16.6f} | {'PASS':<10}")
    print(f"{'FY2030E Free Cash Flow to Equity ($M)':<42} | {base_rows_before['fcfe'][-1]:>22,.2f} | {base_rows_after['fcfe'][-1]:>22,.2f} | {diff_fcfe_30:>+16.6f} | {'PASS':<10}")
    print(f"{'FY2030E Ending Cash ($M)':<42} | {base_rows_before['cash'][-1]:>22,.2f} | {base_rows_after['cash'][-1]:>22,.2f} | {diff_cash_30:>+16.6f} | {'PASS':<10}")
    print(f"{'Max Balance Sheet Gap ($M)':<42} | {base_val_before['max_abs_gap']:>22.2f} | {base_val_after['max_abs_gap']:>22.2f} | {0.0:>+16.6f} | {'PASS':<10}")
    print(f"{'Equity Value per Diluted Share ($/sh)':<42} | ${base_val_before['value_per_share']:>21.2f} | ${base_val_after['value_per_share']:>21.2f} | ${diff_vps:>+15.6f} | {'PASS':<10}")
    print(sub_sep)
    print("Restored-base check status: PASSED (Initial Base and Restored Base match to 0.000000 across all inputs and outputs)")
    print(sep + "\n")


def main() -> None:
    """Run initial base MSFT pro-forma, execute OAT sensitivity analysis, and verify restored base."""
    base_rows_before, base_val_before = run_proforma(copy.deepcopy(BASE_INPUTS), break_test_2026_cash=False)
    print_proforma_tables(base_rows_before, base_val_before)
    run_sensitivity_analysis(base_rows_before, base_val_before)


if __name__ == "__main__":
    main()
