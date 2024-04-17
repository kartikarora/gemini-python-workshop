def calculate_sustainability_score(energy_efficiency, materials_sustainability, water_usage_efficiency,
                                   indoor_air_quality):
    """
    Calculate the sustainability score of a building design.

    Args:
    - energy_efficiency (float): Energy efficiency rating (scaled from 0 to 1).
    - materials_sustainability (float): Materials sustainability rating (scaled from 0 to 1).
    - water_usage_efficiency (float): Water usage efficiency rating (scaled from 0 to 1).
    - indoor_air_quality (float): Indoor air quality rating (scaled from 0 to 1).

    Returns:
    - sustainability_score (float): Overall sustainability score.
    """
    sustainability_score = energy_efficiency * materials_sustainability * water_usage_efficiency * indoor_air_quality
    return sustainability_score
