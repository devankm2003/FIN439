"""Five-year FCFF discounted cash flow model with Sensitivity Grid and Reverse DCF (monetary inputs in USD millions)."""

# ==============================================================================
# EDITABLE INPUTS
# ==============================================================================
# To switch between Microsoft (MSFT) and the training case, toggle comments below.

# --- Company Case: Microsoft Corporation (NASDAQ: MSFT, FY2024 10-K) ---
STARTING_FCFF = 75474.0  # Operating cash flow ($118,548M) + after-tax interest ($1,401M) - CapEx ($44,475M)
YEARLY_GROWTH_RATES = [0.14, 0.12, 0.10, 0.08, 0.06]  # Labelled forecast based on MD&A Item 7
WACC = 0.095  # 9.50% brief estimate: Ke=10.0%, Kd*(1-t)=3.13%, 98.8% equity weight
TERMINAL_GROWTH = 0.03  # 3.00% long-run macroeconomic GDP anchor
NON_OPERATING_CASH = 75543.0  # Cash & cash equivalents ($18,315M) + Short-term investments ($57,228M)
DEBT = 44278.0  # Current portion of long-term debt ($2,249M) + Long-term debt ($42,029M)
DILUTED_SHARES = 7469.0  # Note 19 Diluted weighted-average shares (millions)

# Sensitivity grid inputs (centered on base case: WACC 9.5%, Terminal Growth 3.0%)
GRID_WACC_RATES = [0.085, 0.095, 0.105]
GRID_TERMINAL_GROWTH_RATES = [0.02, 0.03, 0.04]

# Reverse DCF inputs
TARGET_SHARE_PRICE = 491.65  # MSFT share price as of September 10, 2026
REVERSE_DCF_LOWER_BOUND = -0.05  # -5 percentage points
REVERSE_DCF_UPPER_BOUND = 0.35   # +35 percentage points (widened to include target price; [-5%, +10%] reports no solution)

# --- Training Case (uncomment below and comment above to reproduce Tuesday's 12 lines & +1.78 shift) ---
# STARTING_FCFF = 100.0
# YEARLY_GROWTH_RATES = [0.08, 0.06, 0.05, 0.04, 0.03]
# WACC = 0.10
# TERMINAL_GROWTH = 0.03
# NON_OPERATING_CASH = 50.0
# DEBT = 300.0
# DILUTED_SHARES = 50.0
# GRID_WACC_RATES = [0.09, 0.10, 0.11]
# GRID_TERMINAL_GROWTH_RATES = [0.02, 0.03, 0.04]
# TARGET_SHARE_PRICE = 30.00
# REVERSE_DCF_LOWER_BOUND = -0.05
# REVERSE_DCF_UPPER_BOUND = 0.10


def compute_valuation(
    starting_fcff: float,
    growth_rates: list[float],
    wacc: float,
    terminal_growth: float,
    non_operating_cash: float,
    debt: float,
    diluted_shares: float,
) -> dict | None:
    """Calculate DCF values. Returns dict of results or None if invalid."""
    if len(growth_rates) != 5:
        raise SystemExit("Error: exactly five yearly growth rates are required.")
    if terminal_growth >= wacc:
        return None
    if diluted_shares <= 0:
        raise SystemExit("Error: diluted shares must be greater than zero.")

    fcff_by_year = []
    fcff = starting_fcff
    for growth_rate in growth_rates:
        fcff *= 1.0 + growth_rate
        fcff_by_year.append(fcff)

    pv_explicit_fcff = sum(
        yearly_fcff / (1.0 + wacc) ** year
        for year, yearly_fcff in enumerate(fcff_by_year, start=1)
    )
    terminal_value_year_5 = (
        fcff_by_year[-1] * (1.0 + terminal_growth) / (wacc - terminal_growth)
    )
    pv_terminal_value = terminal_value_year_5 / (1.0 + wacc) ** 5
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + non_operating_cash - debt
    value_per_diluted_share = equity_value / diluted_shares
    pv_terminal_value_share_of_ev = pv_terminal_value / enterprise_value

    return {
        "fcff_by_year": fcff_by_year,
        "pv_explicit_fcff": pv_explicit_fcff,
        "terminal_value_year_5": terminal_value_year_5,
        "pv_terminal_value": pv_terminal_value,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_diluted_share": value_per_diluted_share,
        "pv_terminal_value_share_of_ev": pv_terminal_value_share_of_ev,
    }


def print_twelve_lines(results: dict) -> None:
    """Print the twelve standard output lines matching Tuesday's format."""
    for year, yearly_fcff in enumerate(results["fcff_by_year"], start=1):
        print(f"FCFF Year {year}: {yearly_fcff:.4f}")
    print(f"PV of explicit FCFF: {results['pv_explicit_fcff']:.4f}")
    print(f"Terminal value, Year 5: {results['terminal_value_year_5']:,.4f}")
    print(f"PV of terminal value: {results['pv_terminal_value']:,.4f}")
    print(f"Enterprise value: {results['enterprise_value']:,.4f}")
    print(f"Equity value: {results['equity_value']:,.4f}")
    print(f"Value per share: {results['value_per_diluted_share']:.4f}")
    print(
        "PV of TV ÷ enterprise value: "
        f"{results['pv_terminal_value_share_of_ev']:.4f} "
        f"({results['pv_terminal_value_share_of_ev']:.2%})"
    )


