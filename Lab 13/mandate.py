"""
mandate.py - Meridian Foundation Reserve Mandate Checker
FIN439: Corporate Valuation and Investment Policy Analysis
Standard Library Only.
"""

# ==============================================================================
# EDITABLE INPUTS
# ==============================================================================

# Reserve and Distribution Parameters
RESERVE_SIZE = 100.0             # USD millions
QUARTERLY_DISTRIBUTION = 0.75    # USD millions
QUARTERS_TO_COVER = 4            # Number of quarters
LIQUIDITY_WINDOW = 5             # Business days
MIN_LIQUID_SHARE = 90.0          # Minimum liquid percentage
ISSUER_LIMIT = 8.0               # Maximum exposure to single corporate issuer (%)

# Holdings Master Table: (holding_name, issuer, business_days_to_redeem, reserve_eligible)
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

# Exempt Issuers from the single-company concentration cap
EXEMPT_ISSUERS = {"none", "u.s. treasury", "diversified fund"}

# Candidate Portfolios (weights as % of portfolio)
CANDIDATES = {
    "A": {
        "Cash": 2.0,
        "Treasury bills": 2.0,
        "Treasury 10-year note": 10.0,
        "Global equity index fund": 60.0,
        "Investment-grade bond fund": 26.0,
        "Private real estate fund": 0.0,
        "Acme Corp bonds": 0.0,
        "Acme Corp stock": 0.0,
    },
    "B": {
        "Cash": 1.0,
        "Treasury bills": 0.0,
        "Treasury 10-year note": 0.0,
        "Global equity index fund": 55.0,
        "Investment-grade bond fund": 20.0,
        "Private real estate fund": 15.0,
        "Acme Corp bonds": 5.0,
        "Acme Corp stock": 4.0,
    },
    "C": {
        "Cash": 1.0,
        "Treasury bills": 1.0,
        "Treasury 10-year note": 0.0,
        "Global equity index fund": 70.0,
        "Investment-grade bond fund": 20.0,
        "Private real estate fund": 0.0,
        "Acme Corp bonds": 0.0,
        "Acme Corp stock": 8.0,
    },
    # Candidate D: The Attack Candidate
    # Passes all checkable rules (100% sum, long-only, 3% reserve, 100% liquid, 0% company)
    # but violates S4 (Benchmark 60/40) and exposes S9 drawdown risk by holding 97% equities.
    "D": {
        "Cash": 3.0,
        "Treasury bills": 0.0,
        "Treasury 10-year note": 0.0,
        "Global equity index fund": 97.0,
        "Investment-grade bond fund": 0.0,
        "Private real estate fund": 0.0,
        "Acme Corp bonds": 0.0,
        "Acme Corp stock": 0.0,
    },
}

# ==============================================================================
# COMPUTATION & CHECK ENGINE
# ==============================================================================

def compute_reserve_minimum():
    """Computes reserve minimum: quarters × distribution ÷ reserve size (%)"""
    return (QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE) * 100.0


