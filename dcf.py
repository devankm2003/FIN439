"""Five-year FCFF discounted cash flow model (all monetary inputs in USD millions)."""

# Editable inputs
STARTING_FCFF = 100.0
YEARLY_GROWTH_RATES = [0.08, 0.06, 0.05, 0.04, 0.03]
WACC = 0.10
TERMINAL_GROWTH = 0.03
NON_OPERATING_CASH = 50.0
DEBT = 300.0
DILUTED_SHARES = 50.0


def main() -> None:
    """Calculate and print a five-year FCFF DCF valuation."""
    if len(YEARLY_GROWTH_RATES) != 5:
        raise SystemExit("Error: exactly five yearly growth rates are required.")
    if TERMINAL_GROWTH >= WACC:
        raise SystemExit(
            "Error: terminal growth must be less than WACC for the Gordon-growth formula."
        )
    if DILUTED_SHARES <= 0:
        raise SystemExit("Error: diluted shares must be greater than zero.")

    fcff_by_year = []
    fcff = STARTING_FCFF
    for growth_rate in YEARLY_GROWTH_RATES:
        fcff *= 1.0 + growth_rate
        fcff_by_year.append(fcff)

    pv_explicit_fcff = sum(
        yearly_fcff / (1.0 + WACC) ** year
        for year, yearly_fcff in enumerate(fcff_by_year, start=1)
    )
    terminal_value_year_5 = (
        fcff_by_year[-1] * (1.0 + TERMINAL_GROWTH) / (WACC - TERMINAL_GROWTH)
    )
    pv_terminal_value = terminal_value_year_5 / (1.0 + WACC) ** 5
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
    value_per_diluted_share = equity_value / DILUTED_SHARES
    pv_terminal_value_share_of_ev = pv_terminal_value / enterprise_value

    for year, yearly_fcff in enumerate(fcff_by_year, start=1):
        print(f"FCFF Year {year}: {yearly_fcff:.4f}")
    print(f"PV of explicit FCFF: {pv_explicit_fcff:.4f}")
    print(f"Terminal value, Year 5: {terminal_value_year_5:,.4f}")
    print(f"PV of terminal value: {pv_terminal_value:,.4f}")
    print(f"Enterprise value: {enterprise_value:,.4f}")
    print(f"Equity value: {equity_value:,.4f}")
    print(f"Value per share: {value_per_diluted_share:.4f}")
    print(
        "PV of TV ÷ enterprise value: "
        f"{pv_terminal_value_share_of_ev:.4f} ({pv_terminal_value_share_of_ev:.2%})"
    )


if __name__ == "__main__":
    main()
