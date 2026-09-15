"""Comparable-company valuation using Price-to-Earnings (P/E) multiples.

Standard-library Python script reproducing the Asbury Automotive Group (ABG)
training case with AutoNation (AN) and Group 1 Automotive (GPI).
"""

import statistics
from typing import Any

# ==============================================================================
# EDITABLE INPUTS (FROZEN TRAINING CASE)
# ==============================================================================
TARGET = {
    "name": "Asbury Automotive Group",
    "ticker": "ABG",
    "price": 243.03,  # December 31, 2024 closing price ($)
    "eps": 21.50,     # FY2024 total GAAP diluted EPS ($)
}

PEERS = [
    {
        "name": "AutoNation",
        "ticker": "AN",
        "price": 169.84,  # December 31, 2024 closing price ($)
        "eps": 16.92,     # FY2024 total GAAP diluted EPS ($)
    },
    {
        "name": "Group 1 Automotive",
        "ticker": "GPI",
        "price": 421.48,  # December 31, 2024 closing price ($)
        "eps": 36.81,     # FY2024 total GAAP diluted EPS ($)
    },
]


def validate_input(val: Any) -> bool:
    """Return True if value is numeric and strictly positive."""
    if val is None:
        return False
    try:
        f = float(val)
        return f > 0.0
    except (ValueError, TypeError):
        return False


def run_comps() -> None:
    """Execute peer P/E multiple calculation, implied valuation, and leave-one-out sensitivity."""
    sep = "=" * 70
    sub_sep = "-" * 70

    print(sep)
    print("COMPARABLE COMPANY VALUATION: PRICE-TO-EARNINGS (P/E)")
    print(sep)

    # 1. Target Validation
    target_ticker = str(TARGET.get("ticker", "")).strip().upper()
    target_name = str(TARGET.get("name", "")).strip()
    target_price = TARGET.get("price")
    target_eps = TARGET.get("eps")

    target_valid_price = validate_input(target_price)
    target_valid_eps = validate_input(target_eps)

    print(f"Target Company: {target_name} ({target_ticker})")
    if target_valid_price:
        print(f"Target Price:   ${float(target_price):.2f}")
    else:
        print(f"Target Price:   {target_price} (not meaningful / missing)")
    if target_valid_eps:
        print(f"Target EPS:     ${float(target_eps):.2f}")
    else:
        print(f"Target EPS:     {target_eps} (not meaningful / nonpositive)")

    if not target_valid_eps:
        print("\nError: Target diluted EPS must be positive. Implied valuation not meaningful.")
        print(sep)
        return

    # 2. Peer Deduplication & Target Exclusion
    seen_tickers = set()
    cleaned_peers = []
    for peer in PEERS:
        t = str(peer.get("ticker", "")).strip().upper()
        n = str(peer.get("name", "")).strip()
        if not t:
            continue
        # Exclude target if accidentally included in peers
        if t == target_ticker or (target_name and n.lower() == target_name.lower()):
            print(f"\n[Note] Excluded target company ({t}) from peer set.")
            continue
        # Deduplicate peers
        if t in seen_tickers:
            print(f"\n[Note] Duplicate peer ({t}) encountered; keeping first occurrence.")
            continue
        seen_tickers.add(t)
        cleaned_peers.append(peer)

    # 3. Peer Multiple Computation
    print("\n" + sub_sep)
    print(f"{'Peer Company':<26} {'Ticker':<8} {'Price ($)':<12} {'Diluted EPS':<14} {'P/E Multiple':<14}")
    print(sub_sep)

    valid_peers = []
    for p in cleaned_peers:
        t = str(p.get("ticker", "")).strip().upper()
        n = str(p.get("name", "")).strip()
        price = p.get("price")
        eps = p.get("eps")

        p_valid = validate_input(price)
        e_valid = validate_input(eps)

        if p_valid and e_valid:
            price_f = float(price)
            eps_f = float(eps)
            pe_multiple = price_f / eps_f
            valid_peers.append({
                "name": n,
                "ticker": t,
                "price": price_f,
                "eps": eps_f,
                "pe": pe_multiple,
            })
            print(f"{n:<26} {t:<8} ${price_f:<11.2f} ${eps_f:<13.2f} {pe_multiple:<14.6f}×")
        else:
            p_str = f"${float(price):.2f}" if p_valid else "invalid"
            e_str = f"${float(eps):.2f}" if e_valid else "invalid"
            print(f"{n:<26} {t:<8} {p_str:<12} {e_str:<14} not meaningful")

    print(sub_sep)

    num_valid = len(valid_peers)
    if num_valid == 0:
        print("Result: no usable peers.")
        print(sep)
        return

    # 4. Multiples and Implied Price Ranges
    pe_values = [p["pe"] for p in valid_peers]
    med_pe = statistics.median(pe_values)
    min_pe = min(pe_values)
    max_pe = max(pe_values)

    target_eps_f = float(target_eps)
    med_implied = med_pe * target_eps_f
    min_implied = min_pe * target_eps_f
    max_implied = max_pe * target_eps_f

    print("\nPEER MULTIPLES & IMPLIED VALUATION")
    print(sub_sep)
    print(f"Usable peer count: {num_valid}")
    print(f"Peer median P/E:   {med_pe:.6f}×")

    if num_valid == 1:
        p_single = valid_peers[0]
        print(f"\nOne valid peer ({p_single['ticker']}): reference estimate, no range.")
        print(f"Implied price per share: ${med_implied:.2f}")
    else:
        print(f"Peer P/E range:    {min_pe:.6f}× to {max_pe:.6f}×")
        print(f"{target_name} at peer median:   ${med_implied:.2f}")
        print(f"{target_name} peer-implied range: ${min_implied:.2f}–${max_implied:.2f}")

    # 5. Leave-One-Out Peer Sensitivity
    print("\n" + sub_sep)
    print("LEAVE-ONE-PEER-OUT SENSITIVITY (Unrounded calculations)")
    print(sub_sep)

    for removed_peer in valid_peers:
        rem_ticker = removed_peer["ticker"]
        remaining = [p for p in valid_peers if p["ticker"] != rem_ticker]

        if not remaining:
            print(f"Remove {rem_ticker}: no estimate (no remaining peers).")
            continue

        rem_pe_values = [p["pe"] for p in remaining]
        rem_med_pe = statistics.median(rem_pe_values)
        rem_implied = rem_med_pe * target_eps_f
        delta = rem_implied - med_implied

        if len(remaining) == 1:
            surviving = remaining[0]["ticker"]
            print(
                f"Remove {rem_ticker}: remaining {surviving} estimate: ${rem_implied:.2f} "
                f"(change from full-peer estimate: {delta:+.2f})"
            )
        else:
            print(
                f"Remove {rem_ticker}: remaining median estimate: ${rem_implied:.2f} "
                f"(change from full-peer estimate: {delta:+.2f})"
            )

    print(sep)
    print("Note: Never bridge P/E with cash/debt; P/E is an equity multiple.")
    print(sep)


if __name__ == "__main__":
    run_comps()