def evaluate_candidate(candidate_name, weights, reserve_min):
    """Evaluates all mandate rules for a given candidate portfolio."""
    # 1. Weights sum to 100
    total_weight = sum(weights.values())
    sum_pass = abs(total_weight - 100.0) < 1e-5

    # 2. Lowest weight not negative (long-only)
    min_weight = min(weights.values())
    long_only_pass = min_weight >= -1e-5

    # Build holdings lookup
    holdings_dict = {h["holding"]: h for h in HOLDINGS}

    # 3. Reserve-eligible weight
    reserve_weight = 0.0
    for h_name, w in weights.items():
        if holdings_dict[h_name]["reserve_eligible"]:
            reserve_weight += w
    reserve_pass = reserve_weight >= (reserve_min - 1e-5)

    # 4. Redeemable within liquidity window
    liquid_weight = 0.0
    for h_name, w in weights.items():
        if holdings_dict[h_name]["days"] <= LIQUIDITY_WINDOW:
            liquid_weight += w
    liquid_pass = liquid_weight >= (MIN_LIQUID_SHARE - 1e-5)

    # 5. Largest single company (corporate issuer)
    company_totals = {}
    for h_name, w in weights.items():
        issuer = holdings_dict[h_name]["issuer"]
        if issuer.strip().lower() not in EXEMPT_ISSUERS:
            company_totals[issuer] = company_totals.get(issuer, 0.0) + w

    max_company_weight = max(company_totals.values()) if company_totals else 0.0
    company_pass = max_company_weight <= (ISSUER_LIMIT + 1e-5)

    # Tally failures
    rules = [
        ("Weights sum to 100", total_weight, sum_pass),
        ("Long-only (lowest weight)", min_weight, long_only_pass),
        (f"Reserve ≥ {reserve_min:.1f}%", reserve_weight, reserve_pass),
        (f"Redeemable in {LIQUIDITY_WINDOW} days ≥ {MIN_LIQUID_SHARE:.0f}%", liquid_weight, liquid_pass),
        (f"Largest single company ≤ {ISSUER_LIMIT:.0f}%", max_company_weight, company_pass),
    ]

    failed_count = sum(1 for _, _, passed in rules if not passed)

    if failed_count == 0:
        verdict = "passes every checkable rule"
    else:
        verdict = f"fails {failed_count} rule(s)"

    return {
        "rules": rules,
        "failed_count": failed_count,
        "verdict": verdict,
    }


def main():
    reserve_min = compute_reserve_minimum()
    print(f"Reserve minimum: {reserve_min:.1f}% of the portfolio.\n")

    results = {}
    for c_name, weights in CANDIDATES.items():
        results[c_name] = evaluate_candidate(c_name, weights, reserve_min)

    # --------------------------------------------------------------------------
    # Detailed Candidate Printout
    # --------------------------------------------------------------------------
    for c_name, res in results.items():
        print(f"Candidate {c_name}:")
        for r_name, val, passed in res["rules"]:
            status = "pass" if passed else "FAIL"
            print(f"  {r_name}: {val:.1f} {status}")
        print("  Calendar-year loss: requires CIO clarification")
        print(f"  Verdict: {res['verdict']}\n")

    # --------------------------------------------------------------------------
    # Summary Table Comparison (matching Section V rubric table)
    # --------------------------------------------------------------------------
    print("=" * 78)
    print("MANDATE CHECKER SUMMARY MATRIX")
    print("=" * 78)
    header = f"{'Rule':<32} " + " ".join(f"{c:^10}" for c in CANDIDATES.keys())
    print(header)
    print("-" * 78)

    rule_labels = [
        "Weights sum to 100",
        "Long-only (lowest weight)",
        f"Reserve ≥ {reserve_min:.1f}%",
        f"Redeemable in {LIQUIDITY_WINDOW} days ≥ {MIN_LIQUID_SHARE:.0f}%",
        f"Largest single company ≤ {ISSUER_LIMIT:.0f}%",
    ]

    for idx, label in enumerate(rule_labels):
        row_str = f"{label:<32} "
        for c_name in CANDIDATES.keys():
            val = results[c_name]["rules"][idx][1]
            passed = results[c_name]["rules"][idx][2]
            stat = "pass" if passed else "FAIL"
            cell = f"{val:.1f} {stat}"
            row_str += f"{cell:^10} "
        print(row_str)

    # Calendar-year loss row
    cal_row = f"{'Calendar-year loss':<32} " + f"{'requires CIO clarification':^10} " + " ".join(f"{'same':^10}" for _ in list(CANDIDATES.keys())[1:])
    print(cal_row)

    print("-" * 78)
    # Verdict row
    verdict_row = f"{'Verdict':<32} "
    for c_name in CANDIDATES.keys():
        v = results[c_name]["verdict"]
        verdict_row += f"{v:^10} "
    print(verdict_row)
    print("=" * 78)


if __name__ == "__main__":
    main()
