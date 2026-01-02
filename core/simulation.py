def simulate_capital(
    capital_initial: float,
    monthly_contribution: float,
    annual_return: float,
    annual_fee: float,
    years: int
):
    months = years * 12
    monthly_return = annual_return / 100 / 12
    monthly_fee = annual_fee / 100 / 12

    capital_no_fee = []
    capital_with_fee = []

    c_no_fee = capital_initial
    c_with_fee = capital_initial

    for _ in range(months):
        c_no_fee = c_no_fee * (1 + monthly_return) + monthly_contribution
        c_with_fee = c_with_fee * (1 + monthly_return - monthly_fee) + monthly_contribution

        capital_no_fee.append(c_no_fee)
        capital_with_fee.append(c_with_fee)

    return capital_no_fee, capital_with_fee
