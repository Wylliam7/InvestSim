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


def capital_steps_table(capital_list, step):
    steps_data = []
    current_step = step
    for i, value in enumerate(capital_list):
        if value >= current_step:
            steps_data.append((current_step, round(i / 12, 2)))  # (palier, années)
            current_step += step
    return steps_data


def monthly_investment_for_goal(
    current_age: int,
    target_age: int,
    target_amount: float,
    annual_return: float,
    annual_fee: float,
    capital_initial: float = 0
):
    years = target_age - current_age
    if years <= 0:
        raise ValueError("L'âge cible doit être supérieur à l'âge actuel.")

    months = years * 12

    monthly_return = (annual_return - annual_fee) / 100 / 12

    if monthly_return <= 0:
        # Cas sans rendement (ou rendement négatif)
        return (target_amount - capital_initial) / months

    # Formule financière
    factor = (1 + monthly_return) ** months
    monthly_investment = (target_amount - capital_initial * factor) * monthly_return / (factor - 1)

    return monthly_investment