def print_sensitivity_grid() -> None:
    """Print sensitivity grid of value per share across WACC and terminal growth."""
    col_width = 12
    headers = "".join(f"{g:>12.1%}" for g in GRID_TERMINAL_GROWTH_RATES)
    table_width = 24 + len(GRID_TERMINAL_GROWTH_RATES) * col_width
    sep = "-" * table_width

    print()
    print(sep)
    print("Sensitivity Grid: Value per Diluted Share ($)")
    print(sep)
    print(f"{r'WACC \ Terminal Growth':<24}" + headers)

    for w in GRID_WACC_RATES:
        row_str = f"{w:<24.1%}"
        for g in GRID_TERMINAL_GROWTH_RATES:
            res = compute_valuation(
                starting_fcff=STARTING_FCFF,
                growth_rates=YEARLY_GROWTH_RATES,
                wacc=w,
                terminal_growth=g,
                non_operating_cash=NON_OPERATING_CASH,
                debt=DEBT,
                diluted_shares=DILUTED_SHARES,
            )
            if res is None:
                row_str += f"{'invalid':>{col_width}}"
            else:
                row_str += f"{res['value_per_diluted_share']:>{col_width}.2f}"
        print(row_str)
    print(sep)


def run_reverse_dcf() -> None:
    """Solve for uniform shift added to explicit growth rates to match target share price."""
    table_width = 60
    sep = "-" * table_width

    print()
    print(sep)
    print("Reverse DCF (Uniform Shift to Explicit Growth Rates)")
    print(sep)

    # Validate that bounds do not push any growth rate to <= -100%
    for i, r in enumerate(YEARLY_GROWTH_RATES, start=1):
        if r + REVERSE_DCF_LOWER_BOUND <= -1.0:
            print(
                f"Error: Lower bound ({REVERSE_DCF_LOWER_BOUND:+.2%}) pushes Year {i} "
                f"growth rate ({r:+.2%}) to <= -100%. Bracket refused."
            )
            print(sep)
            return
        if r + REVERSE_DCF_UPPER_BOUND <= -1.0:
            print(
                f"Error: Upper bound ({REVERSE_DCF_UPPER_BOUND:+.2%}) pushes Year {i} "
                f"growth rate ({r:+.2%}) to <= -100%. Bracket refused."
            )
            print(sep)
            return

    def value_at_shift(shift: float) -> float:
        shifted_rates = [r + shift for r in YEARLY_GROWTH_RATES]
        res = compute_valuation(
            starting_fcff=STARTING_FCFF,
            growth_rates=shifted_rates,
            wacc=WACC,
            terminal_growth=TERMINAL_GROWTH,
            non_operating_cash=NON_OPERATING_CASH,
            debt=DEBT,
            diluted_shares=DILUTED_SHARES,
        )
        return res["value_per_diluted_share"]

    val_low = value_at_shift(REVERSE_DCF_LOWER_BOUND)
    val_high = value_at_shift(REVERSE_DCF_UPPER_BOUND)

    print(f"Target share price: ${TARGET_SHARE_PRICE:.2f}")
    print(
        f"Search bracket: [{REVERSE_DCF_LOWER_BOUND * 100:+.2f} pts, "
        f"{REVERSE_DCF_UPPER_BOUND * 100:+.2f} pts] "
        f"(Achievable value range: [${val_low:.2f}, ${val_high:.2f}])"
    )

    if TARGET_SHARE_PRICE < val_low or TARGET_SHARE_PRICE > val_high:
        print(
            f"Result: No solution in bracket [{REVERSE_DCF_LOWER_BOUND * 100:+.2f} pts, "
            f"{REVERSE_DCF_UPPER_BOUND * 100:+.2f} pts]. Target price ${TARGET_SHARE_PRICE:.2f} "
            f"is outside achievable range [${val_low:.2f}, ${val_high:.2f}]."
        )
        print("Note: Never returning a bound as if it were the answer.")
        print(sep)
        return

    # Bisection search
    low = REVERSE_DCF_LOWER_BOUND
    high = REVERSE_DCF_UPPER_BOUND
    for _ in range(100):
        mid = (low + high) / 2.0
        val_mid = value_at_shift(mid)
        if val_mid < TARGET_SHARE_PRICE:
            low = mid
        else:
            high = mid

    solved_shift = mid
    solved_val = value_at_shift(solved_shift)
    implied_rates = [r + solved_shift for r in YEARLY_GROWTH_RATES]

    print(
        f"Solved uniform growth shift: {solved_shift * 100:+.2f} percentage points "
        f"({solved_shift:+.4f})"
    )
    print("Implied Year 1–5 growth rates: " + ", ".join(f"{r:.2%}" for r in implied_rates))
    print(f"Resulting value per share: ${solved_val:.2f}")
    print("\nInputs held fixed:")
    print(f"  - Starting FCFF: {STARTING_FCFF:,.2f} USD million")
    print(f"  - WACC: {WACC:.2%}")
    print(f"  - Terminal growth rate: {TERMINAL_GROWTH:.2%}")
    print(f"  - Non-operating cash: {NON_OPERATING_CASH:,.2f} USD million")
    print(f"  - Total debt: {DEBT:,.2f} USD million")
    print(f"  - Diluted shares: {DILUTED_SHARES:,.2f} million")
    print("  - Explicit growth rate decay profile (Year 1–5 shifted uniformly)")
    print(sep)


def main() -> None:
    """Run base DCF valuation, sensitivity grid, and reverse DCF."""
    base_results = compute_valuation(
        starting_fcff=STARTING_FCFF,
        growth_rates=YEARLY_GROWTH_RATES,
        wacc=WACC,
        terminal_growth=TERMINAL_GROWTH,
        non_operating_cash=NON_OPERATING_CASH,
        debt=DEBT,
        diluted_shares=DILUTED_SHARES,
    )
    if base_results is None:
        raise SystemExit(
            "Error: terminal growth must be less than WACC for the Gordon-growth formula."
        )

    print_twelve_lines(base_results)
    print_sensitivity_grid()
    run_reverse_dcf()


if __name__ == "__main__":
    main()

