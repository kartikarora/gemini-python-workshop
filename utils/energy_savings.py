def calculate_total_energy_savings(energy_consumption: float, baseline_energy_price: float,
                                   efficient_energy_price: float):
    """
    Calculate the total energy savings achieved through implementing energy-efficient measures (simplified formula).

    Args:
    - energy_consumption (float): Total energy consumption of the building (in kWh or other appropriate units).
    - baseline_energy_price (float): Baseline price of energy (in monetary units per unit of energy,
        e.g., dollars per kWh).
    - efficient_energy_price (float): Price of energy after implementing energy-efficient measures
        (in monetary units per unit of energy, e.g., dollars per kWh).

    Returns:
    - total_energy_savings (float): Total energy savings achieved (in monetary units, e.g., dollars).
    """
    energy_savings = energy_consumption * (baseline_energy_price - efficient_energy_price)
    return energy_savings
